from PIL import Image, ImageDraw, ImageFont

# 打开PNG图片
image = Image.open('./whitespace/Collab-3.png')

# 创建ImageDraw对象
draw = ImageDraw.Draw(image)

# 设置标题文字
text = 'Before the release of GPT-4'

# 设置标题字体和大小
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', size=40)

# 获取标题文本的宽度和高度
text_width, text_height = draw.textsize(text, font)

# 计算标题的x和y坐标
x = (image.width - text_width) // 2
y = 50

# 在图片中央上方添加标题
draw.text((x, y), text, font=font, fill=(0, 0, 0))

# 保存修改后的图片
image.save('./title/Collab-3.png')


# import cv2
# import numpy as np

# # 打开PNG图片
# img = cv2.imread('./whitespace/Newbing.png')

# # 设置标题文本和字体
# text = 'After the release of GPT-4'
# font = cv2.FONT_HERSHEY_SIMPLEX

# # 获取标题文本的宽度和高度
# textsize = cv2.getTextSize(text, font, 1, 2)[0]
# x = int((img.shape[1] - textsize[0]) / 2)
# y = 50

# # 在图片上绘制标题
# cv2.putText(img, text, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

# # 保存修改后的图片
# cv2.imwrite('./title/Newbingcv2.png', img)
