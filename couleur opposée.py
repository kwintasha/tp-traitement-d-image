

from PIL import Image
des = Image.open("des.png")


def hh(des,d):
    d = des.size
    beau = Image.new('RGB', (d[0], d(1))
    for i in range(d[0]):
        for j in range(d[1]):
            s = des.igetpixel((i,j))
            coul = (255 - s[0], 255 - s[1], 255 - s[2])
            beau.putpixel((i,j), coul)
        des.show()
        beau.show()