# coding: utf-8
# filename: 04-中值滤波
# develop: sif
# date: 2022-09-30 11:05

import cv2
img = cv2.imread('lena.bmp', 1)
# 高斯滤波
rst_1 = cv2.medianBlur(img, 3)
rst_2 = cv2.medianBlur(img, 5)
rst_3 = cv2.medianBlur(img, 401)
# 显示结果
cv2.imshow('img', img)
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.imshow('rst_3', rst_3)
cv2.waitKey()
cv2.destroyAllWindows()
