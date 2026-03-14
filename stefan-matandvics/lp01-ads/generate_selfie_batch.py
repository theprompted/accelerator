#!/usr/bin/env python3
"""
Mat & Vic's LP01 — Mirror Selfie Batch
10 ads: Beautiful German women (25ish) doing mirror selfies
Contradiction: Aesthetic woman vs disaster socks
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime

import fal_client

MODEL = "fal-ai/nano-banana-2"
FAL_KEY = os.environ.get("FAL_KEY", "")
OUTPUT_DIR = Path(__file__).parent / "generated_ad_images"

# Mirror selfie concepts - aesthetic woman, disaster socks
PROMPTS = [
    {
        "id": "selfie_01",
        "name": "Hole in Heel",
        "opener": "Soft socks are the most uncomfortable socks.",
        "prompt": "Raw iPhone mirror selfie in bedroom, 25 year old German woman with blonde hair, aesthetic outfit, taking full body selfie, BUT her white socks have a visible hole at the heel showing skin through. Harsh bedroom ceiling light, slightly tilted phone, bathroom mirror with toothpaste specks, real messy bedroom floor visible. The woman looks put-together but the socks betray her. Shot like she's about to post this then noticed the sock."
    },
    {
        "id": "selfie_02",
        "name": "Bunched Ankle",
        "opener": "The softest socks are the least comfortable.",
        "prompt": "Raw iPhone mirror selfie in bathroom, 25 year old German woman with brown hair, cute loungewear, full body shot, BUT one sock is completely bunched down around her ankle while the other is normal. Fluorescent bathroom light making everything slightly green, mirror has water spots, tile floor visible. She's posing but the sock situation is a mess. Authentic selfie energy."
    },
    {
        "id": "selfie_03",
        "name": "Sweat Stained",
        "opener": "Soft socks are uncomfortable socks.",
        "prompt": "Raw iPhone mirror selfie in gym locker room, 25 year old athletic German woman post-workout, sports bra and leggings, BUT her soft grey socks have visible dark sweat stains around the toes and heel. Harsh locker room lighting, metal lockers visible, slightly steamy mirror. She looks fit and healthy but the socks tell a different story. Post-workout selfie gone wrong."
    },
    {
        "id": "selfie_04",
        "name": "Pilled and Worn",
        "opener": "The most comfortable socks don't feel soft.",
        "prompt": "Raw iPhone mirror selfie in walk-in closet, 25 year old German woman with dark hair, stylish casual outfit, full body, BUT her fuzzy socks are visibly pilled and worn thin, almost see-through in patches. Closet lighting slightly dim, clothes and shoe boxes visible, wooden floor. Fashion-forward except the socks are clearly dying. Outfit check selfie."
    },
    {
        "id": "selfie_05",
        "name": "Elastic Gone",
        "opener": "The softest sock is the worst sock.",
        "prompt": "Raw iPhone mirror selfie in hotel room, 25 year old German woman in travel outfit, cute dress, BUT her ankle socks have lost all elastic and are drooping sadly down her ankles, bunched in wrinkles. Generic hotel mirror, bad hotel room lighting, luggage visible in background. She's dressed for a night out but the socks gave up. Travel selfie fail."
    },
    {
        "id": "selfie_06",
        "name": "Toe Hole",
        "opener": "Soft socks make your feet miserable.",
        "prompt": "Raw iPhone mirror selfie in apartment hallway, 25 year old German woman with red hair, casual home outfit, BUT her sock has a hole at the big toe with the toe poking through visibly. Apartment hallway lighting, coat hooks and shoes visible, wooden floor. She's comfortable at home but the sock is embarrassing. Just-noticed-the-hole energy."
    },
    {
        "id": "selfie_07",
        "name": "Mismatched Disasters",
        "opener": "The softer the sock, the worse it feels.",
        "prompt": "Raw iPhone mirror selfie in messy bedroom, 25 year old German woman in oversized sweater and shorts, BUT she's wearing two different soft socks - one with a hole, one with elastic gone. Bedroom mirror with stickers, fairy lights in background, clothes on floor. Cozy aesthetic ruined by sock chaos. Lazy Sunday selfie."
    },
    {
        "id": "selfie_08",
        "name": "Stretched Out",
        "opener": "Uncomfortable socks always start soft.",
        "prompt": "Raw iPhone mirror selfie in office bathroom, 25 year old German woman in business casual, blazer and slacks, BUT her soft socks are visibly stretched out and baggy around her ankles, no longer holding shape. Office bathroom fluorescent lighting, paper towel dispenser visible, tile floor. Professional top half, sock disaster bottom. Work bathroom mirror check."
    },
    {
        "id": "selfie_09",
        "name": "Faded and Thin",
        "opener": "Soft is what makes socks uncomfortable.",
        "prompt": "Raw iPhone mirror selfie in small apartment bathroom, 25 year old German woman in yoga clothes, sports bra visible, BUT her once-white socks are now grey, faded, thin enough to see skin through. Small bathroom mirror with products around it, harsh overhead light, bath mat visible. Fitness influencer aesthetic destroyed by sock reality. Pre-workout selfie."
    },
    {
        "id": "selfie_10",
        "name": "Multiple Holes",
        "opener": "The sock that feels best is the sock that wears worst.",
        "prompt": "Raw iPhone mirror selfie in dorm room, 25 year old German university student, casual student outfit, BUT her soft socks have multiple small holes - heel, toe, and side visible. Dorm room mirror, textbooks and laptop visible, IKEA furniture in background, string lights. Young and stylish but socks are falling apart. Study break selfie."
    },
]

def generate_image(prompt_data):
    """Generate a single image using fal.ai"""
    try:
        result = fal_client.subscribe(
            MODEL,
            arguments={
                "prompt": prompt_data["prompt"],
                "image_size": "square",
                "num_images": 1,
            },
        )

        if result and "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]

            # Download image
            import urllib.request
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{prompt_data['id']}_{timestamp}.png"
            filepath = OUTPUT_DIR / filename

            OUTPUT_DIR.mkdir(exist_ok=True)
            urllib.request.urlretrieve(image_url, filepath)

            # Also save clean version
            clean_filename = f"{prompt_data['id']}.png"
            clean_filepath = OUTPUT_DIR / clean_filename
            urllib.request.urlretrieve(image_url, clean_filepath)

            return filepath
        else:
            return None
    except Exception as e:
        print(f"  ERROR: {e}")
        return None

def main():
    if not FAL_KEY:
        print("Error: FAL_KEY not set")
        print("Set with: export FAL_KEY='your-key'")
        sys.exit(1)

    os.environ["FAL_KEY"] = FAL_KEY

    print("=" * 60)
    print("MAT & VIC'S LP01 — MIRROR SELFIE BATCH")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print(f"Images: {len(PROMPTS)}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)
    print()

    success = 0
    failed = 0

    for i, prompt_data in enumerate(PROMPTS, 1):
        print(f"[{i}/{len(PROMPTS)}] Generating {prompt_data['id']}: {prompt_data['name']}...")

        filepath = generate_image(prompt_data)

        if filepath:
            print(f"  Saved: {filepath}")
            success += 1
        else:
            print(f"  FAILED")
            failed += 1

        if i < len(PROMPTS):
            print(f"  Waiting 2s...")
            time.sleep(2)

    print()
    print("=" * 60)
    print(f"COMPLETE: {success}/{len(PROMPTS)} images")
    if failed:
        print(f"Failed: {failed}")
    print("=" * 60)

if __name__ == "__main__":
    main()
