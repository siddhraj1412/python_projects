import qrcode
import matplotlib.pyplot as pt
a=input("enter your URL :-")
img=qrcode.make(a)
img.save("oka.png")
pt.imshow(img,cmap='gray')