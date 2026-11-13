// Example only. Install the "docx" package in the project before running.
const fs = require("node:fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, PageOrientation
} = require("docx");

async function main() {
  const document = new Document({
    sections: [{
      properties: {
        page: {
          size: { width: 11906, height: 16838, orientation: PageOrientation.PORTRAIT },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      children: [
        new Paragraph({
          heading: HeadingLevel.TITLE,
          alignment: AlignmentType.CENTER,
          children: [new TextRun("Example Report")]
        }),
        new Paragraph({
          children: [new TextRun("Replace this paragraph with verified document content.")]
        })
      ]
    }]
  });
  const buffer = await Packer.toBuffer(document);
  fs.writeFileSync("example.docx", buffer);
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
