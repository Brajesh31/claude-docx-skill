# WordprocessingML and OOXML Notes

DOCX packages contain XML parts connected by relationship files.

## Common package parts
- word/document.xml: main document body.
- word/styles.xml: paragraph and character styles.
- word/numbering.xml: list definitions.
- word/comments.xml: comment bodies when present.
- word/settings.xml: document settings.
- word/header*.xml and word/footer*.xml: section headers and footers.
- word/_rels/: relationships from package parts.
- [Content_Types].xml: package content type declarations.

## Safe package editing
1. Make a working copy.
2. Extract to a temporary directory.
3. Parse XML with a namespace-aware parser.
4. Modify only required elements.
5. Preserve relationships and content type declarations.
6. Repackage without an extra parent directory.
7. Run ZIP integrity and XML parsing checks.
8. Open or render in a compatible office suite.

## Tracked changes
Word uses revision elements such as w:ins and w:del. Accepting revisions requires handling nested revisions and moving deleted text appropriately. Never remove revision markup with broad string replacement.

## Comments
Comments use IDs and range markers in the document body, with comment content stored separately. A correct comment operation must maintain all related markers and relationships.

These notes are an implementation aid, not a complete schema reference.