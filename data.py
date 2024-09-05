import PyPDF2


def pdf_to_text(pdf_path, output_txt):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ''

        for page_num in range(14, 51):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()