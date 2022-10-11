# coding: utf-8
# filename: 01-像素访问与修改
# develop: sif
# date: 2022-09-27 10:15

# 灰度图像像素的访问与修改
import cv2
import numpy as np
img = np.random.randint(0, 256, size=[5, 5], dtype=np.uint8)
print('修改前:', img)
# 访问像素
print(img.item(0, 3))
# 修改像素
img.itemset((0, 3), 255)
print('修改后:', img)
# 生成一个随机像素值的灰度图像
img_1 = np.random.randint(0, 256, size=(300, 300, 3), dtype=np.uint8)
# itemset修改一个区域
img_2 = cv2.imread("nightingale.jpg", 0)
for i in range(200):
    for j in range(200):
        img_2.itemset((i, j), 0)
# 显示结果
cv2.imshow('img_1', img_1)
cv2.imshow('img_2', img_2)
cv2.waitKey()
cv2.destroyAllWindows()
