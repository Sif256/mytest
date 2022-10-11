# coding: utf-8
# filename: 01-单模板匹配
# develop: sif
# date: 2022-10-07 16:04

# 读取原始图像和模板图像 进行模板匹配 绘制结果
import cv2
img = cv2.imread('lena.bmp', 1)
tmp = cv2.imread('tmp_lena.bmp', 1)
h, w = tmp.shape[:2]
# 模板匹配
res = cv2.matchTemplate(img, tmp, cv2.TM_CCOEFF)
minVar, maxVar, minLoc, maxLoc = cv2.minMaxLoc(res)
# 构建左上角和右下角的坐标
topLeft = maxLoc
bottomRight = (topLeft[0] + w, topLeft[1] + h)
cv2.rectangle(img, topLeft, bottomRight, (12, 23, 31), 2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
