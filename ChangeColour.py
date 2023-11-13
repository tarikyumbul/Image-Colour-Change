Copyright (c) 2023, tarikyumbul
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 


from PIL import Image

print("Welcome to the image color changer. Please provide the destination of the image you want to modify and the RGB values of the colors you want to switch. Make sure to use forward slashes in destination and spaces in RGB inputs to separate values.")
image_path = input("Image Destination: ")
old_r, old_g, old_b = input("Old RGB Values: ").split()
new_r, new_g, new_b = input("New RGB Values: ").split()

old_r, old_g, old_b, new_r, new_g, new_b = int(old_r), int(old_g), int(old_b), int(new_r), int(new_g), int(new_b)

img = Image.open(image_path)
rgb_img = img.convert("RGB")


def change_color(x, y, new_color):
    rgb_img.putpixel((x, y), new_color)


x = 0
while(x <= rgb_img.width - 1):
    y = 0
    while(y <= rgb_img.height - 1):
        r, g, b = rgb_img.getpixel((x, y))
        # print(r,g,b)
        if(r == old_r and g == old_g and b == old_b):
            change_color(x, y, (new_r, new_g, new_b))

        y += 1
    x += 1

rgb_img.save("D:/Tarik/Coding Projects/Python_Image_Manipulation/test_modified.png")

