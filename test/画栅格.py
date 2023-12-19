from PIL import Image, ImageDraw
def draw_grid(image_path, block_width, block_height):
    # 打开图片
    image = Image.open(image_path)
    # 获取图片的宽度和高度
    width, height = image.size
    # 创建一个ImageDraw对象，用于在图片上绘制
    draw = ImageDraw.Draw(image)
    # 计算水平和垂直方向上的小方块数量
    num_horizontal_blocks = width // block_width
    num_vertical_blocks = height // block_height
    # 绘制垂直线
    for i in range(1, num_horizontal_blocks):
        x = i * block_width
        draw.line([(x, 0), (x, height)], fill="white", width=1)
    # 绘制水平线
    for i in range(1, num_vertical_blocks):
        y = i * block_height
        draw.line([(0, y), (width, y)], fill="white", width=1)
    # 保存绘制后的图片
    image.save("../output/spider-2-grid.jpg")
# 用法示例
image_path = "../imgs/spider-2.png"  # 请替换为你的图片路径
block_width = 20  # 小方块的宽度
block_height = 20  # 小方块的高度

draw_grid(image_path, block_width, block_height)
