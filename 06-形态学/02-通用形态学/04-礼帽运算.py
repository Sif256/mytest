# coding: utf-8
# filename: 04-礼帽运算
# develop: sif
# date: 2022-09-30 16:52

# 礼貌运算，获取边缘噪声信息，或者更亮的边缘
import cv2
import numpy as np
img = cv2.imread('JR.jpg', 1)
# 创建结构元
kernel = np.ones((5, 5), np.uint8)
# 开运算
rst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=1)
cv2.imshow('img_1', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
