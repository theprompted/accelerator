# Tics Funnel - GoHighLevel Setup Guide

## What's included

### Landing pages (in `/pages/`)

Three versions of the same two-step funnel. Same headline, same offer flow. Each takes a different route through page 1, so we can test which route converts best.

| Folder | What makes it unique |
|---|---|
| `the-argument/` | The tightest version. Every subhead is a claim about the reader's child. |
| `the-future/` | The only one that shows the destination: the ordinary bedtime scene. |
| `the-list/` | Built on the expense list. The $56,576 record itself is the argument. |

Each folder has `page-1.html` (the story) and `page-2.html` (the offer).

**Your Meta pixel (1435777147172605) is already installed in every page.** Nothing to add there.

### Page images (in `/page-images/`)
The 5 images the landing pages use: the barn photo and the 4 product shots.

### Ad images (in `/ad-images/`)
All 39 ad images, sorted into one folder per angle. Every image in a folder uses the same ad copy.

### Ad copy (in `/ad-copy/`)
One text file per angle. This is the primary text for the ad, ready to paste. `link-headline.txt` is the headline for every ad's link preview.

---

## Part 1: Get the landing pages live in GoHighLevel

### Step 1: Upload page images to Media Library
1. Go to **Sites** > **Media Library**
2. Upload the 5 images from `/page-images/`
3. Click each image and copy its URL. You need these in Step 3.

### Step 2: Create the funnels
1. Go to **Sites** > **Funnels** > **+ Create New Funnel**
2. Make three funnels (or one funnel with six pages, your call). Suggested names: `Tics - The Argument`, `Tics - The Future`, `Tics - The List`
3. Each gets two pages: `page-1` and `page-2`

### Step 3: Paste the HTML
For each page:
1. Open the page in the funnel builder
2. Delete all default elements
3. Add a **Custom HTML/Code** element, full width
4. Open the matching HTML file in a text editor, copy everything, paste it in

### Step 4: Fix the image links
Before pasting (easiest), use Find and Replace in your text editor:

```
src="../../images/ethan-daughters-barn.jpg"  ->  your Media Library URL
src="../../images/kids-cbd-1bottle.png"      ->  your Media Library URL
src="../../images/kids-cbd-3bottles.png"     ->  your Media Library URL
src="../../images/kids-cbd-6bottles.png"     ->  your Media Library URL
src="../../images/kids-cbd-bogo.png"         ->  your Media Library URL
```

### Step 5: Fix the page-1 button
Each page-1 has a button that links to `../page-2/`. Replace that with the real URL of that funnel's page 2.

### Step 6: Test each page on your phone
Page loads, images show, the page-1 button lands on the right page 2, buy buttons work.

---

## Part 2: Load the ads

**The structure: same ads, three funnels.** Any of these 39 ads can drive traffic to any of the three funnels. So the test is simple:

1. Make **three ad sets**
2. Load the **same ads** into each
3. Point ad set 1 at The Argument page 1, ad set 2 at The Future page 1, ad set 3 at The List page 1

The ads stay identical everywhere. The test tells you which funnel converts best.

**Inside each ad set: 4 flexible ads.** Meta takes up to 10 images per flexible ad, so split the 39 images as 10 + 10 + 10 + 9. On each flexible ad, add the 5 copy files as your primary text options (Meta allows 5) and `link-headline.txt` as the headline. Meta finds the winning combos.

That is 12 new ads total, and 117 shots on goal (3 funnels x 39 ads).

**One thing to fill in:** the last line of every copy file ends with `[your funnel link]`. Paste the live page-1 URL of whichever funnel that ad set points at. Same URL goes in the ad's website field.

You can preview every ad exactly as it will look in the feed here:
https://theprompted.github.io/accelerator/ethan-gvn/tics-funnel/ads/

---

## One more thing

This round, loading the pages and ads is manual, because that is fastest. This week we are setting up your agent to do this loading for you, so next time you will not have to.

Questions? Contact Andrew at The Prompted.
