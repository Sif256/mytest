# coding: utf-8
# filename: 04-圆形框绘制
# develop: sif
# date: 2022-10-06 16:35

# 读取一幅图像，获取轮廓，进行最小圆形框轮廓的拟合
import cv2
img = cv2.imread('cc.png', 1)
# 转为灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 转为二值图
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
contours = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
# 获取圆心与半径
(x, y), radius = cv2.minEnclosingCircle(contours[0])
# 转为整型数据
center = (int(x), int(y))
radius = int(radius)
print(center, radius)
# 绘制矩形框
cv2.circle(img, center, radius, (21, 12, 127), 5)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
