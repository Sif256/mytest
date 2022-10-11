# coding: utf-8
# filename: 01-平移变换
# develop: sif
# date: 2022-09-29 10:59

import cv2
import numpy as np
img = cv2.imread('JR.jpg', 1)
line, col = img.shape[:2]
# 构造M矩阵
# 在x轴移动100，y轴移动200
m = np.float32([[1, 0, 100], [0, 1, 200]])
# 仿射变换
rst = cv2.warpAffine(img, m, (line, col))
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
