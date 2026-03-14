#!/usr/bin/env python3
"""
Mat & Vic's LP01 — Toe Touch Stretch Batch
10 ads: German women (25ish) doing seated toe touch stretch
Camera in front showing bottom of socks while stretching
Contradiction: Aesthetic/fit woman vs disaster sock bottoms
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

# Toe touch stretch concepts - aesthetic woman, disaster sock bottoms visible
PROMPTS = [
    {
        "id": "stretch_01",
        "name": "Hole in Heel",
        "prompt": "Raw iPhone photo, attractive 25 year old Gymshark fitness influencer with blonde hair, toned athletic body, sitting on yoga mat doing seated toe touch stretch, legs extended, reaching for toes. Camera positioned in front at floor level showing the BOTTOM of her socks facing camera. Her white socks have visible hole at the heel showing skin through. Gym or living room floor, natural window light. Gorgeous fit influencer but sock bottoms are embarrassing."
    },
    {
        "id": "stretch_02",
        "name": "Worn Through Sole",
        "prompt": "Raw iPhone photo, attractive 25 year old Gymshark fitness influencer with brown hair on hardwood floor doing seated forward fold stretch, reaching past toes. Camera at floor level in front, sock bottoms visible facing camera. Grey athletic socks worn completely thin at the ball of foot, almost see-through. Apartment living room, morning light. Athletic outfit, messy bun, but sock bottoms tell a different story."
    },
    {
        "id": "stretch_03",
        "name": "Pilled Bottom",
        "prompt": "Raw iPhone photo, 25 year old athletic German woman on exercise mat doing toe touch stretch. Camera positioned low in front showing bottom of her fuzzy socks facing lens. Sock bottoms are heavily pilled and matted, grey with dirt. Home gym setting, rubber flooring visible, dumbbells in background. She looks fit and put-together but sock bottoms are gross."
    },
    {
        "id": "stretch_04",
        "name": "Stained Soles",
        "prompt": "Raw iPhone photo, attractive 25 year old Gymshark fitness influencer with dark hair stretching on carpet, seated toe touch position. Camera at floor level facing her, showing bottom of white socks with visible yellow/brown stains on the soles. Living room carpet, couch in background, afternoon light. Cute loungewear but sock bottoms are visibly dirty and stained."
    },
    {
        "id": "stretch_05",
        "name": "Double Holes",
        "prompt": "Raw iPhone photo, attractive 25 year old Gymshark fitness influencer on yoga mat doing hamstring stretch reaching for toes. Camera low in front capturing sock bottoms. Both socks have holes - one at heel, one at big toe, skin visible through both. Studio apartment, minimalist decor, large window. Instagram-ready outfit but sock situation is a disaster."
    },
    {
        "id": "stretch_06",
        "name": "Threadbare Heel",
        "prompt": "Raw iPhone photo, 25 year old red-haired German woman doing seated stretch on wooden floor. Camera positioned in front at ground level, sock bottoms facing lens. Heel area completely threadbare and transparent, you can see skin through the worn fabric. Scandinavian-style apartment, plants visible. Aesthetic space, aesthetic woman, destroyed socks."
    },
    {
        "id": "stretch_07",
        "name": "Dirty Grey",
        "prompt": "Raw iPhone photo, attractive 25 year old Gymshark fitness influencer in workout clothes doing toe touch stretch on gym floor. Camera at floor level in front, capturing sole of socks. Once-white socks now grey and dirty on the bottom, visible grime. Commercial gym floor, equipment in background. Fitness influencer look completely undermined by sock bottoms."
    },
    {
        "id": "stretch_08",
        "name": "Bunched and Torn",
        "prompt": "Raw iPhone photo, attractive 25 year old Gymshark fitness influencer stretching on bedroom floor, reaching for feet. Camera low in front showing sock bottoms. Socks bunched weird with small tear at the ball of foot. Bedroom setting, bed frame visible, soft morning light. Cozy aesthetic ruined by falling-apart socks."
    },
    {
        "id": "stretch_09",
        "name": "Worn Thin Toe",
        "prompt": "Raw iPhone photo, attractive 25 year old Gymshark fitness influencer on foam roller doing forward stretch. Camera at floor level facing her, sock soles visible. Toe area worn paper-thin, almost transparent, texture completely gone. Home fitness setup, resistance bands nearby. Dedicated to fitness but not to sock replacement."
    },
    {
        "id": "stretch_10",
        "name": "Complete Blowout",
        "prompt": "Raw iPhone photo, 25 year old German university student doing homework stretch break on dorm floor, toe touch position. Camera in front at floor level showing sock bottoms. One sock has complete blowout hole at heel, other has multiple small holes. Dorm room floor, textbooks scattered, laptop visible. Young, stylish, but sock situation is catastrophic."
    },
]

def generate_image(prompt_data):
    """Generate a single image using fal.ai"""
    try:
        result = fal_client.subscribe(
            MODEL,
            arguments={
                "prompt": prompt_data["prompt"],
                "aspect_ratio": "1:1",
                "num_images": 1,
            },
        )

        if result and "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]

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
    print("MAT & VIC'S LP01 — TOE TOUCH STRETCH BATCH")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print(f"Size: 512x512 (square)")
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
