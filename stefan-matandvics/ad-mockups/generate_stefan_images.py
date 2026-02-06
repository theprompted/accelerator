#!/usr/bin/env python3
"""
Mat & Vic's Ad Image Generator - OpenAI GPT-Image-1.5
Generates contradiction-based images for Facebook ad mockups

Usage:
    python generate_stefan_images.py --ids draft_01,draft_02,draft_03
    python generate_stefan_images.py --ids all
    python generate_stefan_images.py --list
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
MODEL = "gpt-image-1"  # Note: Use "dall-e-3" if gpt-image-1 unavailable
API_KEY = os.environ.get("OPENAI_API_KEY", "")
OUTPUT_DIR = Path(__file__).parent / "generated_images"
DELAY_BETWEEN_GENERATIONS = 2  # seconds

# Mat & Vic's image prompts - V3: Raw iPhone UGC style
# Philosophy: These should look like actual photos someone took with their phone to text a friend or post on social media. NOT professional, NOT composed, NOT "content creator" - just real person energy.
PROMPTS = [
    {
        "id": "draft_01",
        "name": "The Evidence",
        "prompt": "Raw iPhone photo taken to show a friend. Someone's hand holding up a wool sock with a visible hole at the heel, photographed quickly in their bedroom. Slightly blurry, imperfect lighting from overhead room light, maybe slight motion blur. The background is messy - unmade bed visible, some clutter. This is NOT a content photo - this is 'look at this bullshit' energy. The person is annoyed and took this photo to complain. Bad angles, casual grip, authentic frustration captured."
    },
    {
        "id": "draft_02",
        "name": "The Source",
        "prompt": "Blurry tourist-style iPhone photo of an alpaca at a petting zoo or farm. The alpaca is looking at the camera with that dumb confused expression. Slightly overexposed, the person clearly just snapped this while walking by. Maybe a fence or barn visible in background. This looks like it belongs in someone's camera roll from a random farm visit - not a professional animal photo. Candid, slightly awkward framing, the alpaca looks ridiculous."
    },
    {
        "id": "draft_03",
        "name": "The Instructions",
        "prompt": "iPhone photo of someone's thumb holding a clothing care label, clearly taken to text to someone. Harsh flash visible, the lighting is unflattering. The care label has tiny text with washing instructions. Background is bathroom or laundry room - tile visible, maybe a washing machine edge. This is 'can you believe this?' photo energy. Taken quickly, not composed, slightly out of focus on edges. Real person documenting an annoyance."
    },
    {
        "id": "draft_04",
        "name": "The Drawer",
        "prompt": "Overhead iPhone shot of an open dresser drawer full of socks. Harsh bedroom lighting, slight shadow from the phone/person taking the photo. The drawer is real life messy - mismatched socks, some balled up, some folded, a few with visible wear. This is someone looking down at their drawer and snapping a photo. Not staged, not organized for the photo - just actual drawer chaos that everyone has. Authentic domestic mess."
    },
    {
        "id": "draft_05",
        "name": "The Morning Moment",
        "prompt": "Candid iPhone selfie-style shot, someone's POV looking down at their own feet/legs while sitting on bed putting on socks. Morning light from window but also some harsh room light mixing. Rumpled sheets visible, maybe coffee cup on nightstand blurry in background. The framing is awkward because they're photographing themselves. This is intimate, casual, 'just woke up' energy. Not a lifestyle photo - an actual morning moment."
    },
    {
        "id": "draft_06",
        "name": "The Comparison",
        "prompt": "iPhone photo on a kitchen counter or table. Two navy socks laid next to each other - one looks newer and darker, one is clearly faded and pilled. Taken from above, casual angle. Some kitchen items visible in background - maybe a mug, keys, random counter clutter. The lighting is whatever the kitchen has - not good, not styled. This is someone laying out evidence to show the difference. Quick documentation photo, not art."
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
            # Download from URL if b64 not available
            import urllib.request
            response = urllib.request.urlopen(result.data[0].url)
            return base64.b64encode(response.read()).decode('utf-8')

        return None

    except Exception as e:
        print(f"  ERROR: {str(e)}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Generate Mat & Vic's ad images with OpenAI GPT-Image-1")
    parser.add_argument("--ids", type=str, help="Comma-separated draft IDs (e.g., draft_01,draft_02) or 'all'")
    parser.add_argument("--list", action="store_true", help="List all prompts")
    parser.add_argument("--quality", type=str, default="medium", choices=["low", "medium", "high"],
                        help="Image quality: low (~$0.08), medium (~$0.11), high (~$0.24)")
    args = parser.parse_args()

    if args.list:
        print("\n=== Mat & Vic's Ad Image Prompts ===\n")
        for p in PROMPTS:
            print(f"  {p['id']}: {p['name']}")
        return

    # Check for API key
    if not API_KEY:
        print("Error: OPENAI_API_KEY not set")
        print("Set with: export OPENAI_API_KEY='your-key'")
        sys.exit(1)

    # Determine what to generate
    if not args.ids:
        print("Usage: python generate_stefan_images.py --ids draft_01,draft_02")
        print("       python generate_stefan_images.py --ids all")
        print("       python generate_stefan_images.py --list")
        return

    if args.ids.lower() == "all":
        prompts_to_generate = PROMPTS
    else:
        ids = [s.strip() for s in args.ids.split(",")]
        prompts_to_generate = [p for p in PROMPTS if p["id"] in ids]

    if not prompts_to_generate:
        print(f"No prompts found for: {args.ids}")
        return

    # Cost estimate
    cost_per_image = {"low": 0.08, "medium": 0.11, "high": 0.24}
    estimated_cost = len(prompts_to_generate) * cost_per_image[args.quality]

    # Initialize client
    client = OpenAI(api_key=API_KEY)

    print(f"\n{'='*60}")
    print(f"MAT & VIC'S AD IMAGE GENERATOR (OpenAI)")
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

    # Print file paths for easy copy
    if generated_files:
        print("Generated files:")
        for f in generated_files:
            print(f"  {f}")


if __name__ == "__main__":
    main()
