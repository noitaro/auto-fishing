# pip install pywin32
# pip install keyboard
# pip install pyautogui
# pip install opencv-python
# pip install Pillow

# https://github.com/KianBrose/Image-Recognition-Botting-Tutorial
# https://teratail.com/questions/79973

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import keyboard
import time

def send_keys(element, message):
    element.send_keys(message)
    element.send_keys(Keys.ENTER)

driver = webdriver.Chrome(executable_path="C:\\Users\\katof\\Desktop\\auto-fishing\\chromedriver.exe")

driver.get("https://googlechromelabs.github.io/serial-terminal/")

connectBtn = driver.find_element_by_xpath("//*[@id='connect']")
connectBtn.click()

time.sleep(5)

terminal = driver.find_element_by_xpath("//*[@id='terminal']/div/div[2]/div/textarea")

# 初期化
terminal.send_keys(Keys.CONTROL, "d")
terminal.send_keys(Keys.ENTER)
time.sleep(1)

send_keys(terminal, 'import time')
send_keys(terminal, 'import usb_hid')
send_keys(terminal, 'from adafruit_hid.keyboard import Keyboard')
send_keys(terminal, 'from adafruit_hid.keycode import Keycode')
send_keys(terminal, 'kbd = Keyboard(usb_hid.devices)')

send_keys(terminal, 'def i(*args):')
send_keys(terminal, 'for arg in args:')
send_keys(terminal, 'if arg == 1:')
send_keys(terminal, 'kbd.press(Keycode.ONE)')
send_keys(terminal, 'time.sleep(0.05)')
send_keys(terminal, 'kbd.release(Keycode.ONE)')
send_keys(terminal, 'pass')
terminal.send_keys(Keys.ENTER)
terminal.send_keys(Keys.ENTER)
terminal.send_keys('        ')
send_keys(terminal, 'elif arg == 2:')
send_keys(terminal, 'kbd.press(Keycode.TWO)')
send_keys(terminal, 'time.sleep(0.05)')
send_keys(terminal, 'kbd.release(Keycode.TWO)')
send_keys(terminal, 'pass')
terminal.send_keys(Keys.ENTER)
terminal.send_keys(Keys.ENTER)
terminal.send_keys('        ')
send_keys(terminal, 'elif arg == 3:')
send_keys(terminal, 'kbd.press(Keycode.THREE)')
send_keys(terminal, 'time.sleep(0.05)')
send_keys(terminal, 'kbd.release(Keycode.THREE)')
send_keys(terminal, 'pass')
terminal.send_keys(Keys.ENTER)
terminal.send_keys(Keys.ENTER)
terminal.send_keys('        ')
send_keys(terminal, 'elif arg == 4:')
send_keys(terminal, 'kbd.press(Keycode.FOUR)')
send_keys(terminal, 'time.sleep(0.05)')
send_keys(terminal, 'kbd.release(Keycode.FOUR)')
send_keys(terminal, 'pass')
terminal.send_keys(Keys.ENTER)
terminal.send_keys(Keys.ENTER)
terminal.send_keys('        ')
send_keys(terminal, 'time.sleep(0.05)')
send_keys(terminal, 'pass')
terminal.send_keys(Keys.ENTER)
terminal.send_keys(Keys.ENTER)
terminal.send_keys(Keys.ENTER)

time.sleep(5)

# 画像
ONE_IMG = 'one.png'     # 1
TWO_IMG = 'two.png'     # 2
THREE_IMG = 'three.png'  # 3
FOUR_IMG = 'four.png'   # 4

# 判定比率
CONFIDENCE = 0.8

# Y軸
_Y = 615

# サイズ
_WIDTH = 50
_HEIGHT = 40

