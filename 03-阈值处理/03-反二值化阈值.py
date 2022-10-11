# coding: utf-8
# filename: 03-反二值化阈值
# develop: sif
# date: 2022-09-28 14:40

# 读取一幅图像，进行阈值反阈值
import cv2
img = cv2.imread('JR.jpg', 1)
rst_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
rst_2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.waitKey()
cv2.destroyAllWindows()
