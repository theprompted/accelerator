# Tics Funnel - Setup Guide

## What's in this folder

| Folder | What it is |
|---|---|
| `pages/` | The 3 funnels: `the-argument/`, `the-future/`, `the-list/`. Each has `page-1.html` and `page-2.html`. Your Meta pixel is already installed in every page. |
| `page-images/` | The 5 images the landing pages use. |
| `ad-images/` | The 39 ad images, already split into `flexible-ad-1/` through `flexible-ad-4/` (10 + 10 + 10 + 9). One folder = one flexible ad. |
| `ad-copy/` | The primary text, ready to paste. One folder per funnel, links already filled in: `funnel-1-the-argument/`, `funnel-2-the-future/`, `funnel-3-the-list/`. Each has the same 5 copies, only the link at the end differs. `link-headline.txt` is the headline for every ad. |

**Good to know: the funnels are already live** (the links in the copy files point at them, and they have your pixel). So you can launch ads today with zero page setup, and move the pages onto GoHighLevel whenever you want.

---

## Part 1: Launch the ads (the whole thing is: build one ad set, duplicate it twice)

### Build ad set 1

1. New campaign. Name it `Tics - $56k Hook`.
2. New ad set. Name it `Funnel 1 - The Argument`.
3. Create a **flexible ad** in it:
   - Upload every image from `ad-images/flexible-ad-1/`
   - Primary text: paste all 5 files from `ad-copy/funnel-1-the-argument/` as 5 text options
   - Headline: paste `link-headline.txt`
   - Website URL: the same link that's at the end of the copy (The Argument, page 1)
4. Repeat step 3 three more times, with `flexible-ad-2/`, `flexible-ad-3/`, `flexible-ad-4/`. Same copy, same headline, same URL every time. Only the images change.

Ad set 1 is done: 4 ads, 39 images, pointed at The Argument.

### Duplicate for funnels 2 and 3

5. Duplicate the whole ad set. Rename it `Funnel 2 - The Future`. In each of its 4 ads, change only two things:
   - Primary text: swap in the 5 files from `ad-copy/funnel-2-the-future/`
   - Website URL: the link at the end of those copies (The Future, page 1)
6. Duplicate again. Rename it `Funnel 3 - The List`. Same two swaps, using `ad-copy/funnel-3-the-list/`.

That's it. 3 ad sets, 12 ads, 117 shots on goal. The images never change between ad sets - only the copy folder and the URL.

You can preview every ad as it will look in the feed here:
https://theprompted.github.io/accelerator/ethan-gvn/tics-funnel/ads/

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
7. **Then update the ads:** in each ad set, swap the website URL and the link at the end of each copy to your new GoHighLevel URLs. One find-and-replace per copy.

Questions? Contact Andrew at The Prompted.
