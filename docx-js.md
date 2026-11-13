# DOCX Generation with JavaScript

A JavaScript DOCX library can create paragraphs, runs, tables, images, headers, footers, lists, hyperlinks, and page settings.

## Recommended process
1. Install the package in the project using its existing package manager.
2. Create a document model with explicit section properties.
3. Define default and heading styles.
4. Use numbering definitions for ordered and unordered lists.
5. Set table widths and cell margins deliberately.
6. Add images with explicit dimensions and alternative text where supported.
7. Write the resulting buffer to a new file.
8. Reopen and validate the package.
9. Render the document and inspect every page.

## Page sizing
Do not rely on library defaults. Set the target paper size and margins explicitly. Document units may be expressed in twips or DXA, where 1 inch equals 1440 DXA.

## Common pitfalls
- Tables may overflow when column widths are unconstrained.
- Headings must use semantic styles for navigation and table-of-contents generation.
- Fields may need an office application to update displayed values.
- Font substitution can change pagination.
- Image sizing must preserve aspect ratio.

Pin the library version and verify generated files in the office applications used by the audience.