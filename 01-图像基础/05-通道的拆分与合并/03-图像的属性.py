# coding: utf-8
# filename: 03-图像的属性
# develop: sif
# date: 2022-09-27 15:10

import cv2
img_1 = cv2.imread('nightingale.jpg', 1)
img_2 = cv2.imread('nightingale.jpg', 0)
# 显示图像属性
print(img_2.shape)
print(img_2.size)
print(img_2.dtype)
print(img_1.shape)
print(img_1.size)
print(img_1.dtype)
