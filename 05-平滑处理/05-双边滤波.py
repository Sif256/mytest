# coding: utf-8
# filename: 05-双边滤波
# develop: sif
# date: 2022-09-30 11:18

import cv2
img = cv2.imread('JR.jpg', 1)
# 高斯滤波
rst_1 = cv2.GaussianBlur(img, (5, 5), 0, 0)
rst_2 = cv2.bilateralFilter(img, 9, 150, 150)
# 显示结果
cv2.imshow('img', img)
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.waitKey()
cv2.destroyAllWindows()
