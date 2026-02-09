#!/usr/bin/env python3
"""
CBDog Ad Image Generator - OpenAI GPT-Image-1.5
Generates native image ad photos for Facebook ad mockups
V3 Raw iPhone UGC style - documentary evidence, not ad concepts
Batch 1: 20 images for "5 Reasons Exercise Won't Fix Your Dog's Anxiety" funnel

Usage:
    python generate_cbdog_images.py --ids ad_01,ad_02
    python generate_cbdog_images.py --ids all
    python generate_cbdog_images.py --list
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

# CBDog image prompts - Batch 1
# All 20 prompts from artifacts/image-concepts.md
PROMPTS = [
    {
        "id": "ad_01",
        "name": "Still Panting on the Dog Bed",
        "angle": "1-Flat Denial",
        "opener": "Exercise doesn't calm anxious dogs.",
        "prompt": "Raw iPhone photo taken to show a friend. A medium-sized dog collapsed on a worn dog bed, tongue hanging out, panting hard, eyes still alert. Shot from standing looking straight down. Single harsh overhead light making yellow cast and hard shadows. The dog bed is pushed against a beige wall, has visible dog hair embedded in the fabric. Floor is scratched hardwood with dust in the corners. A slobbery tennis ball sits on the floor near the bed. The dog looks exhausted but the eyes are wide and watchful, not relaxed. This is NOT a content photo - this is 'look at this, she JUST got back from a walk' energy. Thumb shadow visible on edge from holding phone one-handed. Bad angles, casual grip."
    },
    {
        "id": "ad_02",
        "name": "The Worn-Out Sneakers",
        "angle": "1-Flat Denial",
        "opener": "More walks won't fix this.",
        "prompt": "Raw iPhone photo taken to show a friend. A pair of running shoes next to front door, soles visibly worn down at the heels, laces dirty and frayed. Shot from inside entryway looking down at the floor. Single fluorescent ceiling light making everything slightly green. Dirty welcome mat underneath, scuffed baseboards, a dog leash hanging on a hook above. The shoes are kicked off at an angle, not arranged. Some dog hair visible on the mat. The sole wear pattern shows thousands of miles. This is NOT a content photo - this is 'look how destroyed these are from walking her' energy. Autofocus slightly soft on background, sharp on shoes."
    },
    {
        "id": "ad_03",
        "name": "The Mile Tracker",
        "angle": "2-Flip",
        "opener": "You're making your dog's anxiety worse with every extra walk.",
        "prompt": "Raw iPhone photo taken to show a friend. A smartphone propped on a kitchen counter, screen showing 15,847 steps on a fitness app. Shot from standing looking down at the counter. Overhead fluorescent making yellow-green cast. Counter has water rings, crumbs, a dog leash coiled nearby, half-empty water bottle. The phone screen is slightly overexposed from overhead light reflection. Background shows corner of kitchen with messy items. This is NOT a content photo - this is 'look at this insane step count' energy. Slight motion blur on background from hand movement."
    },
    {
        "id": "ad_04",
        "name": "The Pile of Fetch Toys",
        "angle": "2-Flip",
        "opener": "The more you exercise an anxious dog, the more anxious they become.",
        "prompt": "Raw iPhone photo taken to show a friend. A basket overflowing with dog toys - tennis balls (some new, some chewed), frisbees, rope toys, squeaky toys. At least 8-10 toys visible. Shot from above looking into the basket. Basket on worn carpet with visible dog hair and dust bunnies. Some toys have fallen out onto the floor. Late afternoon window light creating warm patch but also harsh shadows. The toys show varying levels of wear - some shredded, some barely used. This is NOT a content photo - this is 'we've tried EVERYTHING' energy. Thumb partially visible at edge of frame."
    },
    {
        "id": "ad_05",
        "name": "The Quote on the Fridge",
        "angle": "3-Attack Advice",
        "opener": "'A tired dog is a calm dog' is the biggest lie in pet ownership.",
        "prompt": "Raw iPhone photo taken to show a friend. A refrigerator door covered with magnets, photos, grocery list. A dog-themed magnet or printout visible among the clutter with text about dogs. Shot straight-on from kitchen. Fluorescent overhead light making everything slightly yellow. Dog bowl visible on floor at bottom of frame. A leash hangs on a hook nearby. The fridge surface has fingerprints and smudges. Real family photos, takeout menus, appointment reminders visible but not readable. This is NOT a content photo - this is 'look at this advice I've been following' energy. Some glare on fridge surface from light."
    },
    {
        "id": "ad_06",
        "name": "The Old Dog Book",
        "angle": "3-Attack Advice",
        "opener": "The advice you keep hearing was made before we knew anything about dog anxiety.",
        "prompt": "Raw iPhone photo taken to show a friend. An old dog training book on a cluttered coffee table, clearly from the 80s or 90s - worn cover, dog-eared pages, cracked spine, dated font and imagery. Shot from above looking down. Natural light from window creating harsh shadows across the table. Coffee mug ring stain on table surface. A modern dog toy or treat visible nearby for contrast. Other items on table - remotes, coasters, mail. This is NOT a content photo - this is 'this is literally what people still recommend' energy. Book is slightly tilted, casual placement."
    },
    {
        "id": "ad_07",
        "name": "The Trail App Map",
        "angle": "4-Attack Trade-Off",
        "opener": "You thought if you walked far enough, the anxiety would stop. It doesn't work that way.",
        "prompt": "Raw iPhone photo taken to show a friend. A smartphone lying flat on a kitchen counter, screen showing a walking/hiking app with a long completed route visible - many miles logged. Shot from above looking down at the counter. Overhead kitchen light creating reflection on screen edge. Counter has everyday clutter - mail, keys, a dog leash. The route on the screen is clearly long and looping. Kitchen in background is lived-in, not staged. This is NOT a content photo - this is 'look how far I walked today' energy. Screen slightly tilted, one-handed capture."
    },
    {
        "id": "ad_08",
        "name": "The Ignored Ball",
        "angle": "4-Attack Trade-Off",
        "opener": "There's no amount of fetch that fixes a nervous system stuck in alarm mode.",
        "prompt": "Raw iPhone photo taken to show a friend. A slobbery, dirt-covered tennis ball in foreground on hardwood floor, in sharp focus. In the background, slightly out of focus, a dog lying down but with alert body language - ears up, eyes wide and watchful, body tense not relaxed. Shot from low angle near floor level. Late afternoon light from window. Floor has scratches and some dog hair. The ball has teeth marks and grass stains. This is NOT a content photo - this is 'we just played fetch for 45 minutes and look at her' energy. Slight dutch angle from holding phone low."
    },
    {
        "id": "ad_09",
        "name": "The Step Counter Watch",
        "angle": "5-Quit Proof",
        "opener": "You've already proven exercise doesn't work. How many miles did it take?",
        "prompt": "Raw iPhone photo taken to show a friend. Close-up of a wrist wearing a fitness watch/tracker, screen showing high step count around 12,000-15,000. The wrist looks slightly sweaty, maybe some dirt. Hand is resting on knee or thigh. Background is blurred living room or porch. Natural light. The watch face is in sharp focus. This is NOT a content photo - this is 'look at this number from today alone' energy. Shot quickly, slightly off-center framing."
    },
    {
        "id": "ad_10",
        "name": "The Ball Chucker on the Ground",
        "angle": "5-Quit Proof",
        "opener": "Your arm gave out from throwing the ball. The anxiety didn't.",
        "prompt": "Raw iPhone photo taken to show a friend. A ball launcher/chucker lying abandoned on patchy grass, with 3-4 tennis balls scattered nearby. Shot from standing looking down. Late afternoon sun creating long shadows. Grass has brown patches and bare spots. The chucker has grass stains and wear marks. Backyard fence visible in background. This is NOT a content photo - this is 'I literally couldn't throw anymore' energy. Casual framing, some grass in soft focus at frame edges."
    },
    {
        "id": "ad_11",
        "name": "The Empty Dog Bed",
        "angle": "6-Real Variable",
        "opener": "Your dog doesn't have an energy problem. They have a nervous system problem.",
        "prompt": "Raw iPhone photo taken to show a friend. A dog bed against a wall that looks pristine and unused - no indentations, no dog hair on it. But the floor AROUND the bed is scratched, has dog hair, maybe a chewed sock nearby. Shot from hallway looking into room. Mixed lighting from overhead and window. The bed looks brand new in contrast to the worn floor around it. This is NOT a content photo - this is 'she has 3 beds and uses none of them' energy. Door frame slightly visible at edge."
    },
    {
        "id": "ad_12",
        "name": "Two Dogs at the Park",
        "angle": "6-Real Variable",
        "opener": "The dogs who are calm aren't more exercised. They have something in their system yours is missing.",
        "prompt": "Raw iPhone photo taken to show a friend. Dog park scene with two dogs visible - one in background lying relaxed in the grass, totally calm. One in foreground showing anxious body language - panting hard, ears alert, body tense. Shot at dog park. Chain link fence visible. Harsh afternoon sunlight creating strong shadows. Ground has bare patches where dogs have worn down the grass. This is NOT a content photo - this is 'same park same walk, look at the difference' energy. Shot quickly, slightly off-kilter framing."
    },
    {
        "id": "ad_13",
        "name": "The Calendar of Walks",
        "angle": "7-Guilt",
        "opener": "You didn't fail your dog. You followed advice that was never designed for what's actually wrong.",
        "prompt": "Raw iPhone photo taken to show a friend. A wall calendar or desk planner with handwritten notes about walk times, miles, or schedules visible. Shot from standing looking at wall or desk. Kitchen or home office context. Messy handwriting, some smudges, maybe something crossed out. Other home items visible in frame. Natural light from window. This is NOT a content photo - this is 'I literally schedule my whole life around her walks' energy. Calendar slightly at angle, not straight-on product shot."
    },
    {
        "id": "ad_14",
        "name": "The Couch After the Walk",
        "angle": "7-Guilt",
        "opener": "You're not lazy. You're exhausted from trying the wrong thing.",
        "prompt": "Raw iPhone photo taken to show a friend. POV shot looking down at own legs stretched out on a couch, still wearing dirty running shoes. A dog leash is visible on the couch cushion nearby. Shot from person's perspective as if they just collapsed. Living room lighting, maybe TV glow visible. The shoes are dirty from the walk. This is NOT a content photo - this is 'just got home can't move' energy. One-handed shot, slightly tilted perspective."
    },
    {
        "id": "ad_15",
        "name": "The Empty Food Bowl",
        "angle": "8-Protect",
        "opener": "Your dog's alarm system isn't broken. It's starving.",
        "prompt": "Raw iPhone photo taken to show a friend. Two dog bowls on a mat on kitchen floor - food bowl empty with some kibble crumbs scattered around, water bowl also nearly empty. Shot from above or low angle. Kitchen floor visible with crumbs and some dog hair. The feeding mat is slightly askew. Harsh overhead fluorescent light. This is NOT a content photo - this is 'she just ate and she's still not settled' energy. Thumb shadow at edge from one-handed shot."
    },
    {
        "id": "ad_16",
        "name": "The Vet Paperwork",
        "angle": "8-Protect",
        "opener": "There's nothing wrong with your dog. There's something missing.",
        "prompt": "Raw iPhone photo taken to show a friend. A stack of paperwork on a kitchen counter - clearly vet visit receipts and records, some with coffee ring stains. Shot from above. Vet clinic letterhead visible but details blurred. Kitchen counter shows everyday clutter. Overhead lighting making harsh shadows. The stack suggests multiple visits. This is NOT a content photo - this is '4 visits and they say nothing is wrong' energy. Papers slightly scattered, not neat pile."
    },
    {
        "id": "ad_17",
        "name": "The Walk Route (Again)",
        "angle": "9-Identity",
        "opener": "You knew the walks weren't enough. You were right.",
        "prompt": "Raw iPhone photo taken to show a friend. View through a house window looking out at a suburban street/sidewalk - the typical neighborhood walking route. Shot from inside, window has some fingerprints/smudges visible. Living room reflected in glass. Morning or evening light on the street outside. The view is familiar, mundane. This is NOT a content photo - this is 'same route same nothing' energy. Window frame visible, not perfectly centered."
    },
    {
        "id": "ad_18",
        "name": "The Kitchen at 6am",
        "angle": "9-Identity",
        "opener": "The exhaustion you feel isn't weakness. It's evidence the approach was wrong.",
        "prompt": "Raw iPhone photo taken to show a friend. Kitchen scene before dawn - coffee maker with light on, dim pre-sunrise light through window. A dog leash visible on the counter. Maybe a phone or clock showing early time like 5:30 or 6:00. The kitchen is shadowy but functional. This is NOT a content photo - this is 'another 5:30am walk before work' energy. Low light creating grain, slightly blurry from slow shutter."
    },
    {
        "id": "ad_19",
        "name": "The Watch After the Walk",
        "angle": "10-Science",
        "opener": "Researchers measured cortisol after a 2-hour walk. It hadn't budged.",
        "prompt": "Raw iPhone photo taken to show a friend. Close-up of fitness watch on wrist showing workout completed - duration around 2 hours or 120 minutes visible. Wrist looks tired, maybe resting on table or steering wheel. Background blurred. The specific time (2 hours) is clearly visible on screen. This is NOT a content photo - this is 'exactly what the studies measured' energy. Quick snap, focused on watch face."
    },
    {
        "id": "ad_20",
        "name": "The Dog Park Aftermath",
        "angle": "10-Science",
        "opener": "Wolves rest 16 hours a day. They don't need exhaustion to stay calm.",
        "prompt": "Raw iPhone photo taken to show a friend. Nearly empty dog park in late afternoon - long shadows, golden hour light. Chain link fence visible. Ground churned up from dogs playing. One dog visible in mid-distance, standing alert - ears up, tail stiff, scanning. The park looks like everyone else has left. This is NOT a content photo - this is 'everyone else left an hour ago and she still won't go' energy. Wide shot showing the emptiness."
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
    parser = argparse.ArgumentParser(description="Generate CBDog ad images with OpenAI GPT-Image-1.5")
    parser.add_argument("--ids", type=str, help="Comma-separated ad IDs (e.g., ad_01,ad_02) or 'all'")
    parser.add_argument("--list", action="store_true", help="List all prompts")
    parser.add_argument("--quality", type=str, default="high", choices=["low", "medium", "high"],
                        help="Image quality: low (~$0.08), medium (~$0.11), high (~$0.24)")
    parser.add_argument("--batch", type=int, help="Generate a specific batch (1-4, each batch is 5 images)")
    args = parser.parse_args()

    if args.list:
        print("\n=== CBDog Ad Image Prompts ===\n")
        for i, p in enumerate(PROMPTS, 1):
            print(f"  {p['id']}: {p['name']} ({p['angle']})")
        return

    if not API_KEY:
        print("Error: OPENAI_API_KEY not set")
        print("Set with: export OPENAI_API_KEY='your-key'")
        sys.exit(1)

    if not args.ids and not args.batch:
        print("Usage: python generate_cbdog_images.py --ids ad_01,ad_02")
        print("       python generate_cbdog_images.py --ids all")
        print("       python generate_cbdog_images.py --batch 1  (generates ads 1-5)")
        print("       python generate_cbdog_images.py --batch 2  (generates ads 6-10)")
        print("       python generate_cbdog_images.py --list")
        return

    if args.batch:
        start_idx = (args.batch - 1) * 5
        end_idx = start_idx + 5
        prompts_to_generate = PROMPTS[start_idx:end_idx]
        print(f"Generating batch {args.batch} (ads {start_idx + 1}-{min(end_idx, len(PROMPTS))})")
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
    print(f"CBDOG AD IMAGE GENERATOR (OpenAI)")
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
