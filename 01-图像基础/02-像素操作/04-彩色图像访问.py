# coding: utf-8
# filename: 04-彩色图像访问
# develop: sif
# date: 2022-09-27 09:52

# 读取一幅彩色图像对其进行访问和修改
import cv2

img = cv2.imread('nightingale.jpg', 1)
# 访问像素
print(img[0, 0])
print(img[0, 0, 1])
# 像素的修改
img[0:100, 0:100] = [235, 75, 99]
# 修改区域
for i in range(0, 50):
    for j in range(100):
        for k in range(3):
            img[i, j, k] = 255
for i in range(50, 100):
    for j in range(100):
        img[i, j] = [128, 123, 128]
for i in range(100, 150):
    for j in range(100):
        img[i, j] = 177
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
