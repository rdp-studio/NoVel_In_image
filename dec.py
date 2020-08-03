## -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from PIL import Image

def decode(im):
    width, height = im.size
    lst = [ ]
    for y in range(height):
        for x in range(width):
            red, green, blue = im.getpixel((x, y))
            if (blue | green | red) == 0:
                break
            
            index = (green << 8) + blue
            lst.append( chr(index) )

    return ''.join(lst)


def main(filename):
    all_text = decode(Image.open(filename))
    with open("{}_decode.txt".format('.'.join(filename.split('.')[:-1])), "w") as f:
        f.write(all_text)

if __name__ == '__main__':
    main('out.bmp')
