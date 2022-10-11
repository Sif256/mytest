# coding: utf-8
# filename: 04-保存训练集
# develop: sif
# date: 2022-10-11 10:47

# 获取训练集中的数据 进行训练 保存结果到一个文件中
import os
import cv2
import numpy as np


def get_faces_and_tag(path_1):
    faces_data_1 = []
    ids_1 = []
    # 获取训练图像数据
    img_paths = [os.path.join(path_1, j) for j in os.listdir(path_1)]
    facecade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    for imgPath in img_paths:
        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facecade.detectMultiScale(gray)
        # 打标签
        user = {'h': 1, 'l': 2, 'y': 3}
        class_id = os.path.split(imgPath)[1].split('_')[0]
        new_id = user[class_id]
        # print(class_id)
        # print(id)
        for x, y, w, h in faces:
            faces_data_1.append(gray[y:y+h, x:x+w])
            ids_1.append(new_id)
    # print(imgPaths)
    return faces_data_1, ids_1


# 1 准备训练集数据
path = "pic/faces_img/"
# 2 获取脸部数据和标签
faces_data, ids = get_faces_and_tag(path)
print(faces_data)
print(ids)
# 3 训练数据并保存训练的数据模型
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces_data, np.array(ids))
recognizer.write('face_data.yml')
