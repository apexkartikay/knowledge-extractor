from src.parser import extract_text
from src.extractor import extract_tables
from src.json_builder import build_json

pdf_path = "data/pdfs/sample.pdf"

text = extract_text(pdf_path)

tables = extract_tables(pdf_path)

output = build_json(text, tables)

with open(
    "outputs/result.json",
    "w",
    encoding="utf-8"
) as f:

    f.write(output)

print("Done")

import os

pdf_path = "data/pdfs/sample.pdf"

if not os.path.exists(pdf_path):
    print(f"PDF not found: {pdf_path}")
    exit()

text = extract_text(pdf_path)