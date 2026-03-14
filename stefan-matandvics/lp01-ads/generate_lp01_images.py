#!/usr/bin/env python3
"""
Mat & Vic's LP01 Ad Image Generator - fal.ai nanobanana2
Generates native image ad photos for Facebook ad mockups
V3 Raw iPhone UGC style - documentary evidence, not ad concepts

Usage:
    python generate_lp01_images.py --ids draft_01,draft_02
    python generate_lp01_images.py --ids all
    python generate_lp01_images.py --list
    python generate_lp01_images.py --ids draft_01,draft_02,draft_03,draft_04,draft_05  # sub-batch 1
"""

import argparse
import base64
import os
import sys
import time
import urllib.request
from pathlib import Path
from datetime import datetime

import fal_client

# Configuration
MODEL = "fal-ai/nano-banana-2"
FAL_KEY = os.environ.get("FAL_KEY", "")
OUTPUT_DIR = Path(__file__).parent / "generated_ad_images"
DELAY_BETWEEN_GENERATIONS = 2  # seconds

# Mat & Vic's LP01 image prompts - V3 Raw iPhone UGC
# Philosophy: 3-layer native test:
#   1. Would someone take this photo? (camera + scene)
#   2. Would they post it? (there's a reason — the contradiction)
#   3. Do you feel something before reading text? (contradiction does the work)
PROMPTS = [
    {
        "id": "draft_01",
        "name": "The 3pm Sock",
        "opener": "Soft socks are the most uncomfortable socks.",
        "prompt": "Raw iPhone photo taken to show a friend. POV looking down at my own feet under a desk at work — one sock is pulled halfway off, bunched around the ankle, clearly damp with visible sweat marks on the sock fabric. Single fluorescent tube overhead making everything yellow-green and slightly overexposed. The background has desk chair wheel, crumpled receipt, power strip with cables. This is NOT a content photo — this is 'my feet are killing me' energy. Autofocus locked on the desk edge so the sock is slightly soft, shot one-handed while sitting, desk edge cutting into frame. Bad angle, authentic 3pm office misery captured."
    },
    {
        "id": "draft_02",
        "name": "The Squeeze Test",
        "opener": "The softest socks are the least comfortable.",
        "prompt": "Raw iPhone photo taken to show a friend. A hand squeezing a pair of packaged socks in a store aisle — the plastic packaging crinkling under the squeeze, price tags dangling, harsh fluorescent store lighting blowing out the whites. The sock wall behind has dozens of options in different colors and packages. This is NOT a content photo — this is 'doing the test we all do' energy. Slightly tilted, motion blur from quick grab, thumb pressing into the soft package, store floor tiles visible at bottom. Shot one-handed while shopping, capturing the universal sock-shopping ritual."
    },
    {
        "id": "draft_03",
        "name": "The Damp Towel Comparison",
        "opener": "Soft socks are uncomfortable socks.",
        "prompt": "Raw iPhone photo taken to show a friend. A soft sock and a damp hand towel lying side by side on a bathroom counter — both slightly crumpled, both looking used and wrinkled. Bathroom vanity light overexposing one side, water spots visible on the counter, toothbrush and soap bottle at the edge of frame. This is NOT a content photo — this is 'realized something gross' energy. Off-angle shot, one item slightly out of focus, casual phone snap capturing the comparison that just clicked. The visual parallel between sock and damp towel is unmistakable."
    },
    {
        "id": "draft_04",
        "name": "The Stretched Elastic",
        "opener": "The most comfortable socks don't feel soft.",
        "prompt": "Raw iPhone photo taken to show a friend. Close-up of a sock's elastic band completely stretched out and loose around a calf — the once-snug cuff is now saggy and falling down, unable to grip. Natural indoor light from a window, slightly dim. My hand is visible at the edge trying to pull the sock up, but the elastic has given up. This is NOT a content photo — this is 'seriously?' energy. Awkward downward angle, bare leg visible, floor or carpet in background. The elastic is dead. Authentic sock failure captured."
    },
    {
        "id": "draft_05",
        "name": "The Heel Hole",
        "opener": "The softest sock is the worst sock.",
        "prompt": "Raw iPhone photo taken to show a friend. A single sock held up by one hand, showing a clear hole worn through the heel — the hole is obvious, you can see through it. Natural indoor light from a window making harsh shadows. Background is a laundry pile or unmade bed. This is NOT a content photo — this is 'another pair done' energy. One-handed grip visible, thumb near the hole, sock slightly wrinkled, background messy with clothes. Shot to document yet another sock failure. Bad angle, authentic resignation captured."
    },
    {
        "id": "draft_06",
        "name": "The Sweaty Shoe Interior",
        "opener": "Soft socks make your feet miserable.",
        "prompt": "Raw iPhone photo taken to show a friend. Looking down into an empty shoe after wearing all day — visible moisture marks and slight discoloration on the insole where sweat accumulated. Harsh overhead indoor lighting. The other shoe is visible at the edge, floor clutter around. This is NOT a content photo — this is 'look what my socks did' energy. Slightly out of focus, shot from above, one shoe removed hastily. The moisture evidence of soft socks failing to wick. Authentic foot-related disgust captured."
    },
    {
        "id": "draft_07",
        "name": "The Before/After Sock",
        "opener": "The softer the sock, the worse it feels.",
        "prompt": "Raw iPhone photo taken to show a friend. Two socks from the same pair laid side by side — one still looks new and fresh, the other is clearly worn out with stretched elastic, faded color, and pilling. Natural indoor light, laid on an unmade bed or wrinkled fabric. This is NOT a content photo — this is 'can you believe this' energy. Casual placement, slight shadow, one sock slightly overlapping the other. The degradation difference is stark. Shot to document the wear comparison. Authentic realization captured."
    },
    {
        "id": "draft_08",
        "name": "The Sock Aisle Hand",
        "opener": "Uncomfortable socks always start soft.",
        "prompt": "Raw iPhone photo taken to show a friend. A hand reaching into a wall of sock packaging in a store — overwhelming rows of different socks, all packaged, the hand touching one package to feel it. Harsh store fluorescent lights slightly blowing out. Price tags visible, store shelves receding into background. This is NOT a content photo — this is 'this is how I've always done it' energy. Tilted angle, motion blur from reaching, the ritual of touching socks to test them. Authentic sock shopping behavior captured."
    },
    {
        "id": "draft_09",
        "name": "The 3pm Adjustment",
        "opener": "Soft is what makes socks uncomfortable.",
        "prompt": "Raw iPhone photo taken to show a friend. A hand reaching down toward a sock-covered foot under a desk — about to pull up or adjust the sock that's slipping down. Office fluorescent lighting, slightly dim under the desk. Cables, desk legs, shoes visible. This is NOT a content photo — this is 'fixing my sock again' energy. Under-desk perspective, awkward angle, the universal mid-afternoon sock adjustment. Shot one-handed while reaching. Authentic office sock frustration captured."
    },
    {
        "id": "draft_10",
        "name": "The Drawer Graveyard",
        "opener": "The sock that feels best is the sock that wears worst.",
        "prompt": "Raw iPhone photo taken to show a friend. An open sock drawer filled with worn-out, mismatched, stretched, and sad-looking socks — a graveyard of soft sock failures. Natural indoor light, overhead angle looking down into the drawer. Other drawers visible at edges, bedroom clutter in background. This is NOT a content photo — this is 'I need new socks again' energy. Some socks overlapping, varied colors and wear levels, no matching pairs visible. The accumulated evidence of soft sock failures. Authentic drawer frustration captured."
    },
    {
        "id": "draft_11",
        "name": "The Soft Label Close-up",
        "opener": "Soft socks are lying to you.",
        "prompt": "Raw iPhone photo taken to show a friend. Close-up of a sock package showing 'ULTRA SOFT' marketing text prominently, with the actual worn/pilled sock visible in the same frame next to it. Indoor lighting, counter or table surface. This is NOT a content photo — this is 'look at this lie' energy. Slightly out of focus on one element, the promise (label) versus the reality (worn sock) visible together. Casual angle, shot to document the marketing irony. Authentic frustration at false advertising captured."
    },
    {
        "id": "draft_12",
        "name": "The Wrong Body Part",
        "opener": "Touch is the worst way to buy socks.",
        "prompt": "Raw iPhone photo taken to show a friend. A hand touching and feeling a sock fabric in the foreground, with bare feet or feet in worn socks visible in the background — showing the disconnect between test method and actual use. Natural indoor light, floor visible. This is NOT a content photo — this is 'wait, this doesn't make sense' energy. Split focus trying to get both in frame, the hand testing what the feet will suffer. Awkward angle capturing both elements. Authentic realization of wrong method captured."
    },
    {
        "id": "draft_13",
        "name": "The Winning Display",
        "opener": "The softest sock wins in the aisle. It loses on your feet.",
        "prompt": "Raw iPhone photo taken to show a friend. A prominent display in a sock aisle featuring the plush/soft option — maybe with a 'bestseller' or 'popular' marker. Store fluorescent lighting. Other products visible around, typical retail clutter. This is NOT a content photo — this is 'they put these here on purpose' energy. Slightly tilted, store floor visible at bottom, the deliberate eye-level placement of soft socks. Shot to document the retail strategy. Authentic skepticism captured."
    },
    {
        "id": "draft_14",
        "name": "The Lifetime Pattern",
        "opener": "You've been choosing the wrong socks your entire life.",
        "prompt": "Raw iPhone photo taken to show a friend. Multiple pairs of worn-out socks in different styles and colors laid out together — stretched elastic, holes, pilling, fading across all of them. Natural indoor light, laid on floor or bed. This is NOT a content photo — this is 'every pair I've bought' energy. Casual arrangement, some overlapping, representing years of the same soft-sock mistake. The quantity tells the story of repeated failure. Authentic pattern recognition captured."
    },
    {
        "id": "draft_15",
        "name": "The Feet vs Hand",
        "opener": "Your feet hate soft socks.",
        "prompt": "Raw iPhone photo taken to show a friend. A hand holding a soft, plush sock in the foreground looking satisfied, while uncomfortable bare feet are visible in the background — just escaped from socks. Natural indoor light. This is NOT a content photo — this is 'my hand loves this, my feet hate it' energy. Split focus, trying to capture both perspectives, the conflict between hand's opinion and feet's experience. Awkward angle. Authentic realization captured."
    },
    {
        "id": "draft_16",
        "name": "The Bunched Heel",
        "opener": "Soft socks are the enemy of your feet.",
        "prompt": "Raw iPhone photo taken to show a friend. Close-up looking inside a shoe that's been pulled back slightly — showing the sock bunched and wrinkled inside, unable to maintain position. Indoor light, slightly dim. Finger pulling back the shoe heel to reveal the problem. This is NOT a content photo — this is 'every single day' energy. Awkward angle peering into shoe, the sock fabric bunched up and uncomfortable-looking. Authentic daily sock frustration captured."
    },
    {
        "id": "draft_17",
        "name": "The Vocabulary Confusion",
        "opener": "You don't want soft socks.",
        "prompt": "Raw iPhone photo taken to show a friend. Two sock packages side by side — one prominently labeled 'SOFT,' one labeled 'COMFORT' or 'ALL-DAY' — both packages look nearly identical otherwise. Store or home lighting. This is NOT a content photo — this is 'wait, these mean different things?' energy. One package slightly overlapping, background clutter visible. The vocabulary confusion consumers face. Casual angle. Authentic confusion captured."
    },
    {
        "id": "draft_18",
        "name": "The Failing Drawer",
        "opener": "Every soft sock in your drawer is failing you.",
        "prompt": "Raw iPhone photo taken to show a friend. POV looking down into an open sock drawer, my hand visible rifling through — every single pair visible has some issue (stretched, faded, pilled, mismatched). Bedroom overhead light making harsh shadows. This is NOT a content photo — this is 'trying to find one good pair' energy. Hand in motion, drawer partially pulled out, room visible at edges. Every option is compromised. Authentic morning sock-search frustration captured."
    },
    {
        "id": "draft_19",
        "name": "The Trap Setup",
        "opener": "Soft socks are a trap.",
        "prompt": "Raw iPhone photo taken to show a friend. A soft sock package positioned prominently at eye level on a store shelf, while other options are on bottom shelves below. Store fluorescent lighting, price tags visible, store floor at bottom of frame. This is NOT a content photo — this is 'they put these at eye level for a reason' energy. Slightly crooked shelves, retail environment. The deliberate placement visible. Authentic 'seeing the system' captured."
    },
    {
        "id": "draft_20",
        "name": "The Repeat Cycle",
        "opener": "You keep buying the wrong socks.",
        "prompt": "Raw iPhone photo taken to show a friend. A shopping bag with new sock packages inside, sitting on the floor next to a trash can with old worn-out socks visible inside it. Indoor overhead light. This is NOT a content photo — this is 'doing this again' energy. Floor clutter visible, both items slightly cut off at edges, the replacement cycle captured in one frame — buying new socks while throwing out the same thing. Authentic cycle recognition captured."
    }
]


