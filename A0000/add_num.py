from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def add_num(image):
    print('add_image_start')
    h,w = image.size

    draw = ImageDraw.Draw(image)
    draw.text((h/6, w/2), '牧师最强王牌', (255, 255, 0) , font=ImageFont.truetype('STZHONGS.ttf', 200))
    image.thumbnail((h/5, w/5))
    image.show()
    image.save('image1.png')


if __name__ == '__main__':
    image = Image.open('timg.jpeg')

    add_num(image)


