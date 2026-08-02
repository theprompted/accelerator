# Tics Funnel - GoHighLevel Setup Guide

## What's included

### Landing pages (in `/pages/`)

Three versions of the same two-step funnel. Same headline, same offer flow. Each takes a different route through page 1, so we can test which route converts best.

| Folder | Version | Page 1 route |
|---|---|---|
| `v5-the-argument/` | v5 | The tightest version. Every subhead is a claim about the reader's child. |
| `v6-the-future/` | v6 | The only one that shows the destination: the ordinary bedtime scene. |
| `v7-the-list/` | v7 | Built on the expense list. The $56,576 record itself is the argument. |

Each folder has `page-1.html` (the story) and `page-2.html` (the offer).

**Your Meta pixel (1435777147172605) is already installed in every page.** Nothing to add there.

### Page images (in `/page-images/`)
The 5 images the landing pages use: the barn photo and the 4 product shots.

### Ad images (in `/ad-images/`)
All 39 ad images, sorted into one folder per angle. Every image in a folder uses the same ad copy and points at the same landing page.

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
2. Make three funnels (or one funnel with six pages, your call). Suggested names: `Tics v5`, `Tics v6`, `Tics v7`
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
Each page-1 has a button that links to `../page-2/`. Replace that with the real URL of that version's page 2 in your funnel.

### Step 6: Test each page on your phone
Page loads, images show, the page-1 button lands on the right page 2, buy buttons work.

---

## Part 2: Load the ads

We suggest **flexible ads**: one ad per angle. Meta takes up to 10 images per flexible ad and finds the winners for you.

**The mapping. One row = one flexible ad:**

| Ad | Images from | Primary text | Link headline | Send traffic to |
|---|---|---|---|---|
| 1 | `angle-a-prescriptions/` (14 - pick your 10 favorites) | `angle-a-prescriptions.txt` | `link-headline.txt` | v7 page 1 |
| 2 | `angle-b-mid-tic/` (13 - pick your 10 favorites) | `angle-b-mid-tic.txt` | `link-headline.txt` | v5 page 1 |
| 3 | `angle-c-what-it-cost/` (all 7) | `angle-c-what-it-cost.txt` | `link-headline.txt` | v7 page 1 |
| 4 | `angle-d-her-records/` (all 4) | `angle-d-her-records.txt` | `link-headline.txt` | v6 page 1 |
| 5 | `angle-e-prescription-forty/` (1 image, regular single-image ad) | `angle-e-prescription-forty.txt` | `link-headline.txt` | v7 page 1 |

**Important: swap the links.** The last line of every copy file, and the "Send traffic to" URL, currently point at our preview site (`theprompted.github.io/...`). Once your GoHighLevel pages are live, replace those with YOUR live URLs. One find-and-replace per copy file.

You can preview every ad exactly as it will look in the feed here:
https://theprompted.github.io/accelerator/ethan-gvn/tics-funnel/ads/

---

## One more thing

This round, loading the pages and ads is manual, because that is fastest. This week we are setting up your agent to do this loading for you, so next time you will not have to.

Questions? Contact Andrew at The Prompted.