def save_image(image_url: str, prompt_id: str, output_dir: Path) -> Path:
    """Download and save generated image"""
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prompt_id}_{timestamp}.png"
    filepath = output_dir / filename

    # Download the image from URL
    response = urllib.request.urlopen(image_url)
    image_bytes = response.read()

    with open(filepath, "wb") as f:
        f.write(image_bytes)

    # Also save a "latest" copy without timestamp for HTML reference
    latest_path = output_dir / f"{prompt_id}.png"
    with open(latest_path, "wb") as f:
        f.write(image_bytes)

    return filepath


def generate_image(prompt_text: str):
    """Generate a single image using fal.ai nanobanana2"""
    try:
        result = fal_client.subscribe(
            MODEL,
            arguments={
                "prompt": prompt_text,
                "image_size": "square_hd",  # 1024x1024
                "num_images": 1,
                "enable_safety_checker": True
            }
        )

        if result and "images" in result and len(result["images"]) > 0:
            return result["images"][0]["url"]

        return None

    except Exception as e:
        print(f"  ERROR: {str(e)}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Generate Mat & Vic's LP01 ad images with fal.ai nanobanana2")
    parser.add_argument("--ids", type=str, help="Comma-separated draft IDs (e.g., draft_01,draft_02) or 'all'")
    parser.add_argument("--list", action="store_true", help="List all prompts")
    args = parser.parse_args()

    if args.list:
        print("\n=== Mat & Vic's LP01 Ad Image Prompts ===\n")
        for p in PROMPTS:
            print(f"  {p['id']}: {p['name']}")
            print(f"    Opener: {p['opener'][:50]}...")
        return

    if not FAL_KEY:
        print("Error: FAL_KEY not set")
        print("Set with: export FAL_KEY='your-key'")
        sys.exit(1)

    if not args.ids:
        print("Usage: python generate_lp01_images.py --ids draft_01,draft_02")
        print("       python generate_lp01_images.py --ids all")
        print("       python generate_lp01_images.py --list")
        print("\nSub-batch example (5 at a time):")
        print("       python generate_lp01_images.py --ids draft_01,draft_02,draft_03,draft_04,draft_05")
        return

    if args.ids.lower() == "all":
        prompts_to_generate = PROMPTS
    else:
        ids = [s.strip() for s in args.ids.split(",")]
        prompts_to_generate = [p for p in PROMPTS if p["id"] in ids]

    if not prompts_to_generate:
        print(f"No prompts found for: {args.ids}")
        return

    print(f"\n{'='*60}")
    print(f"MAT & VIC'S LP01 AD IMAGE GENERATOR (fal.ai)")
    print(f"{'='*60}")
    print(f"Model: {MODEL}")
    print(f"Images to generate: {len(prompts_to_generate)}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"{'='*60}\n")

    successful = 0
    failed = 0
    generated_files = []

    for i, prompt_data in enumerate(prompts_to_generate, 1):
        print(f"[{i}/{len(prompts_to_generate)}] Generating {prompt_data['id']}: {prompt_data['name']}...")

        image_url = generate_image(prompt_data["prompt"])

        if image_url:
            filepath = save_image(image_url, prompt_data["id"], OUTPUT_DIR)
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
