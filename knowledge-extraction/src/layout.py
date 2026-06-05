import fitz

def get_blocks(pdf_path):

    doc = fitz.open(pdf_path)

    blocks = []

    for page in doc:

        page_blocks = page.get_text("blocks")

        blocks.extend(page_blocks)

    return blocks