"""
Our data is non-traditional, so to extract it in a desired format I'll be applying regex functions to 
classify text correctly , i.e. '90 - 100' would be a range; 'u/dL' a unit etc...
"""
import os
from PIL import Image
from paddleocr import PaddleOCR
import os

class Classifier:
    