import fitz


def load_pdf(pdf_path):
    document = fitz.open(pdf_path)

    text = ""

    for page_num in range(len(document)):
        page = document[page_num]
        text+=page.get_text()

    document.close()

    return text