## -*- coding: utf-8 -*-

from PIL import Image
import math

def encode(text, color):
    str_len = len(text)
    width = math.ceil(str_len**0.5)
    im = Image.new("RGB", (width, width), 0x0)

    x, y = 0, 0
    for i in text:
        index = ord(i)
        rgb = ( int(color),  (index & 0xFF00) >> 8,  index & 0xFF)
        im.putpixel( (x, y),  rgb )
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    return im

def main(filename, color):
    with open(filename, encoding="utf-8") as f:
        all_text = f.read()
        
    im = encode(all_text, color)
    im.save("{}_layout.bmp".format('.'.join(filename.split('.')[:-1])))

if __name__ == '__main__':
    main('三体全集.txt')

#(index & 0xFF0000) >> 16
