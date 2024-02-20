from PIL import Image
from Crypto.Util.number import*
imgt = Image.open(r"hidden_image.png")
img = imgt.convert("RGB")
pixel = img.load()


flag = ""
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r,g,b = pixel[i,j]
        if (len(flag) < 15*8):
            flag += bin(r)[-1]
            flag += bin(g)[-1]
            flag += bin(b)[-1]
print(long_to_bytes(int(flag,2)))