from PIL import Image
import pytesseract
#image = Image.open('666.png',)
#vcode = pytesseract.image_to_string(image)
#print(vcode)
#2
#上面都是导包，只需要下面这一行就能实现图片文字识别 
text=pytesseract.image_to_string(Image.open('111.png'),lang='chi_sim') 
print(text)
