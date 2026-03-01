#!/usr/bin/env python3
"""
Mat & Vic's Ad Image Generator - OpenAI GPT-Image-1.5
Generates native image ad photos for Facebook ad mockups
V3 Raw iPhone UGC style - documentary evidence, not ad concepts
Heavy on contradiction-based images, all sock-visible for Meta targeting

Usage:
    python generate_stefan_images.py --ids draft_01,draft_02
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
MODEL = "gpt-image-1.5"
API_KEY = os.environ.get("OPENAI_API_KEY", "")
OUTPUT_DIR = Path(__file__).parent / "generated_ad_images"
DELAY_BETWEEN_GENERATIONS = 2  # seconds

# Mat & Vic's image prompts - V3 Native + Subtle Contradiction
# Philosophy: 3-layer native test:
#   1. Would someone take this photo? (camera + scene)
#   2. Would they post it? (there's a reason — the contradiction)
#   3. Do you feel something before reading text? (contradiction does the work)
# All images sock-visible for Meta algorithm targeting
PROMPTS = [
    {
        "id": "draft_01",
        "name": "The Alpaca Doesn't Live Here",
        "opener": "Natural fibers aren't better. They're just more expensive.",
        "prompt": "Raw iPhone photo taken to show a friend. Premium alpaca socks (dark brown, thick knit, pilling visible on heel) sitting on an office desk next to a half-empty coffee mug with coffee ring stain on desk. Single fluorescent tube overhead making everything yellow-green, harsh shadows. The background is messy - monitor cable dangling, crumpled sticky note, pen with chewed end. This is NOT a content photo - this is 'can you believe this costs €50' energy. Autofocus slightly off, socks soft while desk clutter is sharp. Shot one-handed during a desk break, slight tilt."
    },
    {
        "id": "draft_02",
        "name": "The 5pm Sock",
        "opener": "That 'soft' wool sock is making your feet sweat more, not less.",
        "prompt": "Raw iPhone photo taken to show a friend. Someone's feet up on a coffee table at evening, one dark wool sock pulled halfway off revealing damp interior with visible moisture darkening near ankle. The sock exterior looks fine, the interior looks wet. Living room evening light from window creating mixed warm/cool shadows. Background messy - TV remote, water glass with fingerprints, magazine corner. This is NOT a content photo - this is 'bro my feet feel disgusting' energy. Slightly blurry from being taken quickly before pulling sock fully off. Shot looking down at own feet."
    },
    {
        "id": "draft_03",
        "name": "The Care Label Essay",
        "opener": "That care label isn't proof of quality. It's an admission of failure.",
        "prompt": "Raw iPhone photo taken to show a friend. Extreme close-up of a sock care label being held by a thumb, the label has dense text across 5-6 lines of washing instructions. Words like 'cold water only', 'gentle cycle', 'lay flat to dry', 'no fabric softener', 'reshape while damp' partially visible. Laundry room fluorescent lighting casting yellow, background blurred (edge of washing machine visible). This is NOT a content photo - this is 'are you seeing this nonsense' energy. Thumb partially covering lens corner, tilted at angle someone would actually hold phone to read a label. Overexposed from being too close to light source."
    },
    {
        "id": "draft_04",
        "name": "€50 After Six Months",
        "opener": "You thought you were trading money for durability. You got the opposite.",
        "prompt": "Raw iPhone photo taken to show a friend. Premium sock packaging on bathroom counter - one elegant box torn open, price tag showing €49.95 or similar, tissue paper crumpled. The actual socks visible are destroyed - obvious pilling on soles, thin heel area, stretched out shape. Harsh overhead bathroom light creating unflattering shadows. Background messy - toothbrush holder, hand soap pump, water spots on counter. This is NOT a content photo - this is 'I want my money back' energy. Slight motion blur from hand trembling with annoyance. White balance wrong, everything looks slightly orange."
    },
    {
        "id": "draft_05",
        "name": "The Sock Drawer Audit",
        "opener": "You already know premium socks don't last. Your sock drawer proved it.",
        "prompt": "Raw iPhone photo taken to show a friend. Bird's eye view looking down into an open sock drawer. Half the socks are clearly destroyed - holes visible, pilling, faded colors, misshapen elastic. The destroyed ones include darker premium-looking socks (thick merino, alpaca visible). Other half look newer but basic. Bedroom lighting from window creating uneven light across drawer. Background shows dresser top clutter - loose change, receipt, dust. This is NOT a content photo - this is 'my drawer is a sock graveyard' energy. Shot one-handed holding drawer open, slight camera shake visible."
    },
    {
        "id": "draft_06",
        "name": "The Commute vs The Andes",
        "opener": "It was never about the fiber. It was about who the fiber was designed for.",
        "prompt": "Raw iPhone photo taken to show a friend. Premium alpaca socks (label partially visible saying 'alpaca' or similar) stuffed into leather business shoes sitting on doormat by front door. Keys on floor nearby, umbrella leaning against wall, messenger bag strap visible. Morning light from side window creating long shadows. Background messy - shoes slightly muddy, doormat dirty, mail on floor. This is NOT a content photo - this is 'designed for mountains going to an office' energy. Slight blur from morning rush, phone held low near ground to capture shoes, tilted angle."
    },
    {
        "id": "draft_07",
        "name": "The Felted Disaster",
        "opener": "You didn't ruin those expensive socks. They were never built to last.",
        "prompt": "Raw iPhone photo taken to show a friend. Attractive 35-year-old woman in business casual (blazer visible, nice dress hem), standing in bedroom, but camera reveals her feet on hardwood floor: dingy pilled socks with visible holes, the two socks don't match. She's looking DOWN at her own feet with mild embarrassment, NOT looking at camera. Mixed bedroom lighting - window light plus lamp creating uneven tones. Background messy - edge of bed visible, maybe a shoe on floor. This is NOT a content photo - this is 'getting ready but look at this situation' energy. Shot by her or by someone else capturing the moment, slight dutch angle."
    },
    {
        "id": "draft_08",
        "name": "What Survived",
        "opener": "The socks that survive your life aren't fancy. They're engineered.",
        "prompt": "Raw iPhone photo taken to show a friend. Inside view of open dryer drum showing aftermath of a wash cycle. Two or three premium-looking wool socks (darker, thicker) are visibly felted and shrunken, matted together. One pair of basic cotton-blend socks (lighter color, thinner) looks totally fine next to them. Harsh dryer drum light creating industrial look. Background shows lint on drum edges, maybe a dryer sheet stuck to wall. This is NOT a content photo - this is 'guess which ones cost more' energy. Shot leaning into dryer, slightly awkward angle, some lens flare from drum light."
    },
    {
        "id": "draft_09",
        "name": "The Premium Promise",
        "opener": "You suspected 'natural' was just a word. You were right.",
        "prompt": "Raw iPhone photo taken to show a friend. Beautiful premium sock gift box sitting open on dining table - tissue paper, ribbon, elegant '100% Alpaca' label visible on box. But inside the box is a completely ruined sock - shrunken, felted, misshapen, doesn't resemble original form at all. Natural afternoon light from window but white balance slightly off making everything look cool/blue. Background shows table surface with some crumbs, edge of plate visible. This is NOT a content photo - this is 'found this box I saved for the warranty' energy. Shot looking down at table, phone shadow partially visible on table."
    },
    {
        "id": "draft_10",
        "name": "The Moisture Line",
        "opener": "Your feet produce half a pint of sweat per day. Wool holds it. Polyamide moves it.",
        "prompt": "Raw iPhone photo taken to show a friend. Single dark wool sock dropped on bathroom tile floor, visible tide mark/moisture line around the ankle area where sweat accumulated and dried, creating a clear stain boundary. Harsh overhead bathroom light creating unflattering bright spot. Background shows bathroom tile pattern, edge of bath mat, maybe a hair on floor. This is NOT a content photo - this is 'that's not a pattern, that's my sweat' energy. Shot quickly looking down, slight motion blur, phone held at angle someone would stand to photograph floor."
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
    parser = argparse.ArgumentParser(description="Generate Mat & Vic's ad images with OpenAI GPT-Image-1.5")
    parser.add_argument("--ids", type=str, help="Comma-separated draft IDs (e.g., draft_01,draft_02) or 'all'")
    parser.add_argument("--list", action="store_true", help="List all prompts")
    parser.add_argument("--quality", type=str, default="high", choices=["low", "medium", "high"],
                        help="Image quality: low (~$0.08), medium (~$0.11), high (~$0.24)")
    args = parser.parse_args()

    if args.list:
        print("\n=== Mat & Vic's Ad Image Prompts ===\n")
        for p in PROMPTS:
            print(f"  {p['id']}: {p['name']}")
        return

    if not API_KEY:
        print("Error: OPENAI_API_KEY not set")
        print("Set with: export OPENAI_API_KEY='your-key'")
        sys.exit(1)

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

    cost_per_image = {"low": 0.08, "medium": 0.11, "high": 0.24}
    estimated_cost = len(prompts_to_generate) * cost_per_image[args.quality]

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

    if generated_files:
        print("Generated files:")
        for f in generated_files:
            print(f"  {f}")


if __name__ == "__main__":
    main()
