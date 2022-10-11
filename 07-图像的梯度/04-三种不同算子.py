# coding: utf-8
# filename: 04-三种不同算子
# develop: sif
# date: 2022-10-05 11:55

import cv2
img = cv2.imread('lena.bmp', 1)
# sobel在x轴方向求导
sobelx = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0)
sobelx = cv2.convertScaleAbs(sobelx)
# sobel在y轴方向求导
sobely = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1)
sobely = cv2.convertScaleAbs(sobely)
# 加权和
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv2.imshow('img', img)
cv2.imshow('sobelxy', sobelxy)
# sobel在x轴方向求导
scharrx = cv2.Scharr(img, cv2.CV_64F, dx=1, dy=0)
scharrx = cv2.convertScaleAbs(scharrx)
# sobel在y轴方向求导
scharry = cv2.Scharr(img, cv2.CV_64F, dx=0, dy=1)
scharry = cv2.convertScaleAbs(scharry)
# 加权和
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
cv2.imshow('scharrxy', scharrxy)
# 拉普拉斯
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = cv2.convertScaleAbs(lap)
cv2.imshow('lap', lap)
cv2.waitKey()
cv2.destroyAllWindows()
