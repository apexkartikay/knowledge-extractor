from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True)

def image_to_text(image_path):

    result = ocr.ocr(image_path)

    texts = []

    for line in result[0]:
        texts.append(line[1][0])

    return "\n".join(texts)