# coding: utf-8
# filename: 03-拉普拉斯
# develop: sif
# date: 2022-10-05 11:50

# 读取图像，进行拉普拉斯获取图像边缘信息
import cv2
img = cv2.imread('JR.jpg', 1)
# 拉普拉斯
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = cv2.convertScaleAbs(lap)
cv2.imshow('img', img)
cv2.imshow('lap', lap)
cv2.waitKey()
cv2.destroyAllWindows()
