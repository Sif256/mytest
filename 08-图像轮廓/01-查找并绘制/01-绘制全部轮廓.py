# coding: utf-8
# filename: 01-绘制全部轮廓
# develop: sif
# date: 2022-10-05 16:37

# 读取图像 获取轮廓 进行绘制
import cv2
img = cv2.imread('lena.bmp', 0)
img_1 = cv2.imread('lena.bmp', 1)
# 转化为二值图
binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
# 查找轮廓
contours, hiearay = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
n = len(contours)
print(n)

cv2.drawContours(img_1, contours, -1, (126, 55, 255), 10)
cv2.imshow('img_1', img_1)
cv2.waitKey()
cv2.destroyAllWindows()
