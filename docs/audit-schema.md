# Audit schema

## `progress/progress.csv`

- `version`: deliverable checkpoint
- `date`: validation date
- `base`: prior checkpoint
- `pdf_pages`: physical PDF page range
- `printed_pages`: printed-page range or front-matter designation
- `scope`: short non-verbatim description
- `records`: positioned records or high-risk line records, depending on the checkpoint mode
- `characters`: positioned character operations
- `nonspace`: non-space characters
- `zero_ink`: non-space character boxes not confirmed by the conservative source-ink mask
- `fullbook_visual_identical`: low-resolution whole-book regression result
- `sha256`: local deliverable checksum; the deliverable itself is not distributed here
- `status`: checkpoint state

### Interpreting `zero_ink`

`zero_ink` is a QA queue size, not automatically an OCR error count. A conservative mask can miss thin punctuation, anti-aliased strokes, pale printing, small figure labels or characters touching non-text graphics. A nonzero value is allowed only when the checkpoint status explicitly contains `deferred`; those items must remain available for later visual-semantic adjudication. The metric must never be driven to zero by moving character boxes onto unrelated page ink.

## `progress/page_status.csv`

- `pdf_start`, `pdf_end`: inclusive physical PDF range
- `printed_start`, `printed_end`: corresponding printed-page range when applicable
- `status`: pending, scheduled, TOC-complete, sequentially rebuilt, or batch deep-checked with explicit deferred review
- `completed_in`: checkpoint that completed the range
- `next_action`: scheduling or follow-up field

## `progress/special_remediation.csv`

Tracks earlier targeted cleanup work that does not by itself qualify a whole page as fully proofed.

## Public-repository boundary

Do not commit textbook scans, page images, corrected textbook PDFs, complete transcriptions, or character-level textbook content. Public files may contain page ranges, counts, checksums, error categories, workflow code and validation summaries.
