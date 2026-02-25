#!/usr/bin/env python3
"""
Anxiety Ad Image Generator - OpenAI GPT-Image-1.5
Generates native image ad photos for Facebook ad mockups
V3 Raw iPhone UGC style - documentary evidence, not ad concepts
Batch 1: 10 images for 5 Reasons Why Calming Your Nervous System Won't Fix Your Anxiety

Usage:
    python generate_anxiety_images.py --ids draft_01,draft_02
    python generate_anxiety_images.py --ids all
    python generate_anxiety_images.py --list
"""

import argparse
import base64
import os
import sys
import time
from pathlib import Path
from datetime import datetime

from openai import OpenAI

# Configuration
MODEL = "gpt-image-1.5"
API_KEY = os.environ.get("OPENAI_API_KEY", "")
OUTPUT_DIR = Path(__file__).parent / "generated_ad_images"
DELAY_BETWEEN_GENERATIONS = 2  # seconds

# Anxiety ad image prompts - V4: Native + Subtle Contradiction
# Philosophy: 3-layer native test:
#   1. Would someone take this photo? (camera + scene)
#   2. Would they post it? (there's a reason — the contradiction)
#   3. Do you feel something before reading text? (contradiction does the work)
# All concepts use object-as-subject, no people performing emotions
PROMPTS = [
    {
        "id": "draft_01",
        "name": "The Unchanged Journal Entry",
        "opener": "Deep breathing doesn't fix anxiety. It manages it.",
        "prompt": "Raw iPhone photo of an open journal on a nightstand, taken to send a frustrated friend. The visible page shows handwritten text \"Did breathing exercise. Still anxious.\" with faded similar text barely visible from a previous page. Harsh single bedside lamp creating yellow-orange cast on left side, dark shadows on right. Phone charger cable dangling off nightstand edge. Water glass with visible lip marks and dust at base. Slight motion blur on the edge of the journal — shot one-handed while lying in bed. This is \"3am can't sleep\" energy, not journaling content."
    },
    {
        "id": "draft_02",
        "name": "The Alarm Progression",
        "opener": "The more you practice calming techniques, the more dependent you become on them.",
        "prompt": "Raw iPhone photo of a phone screen showing the iPhone alarm list with 6 wellness alarms visible: \"5:00am Breathwork\", \"7:00am Meditate\", \"12:00pm Journal break\", \"3:00pm Walk\", \"6:00pm Yoga\", \"9:00pm Gratitude\". Phone lying on messy nightstand with crumpled tissue, lotion bottle on its side, tangled earbuds. Overhead bedroom light making everything flat and washed out. The phone screen is slightly tilted in frame — grabbed quickly to screenshot. Fingerprint smudge visible on phone screen. This is \"ugh look at this\" energy, not productivity content."
    },
    {
        "id": "draft_03",
        "name": "The Supplement Cabinet",
        "opener": "Everyone told you to regulate your nervous system. Nobody told you it was running on empty.",
        "prompt": "Raw iPhone photo of bathroom medicine cabinet half-open, showing a row of supplement bottles: ashwagandha, magnesium calm, L-theanine, lavender capsules. All bottles are nearly full, only a few pills missing from each. Single harsh fluorescent bathroom light creating yellow-green cast on everything. Toothpaste tube squeezed in the middle visible on shelf. Hair tie draped over shelf edge. Cabinet mirror has water spots on the edge. Phone held at slight upward angle to catch the shelf contents. This is \"look at my supplement graveyard\" energy, documenting embarrassment."
    },
    {
        "id": "draft_04",
        "name": "The Calendar Blocks",
        "opener": "You traded 10 minutes every morning for a few hours of relief. That's not a solution. That's a shift rate.",
        "prompt": "Raw iPhone photo of laptop screen showing a Google Calendar weekly view, where the same event \"Breathing / Meditation\" appears as a repeating blue block at the same time every single day for the visible week. Laptop on messy desk with 2 coffee mugs (one empty, one half-full cold). Sticky notes scattered. Lamp creating glare on part of the screen. Shot from slight side angle — not straight on. Crumpled napkin visible at desk edge. This is \"this is my life now\" energy, resignation not productivity."
    },
    {
        "id": "draft_05",
        "name": "The 2019 Streak",
        "opener": "You've been meditating for years. If it was going to work, it would have worked by now.",
        "prompt": "Raw iPhone photo of another phone screen showing a meditation app profile page: \"Member since 2019\" and a streak number showing \"847 consecutive days\" with achievement badges. Phone being held in a woman's hand, thumb visible on the edge. Background is messy desk with coffee ring stains on papers, charger cable tangled. Warm lamp light on one side, cold laptop screen glow on the other — ugly mixed lighting. Screen has visible fingerprint smudge. This is \"is this even working\" energy, not achievement celebration."
    },
    {
        "id": "draft_06",
        "name": "The Complete Screen in Chaos",
        "opener": "It was never about how you breathe. It was about what's missing when you're not breathing.",
        "prompt": "Raw iPhone photo of a phone screen showing a breathing app completion screen with a green checkmark and \"Session Complete!\" text. The phone is lying flat on a desk covered in visible chaos: 3 coffee cups in various states, crumpled paper, open laptop behind it showing email notification badges (47 unread), receipts, a pen with the cap off. Harsh overhead fluorescent creating flat unflattering light with visible shadows. Phone slightly askew in frame. This is \"technically I did my breathwork\" energy, documenting ironic futility."
    },
    {
        "id": "draft_07",
        "name": "The Right Tools, Wrong Room",
        "opener": "You weren't failing at calming techniques. You were using the right tool for the wrong problem.",
        "prompt": "Raw iPhone photo taken from a doorway, showing a home office corner: meditation cushion on the floor with lit candle and incense holder, but directly next to a desk with an open laptop showing Teams or Slack notifications. The cushion is maybe 2 feet from the desk. Mixed lighting — warm candle glow clashing with cold laptop screen. Papers scattered on floor near cushion. Coffee cup on desk. The frame is slightly tilted, shot quickly from hallway. This is \"where I try to meditate next to where I panic\" energy."
    },
    {
        "id": "draft_08",
        "name": "The Low Fuel Navigation",
        "opener": "Your body has a calming system that was supposed to handle all of this automatically. It's been running on empty.",
        "prompt": "Raw iPhone photo of a car dashboard at night, showing the fuel gauge near empty with the low fuel warning light on, and the navigation screen showing a route with \"3 stops remaining\" or multiple destination pins. Steering wheel partially visible. Dashboard lights reflecting slightly on the windshield. The phone camera captured some motion blur from being in a moving car. Slight fingerprint smudge on nav screen visible. This is \"running on fumes with 3 more things to do\" energy, not aesthetic car content."
    },
    {
        "id": "draft_09",
        "name": "The Private Doubt",
        "opener": "You knew deep down the techniques weren't fixing anything. You just couldn't prove it.",
        "prompt": "Raw iPhone photo of a phone screen showing the Notes app with a note titled \"Questions for therapist\" — visible text includes \"Why am I still anxious after 2 years of doing everything right?\" and maybe another partially visible bullet point. Phone lying on rumpled white bed sheets. Soft morning window light from one side. The phone screen has a slight crack or scratch visible. Hair on the pillow edge visible at frame edge. This is \"the note I've been too scared to bring up\" energy, vulnerable screenshot."
    },
    {
        "id": "draft_10",
        "name": "The Broken Streak",
        "opener": "A 2023 Stanford study found the calming effect of deep breathing only holds if you practice every single day.",
        "prompt": "Raw iPhone photo of a phone screen showing a meditation app with \"Current Streak: 0 days\" prominently displayed, with smaller text showing \"Previous streak: 47 days\" visible below. Phone lying on messy bedside table — half-empty water glass, crumpled tissue, book with bent corner. Early morning light through window creating harsh shadows. The screen has a thumbprint visible at the bottom. This is \"missed one day and it's all gone\" energy, documenting loss."
    },
    # BATCH 2 - Added 2026-02-24
    {
        "id": "draft_11",
        "name": "The Notification Badges",
        "opener": "Your meditation app isn't healing anything. It's making you a calmer passenger in a car that still can't stop.",
        "prompt": "Raw iPhone photo of a phone lying face-up on bathroom counter, screen showing home screen with Calm or Headspace app icon displaying a red notification badge showing \"365\". Phone surrounded by anxiety products: lavender roller bottle on its side, ashwagandha bottle with lid off, magnesium spray, CBD lotion tube squeezed in middle. Single harsh bathroom fluorescent making everything yellow-green. Water spots on counter. Hair tie and bobby pins scattered. Phone has visible fingerprint smudges on screen. Shot from above, slightly tilted. This is \"achieved the streak, still need all this\" energy."
    },
    {
        "id": "draft_12",
        "name": "The Morning Ritual Station",
        "opener": "Every morning you open Calm, you reinforce a belief that's quietly running your life: 'I am someone who needs to DO something to be calm.'",
        "prompt": "Raw iPhone photo of kitchen corner at 6am — yoga mat rolled and leaning against cabinet, meditation cushion on floor nearby, digital timer showing 15:00, coffee maker running with red light on. Harsh early morning light through window creating long shadows. Counter has yesterday's mail pile, keys tossed, single dirty coffee mug. One sock visible on floor near cushion. Everything staged and ready but the room feels cold and reluctant. Shot from standing height looking down. This is \"mandatory morning routine\" energy, not wellness content."
    },
    {
        "id": "draft_13",
        "name": "The Wellness Feed Graveyard",
        "opener": "Instagram said 'dysregulated.' Science says depleted. Those are different problems with different solutions.",
        "prompt": "Raw iPhone photo of bathroom counter with phone lying FACE DOWN, surrounded by wellness products Instagram recommended: ashwagandha bottle half-empty, magnesium calm powder with scoop sticking out, adaptogen packet torn open, essential oil roller, nervous system supplement bottle. All products opened and partially used. Phone is face-down — screen not visible. Single harsh fluorescent overhead making everything flat and unflattering. Toothpaste cap off to the side, hair in the sink edge. Water spots on mirror visible in background. Shot quickly from above. This is \"I tried everything the algorithm told me\" energy."
    },
    {
        "id": "draft_14",
        "name": "The Two Timers",
        "opener": "Deep breathing buys you 20 minutes. Meditation buys you maybe an hour. Neither buys you tomorrow.",
        "prompt": "Raw iPhone photo of bathroom counter with two objects side by side: a meditation timer app on phone showing 20:00 completed, and a regular alarm clock showing 3:47 AM. Both objects clearly visible, stark comparison. Harsh overhead bathroom light creating ugly shadows. Prescription bottle blurry in background. Wadded tissue nearby. Counter has water spots and toothpaste smear. Phone screen has fingerprint visible. Shot straight down from above. This is \"20 minutes bought, 3:47am still happened\" energy."
    },
    {
        "id": "draft_15",
        "name": "The Habit Tracker Grid",
        "opener": "You did the deep breathing. You did the journaling. You did the cold showers. The anxiety is still there every Monday morning.",
        "prompt": "Raw iPhone photo of a physical habit tracker page taped to bathroom wall with masking tape, showing a full month grid with checkmarks for \"breathwork\", \"journal\", \"meditate\" — every single box checked. Paper is slightly crooked, tape peeling at one corner. Mirror edge visible showing tired reflection (blurry, not the focus). Toiletries crowded on shelf below — face wash, lotion, q-tips container. Harsh overhead bathroom light. Paper has a coffee ring stain in corner. This is \"I checked every box and nothing changed\" energy."
    },
    {
        "id": "draft_16",
        "name": "The Two Desks",
        "opener": "Your colleague handles the same pressure without white knuckles. Same meetings. Same deadlines. Different levels of one molecule you've never heard of.",
        "prompt": "Raw iPhone photo showing corner of open office with two workstations visible in frame. LEFT desk: minimal, clean, single coffee mug, tidy cables, calm. RIGHT desk: multiple coffee cups, crumpled tissues, supplement bottles, stress ball, cluttered sticky notes, hand cream. Both screens showing same Monday 9am meeting invite visible. Harsh fluorescent office lighting, that sick green-white color. Shot from standing in aisle between desks, slightly tilted. Ceiling tiles visible at top of frame. This is \"same pressure, different chemistry\" energy."
    },
    {
        "id": "draft_17",
        "name": "The Timer Progression",
        "opener": "The fact that you need 15 minutes of deep breathing now instead of 2 isn't weakness. It's a depleted system asking for more than you can give it.",
        "prompt": "Raw iPhone photo of nightstand with three timers/phones lined up showing progression: first showing 5:00, second showing 10:00, third showing 15:00. The visual story of needing MORE each time. Each device looks used — scratches, worn cases. Nightstand cluttered with sleep mask tangled, melatonin bottle, book with cracked spine, water glass with dust at waterline. Harsh bedside lamp creating yellow-orange cast. Shot from bed level, one-handed. This is \"tolerance is building\" energy."
    },
    {
        "id": "draft_18",
        "name": "The Low Battery",
        "opener": "The anxiety isn't a sign that something is wrong with you. It's a signal that something ran out.",
        "prompt": "Raw iPhone photo of phone on nightstand showing low battery warning at 5%, red battery icon prominent, charging cable clearly plugged in but phone still dying. Surrounding objects: supplement bottles (magnesium, B-complex), sleep mask pushed aside, tangled earbuds, half-empty water glass. Soft morning light from window but phone screen harsh in contrast. The metaphor is visual: plugged in all night, still empty. Fingerprint smudge on phone screen. This is \"depleted system not getting recharged\" energy."
    },
    {
        "id": "draft_19",
        "name": "The Bookmarked Page",
        "opener": "That voice that said 'something else is going on here' — it was right. There was something underneath the techniques couldn't reach.",
        "prompt": "Raw iPhone photo of open self-help book lying on unmade bed, spine cracked and broken from overuse. Multiple pages dog-eared and bookmarked with colored tabs — this book has been read 3+ times. Highlighter marks visible on open pages. Reading glasses on pillow nearby. Coffee mug ring stain on nightstand edge visible. Soft morning window light, sheets rumpled. The book is clearly \"The Anxiety Workbook\" or similar self-help title (generic, no real brand). This is \"I've done this cover to cover twice and I'm back\" energy."
    },
    {
        "id": "draft_20",
        "name": "The Research Printouts",
        "opener": "Your nervous system was wired for anxiety before you were born. Not because something is wrong with you. Because something is missing.",
        "prompt": "Raw iPhone photo of desk with stack of printed research papers, highlighted and annotated with handwritten notes in margins. Laptop behind showing blurry PubMed or Google Scholar search visible. Papers have coffee ring stains, some pages bent at corners. Yellow highlighter with cap off. Reading glasses folded on top of papers. Harsh desk lamp creating glare on paper edges. Empty coffee mug with dried residue. This is \"I've actually done the research, not just scrolled Instagram\" energy."
    }
]


