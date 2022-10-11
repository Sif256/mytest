# coding: utf-8
# filename: 01-轮廓矩
# develop: sif
# date: 2022-10-06 11:01

# 读取图像，获取图像的矩，显示图像的矩信息
import cv2
img = cv2.imread('cc.png', 0)
# 转为二值图
binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
contour = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 获取矩
rst = cv2.moments(contour[0])
print(rst)
