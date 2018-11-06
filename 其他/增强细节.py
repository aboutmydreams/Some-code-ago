# -*- coding: UTF-8 -*_
from PIL import Image,ImageFilter
im02 = Image.open("111.png")
im = im02.filter(ImageFilter.DETAIL)
im.show()
