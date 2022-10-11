# coding: utf-8
# filename: 04-Hu矩
# develop: sif
# date: 2022-10-06 11:53

# 验证h0 = nu[02] + nu[20]
import cv2
img = cv2.imread('cc.png', 0)
# 获取Hu矩
Hu = cv2.HuMoments(cv2.moments(img)).flatten()
print(Hu[0])
# 归一化中心矩
mom = cv2.moments(img)
print(mom['nu02'] + mom['nu20'])
