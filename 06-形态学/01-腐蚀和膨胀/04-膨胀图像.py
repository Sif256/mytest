# coding: utf-8
# filename: 04-膨胀图像
# develop: sif
# date: 2022-09-30 15:47

import cv2
import numpy as np
img = cv2.imread('erode2.png')
# 创建结构元
kernel = np.ones((5, 5), np.uint8)
# 膨胀
rst = cv2.dilate(img, kernel, iterations=20)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.imwrite("fs.png", rst)
cv2.waitKey()
cv2.destroyAllWindows()
