from PIL import Image
import tesseract
p1 = Image.open('31.png')
tesseract.image_to_text(p1)