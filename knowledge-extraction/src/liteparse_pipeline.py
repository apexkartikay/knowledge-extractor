from liteparse import LiteParser

parser = LiteParser()

result = parser.parse(
    "data/pdfs/sample.pdf"
)

print(result)