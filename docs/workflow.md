# OCR QC workflow

## 1. Render and inspect

Render the source pages at high resolution. Read body text, headings, captions, figure labels, page headers and footers. Handwritten annotations are treated as annotations, not printed-text OCR.

Two operating modes are recorded separately:

- **Sequential full-page rebuild**: transcribe and rebuild each target page from the source scan.
- **Fifty-page batch deep check**: use the existing OCR as a baseline, refit the complete character layer, then visually reconstruct or correct high-risk body lines, captions, labels and tables. A later book-wide semantic sweep remains required.

## 2. Rebuild the invisible text layer

Remove only the prior invisible OCR stream for each target page. Preserve scanned imagery, annotations, page geometry and non-OCR content streams. Place each character or tightly coupled token on the corresponding printed ink.

For batch mode, every target page must receive a new OCR stream. Coordinate fitting alone is not enough: source-scan-confirmed text corrections and manual reconstruction of high-risk regions must be logged separately.

## 3. Character and coordinate validation

Parse the generated OCR stream and compare every operation against the audit CSV. Confirm exact character sequence, expected operation count and coordinate round-trip tolerance. Check that every non-space character box intersects printed ink.

Ink intersection is a coordinate check, not proof that every semantic character is correct. Keep this distinction explicit in reports and status metadata.

## 4. Regression validation

- Compare all edited pages with the baseline at a practical batch resolution.
- Compare representative high-risk pages with both the baseline and source scan at higher resolution.
- Use at least two renderers for the representative set when practical.
- Compare the whole book at low resolution.
- Verify unedited pages, page labels, bookmarks, annotations, resources and geometry remain unchanged.

## 5. Batch cadence

The default cadence is **50 PDF pages per delivery**. Stop early only for a blocking structural failure, page-order anomaly or an ambiguity that prevents reliable reconstruction of the batch.

## 6. Record progress

Update `progress/progress.csv` and `progress/page_status.csv`, and add a checkpoint metadata file. Use `complete_sequential_rebuild` and `complete_batch_deepcheck` as distinct statuses. Do not commit copyrighted source material, page images, full-text transcriptions or corrected PDFs.