# QET
QUADRUPLE_LEFT_OUTSIDE_X = 686   # 四連左外
TRIPLE_LEFT_X = 768              # 三連左
QUADRUPLE_LEFT_INSIDE_X = 850    # 四連左中
TRIPLE_CENTER_X = 932            # 三連中
QUADRUPLE_RIGHT_INSIDE_X = 1015  # 四連右中
TRIPLE_RIGHT_X = 1097            # 三連右
QUADRUPLE_RIGHT_OUTSIDE_X = 1179 # 四連右外

oldargs = ''
while keyboard.is_pressed('ctrl') == False:
    command = []
    triple = False
    double = False
    quadruple = False

    # 四連
    # 左外
    if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
        command.append(1)
        quadruple = True
        pass
    elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
        command.append(2)
        quadruple = True
        pass
    elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
        command.append(3)
        quadruple = True
        pass
    elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
        command.append(4)
        quadruple = True
        pass
    else:
        pass

    if quadruple:
        # 左中
        if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(1)
            pass
        elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(2)
            pass
        elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(3)
            pass
        elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(4)
            pass
        else:
            pass

        # 右中
        if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(1)
            pass
        elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(2)
            pass
        elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(3)
            pass
        elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(4)
            pass
        else:
            pass
        pass

        # 右外
        if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(1)
            pass
        elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(2)
            pass
        elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(3)
            pass
        elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(4)
            pass
        else:
            pass

        pass
    else:
        # 二連
        # 左
        if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(1)
            double = True
            pass
        elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(2)
            double = True
            pass
        elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(3)
            double = True
            pass
        elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            command.append(4)
            double = True
            pass
        else:
            pass

        if double:
            # 右
            if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
                command.append(1)
                double = True
                pass
            elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
                command.append(2)
                double = True
                pass
            elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
                command.append(3)
                double = True
                pass
            elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_RIGHT_INSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
                command.append(4)
                double = True
                pass
            else:
                pass
            pass
        else:
            # 三連
            # 左
            if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_LEFT_X, _Y, _WIDTH, _HEIGHT)) != None:
                command.append(1)
                triple = True
                pass
            elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_LEFT_X, _Y, _WIDTH, _HEIGHT)) != None:
                command.append(2)
                triple = True
                pass
            elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_LEFT_X, _Y, _WIDTH, _HEIGHT)) != None:
                command.append(3)
                triple = True
                pass
            elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_LEFT_X, _Y, _WIDTH, _HEIGHT)) != None:
                command.append(4)
                triple = True
                pass
            else:
                pass

            if triple:
                # 中央
                if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_CENTER_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(1)
                    pass
                elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_CENTER_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(2)
                    pass
                elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_CENTER_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(3)
                    pass
                elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_CENTER_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(4)
                    pass
                else:
                    pass
                # 右
                if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_RIGHT_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(1)
                    pass
                elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_RIGHT_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(2)
                    pass
                elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_RIGHT_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(3)
                    pass
                elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_RIGHT_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(4)
                    pass
                else:
                    pass
                pass
            else:
                # 単一
                if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_CENTER_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(1)
                    pass
                elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_CENTER_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(2)
                    pass
                elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_CENTER_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(3)
                    pass
                elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(TRIPLE_CENTER_X, _Y, _WIDTH, _HEIGHT)) != None:
                    command.append(4)
                    pass
                else:
                    pass
                pass
            pass
        pass

    # ダブルが終わった後、トリプルじゃなかったか確認
    if double:
        isNG = False
        # 四連
        # 左外
        if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            isNG = True
            pass
        elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            isNG = True
            pass
        elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            isNG = True
            pass
        elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(QUADRUPLE_LEFT_OUTSIDE_X, _Y, _WIDTH, _HEIGHT)) != None:
            isNG = True
            pass
        else:
            pass
        pass

        # トリプルだったらやり直し
        if isNG:
            continue

    if len(command) > 0:
        args = ''
        for cmd in command:
            args += str(cmd) + ','
            pass
        if oldargs != args:
            oldargs = args
            print(args)
            send_keys(terminal, 'i(*[' + args + '])')
            time.sleep(1)
            pass

driver.close()
driver.quit()