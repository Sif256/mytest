# coding: utf-8
# filename: scharr算子
# develop: sif
# date: 2022-10-05 11:36

# 读取图像进行scharr算子，获取图像梯度
import cv2
img = cv2.imread('jing.png', 1)
# sobel在x轴方向求导
scharrx = cv2.Scharr(img, cv2.CV_64F, dx=1, dy=0)
scharrx = cv2.convertScaleAbs(scharrx)
# sobel在y轴方向求导
scharry = cv2.Scharr(img, cv2.CV_64F, dx=0, dy=1)
scharry = cv2.convertScaleAbs(scharry)

# 加权和
scharrxy = cv2.addWeighted(scharrx, 0.1, scharry, 0.1, 0)
cv2.imshow('img', img)
cv2.imshow('scharrx', scharrx)
cv2.imshow('scharry', scharry)
cv2.imshow('scharrxy', scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()
