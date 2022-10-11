# coding: utf-8
# filename: 01-开运算
# develop: sif
# date: 2022-09-30 16:02

# 读取两幅图像，进行开运算，去除物体边缘的杂质,计数
import cv2
import numpy as np
img_1 = cv2.imread('erode.png', 1)
img_2 = cv2.imread('fangkuai.jpg', 1)
# 创建结构元
kernel = np.ones((5, 5), np.uint8)
# 开运算
rst = cv2.morphologyEx(img_1, cv2.MORPH_OPEN, kernel, iterations=4)
rst_2 = cv2.morphologyEx(img_2, cv2.MORPH_OPEN, kernel, iterations=4)
cv2.imshow('img_1', img_1)
cv2.imshow('img_2', img_2)
cv2.imshow('rst', rst)
cv2.imshow('rst_2', rst_2)
cv2.imwrite('fangkuai_1.jpg', rst_2)
cv2.waitKey()
cv2.destroyAllWindows()
