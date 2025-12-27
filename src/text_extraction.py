import numpy as np
from PIL import Image
from itertools import product
import os
from PIL import Image
# Initialize PaddleOCR instance
from paddleocr import PaddleOCR
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)

ocr = PaddleOCR(use_angle_cls=True, lang='en')
# This will take some time to fully install all models needed for PaddleOCR.
allowed_ext = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")

for filename in os.listdir('images/lab_tests'):
    if filename.lower().endswith(allowed_ext):
        filepath = os.path.join('images/lab_tests', filename)
        
        if filename.lower().endswith((".tiff", ".tif")):
            img = Image.open(filepath)
            png_path = os.path.splitext(filepath)[0] + '.png'            
            img.save(png_path)
            os.remove(filepath)
            result = ocr.predict(png_path)
        else:
            result = ocr.predict(filepath)
        for text, score in zip(result[0]['rec_texts'], result[0]['rec_scores']):
            print(f"{text} ({score:.2f})")
        print()
        print("="*50)
        print()
        