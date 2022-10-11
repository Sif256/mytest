# coding: utf-8
# filename: 04-模拟图像亮度调节
# develop: sif
# date: 2022-09-27 17:13

# 模拟图像，进行亮度调节
import cv2
import numpy as np
img = np.random.randint(0, 256, size=[5, 5], dtype=np.uint8)
# 显示图像
print('img=\n', img)
rst = cv2.add(img, 100)
print('rst=\n', rst)
