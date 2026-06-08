#!/usr/bin/env python3
"""
Strawesome Ad Image Generator - OpenAI GPT-Image-1.5
Generates native image ad photos for Facebook ad mockups
V3 Raw iPhone UGC style - documentary evidence, not ad concepts
Batch 3: 12 belief-violation images for metal straw campaign

Usage:
    python generate_strawesome_images.py --ids draft_01,draft_02
    python generate_strawesome_images.py --ids all
    python generate_strawesome_images.py --list
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

# Strawesome Batch 3 image prompts - V3: Native + Subtle Contradiction
# Philosophy: 3-layer native test:
#   1. Would someone take this photo? (camera + scene)
#   2. Would they post it? (there's a reason — the contradiction)
#   3. Do you feel something before reading text? (contradiction does the work)
# All concepts: Object-focused, subtle contradictions, no performed emotions
PROMPTS = [
    {
        "id": "draft_01",
        "name": "The Two Straws",
        "opener": "Metal straws aren't safer. They just feel safer.",
        "angle": "Flat Denial (#1)",
        "prompt": "Raw iPhone photo taken to show a friend. Metal straw and clear glass straw lying side by side on a kitchen counter. The metal straw has visible scratches and scuff marks from use. The glass straw looks pristine and clear. Single overhead LED creating harsh shadows, white balance slightly too warm. Counter has crumbs, a water ring stain, and a crumpled paper towel edge visible. Shot one-handed, slightly tilted. Autofocus locked on the glass straw so metal straw is slightly soft. Natural 'look at this weird thing I noticed' energy."
    },
    {
        "id": "draft_02",
        "name": "The Scratch Pattern",
        "opener": "The 'safe' straw in your tumbler has a body count.",
        "angle": "Flat Denial (#4)",
        "prompt": "Raw iPhone close-up photo of a metal straw showing visible scoring and scratches from repeated teeth contact. Multiple scratch lines running along the same section where mouth bites happen. Kitchen counter background blurred, single fluorescent overhead making everything yellow-green. The straw surface catches the light to show the damage clearly. Shot at close range to document the marks, slight motion blur from holding phone too close. 'Just noticed my straw looks like this' energy."
    },
    {
        "id": "draft_03",
        "name": "The Bend Test",
        "opener": "The straw you chose to protect yourself is the one most likely to hurt you.",
        "angle": "Flip (#5)",
        "prompt": "Raw iPhone photo showing two straws on a counter — a slightly curved/flexible glass straw showing visible bend, and a rigidly straight metal straw. The glass straw demonstrates give while metal stays perfectly straight. Kitchen background with cluttered counter, mixed lighting from window and overhead fluorescent. Shot from above at slight angle, one hand might be touching the straws. 'Comparing these two' energy. Autofocus slightly off, captured quickly."
    },
    {
        "id": "draft_04",
        "name": "The Morning After",
        "opener": "Metal straws are safer than glass the way concrete walls are safer than guardrails.",
        "angle": "Flip (#6)",
        "prompt": "Raw iPhone photo of a drinking glass with a visible chip on the rim, metal straw resting inside or next to it. The chip is clearly from impact — small triangular piece missing from the glass edge. Morning kitchen light from window, counter has coffee rings and toast crumbs. The metal straw is positioned near the chip, implying it caused the damage. 'Wait how did this happen' energy. Shot quickly to document the damage."
    },
    {
        "id": "draft_05",
        "name": "The Eco-Friendly Starter Kit",
        "opener": "Everyone told you metal was the responsible choice.",
        "angle": "Attack Advice (#9)",
        "prompt": "Raw iPhone photo of a casual pile of eco-friendly items on a kitchen counter or shelf — reusable grocery bag, bamboo utensils in a holder, metal straw prominent in the group. NOT a styled flatlay — these are items that live together, slightly messy. Mixed lighting, some items overlapping casually. The metal straw is visible among the 'trusted' eco products. 'My sustainable corner' energy but not curated. Some items slightly dusty. Shot quickly without arranging."
    },
    {
        "id": "draft_06",
        "name": "Inside vs. Outside",
        "opener": "You traded visibility for opacity.",
        "angle": "Attack Trade-Off (#14)",
        "prompt": "Raw iPhone close-up photo of a metal straw that has been cut in half, showing dark brown/gray residue and gunk buildup inside while the outside surface looks shiny and clean. Harsh overhead light illuminating the interior. Kitchen counter with paper towel underneath. The contrast between shiny exterior and grimy interior is the focus. 'I finally cut one open to see' energy. Macro-style phone shot, slight overexposure from flash."
    },
    {
        "id": "draft_07",
        "name": "The Light Test",
        "opener": "You own the tiny brush. You've tried to clean the inside.",
        "angle": "Quit Proof (#18)",
        "prompt": "Raw iPhone photo of a hand holding a metal straw up against a bright window, attempting to see through it. Complete darkness/opacity visible — you cannot see any light through the straw. The window behind is overexposed from the backlight. Kitchen setting visible in periphery. The futility of the test is obvious — total blackout inside the tube. 'Tried to check if it's clean' energy. Shot one-handed while holding straw with the other."
    },
    {
        "id": "draft_08",
        "name": "Impact Mark",
        "opener": "It was never about glass being fragile. It was about metal being rigid.",
        "angle": "Real Variable (#21)",
        "prompt": "Raw iPhone close-up photo of a granite countertop showing a small scratch or nick, with a metal straw lying nearby as the implied culprit. The scratch catches overhead light. Counter has some crumbs and a coffee mug visible in background. Shot to document the damage — 'did my straw do this?' energy. Autofocus on the scratch, straw slightly soft in background. Harsh overhead LED light."
    },
    {
        "id": "draft_09",
        "name": "The Gift",
        "opener": "You didn't make the wrong choice. You made the choice everyone told you to make.",
        "angle": "Guilt (#25)",
        "prompt": "Raw iPhone photo of a metal straw set in gift packaging — a small box with tissue paper, maybe a ribbon partially visible. The kind of packaging for a 'thoughtful eco gift.' Kitchen or bedroom background, natural window light mixed with indoor lamp. The gift presentation is slightly disheveled, not fresh — been sitting around. 'This is how I got my metal straw' energy. Shot at slight angle, casual."
    },
    {
        "id": "draft_10",
        "name": "The Lemon Water",
        "opener": "Your instinct to avoid the metallic taste was right.",
        "angle": "Protect (#29)",
        "prompt": "Raw iPhone photo of a glass of lemon water with visible lemon slices and a metal straw inside. Condensation on the outside of the glass. Morning kitchen light, counter has breakfast crumbs visible. The acidic citrus + metal combination is the focus. 'My healthy morning drink' energy but with metal straw creating the problem. Shot casually, slightly tilted, condensation droplets catching light."
    },
    {
        "id": "draft_11",
        "name": "The Lip Mark",
        "opener": "You knew something was off about metal straws.",
        "angle": "Identity (#33)",
        "prompt": "Raw iPhone close-up photo of a metal straw showing visible lip print residue or slight discoloration near the opening where mouth contacts it. The mark shows the intimate contact point. Kitchen counter background blurred, harsh overhead light. Shot in close-up to document the mark — 'this is where my lips touch' energy. Slight motion blur from handheld macro attempt."
    },
    {
        "id": "draft_12",
        "name": "The Straw Collection",
        "opener": "You're not paranoid for wondering what's growing inside an opaque tube.",
        "angle": "Identity (#35)",
        "prompt": "Raw iPhone photo of multiple metal straws of varying sizes standing in a utensil holder or cup on a kitchen counter. Some straws show wear, different finishes, accumulated over time. Not organized — just where they live. Mixed lighting from window and overhead. 'My collection of straws I haven't thought about in a while' energy. Counter has some clutter around the holder. Shot quickly, off-center composition."
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
    parser = argparse.ArgumentParser(description="Generate Strawesome ad images with OpenAI GPT-Image-1.5")
    parser.add_argument("--ids", type=str, help="Comma-separated draft IDs (e.g., draft_01,draft_02) or 'all'")
    parser.add_argument("--list", action="store_true", help="List all prompts")
    parser.add_argument("--quality", type=str, default="medium", choices=["low", "medium", "high"],
                        help="Image quality: low (~$0.08), medium (~$0.11), high (~$0.24)")
    args = parser.parse_args()

    if args.list:
        print("\n=== Strawesome Ad Image Prompts (Batch 3) ===\n")
        for p in PROMPTS:
            print(f"  {p['id']}: {p['name']} ({p['angle']})")
        return

    if not API_KEY:
        print("Error: OPENAI_API_KEY not set")
        print("Set with: export OPENAI_API_KEY='your-key'")
        sys.exit(1)

    if not args.ids:
        print("Usage: python generate_strawesome_images.py --ids draft_01,draft_02")
        print("       python generate_strawesome_images.py --ids all")
        print("       python generate_strawesome_images.py --list")
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
    print(f"STRAWESOME AD IMAGE GENERATOR (OpenAI)")
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