def save_image(image_base64: str, prompt_id: str, output_dir: Path) -> Path:
    """Save generated image"""
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prompt_id}_{timestamp}.png"
    filepath = output_dir / filename

    image_bytes = base64.b64decode(image_base64)
    with open(filepath, "wb") as f:
        f.write(image_bytes)

    # Also save a "latest" copy without timestamp for HTML reference
    latest_path = output_dir / f"{prompt_id}.png"
    with open(latest_path, "wb") as f:
        f.write(image_bytes)

    return filepath


def generate_image(client: OpenAI, prompt_text: str, quality: str = "medium"):
    """Generate a single image using OpenAI GPT-Image-1"""

    try:
        result = client.images.generate(
            model=MODEL,
            prompt=prompt_text,
            n=1,
            size="1024x1024",
            quality=quality
        )

        if result.data and result.data[0].b64_json:
            return result.data[0].b64_json
        elif result.data and result.data[0].url:
            import urllib.request
            response = urllib.request.urlopen(result.data[0].url)
            return base64.b64encode(response.read()).decode('utf-8')

        return None

    except Exception as e:
        print(f"  ERROR: {str(e)}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Generate Anxiety ad images with OpenAI GPT-Image-1")
    parser.add_argument("--ids", type=str, help="Comma-separated draft IDs (e.g., draft_01,draft_02) or 'all'")
    parser.add_argument("--list", action="store_true", help="List all prompts")
    parser.add_argument("--quality", type=str, default="medium", choices=["low", "medium", "high"],
                        help="Image quality: low (~$0.08), medium (~$0.11), high (~$0.24)")
    args = parser.parse_args()

    if args.list:
        print("\n=== Anxiety Ad Image Prompts ===\n")
        for p in PROMPTS:
            print(f"  {p['id']}: {p['name']}")
        return

    if not API_KEY:
        print("Error: OPENAI_API_KEY not set")
        print("Set with: export OPENAI_API_KEY='your-key'")
        sys.exit(1)

    if not args.ids:
        print("Usage: python generate_anxiety_images.py --ids draft_01,draft_02")
        print("       python generate_anxiety_images.py --ids all")
        print("       python generate_anxiety_images.py --list")
        return

    if args.ids.lower() == "all":
        prompts_to_generate = PROMPTS
    else:
        ids = [s.strip() for s in args.ids.split(",")]
        prompts_to_generate = [p for p in PROMPTS if p["id"] in ids]

    if not prompts_to_generate:
        print(f"No prompts found for: {args.ids}")
        return

    cost_per_image = {"low": 0.08, "medium": 0.11, "high": 0.24}
    estimated_cost = len(prompts_to_generate) * cost_per_image[args.quality]

    client = OpenAI(api_key=API_KEY)

    print(f"\n{'='*60}")
    print(f"ANXIETY AD IMAGE GENERATOR (OpenAI)")
    print(f"{'='*60}")
    print(f"Model: {MODEL}")
    print(f"Quality: {args.quality} (~${cost_per_image[args.quality]}/image)")
    print(f"Images to generate: {len(prompts_to_generate)}")
    print(f"Estimated cost: ~${estimated_cost:.2f}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"{'='*60}\n")

    successful = 0
    failed = 0
    generated_files = []

    for i, prompt_data in enumerate(prompts_to_generate, 1):
        print(f"[{i}/{len(prompts_to_generate)}] Generating {prompt_data['id']}: {prompt_data['name']}...")

        image_data = generate_image(client, prompt_data["prompt"], args.quality)

        if image_data:
            filepath = save_image(image_data, prompt_data["id"], OUTPUT_DIR)
            print(f"  Saved: {filepath}")
            successful += 1
            generated_files.append(str(filepath))
        else:
            print(f"  FAILED")
            failed += 1

        if i < len(prompts_to_generate):
            print(f"  Waiting {DELAY_BETWEEN_GENERATIONS}s...")
            time.sleep(DELAY_BETWEEN_GENERATIONS)

    print(f"\n{'='*60}")
    print(f"COMPLETE: {successful}/{len(prompts_to_generate)} images")
    if failed > 0:
        print(f"Failed: {failed}")
    print(f"{'='*60}\n")

    if generated_files:
        print("Generated files:")
        for f in generated_files:
            print(f"  {f}")


if __name__ == "__main__":
    main()
