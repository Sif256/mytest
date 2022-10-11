# coding: utf-8
# filename: 08-凸包
# develop: sif
# date: 2022-10-07 11:11

# 读取图像，在轮廓外围建立凸包
import cv2
img = cv2.imread('hand.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
# 查找轮廓
contour = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 在轮廓外围建立凸包
hull = cv2.convexHull(contour[0])
# 绘制
cv2.polylines(img, [hull], 0, (211, 21, 212), 2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
