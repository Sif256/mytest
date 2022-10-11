# coding: utf-8
# filename: 02-图像的加权和
# develop: sif
# date: 2022-09-27 16:57

# 读取两幅图像，进行加权和
import cv2
img_1 = cv2.imread('one.jpg', 1)
img_2 = cv2.imread('two.jpg', 1)
# 加权和
rst = cv2.addWeighted(img_1, 0.8, img_2, 0.2, 0)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
