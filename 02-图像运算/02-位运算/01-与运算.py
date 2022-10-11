# coding: utf-8
# filename: 01-与运算
# develop: sif
# date: 2022-09-27 17:25

# 读取一幅图像，与掩膜图像进行运算
import cv2
import numpy as np
img = cv2.imread('nightingale.jpg', 0)
# 生成掩膜图像
img_1 = np.zeros(img.shape, dtype=np.uint8)
img_1[100:400, 200:400] = 200
img_1[100:500, 100:200] = 200
# 与运算
rst = cv2.bitwise_and(img, img_1)
# 显示结果
cv2.imshow('mask', img_1)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
