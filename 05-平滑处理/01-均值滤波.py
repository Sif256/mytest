# coding: utf-8
# filename: 01-均值滤波
# develop: sif
# date: 2022-09-29 17:05

# 读取一幅图像，进行均值滤波，不同的核，查看效果
import cv2
img = cv2.imread('lena.bmp', 1)
# 均值滤波
rst_1 = cv2.blur(img, (3, 3))
rst_2 = cv2.blur(img, (5, 5))
rst_3 = cv2.blur(img, (30, 30))
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.imshow('rst_3', rst_3)
cv2.waitKey()
cv2.destroyAllWindows()
