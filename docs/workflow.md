# OCR QC workflow

## 1. Render and inspect

Render the source page at high resolution. Read the page visually, including body text, headings, captions, figure labels, page headers and footers. Handwritten annotations are treated as annotations, not printed-text OCR.

## 2. Rebuild the invisible text layer

Remove only the prior invisible OCR stream for the target page. Preserve scanned imagery, annotations, page geometry and non-OCR content streams. Place each character or tightly coupled token on the corresponding printed ink.

## 3. Character and coordinate validation

Parse the generated OCR stream and compare every operation against the audit CSV. Confirm exact character sequence, expected operation count and coordinate round-trip tolerance. Check that every non-space character box intersects printed ink.

## 4. Regression validation

Compare edited pages with the baseline and source scan at high resolution in at least two renderers when practical. Compare the whole book at low resolution. Verify unedited pages, page labels, bookmarks and annotations remain unchanged.

## 5. Record progress

Update `progress/progress.csv` and `progress/page_status.csv`. Do not commit copyrighted source material or full-text transcriptions.
