from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string


def gen_code(lenth=4):
    height = 60
    width = 60 * lenth

    im = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('STZHONGS.ttf', 36)

    [draw.point((x, y), fill=random_color_background()) for x in range(width) for y in range(height)]

    for idx in range(lenth):
        draw.text((12 + idx*60, 12), random_chr(), font=font, fill=random_color_word())

    # im = im.filter(ImageFilter.MaxFilter)

    im.show()


def random_chr():
    return random.choice(string.ascii_letters + string.digits)


def random_color_background():
    return random.randint(64, 200), random.randint(64, 200), random.randint(64, 200)


def random_color_word():
    return random.randint(32, 120), random.randint(32, 120), random.randint(32, 120)


if __name__ == '__main__':
    gen_code()