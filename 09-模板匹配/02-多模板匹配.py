# coding: utf-8
# filename: 02-多模板匹配
# develop: sif
# date: 2022-10-07 16:53

# 读取原图和模板图片 进行一个多模板匹配 绘制并显示结果
import cv2
import numpy as np
img = cv2.imread('lenas.png', 1)
tmp = cv2.imread('tmp_lenas.png', 1)
w, h = tmp.shape[1::-1]
# 多模板匹配
res = cv2.matchTemplate(img, tmp, cv2.TM_CCOEFF_NORMED)
thr = 0.9
loc = np.where(res >= thr)
# 遍历匹配
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (12, 122, 11), 2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
