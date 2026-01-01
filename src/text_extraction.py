import numpy as np
from PIL import Image
from itertools import product
import os
from PIL import Image
from paddleocr import PaddleOCR

os.environ['PADDLEX_ROOT'] = r"C:\Users\User\.paddlex"
ocr = PaddleOCR(use_angle_cls=True, lang='en')
allowed_ext = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")

class TextExtractor:
    def __init__(self):
        self.image = 
    def _paddle_OCR():
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
                
