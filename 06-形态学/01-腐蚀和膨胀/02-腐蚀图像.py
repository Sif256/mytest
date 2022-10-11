# coding: utf-8
# filename: 02-腐蚀图像
# develop: sif
# date: 2022-09-30 12:09

import cv2
import numpy as np
img = cv2.imread('JR.jpg')
# 创建结构元
kernel = np.ones((5, 5), np.uint8)
# 腐蚀
rst = cv2.erode(img, kernel, iterations=5)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.imwrite("fs.png", rst)
cv2.waitKey()
cv2.destroyAllWindows()
