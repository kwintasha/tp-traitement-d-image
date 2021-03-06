
from PIL.Image import *
i = open("gymnaseInitial.png")
i.show()
(l, h) = i.size

def niveaugrisinv(x):
    for y in range (h):
        for x in range (l):
            p = i.getpixel((x,y))

    coulmoy = (p[0]+p[1]+p[2])//3
    coulinv = 255 - coulmoy
    nouvcoul = (coulinv, coulinv, coulinv)
    i.putpixel((x,y), nouvcoul)
    return 

niveaugrisinv(i)

def eclaicir(i, ec):
    ec = ec/100
    for y in range (h):
        for x in range (l):
            p = i.getpixel((x,y))
            r,b,v = p[0] + ec * p[0], p[1] + ec * p[1], p[2] + ec * p[2]
            if r > 255 :
                r = 255
            elif v > 255 :
                v = 255
            elif b > 255 :
                b = 255
            nouvcoul = int(r), int(v), int(b)
            i.putpixel((x,y), nouvcoul)
    return i


            