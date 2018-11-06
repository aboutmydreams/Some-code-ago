from PIL import Image,ImageDraw,ImageChops
import pytesseract
#首先读取图片
def heibai(a,b,c=None):#a为图片路径，b为阈值
    img = Image.open(a)
    new_imgname = str(img.format)
    im = img.convert('L')

    def initTable(threshold):
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return table
    binaryImage = im.point(initTable(b), '1')#在这里修改阈值
    binaryImage.show()
    if c:
        print(new_imgname)
        binaryImage.save('{}'.format(str(c)+'.'+new_imgname),'{}'.format(new_imgname))
#heibai('C:\\Users\\T-bao\\Desktop\\软件代码\\img\\classroom1.png',190,'周一')#文件路径，阈值，(可选）保存名。
heibai('1054.png',190)