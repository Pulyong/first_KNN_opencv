import cv2
import numpy as np
import re
import os

os.chdir("C:/Users/rla02/OneDrive/바탕 화면/용진/파이썬/Git/opencv_Knn/Opencv_test")
BLUE = 0
GREEN = 1
RED = 2
# 특정한 색상의 모든 단어가 포함된 이미지를 추출합니다.
def get_chars(image, color):
    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3

    c = image[:, :, other_1] == 255 #선택하지 않은 색을 검은색으로
    image[c] = [0, 0, 0]
    c = image[:, :, other_2] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, color] < 170 # 겹치는 부분중 선택하지 않은색 검은색으로
    image[c] = [0, 0, 0]
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255]
    return image

def extract_chars(image):
    chars = []
    colors = [BLUE, GREEN, RED]
    for color in colors:
        image_from_one_color = get_chars(image.copy(), color)
        image_gray = cv2.cvtColor(image_from_one_color, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image_gray, 127, 255, 0)
        # RETR_EXTERNAL 옵션으로 숫자의 외각을 기준으로 분리
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            # 추출된 이미지 크기가 50 이상인 경우만 실제 문자 데이터인 것으로 파악
            area = cv2.contourArea(contour)
            if area > 50:
                x, y, width, height = cv2.boundingRect(contour)
                roi = image_gray[y:y + height, x:x + width]
                chars.append((x, roi))
    chars = sorted(chars, key=lambda char: char[0])
    return chars

# 특정한 이미지를 (20x20) 크기로 scaling
def resize20(image):
    resized = cv2.resize(image,(20,20))
    return resized.reshape(-1,400).astype(np.float32)

def remove_first_0(string):
    temp = []
    for i in string:
        if i == '+' or i == '-' or i == '*':
            temp.append(i)
    split = re.split('\*|\+|-', string)
    i = 0
    temp_count = 0
    result = ""
    for a in split:
        a = a.lstrip('0')
        if a == '':
            a = '0'
        result += a
        if i < len(split) - 1:
            result += temp[temp_count]
            temp_count = temp_count + 1
        i = i + 1
    return result