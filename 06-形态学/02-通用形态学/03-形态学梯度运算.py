# coding: utf-8
# filename: 03-形态学梯度运算
# develop: sif
# date: 2022-09-30 16:43

import cv2
import numpy as np
img = cv2.imread('fangkuai_1.jpg', 1)
# 创建结构元
kernel = np.ones((5, 5), np.uint8)
# 开运算
rst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=1)
cv2.imshow('img_1', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
