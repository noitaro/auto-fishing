# pip install pywin32
# pip install keyboard
# pip install pyautogui
# pip install opencv-python
# pip install Pillow

# https://github.com/KianBrose/Image-Recognition-Botting-Tutorial
# https://teratail.com/questions/79973

import pyautogui
import keyboard
import time

# 画像
ONE_IMG = 'one.png'     # 1
TWO_IMG = 'two.png'     # 2
THREE_IMG = 'three.png' # 3
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

def main():

    pyautogui.hotkey('alt', 'tab')

    time.sleep(1)

    pyautogui.typewrite('print("Hello")\n')

    pyautogui.typewrite('import time\n')
    pyautogui.typewrite('import usb_hid\n')
    pyautogui.typewrite('from adafruit_hid.keyboard import Keyboard\n')
    pyautogui.typewrite('from adafruit_hid.keycode import Keycode\n')
    pyautogui.typewrite('kbd = Keyboard(usb_hid.devices)\n')

    pyautogui.typewrite('def i(*args):\n')
    pyautogui.typewrite('time.sleep(0.4)\n')
    pyautogui.typewrite('for arg in args:\n')
    pyautogui.typewrite('if arg == 1:\n')
    pyautogui.typewrite('kbd.press(Keycode.ONE)\n')
    pyautogui.typewrite('time.sleep(0.04)\n')
    pyautogui.typewrite('kbd.release(Keycode.ONE)\n')
    pyautogui.typewrite('pass\n\n\n')
    pyautogui.typewrite('        ')
    pyautogui.typewrite('elif arg == 2:\n')
    pyautogui.typewrite('kbd.press(Keycode.TWO)\n')
    pyautogui.typewrite('time.sleep(0.04)\n')
    pyautogui.typewrite('kbd.release(Keycode.TWO)\n')
    pyautogui.typewrite('pass\n\n\n')
    pyautogui.typewrite('        ')
    pyautogui.typewrite('elif arg == 3:\n')
    pyautogui.typewrite('kbd.press(Keycode.THREE)\n')
    pyautogui.typewrite('time.sleep(0.04)\n')
    pyautogui.typewrite('kbd.release(Keycode.THREE)\n')
    pyautogui.typewrite('pass\n\n\n')
    pyautogui.typewrite('        ')
    pyautogui.typewrite('elif arg == 4:\n')
    pyautogui.typewrite('kbd.press(Keycode.FOUR)\n')
    pyautogui.typewrite('time.sleep(0.04)\n')
    pyautogui.typewrite('kbd.release(Keycode.FOUR)\n')
    pyautogui.typewrite('pass\n\n\n')
    pyautogui.typewrite('        ')
    pyautogui.typewrite('time.sleep(0.04)\n')
    pyautogui.typewrite('pass\n\n\n')
    pyautogui.typewrite('    ')
    pyautogui.typewrite('time.sleep(1)\n')
    pyautogui.typewrite('kbd.press(Keycode.ALT)\n')
    pyautogui.typewrite('time.sleep(0.1)\n')
    pyautogui.typewrite('kbd.press(Keycode.TAB)\n')
    pyautogui.typewrite('time.sleep(0.1)\n')
    pyautogui.typewrite('kbd.release(Keycode.TAB)\n')
    pyautogui.typewrite('time.sleep(0.1)\n')
    pyautogui.typewrite('kbd.release(Keycode.ALT)\n')
    pyautogui.typewrite('time.sleep(0.2)\n')
    pyautogui.typewrite('\n\n\n')

    time.sleep(5)

    oldargs = ''
    while keyboard.is_pressed('ctrl') == False:
        command = []

        # 四連
        # 左外
        ret = screen_search(QUADRUPLE_LEFT_OUTSIDE_X)
        if ret != None:
            command.append(ret)

            # 左中
            ret = screen_search(QUADRUPLE_LEFT_INSIDE_X)
            if ret != None:
                command.append(ret)

                # 右中
                ret = screen_search(QUADRUPLE_RIGHT_INSIDE_X)
                if ret != None:
                    command.append(ret)

                    # 右外
                    ret = screen_search(QUADRUPLE_RIGHT_OUTSIDE_X)
                    if ret != None:
                        command.append(ret)

        else:
            # 三連
            # 左
            ret = screen_search(TRIPLE_LEFT_X)
            if ret != None:
                command.append(ret)

                # 中央
                ret = screen_search(TRIPLE_CENTER_X)
                if ret != None:
                    command.append(ret)

                    # 右
                    ret = screen_search(TRIPLE_RIGHT_X)
                    if ret != None:
                        command.append(ret)

            else:
                # 二連
                # 左
                ret = screen_search(QUADRUPLE_LEFT_INSIDE_X)
                if ret != None:
                    command.append(ret)

                    # 右
                    ret = screen_search(QUADRUPLE_RIGHT_INSIDE_X)
                    if ret != None:
                        command.append(ret)

                else:
                    # 単一
                    ret = screen_search(TRIPLE_CENTER_X)
                    if ret != None:
                        command.append(ret)

        if len(command) > 0:
            args = ''
            for cmd in command:
                args += str(cmd) + ','
                pass
            if oldargs != args:
                oldargs = args
                print(args)
                pyautogui.typewrite('i(*[' + args + '])\n')
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                time.sleep(1)
                pass

def screen_search(_x):
    if pyautogui.locateCenterOnScreen(ONE_IMG, grayscale=True, confidence=CONFIDENCE, region=(_x, _Y, _WIDTH, _HEIGHT)) != None:
        return 1
    elif pyautogui.locateCenterOnScreen(TWO_IMG, grayscale=True, confidence=CONFIDENCE, region=(_x, _Y, _WIDTH, _HEIGHT)) != None:
        return 2
    elif pyautogui.locateCenterOnScreen(THREE_IMG, grayscale=True, confidence=CONFIDENCE, region=(_x, _Y, _WIDTH, _HEIGHT)) != None:
        return 3
    elif pyautogui.locateCenterOnScreen(FOUR_IMG, grayscale=True, confidence=CONFIDENCE, region=(_x, _Y, _WIDTH, _HEIGHT)) != None:
        return 4
    else:
        return None

if __name__ == "__main__":
    main()