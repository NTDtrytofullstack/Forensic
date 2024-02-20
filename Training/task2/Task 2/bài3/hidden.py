from PIL import Image

imgt = Image.open("nhatziet.png")
img = imgt.convert("RGB")
pixel = img.load()
nhatziet = Image.new(img.mode, img.size)
ziet = nhatziet.load()

data = "nhatvietngu"
cipher = ""
for i in data:
    cipher += bin(ord(i))[2:].zfill(8)
while len(cipher)%3!=0:
    cipher = cipher + '0'
cipher_index = 0
for x in range(img.size[0]):
    for y in range(img.size[1]):
        r, g, b = pixel[x, y]
        if cipher_index < len(cipher):
            red = int(bin(r)[2:].zfill(8)[:-1] + cipher[cipher_index], 2)
            green = int(bin(g)[2:].zfill(8)[:-1] + cipher[cipher_index + 1], 2)
            blue = int(bin(b)[2:].zfill(8)[:-1] + cipher[cipher_index + 2], 2)
            ziet[x, y] = red, green, blue
            cipher_index += 3
        else:
            ziet[x, y] = r, g, b

nhatziet.save("hidden_image.png")
# img = Image.open(r"2.png")
# pixel = img.load()

# with open ("rgb_hidden.txt", "w") as f:
#     for x in range(img.size[0]):
#         for y in range(img.size[1]):
#             r, g, b= pixel[x, y]
#             f.write("[" + str(r) + "," + str(g) + "," + str(b) + "] ")
#         f.write("\n")