import os
import cv2
import numpy as np

file_names = list(range(0, 13)) 
train = []
train_labels = []
for file_name in file_names: 
    path = './training_data/' + str(file_name) + '/' #0 부터 12 폴더 경로
    file_count = len(next(os.walk(path))[2]) # 폴더 내의 파일 개수 확인
    for i in range(1, file_count + 1): # 파일 개수만큼 이미지를 흑백화
        img = cv2.imread(path + str(i) + '.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        train.append(gray) # 이미지
        train_labels.append(file_name) # 이미지 라벨

x = np.array(train)
train = x[:, :].reshape(-1, 400).astype(np.float32) # 러닝머신을 위한 정제
train_labels = np.array(train_labels)[:, np.newaxis] 

np.savez("trained.npz", train=train, train_labels=train_labels)