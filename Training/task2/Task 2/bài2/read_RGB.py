from PIL import Image

with open("rgb_values.txt","r") as f:
    lines = f.readlines()
    width = len(lines)
    tmp = lines[1].split(" ")
    length = len(tmp) - 1
        
imgsize = (width,length)
img = Image.new("RGB", imgsize)
pix = img.load()
for i in range (width):
    temp = lines[i].split(" ")
    for j in range (length):
        temp[j] = temp[j].replace('[','')
        temp[j] = temp[j].replace(']','')
        t = temp[j].split(",")
        t2 = (int(t[0]), int(t[1]), int(t[2]))
        pix[i, j] = t2
img.save('ảnhghép.jpg')