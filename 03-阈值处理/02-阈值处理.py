# coding: utf-8
# filename: 02-阈值处理
# develop: sif
# date: 2022-09-28 14:11

import cv2
img = cv2.imread('JR.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 阈值处理
# val, rst = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
rst = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)[1]  # 不需要返回阈值
print(vars)
cv2.imshow('rst', rst)
cv2.waitKey()
cv2.destroyAllWindows()
