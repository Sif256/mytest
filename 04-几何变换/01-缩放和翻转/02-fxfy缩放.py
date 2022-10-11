# coding: utf-8
# filename: 02-fxfy缩放
# develop: sif
# date: 2022-09-28 15:24


# 读取一幅图像，用fx，fy进行放大和缩小
import cv2
img = cv2.imread('JR.jpg', 1)
# 放大,缩小
rst = cv2.resize(img, None, fx=2, fy=2)
rst_1 = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
cv2.imshow('img', img)
cv2.imshow('rst_1', rst_1)
cv2.waitKey()
cv2.destroyAllWindows()
