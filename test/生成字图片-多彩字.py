from PIL import Image, ImageDraw, ImageFont
import numpy as np
hanzis = "派森斗罗您好啊~"
for hanzi in hanzis:
    font_size = 48
    # 使用系统字体或指定字体文件
    font = ImageFont.truetype(r"D:\文件夹\github_\myshare_github\Python-Project-Pro\字符画原理及实现代码笔记\1.ttf", font_size)
    # 计算汉字的大小
    text_bbox = font.getbbox(hanzi)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    # 设置填充大小
    padding = 5
    # 定义颜色
    colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0),
              (0, 255, 255), (0, 0, 255), (128, 0, 128),(255,255,255),(0,0,0)]
    bg_color=(0,0,0)
    for font_color in colors:
        if font_color==bg_color:
            continue
        # 创建一个空白图像，大小根据文本计算，并添加填充
        pattern_size = (text_width + 2 * padding, text_height + 2 * padding)
        pattern_image = Image.new('RGB', pattern_size, color=bg_color)
        pattern_draw = ImageDraw.Draw(pattern_image)
        # 在花纹背景上绘制汉字，考虑填充
        pattern_draw.text((-text_bbox[0] + padding, -text_bbox[1] + padding), hanzi, fill=font_color, font=font)
        # 将花纹图像转换为NumPy数组以便处理
        pattern_data = np.array(pattern_image)
        # 创建Pillow图像对象并显示
        pattern_image = Image.fromarray(pattern_data)
        # 保存花纹图像
        pattern_image.save('hanzi-font/'+hanzi+ f'{bg_color}-{font_color}.jpg')