# pip install pywin32
from cv2 import Mat
import win32api # pip install pywin32
import win32con
import ctypes
import time
import pyautogui
import pydirectinput
import cv2
import numpy as np
import datetime

import os
import sys
import win32com.shell.shell as shell
if not shell.IsUserAnAdmin():
    print("Administrator permissions required. Restarting...")
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=os.path.abspath(__file__), nShow=1)
    sys.exit()

# time.sleep(5)
# pydirectinput.press('c')

# 画像データを持つOpenCVのmat形式の画像データ
image_one = cv2.imread("one.png")
image_one = cv2.cvtColor(image_one, cv2.COLOR_BGR2GRAY)
image_two = cv2.imread("two.png")
image_two = cv2.cvtColor(image_two, cv2.COLOR_BGR2GRAY)
image_three = cv2.imread("three.png")
image_three = cv2.cvtColor(image_three, cv2.COLOR_BGR2GRAY)
image_four = cv2.imread("four.png")
image_four = cv2.cvtColor(image_four, cv2.COLOR_BGR2GRAY)
template_image = [image_one, image_two, image_three, image_four]

# def matchTemplate(img: Mat, template: Mat):
#     result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
#     _, max_val, _, _ = cv2.minMaxLoc(result)
#     return 0.8 < max_val

# 1600 x 900
y, w, h = 617, 25, 29
x1_1 = 705
x2_1 = 787
x1_2 = 869
x2_2 = 952
x1_3 = 1034
x2_3 = 1117
x1_4 = 1198

