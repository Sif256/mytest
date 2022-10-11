# coding: utf-8
# filename: 01-sobel算子
# develop: sif
# date: 2022-10-05 11:04

# 读取图像进行sobel算子，获取图像梯度
import cv2
img = cv2.imread('jing.png', 1)
# sobel在x轴方向求导
sobelx = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0)
sobelx = cv2.convertScaleAbs(sobelx)
# sobel在y轴方向求导
sobely = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1)
sobely = cv2.convertScaleAbs(sobely)
# 加权和
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 1, 0)
cv2.imshow('img', img)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('sobelxy', sobelxy)
cv2.waitKey()
cv2.destroyAllWindows()
