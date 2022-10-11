# coding: utf-8
# filename: 02-加密解密
# develop: sif
# date: 2022-09-28 10:03

# 读取灰度图像，进行加密，显示，解密，显示
import cv2
import numpy as np
img = cv2.imread('JR.jpg', 0)
# 密钥图像
key = np.random.randint(0, 256, size=img.shape, dtype=np.uint8)
# 加密运算
en = cv2.bitwise_xor(img, key)
# 解密运算
de = cv2.bitwise_xor(en, key)
cv2.imshow('img', img)
cv2.imshow('key', key)
cv2.imshow('en', en)
cv2.imshow('de', de)
cv2.waitKey()
cv2.destroyAllWindows()
