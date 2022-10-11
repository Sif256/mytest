# coding: utf-8
# filename: 03-高斯滤波
# develop: sif
# date: 2022-09-30 10:58

# 读取一幅图像 进行高斯滤波
import cv2
img = cv2.imread('lena.bmp', 1)
# 高斯滤波
rst_1 = cv2.GaussianBlur(img, (3, 3), 0, 0)
rst_2 = cv2.GaussianBlur(img, (5, 7), 0, 0)
rst_3 = cv2.GaussianBlur(img, (11, 11), 0, 0)
# 显示结果
cv2.imshow('img', img)
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.imshow('rst_3', rst_3)
cv2.waitKey()
cv2.destroyAllWindows()
