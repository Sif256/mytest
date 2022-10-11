# coding: utf-8
# filename: 02-轮廓的面积
# develop: sif
# date: 2022-10-06 11:13

# 读取一幅图像，获取轮廓的面积
import cv2
img = cv2.imread('cnt.png', 0)
# 转化为二值图
binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
contour = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0]
n = len(contour)
for i in range(n):
    print("第%d个轮廓面积为:%s" % (i, cv2.contourArea(contour[i])))
