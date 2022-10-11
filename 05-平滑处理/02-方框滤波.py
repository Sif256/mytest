# coding: utf-8
# filename: 02-方框滤波
# develop: sif
# date: 2022-09-29 17:17

# 读取一幅图像，进行方框滤波，显示效果
import cv2
img = cv2.imread('lena.bmp', 1)
# 方框滤波
rst_1 = cv2.boxFilter(img, -1, (3, 3))
rst_2 = cv2.boxFilter(img, -1, (50, 50))
rst_3 = cv2.boxFilter(img, -1, (2, 2), normalize=0)
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.imshow('rst_3', rst_3)
cv2.waitKey()
cv2.destroyAllWindows()
