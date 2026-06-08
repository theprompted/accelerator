#!/usr/bin/env python3
"""
Strawesome Batch 3 Image Generator - 12 images
"""

import base64
import os
import sys
import time
from pathlib import Path
from datetime import datetime
from openai import OpenAI

MODEL = "gpt-image-1.5"
API_KEY = os.environ.get("OPENAI_API_KEY", "")
OUTPUT_DIR = Path(__file__).parent / "generated_ad_images"

PROMPTS = [
    {
        "id": "draft_06",
        "name": "The Two Straws",
        "prompt": """Raw iPhone photo taken to show a friend. Metal straw and clear glass straw lying side by side on a kitchen counter. The metal straw has visible scratches and scuff marks from use. The glass straw looks pristine and clear. Single overhead LED creating harsh shadows, white balance slightly too warm. Counter has crumbs, a water ring stain, and a crumpled paper towel edge visible. Shot one-handed, slightly tilted. Autofocus locked on the glass straw so metal straw is slightly soft. Natural 'look at this weird thing I noticed' energy."""
    },
    {
        "id": "draft_07",
        "name": "The Scratch Pattern",
        "prompt": """Raw iPhone close-up photo of a metal straw showing visible scoring and scratches from repeated teeth contact. Multiple scratch lines running along the same section where mouth bites happen. Kitchen counter background blurred, single fluorescent overhead making everything yellow-green. The straw surface catches the light to show the damage clearly. Shot at close range to document the marks, slight motion blur from holding phone too close. 'Just noticed my straw looks like this' energy."""
    },
    {
        "id": "draft_08",
        "name": "The Bend Test",
        "prompt": """Raw iPhone photo showing two straws on a counter — a slightly curved/flexible glass straw showing visible bend, and a rigidly straight metal straw. The glass straw demonstrates give while metal stays perfectly straight. Kitchen background with cluttered counter, mixed lighting from window and overhead fluorescent. Shot from above at slight angle, one hand might be touching the straws. 'Comparing these two' energy. Autofocus slightly off, captured quickly."""
    },
    {
        "id": "draft_09",
        "name": "The Morning After",
        "prompt": """Raw iPhone photo of a drinking glass with a visible chip on the rim, metal straw resting inside or next to it. The chip is clearly from impact — small triangular piece missing from the glass edge. Morning kitchen light from window, counter has coffee rings and toast crumbs. The metal straw is positioned near the chip, implying it caused the damage. 'Wait how did this happen' energy. Shot quickly to document the damage."""
    },
    {
        "id": "draft_10",
        "name": "The Eco-Friendly Starter Kit",
        "prompt": """Raw iPhone photo of a casual pile of eco-friendly items on a kitchen counter or shelf — reusable grocery bag, bamboo utensils in a holder, metal straw prominent in the group. NOT a styled flatlay — these are items that live together, slightly messy. Mixed lighting, some items overlapping casually. The metal straw is visible among the 'trusted' eco products. 'My sustainable corner' energy but not curated. Some items slightly dusty. Shot quickly without arranging."""
    },
    {
        "id": "draft_11",
        "name": "Inside vs Outside",
        "prompt": """Raw iPhone close-up photo of a metal straw that has been cut in half, showing dark brown/gray residue and gunk buildup inside while the outside surface looks shiny and clean. Harsh overhead light illuminating the interior. Kitchen counter with paper towel underneath. The contrast between shiny exterior and grimy interior is the focus. 'I finally cut one open to see' energy. Macro-style phone shot, slight overexposure from flash."""
    },
    {
        "id": "draft_12",
        "name": "The Light Test",
        "prompt": """Raw iPhone photo of a hand holding a metal straw up against a bright window, attempting to see through it. Complete darkness/opacity visible — you cannot see any light through the straw. The window behind is overexposed from the backlight. Kitchen setting visible in periphery. The futility of the test is obvious — total blackout inside the tube. 'Tried to check if it's clean' energy. Shot one-handed while holding straw with the other."""
    },
    {
        "id": "draft_13",
        "name": "Impact Mark",
        "prompt": """Raw iPhone close-up photo of a granite countertop showing a small scratch or nick, with a metal straw lying nearby as the implied culprit. The scratch catches overhead light. Counter has some crumbs and a coffee mug visible in background. Shot to document the damage — 'did my straw do this?' energy. Autofocus on the scratch, straw slightly soft in background. Harsh overhead LED light."""
    },
    {
        "id": "draft_14",
        "name": "The Gift",
        "prompt": """Raw iPhone photo of a metal straw set in gift packaging — a small box with tissue paper, maybe a ribbon partially visible. The kind of packaging for a 'thoughtful eco gift.' Kitchen or bedroom background, natural window light mixed with indoor lamp. The gift presentation is slightly disheveled, not fresh — been sitting around. 'This is how I got my metal straw' energy. Shot at slight angle, casual."""
    },
    {
        "id": "draft_15",
        "name": "The Lemon Water",
        "prompt": """Raw iPhone photo of a glass of lemon water with visible lemon slices and a metal straw inside. Condensation on the outside of the glass. Morning kitchen light, counter has breakfast crumbs visible. The acidic citrus + metal combination is the focus. 'My healthy morning drink' energy but with metal straw creating the problem. Shot casually, slightly tilted, condensation droplets catching light."""
    },
    {
        "id": "draft_16",
        "name": "The Lip Mark",
        "prompt": """Raw iPhone close-up photo of a metal straw showing visible lip print residue or slight discoloration near the opening where mouth contacts it. The mark shows the intimate contact point. Kitchen counter background blurred, harsh overhead light. Shot in close-up to document the mark — 'this is where my lips touch' energy. Slight motion blur from handheld macro attempt."""
    },
    {
        "id": "draft_17",
        "name": "The Straw Collection",
        "prompt": """Raw iPhone photo of multiple metal straws of varying sizes standing in a utensil holder or cup on a kitchen counter. Some straws show wear, different finishes, accumulated over time. Not organized — just where they live. Mixed lighting from window and overhead. 'My collection of straws I haven't thought about in a while' energy. Counter has some clutter around the holder. Shot quickly, off-center composition."""
    }
]

def save_image(image_base64: str, prompt_id: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prompt_id}_{timestamp}.png"
    filepath = output_dir / filename
    image_bytes = base64.b64decode(image_base64)
    with open(filepath, "wb") as f:
        f.write(image_bytes)
    latest_path = output_dir / f"{prompt_id}.png"
    with open(latest_path, "wb") as f:
        f.write(image_bytes)
    return filepath

def generate_image(client: OpenAI, prompt_text: str, quality: str = "medium"):
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
    if not API_KEY:
        print("Error: OPENAI_API_KEY not set")
        sys.exit(1)

    client = OpenAI(api_key=API_KEY)
    print(f"\nGenerating 12 Batch 3 images...")
    print(f"Output: {OUTPUT_DIR}\n")

    for i, p in enumerate(PROMPTS, 1):
        print(f"[{i}/12] {p['id']}: {p['name']}...")
        image_data = generate_image(client, p["prompt"], "medium")
        if image_data:
            filepath = save_image(image_data, p["id"], OUTPUT_DIR)
            print(f"  Saved: {filepath.name}")
        else:
            print(f"  FAILED")
        if i < 12:
            time.sleep(2)

    print("\nDone!")

if __name__ == "__main__":
    main()
