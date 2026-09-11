# Audit schema

## `progress/progress.csv`

- `version`: deliverable checkpoint
- `date`: validation date
- `base`: prior checkpoint
- `pdf_pages`: physical PDF page range
- `printed_pages`: printed-page range or front-matter designation
- `scope`: short non-verbatim description
- `records`: positioned text records
- `characters`: positioned character operations
- `nonspace`: non-space characters
- `zero_ink`: non-space character boxes with no detected source ink
- `fullbook_visual_identical`: low-resolution whole-book regression result
- `sha256`: local deliverable checksum; the deliverable itself is not distributed here
- `status`: checkpoint state

## `progress/page_status.csv`

- `pdf_start`, `pdf_end`: inclusive physical PDF range
- `printed_start`, `printed_end`: corresponding printed-page range when applicable
- `status`: pending, scheduled, TOC-complete, or sequentially rebuilt
- `completed_in`: checkpoint that completed the range
- `next_action`: scheduling field

## `progress/special_remediation.csv`

Tracks earlier targeted cleanup work that does not by itself qualify a whole page as fully proofed.
