# python练习题项目 --- 第000题
# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageFont, ImageDraw
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

inputFile = '/Users/flyhero/Desktop/example.jpg'
outputFile = '/Users/flyhero/Desktop/output.jpg'

image = Image.open(inputFile, 'r')
w, h = image.size

# 创建字体对象
font = ImageFont.truetype('/Library/Fonts/Arial Bold Italic.ttf', int(h/4))

# 绘制圆形
ImageDraw.Draw(image).pieslice([(w/3*2, 0), (w, h/3)], 0, 360, fill='red')
ImageDraw.Draw(image).text((w*0.76, h*0.02), '3', font=font, fill='white')

# 展示绘制结果
image.show()

# 保存绘制结果
image.save(outputFile)