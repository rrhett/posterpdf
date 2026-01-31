# Poster PDF Utilities

This repository contains a utility to split landscape PDFs (with two pages side by side on each landscape page) to portrait PDFs (single pages).

# Quick guide

You must have `pdftk` and `mutool` installed.

If you have the file `LandscapeFile.pdf` with 5 pages, starting at page 2 (e.g. the first page is a cover), and the last page is a single page, so already portrait:

```
python3 poster.py -i LandscapeFile.pdf -o PortraitFile.pdf -n 20 -s 2 -e
```

## Examples

Suppose your input.pdf looks like `[C1, P2P3, P4P5, P6]` (`C1` is a cover page). Run `python3 poster.py -i input.pdf -o output.pdf -s 2 -n 5 -e`. Your output will be `[P2, P3, P4, P5, P6]`.

Suppose your input.pdf looks like `[P1P2, P3P4]`. Run `python3 poster.py -i input.pdf -o output.pdf -s 1 -n 2`. Your output will be `[P1, P2, P3, P4]`.

# Details

It supports the following options (all but `-e` are required):

**-i** **--input**: Specify the input file name.

**-o** **--output**: Specify the output file name.

**-s**: Start on this page (one-indexed) (e.g. if the first page is a title/cover, you can specify `-s 2` to skip it).

**-n**: The number of pages to extract from the input (the number of landscape pages). Your final output PDF will twice this many pages (or twice minus 1 if `-e` is specified).

**-e**: If the last page is already a portrait page, include this. If the last page is a landscape page, omit it.

# Background

This utility was created in response to a Reddit post:

https://www.reddit.com/r/pdf/comments/su94ts/how_to_split_a_landscape_pdf_into_two_separate/kiumm4o/
