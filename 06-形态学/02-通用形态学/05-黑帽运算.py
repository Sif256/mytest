# coding: utf-8
# filename: 05-黑帽运算
# develop: sif
# date: 2022-09-30 17:01

# 黑帽运算，获取图像内部小孔或者更暗的边缘
import cv2
import numpy as np
img = cv2.imread('erode2.png', 1)
# 创建结构元
kernel = np.ones((5, 5), np.uint8)
# 开运算
rst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=1)
cv2.imshow('img_1', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
