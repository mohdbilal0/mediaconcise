import pytesseract
from PIL import Image

def extract_img(img):
    # Open the image file
    image = Image.open(img)

    # Perform OCR using PyTesseract
    text = pytesseract.image_to_string(image)
    return text