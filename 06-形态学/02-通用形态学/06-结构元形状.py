# coding: utf-8
# filename: 06-结构元形状
# develop: sif
# date: 2022-09-30 17:13

# 显示不同形状的结构元
import cv2
kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
kernel_2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (10, 10))
kernel_3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
print('kernel_1=\n', kernel_1)
print('kernel_2=\n', kernel_2)
print('kernel_3=\n', kernel_3)
