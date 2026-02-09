#!/usr/bin/env python3
"""
CBDog Ad Image Generator - Batch 2 - OpenAI GPT-Image-1.5
Generates 11 native image ad photos for Facebook ad mockups
V3 Raw iPhone UGC style - documentary evidence, not ad concepts
Batch 2: 11 images for "5 Reasons Exercise Won't Fix Your Dog's Anxiety" funnel

Usage:
    python generate_cbdog_images_batch2.py --ids ad_01,ad_02
    python generate_cbdog_images_batch2.py --ids all
    python generate_cbdog_images_batch2.py --list
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
OUTPUT_DIR = Path(__file__).parent / "generated_ad_images_batch2"
DELAY_BETWEEN_GENERATIONS = 2  # seconds

# CBDog image prompts - Batch 2
# All 11 prompts from artifacts/image-concepts-batch2.md
PROMPTS = [
    {
        "id": "ad_01",
        "name": "The Leash Collection",
        "angle": "1-Flat Denial",
        "expr": "#2",
        "opener": "A tired dog is not a calm dog.",
        "contradiction": "Quantity That Feels Wrong",
        "prompt": "Raw iPhone photo taken to show a friend. Five or six different dog leashes hanging on wall hooks by a front door — different colors, different styles, some fabric, some leather, some retractable. The wall has scuff marks around the hooks. One leash is slightly off its hook. Visible keys, a mask hanging nearby, normal entryway clutter. Slightly blurry because shot one-handed while holding something. Single harsh overhead hallway light making hard shadows on the wall. Dust visible in the light beam. This is NOT a content photo — this is 'look how many leashes I own now' energy. Autofocus locked on wrong leash, another slightly soft. Tilted frame, casual grip, authentic frustration captured."
    },
    {
        "id": "ad_02",
        "name": "The Paw-Print Trail",
        "angle": "2-Flip",
        "expr": "#7",
        "opener": "That long walk is feeding the panic, not draining it.",
        "contradiction": "Evidence of Failure",
        "prompt": "Raw iPhone photo taken to show a friend. Muddy paw prints on hardwood floor leading from the entryway further into the house. The prints are still wet, glistening under the kitchen overhead light. Some prints are smeared where the dog didn't stop — trajectory shows movement, not settling. Floor shows dust, scratches, normal wear. A single shoe visible at frame edge. Shot looking down from standing. Harsh overhead light causing glare on the wet wood. Autofocus caught the floor texture, prints slightly soft. This is NOT a content photo — this is 'just got back from a 45-minute walk and look at this' energy. Tilted frame, one-handed grip, authentic exhaustion captured."
    },
    {
        "id": "ad_03",
        "name": "The Frayed Leash",
        "angle": "3-Attack Advice",
        "expr": "#10",
        "opener": "Everyone giving you exercise advice has never measured what's happening inside your dog.",
        "contradiction": "Evidence of Failure",
        "prompt": "Raw iPhone photo taken to show a friend. Close-up of a dog leash handle showing visible fraying, stress marks, threads coming loose where the dog has pulled repeatedly. The leash is laid on a kitchen counter with crumbs, a receipt, normal mess around it. Harsh overhead kitchen light making the frayed threads cast tiny shadows. The weave is coming apart in one spot. This is NOT a content photo — this is 'look what [X] months of walks did' energy. Autofocus slightly off, background counter in focus instead of the frayed section. One-handed shot, slightly tilted, authentic weariness captured."
    },
    {
        "id": "ad_04",
        "name": "The Playlist",
        "angle": "4-Attack Trade-Off",
        "expr": "#15",
        "opener": "You can't outrun a chemical imbalance.",
        "contradiction": "Wait What? Detail",
        "prompt": "Raw iPhone photo of another phone screen showing a music app with a playlist called 'Calming Dog Music' or similar. The play count shows hundreds of hours. Screen has fingerprint smudges visible. The phone is laying on a messy kitchen counter — crumbs, a half-drunk coffee cup, mail pile. Overhead light causing screen glare in one corner. This is NOT a content photo — this is 'when the calming playlist has 400 hours and nothing changed' energy. Thumb edge visible at bottom of frame. Shot one-handed, slightly crooked, authentic irony captured."
    },
    {
        "id": "ad_05",
        "name": "The Couch Cushion",
        "angle": "5-Quit Proof",
        "expr": "#18",
        "opener": "If exercise fixed dog anxiety, yours would be calm by now.",
        "contradiction": "Evidence of Failure",
        "prompt": "Raw iPhone photo taken to show a friend. Single couch cushion showing visible wear — claw marks in the fabric, pilling, areas where a dog has circled and scratched trying to settle. The couch is a normal lived-in color (beige, grey, brown). Natural light from a nearby window creating uneven lighting, one side brighter. Remote control visible at edge of frame. This is NOT a content photo — this is 'this is what resting looks like for my dog' energy. Shot from standing looking down, phone tilted, one-handed grip. Autofocus slightly off, authentic resignation captured."
    },
    {
        "id": "ad_06",
        "name": "The Water Bowl Puddle",
        "angle": "6-Real Variable",
        "expr": "#22",
        "opener": "Anxiety isn't excess energy. It's a depleted reset mechanism.",
        "contradiction": "Evidence of Failure",
        "prompt": "Raw iPhone photo taken to show a friend. Dog water bowl nearly empty with a wet puddle surrounding it on the kitchen floor. Water sloshed over the rim from frantic drinking. The bowl is stainless steel, showing water marks. Tile or vinyl floor with the reflection of the overhead light visible in the puddle. A few pieces of kibble floating. This is NOT a content photo — this is 'post-walk hydration situation' energy. Shot looking down at floor, harsh overhead kitchen light causing glare in the puddle. Phone held at awkward angle, slightly blurry, authentic tiredness captured."
    },
    {
        "id": "ad_07",
        "name": "The Sunrise Alarm",
        "angle": "7-Guilt",
        "expr": "#26",
        "opener": "The guilt you feel isn't proof you're a bad owner. It's proof you were handed the wrong tool.",
        "contradiction": "Object in Wrong Context",
        "prompt": "Raw iPhone photo taken in dark bedroom. Alarm clock or phone showing 5:15 AM glowing on a messy nightstand. Other items visible: phone charger cable, water glass with fingerprints, maybe a book. The bedroom is dark except for the clock glow and maybe a crack of early light through curtains. This is NOT a content photo — this is 'dog owner alarm time' energy. Phone camera struggling with low light, grainy image. Shot from bed level, one-handed, tilted frame. Authentic exhaustion captured before the day even starts."
    },
    {
        "id": "ad_08",
        "name": "The Grass Stains",
        "angle": "8-Protect",
        "expr": "#31",
        "opener": "Your dog isn't defective. Their reset mechanism just needs fuel.",
        "contradiction": "Evidence of Failure",
        "prompt": "Raw iPhone photo taken to show a friend. Pair of jeans or khaki shorts tossed on a washing machine or in a laundry basket, showing visible grass stains at both knees. Maybe some dirt smudges too. Laundry room or mudroom setting — detergent bottle visible, lint, normal mess. Harsh overhead utility light making the stains look vivid green against fabric. This is NOT a content photo — this is 'my fetch pants' energy. Shot from hip level, phone tilted, one-handed grip. Autofocus slightly off, authentic daily-grind captured."
    },
    {
        "id": "ad_09",
        "name": "The Dog Gate",
        "angle": "8-Protect",
        "expr": "#32",
        "opener": "The anxiety isn't who they are. It's what happens when the system runs empty.",
        "contradiction": "Object in Wrong Context",
        "prompt": "Raw iPhone photo taken to show a friend. Baby gate installed in doorway showing visible scratch marks on both the gate and the door frame around it. The gate is white or wood colored. Deep scratches where a dog has clawed trying to get through. Natural light from the next room creating uneven exposure. This is NOT a content photo — this is 'the gate that was supposed to help' energy. Shot from hip level looking at the doorway, phone slightly crooked, one-handed. Paint chips visible where scratches went deep. Authentic frustration captured."
    },
    {
        "id": "ad_10",
        "name": "The Recall Notes",
        "angle": "9-Identity",
        "expr": "#34",
        "opener": "That instinct that told you 'this isn't working' was correct.",
        "contradiction": "Wait What? Detail",
        "prompt": "Raw iPhone photo of another phone screen showing a notes app with a detailed list. The list shows weeks of trying different things: 'Week 1: 2 hr walks', 'Week 2: added morning + evening', 'Week 3: tried the puzzle toy', etc. Long list showing many weeks of experiments. Phone laying on messy kitchen counter — coffee cup ring stain, crumbs, pen nearby. This is NOT a content photo — this is 'my anxiety experiment log' energy. Screen has fingerprint smudges. Shot one-handed, slightly tilted. Autofocus slightly off, background sharper than screen. Authentic data-driven desperation captured."
    },
    {
        "id": "ad_11",
        "name": "The Double Bowls",
        "angle": "10-Science",
        "expr": "#38",
        "opener": "Physical fatigue and nervous system regulation run on completely different tracks.",
        "contradiction": "Object in Wrong Context",
        "prompt": "Raw iPhone photo taken to show a friend. Two dog bowls on kitchen floor — one food, one water — positioned oddly far apart or at wrong angles, like they've been pushed around by a restless dog. Water splashed around the water bowl. Kibble crumbs around the food bowl. Kitchen floor showing normal wear, maybe a dropped piece of mail nearby. Harsh overhead kitchen light casting shadows from the bowls. This is NOT a content photo — this is 'why are the bowls always in different places' energy. Shot looking down from standing, phone tilted, one-handed grip. Authentic daily mystery captured."
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


def generate_image(client: OpenAI, prompt_text: str, quality: str = "high"):
    """Generate a single image using OpenAI GPT-Image-1.5"""

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
    parser = argparse.ArgumentParser(description="Generate CBDog ad images Batch 2 with OpenAI GPT-Image-1.5")
    parser.add_argument("--ids", type=str, help="Comma-separated ad IDs (e.g., ad_01,ad_02) or 'all'")
    parser.add_argument("--list", action="store_true", help="List all prompts")
    parser.add_argument("--quality", type=str, default="high", choices=["low", "medium", "high"],
                        help="Image quality: low (~$0.08), medium (~$0.11), high (~$0.24)")
    parser.add_argument("--batch", type=int, help="Generate a specific batch (1-3, batch 1=5 images, batch 2=5 images, batch 3=1 image)")
    args = parser.parse_args()

    if args.list:
        print("\n=== CBDog Ad Image Prompts - Batch 2 ===\n")
        for i, p in enumerate(PROMPTS, 1):
            print(f"  {p['id']}: {p['name']} ({p['angle']}) - {p['expr']}")
        return

    if not API_KEY:
        print("Error: OPENAI_API_KEY not set")
        print("Set with: export OPENAI_API_KEY='your-key'")
        sys.exit(1)

    if not args.ids and not args.batch:
        print("Usage: python generate_cbdog_images_batch2.py --ids ad_01,ad_02")
        print("       python generate_cbdog_images_batch2.py --ids all")
        print("       python generate_cbdog_images_batch2.py --batch 1  (generates ads 1-5)")
        print("       python generate_cbdog_images_batch2.py --batch 2  (generates ads 6-10)")
        print("       python generate_cbdog_images_batch2.py --batch 3  (generates ad 11)")
        print("       python generate_cbdog_images_batch2.py --list")
        return

    if args.batch:
        if args.batch == 1:
            prompts_to_generate = PROMPTS[0:5]
        elif args.batch == 2:
            prompts_to_generate = PROMPTS[5:10]
        elif args.batch == 3:
            prompts_to_generate = PROMPTS[10:11]
        else:
            print(f"Invalid batch number: {args.batch}. Use 1, 2, or 3.")
            return
        print(f"Generating batch {args.batch}")
    elif args.ids.lower() == "all":
        prompts_to_generate = PROMPTS
    else:
        ids = [s.strip() for s in args.ids.split(",")]
        prompts_to_generate = [p for p in PROMPTS if p["id"] in ids]

    if not prompts_to_generate:
        print(f"No prompts found for: {args.ids if args.ids else f'batch {args.batch}'}")
        return

    cost_per_image = {"low": 0.08, "medium": 0.11, "high": 0.24}
    estimated_cost = len(prompts_to_generate) * cost_per_image[args.quality]

    client = OpenAI(api_key=API_KEY)

    print(f"\n{'='*60}")
    print(f"CBDOG AD IMAGE GENERATOR - BATCH 2 (OpenAI)")
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
