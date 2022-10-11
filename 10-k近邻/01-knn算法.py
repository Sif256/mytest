# coding: utf-8
# filename: 01-knn算法
# develop: sif
# date: 2022-10-10 09:46

# 0~7图像 作为训练数据 test_7作为测试数据 实现图像识别
# 1 获取训练集数据
import cv2
import numpy as np
num = 8
row = 240
col = 240
a = np.zeros((num, row, col))
print(a.ndim)
for i in range(num):
    img = cv2.imread('temp/%d.png' % i, 0)
    a[i, :, :] = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('img' + str(i), img)
# 2 提取样本数据的特征值
feature = np.zeros((num, round(row/5), round(col/5)))
for ni in range(num):
    for nr in range(row):
        for nc in range(col):
            if a[ni, nr, nc] == 255:
                feature[ni, int(nr/5), int(nc/5)] += 1

train = feature[:, :].reshape(-1, round(row/5)*round(col/5)).astype(np.float32)
print(train)
# 3 贴标签
trainLabel = [i for i in range(num)]
trainLabel = np.array(trainLabel)
# print(trainLabel)
# 4 测试样本并获取特征值
o = cv2.imread('test_num7.png', 0)
o = cv2.threshold(o, 127, 255, cv2.THRESH_BINARY)[1]
of = np.zeros((round(row/5), round(col/5)))
for nr in range(row):
    for nc in range(col):
        if o[nr, nc] == 255:
            of[int(nr/5), int(nc/5)] += 1
test = of.reshape(-1, round(row/5)*round(col/5)).astype(np.float32)
# 5 knn算法进行数字识别
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, trainLabel)
rt, result, bour, dlist = knn.findNearest(test, 3)
print('类型', result)
print('最近的几个邻居', bour)
print('最近几个邻居的距离', dlist)
