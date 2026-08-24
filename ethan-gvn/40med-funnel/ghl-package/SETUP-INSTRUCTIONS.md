# 40 Medications Funnel - Setup Guide

## What's in this folder

| Folder | What it is |
|---|---|
| `ad-images/` | The 40 ad images, already split into `flexible-ad-1/` through `flexible-ad-4/` (10 + 10 + 10 + 10). One folder = one flexible ad. |
| `ad-copy/` | The 5 primary texts (`copy-1` through `copy-5`) and the headline (`link-headline.txt`). Paste-ready. |
| `pages/` | The 3 funnels: `the-argument/`, `the-future/`, `the-list/`. Each has `page-1.html` and `page-2.html`. Your Meta pixel is already in every page. |
| `page-images/` | The 5 images the landing pages use. |

**The funnels are already live with your pixel**, so you can launch ads today with zero page setup:

- The Ladder: https://theprompted.github.io/accelerator/ethan-gvn/40med-funnel/v8/page-1/
- The Fog: https://theprompted.github.io/accelerator/ethan-gvn/40med-funnel/v9/page-1/
- The Prescription: https://theprompted.github.io/accelerator/ethan-gvn/40med-funnel/v10/page-1/

---

## Part 1: The ads. One ad set, 12 ads, three steps.

**Step 1 - build 4 flexible ads.**

New ad set, name it **40 Medications Funnel**. In it, create 4 flexible ads. Every ad gets the same text and destination - only the images differ:

| Ad name | Images | Primary text (all 5 slots) | Headline | Destination |
|---|---|---|---|---|
| Ladder - 1 | everything in `flexible-ad-1/` | `copy-1` through `copy-5` | `link-headline.txt` | The Ladder, page 1 |
| Ladder - 2 | everything in `flexible-ad-2/` | same 5 | same | same |
| Ladder - 3 | everything in `flexible-ad-3/` | same 5 | same | same |
| Ladder - 4 | everything in `flexible-ad-4/` | same 5 | same | same |

**Step 2 - duplicate those 4 ads.** Rename the copies **Fog - 1, 2, 3, 4** and change exactly one thing on each: the destination URL, to The Fog page 1.

**Step 3 - duplicate once more.** Rename **Prescription - 1, 2, 3, 4**, destination URL to The Prescription page 1.

Done: 12 ads, every funnel gets all 40 images and all 5 copies, and the ad name always tells you which funnel it feeds. 120 shots on goal.

---

## Part 2 (whenever you want): Move the pages onto GoHighLevel

The ads work without this. Do it when you want the funnels on your own domain.

1. **Media Library:** upload the 5 images from `page-images/`, copy each one's URL.
2. **Funnels:** create three (suggested names: `Tics 2 - The Ladder`, `Tics 2 - The Fog`, `Tics 2 - The Prescription`), two pages each: `page-1` and `page-2`.
3. **Each page:** delete the default elements, add a full-width **Custom HTML/Code** element, paste in the whole matching HTML file.
4. **Before pasting, find-and-replace the image links** in the HTML:

```
src="../../images/ethan-daughters-barn.jpg"  ->  your Media Library URL
src="../../images/kids-cbd-1bottle.png"      ->  your Media Library URL
src="../../images/kids-cbd-3bottles.png"     ->  your Media Library URL
src="../../images/kids-cbd-6bottles.png"     ->  your Media Library URL
src="../../images/kids-cbd-bogo.png"         ->  your Media Library URL
```

5. **Each page-1** has a button linking to `../page-2/`. Point it at that funnel's real page-2 URL.
6. **Test on your phone:** pages load, images show, page-1 button lands on page 2, buy buttons work.
7. **Then update the ads:** swap each ad's destination URL to your new GoHighLevel URLs. The ad text needs no changes.

Questions? Contact Andrew at The Prompted.
