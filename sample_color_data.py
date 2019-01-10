import cv2
import os

image_path = "/Users/migmikael/Downloads/Color-Consistency-Test/S8_image/"

choose_img_path = image_path
count = 1

pixel_list = []

for filename in os.listdir(choose_img_path):
    if filename.endswith('jpg'):
        img = cv2.imread(choose_img_path + filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print(filename)
        print("shape 0", img.shape[0])
        print("shape 1", img.shape[1])

        with open("coord.txt") as coord_file:
            for line in coord_file:
                num, i, j = line.split(",")
                r = img[int(i)][int(j)][0]
                g = img[int(i)][int(j)][1]
                b = img[int(i)][int(j)][2]
                pixel_list.append([r, g, b])

print(pixel_list)
print(len(pixel_list))