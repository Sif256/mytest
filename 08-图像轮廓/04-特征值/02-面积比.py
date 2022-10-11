# coding: utf-8
# filename: 02-面积比
# develop: sif
# date: 2022-10-07 11:52

# 读取图像 获取轮廓 计算面积比
import cv2
img = cv2.imread('cc.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
# 查找轮廓
contour = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 矩形框
x, y, w, h = cv2.boundingRect(contour[0])
# 绘制
cv2.rectangle(img, (x, y), (x + w, y + h), (213, 21, 166), 2)
# 计算宽高比
rst = w * h
area = cv2.contourArea(contour[0])
extend = area/rst
print(extend)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
