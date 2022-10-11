# coding: utf-8
# filename: 05-人脸识别
# develop: sif
# date: 2022-10-11 11:42

# 读取一幅新的图像 样品的测试 进行识别 显示识别结果
import cv2
# 1 读取训练模型数据
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_data.yml')
# 2 新的人脸图像的识别
img = cv2.imread('pic/test_l_10.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
facecade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
face = facecade.detectMultiScale(gray)
names = {1: '鹿晗', 2: '刘诗诗', 3: '杨幂'}
# 显示结果
for x, y, h , w in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (123, 32, 233), 2)
    # 3 人脸识别
    new_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
    print('识别的用户是:%s, 置信评分:%s' % (names[new_id], confidence))
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
