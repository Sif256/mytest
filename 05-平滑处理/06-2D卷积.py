# coding: utf-8
# filename: 06-2D卷积
# develop: sif
# date: 2022-09-30 11:41

# 读取图像，自定义卷积核，进行滤波
import cv2
import numpy as np
img = cv2.imread('lena.bmp', 1)
# 定义卷积核
kernel = np.ones((5, 5), np.float32) / 25
print(kernel)
# 2d卷积
rst = cv2.filter2D(img, -1, kernel)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
