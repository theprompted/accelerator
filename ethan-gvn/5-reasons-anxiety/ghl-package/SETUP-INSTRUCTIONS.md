# 5 Reasons Anxiety Funnel — GoHighLevel Setup

## What's Included

```
ghl-package/
├── page-1.html          # Education page (landing page for ads)
├── page-2.html          # Offer page (product bundles + checkout)
├── images/              # All images used in both pages
│   ├── illustrated/     # Feeling-state illustrations
│   └── *.png            # Product images
└── SETUP-INSTRUCTIONS.md
```

## Quick Start

### Step 1: Create Funnel in GHL
1. Go to Sites → Funnels → Create New Funnel
2. Name it "5 Reasons Anxiety"
3. Create two pages: "Education" and "Offer"

### Step 2: Upload Images
1. Go to Media Library
2. Upload the entire `images/` folder
3. Note the URLs — you'll need them in Step 4

### Step 3: Add HTML to Pages

**For each page:**
1. Add a "Custom Code" element (full width)
2. Open the corresponding HTML file (page-1.html or page-2.html)
3. Copy the entire contents
4. Paste into the Custom Code element

### Step 4: Update Image URLs

Find and replace all image paths with your GHL media URLs:

**Page 1 images:**
- `../images/illustrated/illust_01_hero_edge_of_bed.png`
- `../images/illustrated/illust_02_r1_bathroom_deep breathing.png`
- `../images/illustrated/illust_03_r2_office_depleted.png`
- `../images/illustrated/illust_04_r3_meditation_app.png`
- `../images/illustrated/illust_05_r4_two_women_meeting.png`
- `../images/illustrated/illust_06_r5_3am_wide_awake.png`
- `../images/illustrated/illust_07_cta_kitchen_worn.png`

**Page 2 images:**
- `../images/illustrated/illust_p2_01_solution_reveal.png`
- `../images/illustrated/illust_p2_02_bridge_contrast.png`
- `../images/illustrated/illust_p2_03_raw_materials.png`
- `../images/illustrated/illust_p2_04_future_pacing.png`
- `../images/illustrated/illust_p2_05_your_moment.png`
- `../images/gvn-cbd-oil-6bottles.png`
- `../images/gvn-cbd-oil-3bottles.png`
- `../images/gvn-cbd-oil-1bottle.png`

### Step 5: Update Checkout URLs

Page 2 contains buy buttons. Find all instances of:
```
href="https://greenvalleynutrition.com/cart/19414041886789:N"
```

Replace with your actual Shopify cart URLs:
- 6-bottle bundle: `/cart/YOUR_6_BOTTLE_VARIANT_ID:1`
- 3-bottle bundle: `/cart/YOUR_3_BOTTLE_VARIANT_ID:1`
- 1-bottle: `/cart/YOUR_1_BOTTLE_VARIANT_ID:1`

### Step 6: Connect Page 1 → Page 2

In page-1.html, find the CTA button link:
```
href="page-2/"
```

Replace with your GHL page-2 URL.

## Page Flow

```
Facebook Ad → Page 1 (Education) → Page 2 (Offer) → Shopify Checkout
```

- **Page 1** is CBD-free, safe for paid ads
- **Page 2** reveals the product and handles the sale

## Support

Built by The Prompted
https://theprompted.com