while True:

    # スクリーンショットを取得し、PIL Imageとして取得する
    screenshot = pyautogui.screenshot()
    pil_image = screenshot.convert('RGB')

    # PIL ImageをNumPy配列に変換する
    numpy_image = np.array(pil_image)

    # NumPy配列をOpenCVのmat形式に変換する
    image_data = cv2.cvtColor(numpy_image, cv2.COLOR_BGR2GRAY)

    # PNG形式で画像を保存する
    # cv2.imwrite("image.png", image_data, [cv2.IMWRITE_PNG_COMPRESSION, 0])

    # 指定された範囲で画像をトリミングする
    # img[top : bottom, left : right]
    cropped_image1_1 = image_data[y:y+h, x1_1:x1_1+w]
    cropped_image2_1 = image_data[y:y+h, x2_1:x2_1+w]
    cropped_image1_2 = image_data[y:y+h, x1_2:x1_2+w]
    cropped_image2_2 = image_data[y:y+h, x2_2:x2_2+w]
    cropped_image1_3 = image_data[y:y+h, x1_3:x1_3+w]
    cropped_image2_3 = image_data[y:y+h, x2_3:x2_3+w]
    cropped_image1_4 = image_data[y:y+h, x1_4:x1_4+w]

    key_press = []
    completion = False

    if completion == False:
        key_press1 = []
        pattern1 = [cropped_image1_1, cropped_image1_2, cropped_image1_3, cropped_image1_4]
        for i, img in enumerate(pattern1):
            result1 = cv2.matchTemplate(img, image_one, cv2.TM_CCOEFF_NORMED)
            result2 = cv2.matchTemplate(img, image_two, cv2.TM_CCOEFF_NORMED)
            result3 = cv2.matchTemplate(img, image_three, cv2.TM_CCOEFF_NORMED)
            result4 = cv2.matchTemplate(img, image_four, cv2.TM_CCOEFF_NORMED)
            
            _, max_val1, _, _ = cv2.minMaxLoc(result1)
            _, max_val2, _, _ = cv2.minMaxLoc(result2)
            _, max_val3, _, _ = cv2.minMaxLoc(result3)
            _, max_val4, _, _ = cv2.minMaxLoc(result4)

            result = 0
            if 0.8 < max_val1: result = 1
            if 0.8 < max_val2 and max_val1 < max_val2: result = 2
            if 0.8 < max_val3 and max_val2 < max_val3: result = 3
            if 0.8 < max_val4 and max_val3 < max_val4: result = 4

            if result >= 1: key_press1.append(str(result))
            pass

        if len(key_press1) == len(pattern1):
            completion = True
            key_press = key_press1
            pass
        pass

    if completion == False:
        key_press2 = []
        pattern2 = [cropped_image2_1, cropped_image2_2, cropped_image2_3]
        for i, img in enumerate(pattern2):
            result1 = cv2.matchTemplate(img, image_one, cv2.TM_CCOEFF_NORMED)
            result2 = cv2.matchTemplate(img, image_two, cv2.TM_CCOEFF_NORMED)
            result3 = cv2.matchTemplate(img, image_three, cv2.TM_CCOEFF_NORMED)
            result4 = cv2.matchTemplate(img, image_four, cv2.TM_CCOEFF_NORMED)
            
            _, max_val1, _, _ = cv2.minMaxLoc(result1)
            _, max_val2, _, _ = cv2.minMaxLoc(result2)
            _, max_val3, _, _ = cv2.minMaxLoc(result3)
            _, max_val4, _, _ = cv2.minMaxLoc(result4)

            result = 0
            if 0.8 < max_val1: result = 1
            if 0.8 < max_val2 and max_val1 < max_val2: result = 2
            if 0.8 < max_val3 and max_val2 < max_val3: result = 3
            if 0.8 < max_val4 and max_val3 < max_val4: result = 4

            if result >= 1: key_press2.append(str(result))
            pass

        if len(key_press2) == len(pattern2):
            completion = True
            key_press = key_press2
            pass
        pass
    
    if completion == False:
        key_press3 = []
        pattern3 = [cropped_image1_2, cropped_image1_3]
        for i, img in enumerate(pattern3):
            result1 = cv2.matchTemplate(img, image_one, cv2.TM_CCOEFF_NORMED)
            result2 = cv2.matchTemplate(img, image_two, cv2.TM_CCOEFF_NORMED)
            result3 = cv2.matchTemplate(img, image_three, cv2.TM_CCOEFF_NORMED)
            result4 = cv2.matchTemplate(img, image_four, cv2.TM_CCOEFF_NORMED)
            
            _, max_val1, _, _ = cv2.minMaxLoc(result1)
            _, max_val2, _, _ = cv2.minMaxLoc(result2)
            _, max_val3, _, _ = cv2.minMaxLoc(result3)
            _, max_val4, _, _ = cv2.minMaxLoc(result4)

            result = 0
            if 0.8 < max_val1: result = 1
            if 0.8 < max_val2 and max_val1 < max_val2: result = 2
            if 0.8 < max_val3 and max_val2 < max_val3: result = 3
            if 0.8 < max_val4 and max_val3 < max_val4: result = 4

            if result >= 1: key_press3.append(str(result))
            pass

        if len(key_press3) == len(pattern3):
            completion = True
            key_press = key_press3
            pass
        pass
    
    if completion == False:
        key_press4 = []
        pattern4 = [cropped_image2_2]
        for i, img in enumerate(pattern4):
            result1 = cv2.matchTemplate(img, image_one, cv2.TM_CCOEFF_NORMED)
            result2 = cv2.matchTemplate(img, image_two, cv2.TM_CCOEFF_NORMED)
            result3 = cv2.matchTemplate(img, image_three, cv2.TM_CCOEFF_NORMED)
            result4 = cv2.matchTemplate(img, image_four, cv2.TM_CCOEFF_NORMED)
            
            _, max_val1, _, _ = cv2.minMaxLoc(result1)
            _, max_val2, _, _ = cv2.minMaxLoc(result2)
            _, max_val3, _, _ = cv2.minMaxLoc(result3)
            _, max_val4, _, _ = cv2.minMaxLoc(result4)

            result = 0
            if 0.8 < max_val1: result = 1
            if 0.8 < max_val2 and max_val1 < max_val2: result = 2
            if 0.8 < max_val3 and max_val2 < max_val3: result = 3
            if 0.8 < max_val4 and max_val3 < max_val4: result = 4

            if result >= 1: key_press4.append(str(result))
            pass
        
        if len(key_press4) == len(pattern4):
            completion = True
            key_press = key_press4
            pass
        pass
    
    if completion == True:
        now = datetime.datetime.now()
        print("{}: {}".format(now.strftime("%Y-%m-%d %H:%M:%S"), ", ".join(map(str, key_press))))

        # # PNG形式で画像を保存する
        # cv2.imwrite(f'imwrite\image_{now.strftime("%Y%m%d%H%M%S")}_{"".join(map(str, key_press))}.png', image_data, [cv2.IMWRITE_PNG_COMPRESSION, 0])

        for key in key_press:
            pydirectinput.keyDown(key)
            pydirectinput.keyUp(key)
            pass
        pass

    pass


# # トリミングした画像を表示する
# cv2.imshow("Cropped Image", cropped_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
