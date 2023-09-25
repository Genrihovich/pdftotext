from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
import logging
import os

from gpytranslate import SyncTranslator

logging.basicConfig(level=logging.INFO)


def process_file(filename):
    pdf_document = Document(
        document_path=f"./input/{filename}",
        language='ukr'
    )
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    print(content)

    t = SyncTranslator()
    translation = t.translate(content[0]["text"], targetlang="ru")
    language = t.detect(translation.text)
    print(f"Translation: {translation.text}\nDetected language: {language}")

    f = open(f"./output/{filename}.txt", "w",  encoding="utf-8")
    # f.write(content[0]["text"])
    f.write(translation.text)
    f.close()


def main():
    filenames = os.listdir('./input')
    for filename in filenames:
        process_file(filename)

    print(filenames)
    return
    # create document for extraction with configurations


if __name__ == "__main__":
    main()
