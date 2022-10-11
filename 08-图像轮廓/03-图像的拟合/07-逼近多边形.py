# coding: utf-8
# filename: 07-逼近多边形
# develop: sif
# date: 2022-10-07 10:55

# 读取图像，进行轮廓拟合
import cv2
img = cv2.imread('cc.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
# 查总找轮廓
contour = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 逼近多边形
esp = 0.02 * cv2.arcLength(contour[0], True)
app = cv2.approxPolyDP(contour[0], esp, True)
# 绘制
cv2.drawContours(img, [app], 0, (211, 21, 212), 2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
