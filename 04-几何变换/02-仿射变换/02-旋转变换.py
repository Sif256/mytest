# coding: utf-8
# filename: 02-旋转变换
# develop: sif
# date: 2022-09-29 11:14

# 读取一幅图像，进行旋转
import cv2

img = cv2.imread('JR.jpg', 1)
line, col = img.shape[:2]
# 构造m矩阵
m = cv2.getRotationMatrix2D([int(col/2), int(line/2)], 90, 0.5)
# 仿射变换
ret = cv2.warpAffine(img, m, (col, line))
cv2.imshow('img', img)
cv2.imshow('rst', ret)
cv2.waitKey()
cv2.destroyAllWindows()
