# $56k Funnel - Setup Guide

## What's in this folder

| Folder | What it is |
|---|---|
| `ad-images/` | The 39 ad images, already split into `flexible-ad-1/` through `flexible-ad-4/` (10 + 10 + 10 + 9). One folder = one flexible ad. |
| `ad-copy/` | The 5 primary texts (`copy-1` through `copy-5`) and the headline (`link-headline.txt`). Paste-ready. |
| `pages/` | The 3 funnels: `the-argument/`, `the-future/`, `the-list/`. Each has `page-1.html` and `page-2.html`. Your Meta pixel is already in every page. |
| `page-images/` | The 5 images the landing pages use. |

**The funnels are already live with your pixel**, so you can launch ads today with zero page setup:

- The Argument: https://theprompted.github.io/accelerator/ethan-gvn/tics-funnel/v5/page-1/
- The Future: https://theprompted.github.io/accelerator/ethan-gvn/tics-funnel/v6/page-1/
- The List: https://theprompted.github.io/accelerator/ethan-gvn/tics-funnel/v7/page-1/

---

## Part 1: The ads. One ad set, 12 ads, three steps.

**Step 1 - build 4 flexible ads.**

New ad set, name it **$56k Funnel**. In it, create 4 flexible ads. Every ad gets the same text and destination - only the images differ:

| Ad name | Images | Primary text (all 5 slots) | Headline | Destination |
|---|---|---|---|---|
| Argument - 1 | everything in `flexible-ad-1/` | `copy-1` through `copy-5` | `link-headline.txt` | The Argument, page 1 |
| Argument - 2 | everything in `flexible-ad-2/` | same 5 | same | same |
| Argument - 3 | everything in `flexible-ad-3/` | same 5 | same | same |
| Argument - 4 | everything in `flexible-ad-4/` | same 5 | same | same |

**Step 2 - duplicate those 4 ads.** Rename the copies **Future - 1, 2, 3, 4** and change exactly one thing on each: the destination URL, to The Future page 1.

**Step 3 - duplicate once more.** Rename **List - 1, 2, 3, 4**, destination URL to The List page 1.

Done: 12 ads, every funnel gets all 39 images and all 5 copies, and the ad name always tells you which funnel it feeds. 117 shots on goal.

---

## Part 2 (whenever you want): Move the pages onto GoHighLevel

The ads work without this. Do it when you want the funnels on your own domain.

1. **Media Library:** upload the 5 images from `page-images/`, copy each one's URL.
2. **Funnels:** create three (suggested names: `Tics - The Argument`, `Tics - The Future`, `Tics - The List`), two pages each: `page-1` and `page-2`.
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
