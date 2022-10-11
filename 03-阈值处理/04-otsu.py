# coding: utf-8
# filename: 04-otsu
# develop: sif
# date: 2022-09-28 14:55


# 读取一幅图像（色彩分布不均匀），进行阈值处理
import cv2
img = cv2.imread('JR.jpg', 0)
rst_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
var, rst_2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(var)
cv2.imshow('rst_1', rst_1)
cv2.imshow('rst_2', rst_2)
cv2.waitKey()
cv2.destroyAllWindows()
