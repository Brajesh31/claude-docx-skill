---
name: docx
description: Create, read, edit, and analyze Word DOCX files, including tables, images, comments, tracked revisions, and formatting-sensitive documents.
---

# DOCX Toolkit

## Scope
Use for Word .docx files. Do not use for PDF-only work, spreadsheets, Google Docs, or unrelated programming.

## Choose the method
- Create a new document: use a DOCX-generation library such as docx for JavaScript or python-docx for Python.
- Read content: extract paragraphs and tables while preserving order; inspect package XML when required.
- Edit existing content: prefer targeted edits and preserve styles, sections, relationships, and embedded media.
- Track changes and comments: use a toolchain that supports WordprocessingML revisions and comment relationships. Do not pretend ordinary paragraph editing preserves review markup.
- Convert legacy .doc: use an installed office suite and verify the converted file.

## Before editing
1. Inspect file type and package integrity.
2. Record section sizes, margins, orientation, styles, tables, images, and headers/footers.
3. Identify comments, tracked changes, fields, hyperlinks, and embedded objects.
4. Confirm whether layout must be preserved.
5. Work on a copy unless replacement is requested.

## Creating documents
Set page size, margins, fonts, heading styles, numbering, tables, and headers/footers explicitly. Use semantic styles. Keep content accessible and avoid manual spacing hacks.

## Editing existing documents
A DOCX is a ZIP package of XML parts and relationships. Changes to one part can affect references elsewhere. Preserve relationship IDs and content types. Do not rebuild a package from scratch for a small edit.

## Review features
- Track insertions and deletions only when the library supports revision markup.
- Keep comment ranges and comment references consistent.
- Do not silently accept or reject tracked changes.
- Explain limitations when the available library cannot preserve advanced Word features.

## Validation
Use scripts/inspect_docx.py and scripts/validate_docx.py for package checks. Render documents when visual layout matters. Consult docx-js.md and ooxml.md for implementation notes.