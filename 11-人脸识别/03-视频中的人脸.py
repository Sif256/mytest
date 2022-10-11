# coding: utf-8
# filename: 03-视频中的人脸
# develop: sif
# date: 2022-10-10 15:34

# 捕获视频中的人脸
import cv2


def demo_video(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 调用级联分级器
    facecade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    face = facecade.detectMultiScale(gray)
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (32, 155, 122), 2)
    cv2.imshow('img', img)


# 读取视频中的人脸
cap = cv2.VideoCapture('t9.mp4')

# 使用while播放
while True:
    flag, frame = cap.read()
    if not flag:
        break;
    demo_video(frame)
    if ord('q') == cv2.waitKey(5):
        break;
cv2.destroyAllWindows()
cap.release()
