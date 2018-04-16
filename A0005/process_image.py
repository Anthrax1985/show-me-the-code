from PIL import Image
import os
import pathlib
import sys

IPHONE_H = 1334
IPHONE_W = 640


def process_image(spath):
    rate = 0
    im = Image.open(spath)
    print('%s before size: %s , %s' % (os.path.split(spath)[1], im.size[0], im.size[1]))
    if im.size[0] < im.size[1]:
        w, h = im.size
    else:
        h, w = im.size
    rate = (h / IPHONE_H) if (h / IPHONE_H) > (w / IPHONE_W) else (w / IPHONE_W)
    im.transform((h, w), Image.EXTENT, (0,0,int(w/rate),int(h/rate)))
    print('%s After size: %s , %s' % (os.path.split(spath)[1], im.size[0], im.size[1]))
    im.save('output_' + os.path.split(spath)[1])


if __name__ == '__main__':
    for path in os.listdir('pics'):
        process_image('pics/' + path)