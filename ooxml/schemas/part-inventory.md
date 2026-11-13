# OOXML Package Part Inventory

| Part | Typical responsibility |
|---|---|
| [Content_Types].xml | Declares package content types |
| _rels/.rels | Package-level relationships |
| word/document.xml | Main document body |
| word/styles.xml | Named paragraph and character styles |
| word/numbering.xml | Numbering and list definitions |
| word/settings.xml | Document-level settings |
| word/comments.xml | Comment bodies |
| word/header*.xml | Section headers |
| word/footer*.xml | Section footers |
| word/media/* | Embedded images and other media |
| word/_rels/* | Relationships from Word parts |

Not every package contains every part. Inspect relationships before editing or removing a part.