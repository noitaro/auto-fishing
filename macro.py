import pyautogui
import keyboard
import time

pyautogui.hotkey('alt', 'tab')

time.sleep(1)

pyautogui.typewrite('print("Hello")\n')

pyautogui.typewrite('import time\n')
pyautogui.typewrite('import usb_hid\n')
pyautogui.typewrite('from adafruit_hid.keyboard import Keyboard\n')
pyautogui.typewrite('from adafruit_hid.keycode import Keycode\n')
pyautogui.typewrite('from adafruit_hid.mouse import Mouse\n')
# pyautogui.typewrite('from machine import Pin\n')

pyautogui.typewrite('kbd = Keyboard(usb_hid.devices)\n')
pyautogui.typewrite('m = Mouse(usb_hid.devices)\n')
# pyautogui.typewrite('led = Pin(25, Pin.OUT)\n')

pyautogui.typewrite('def reset():\n')
pyautogui.typewrite('kbd.press(Keycode.ALT)\n')
pyautogui.typewrite('time.sleep(0.2)\n')
pyautogui.typewrite('kbd.press(Keycode.TAB)\n')
pyautogui.typewrite('time.sleep(0.2)\n')
pyautogui.typewrite('kbd.release(Keycode.TAB)\n')
pyautogui.typewrite('time.sleep(0.2)\n')
pyautogui.typewrite('kbd.release(Keycode.ALT)\n')
pyautogui.typewrite('time.sleep(0.2)\n')
pyautogui.typewrite('\n\n\n')

pyautogui.typewrite('def one():\n')
pyautogui.typewrite('time.sleep(0.2)\n')
pyautogui.typewrite('kbd.send(Keycode.ONE)\n')
pyautogui.typewrite('time.sleep(0.1)\n')
pyautogui.typewrite('\n\n\n')

pyautogui.typewrite('def two():\n')
pyautogui.typewrite('time.sleep(0.2)\n')
pyautogui.typewrite('kbd.send(Keycode.TWO)\n')
pyautogui.typewrite('time.sleep(0.1)\n')
pyautogui.typewrite('\n\n\n')

pyautogui.typewrite('def three():\n')
pyautogui.typewrite('time.sleep(0.2)\n')
pyautogui.typewrite('kbd.send(Keycode.THREE)\n')
pyautogui.typewrite('time.sleep(0.1)\n')
pyautogui.typewrite('\n\n\n')

pyautogui.typewrite('def four():\n')
pyautogui.typewrite('time.sleep(0.2)\n')
pyautogui.typewrite('kbd.send(Keycode.FOUR)\n')
pyautogui.typewrite('time.sleep(0.1)\n')
pyautogui.typewrite('\n\n\n')

# pyautogui.typewrite('main()\n')
# pyautogui.keyDown('alt')
# pyautogui.press('tab')
# pyautogui.keyUp('alt')

time.sleep(5)

while keyboard.is_pressed('ctrl') == False:
    command = []
    triple = False

    # 三連
    # 左
    if pyautogui.locateCenterOnScreen('one.png', grayscale=True, confidence=0.8, region=(768, 615, 50, 40)) != None:
        print("1")
        command.append('one()\n')
        triple = True
        pass
    elif pyautogui.locateCenterOnScreen('two.png', grayscale=True, confidence=0.8, region=(768, 615, 50, 40)) != None:
        print("2")
        command.append('two()\n')
        triple = True
        pass
    elif pyautogui.locateCenterOnScreen('three.png', grayscale=True, confidence=0.8, region=(768, 615, 50, 40)) != None:
        print("3")
        command.append('three()\n')
        triple = True
        pass
    elif pyautogui.locateCenterOnScreen('four.png', grayscale=True, confidence=0.8, region=(768, 615, 50, 40)) != None:
        print("4")
        command.append('four()\n')
        triple = True
        pass
    else:
        pass

    if triple:
        # 中央
        if pyautogui.locateCenterOnScreen('one.png', grayscale=True, confidence=0.8, region=(932, 615, 50, 40)) != None:
            print("1")
            command.append('one()\n')
            pass
        elif pyautogui.locateCenterOnScreen('two.png', grayscale=True, confidence=0.8, region=(932, 615, 50, 40)) != None:
            print("2")
            command.append('two()\n')
            pass
        elif pyautogui.locateCenterOnScreen('three.png', grayscale=True, confidence=0.8, region=(932, 615, 50, 40)) != None:
            print("3")
            command.append('three()\n')
            pass
        elif pyautogui.locateCenterOnScreen('four.png', grayscale=True, confidence=0.8, region=(932, 615, 50, 40)) != None:
            print("4")
            command.append('four()\n')
            pass
        else:
            pass
        # 右
        if pyautogui.locateCenterOnScreen('one.png', grayscale=True, confidence=0.8, region=(1097, 615, 50, 40)) != None:
            print("1")
            command.append('one()\n')
            pass
        elif pyautogui.locateCenterOnScreen('two.png', grayscale=True, confidence=0.8, region=(1097, 615, 50, 40)) != None:
            print("2")
            command.append('two()\n')
            pass
        elif pyautogui.locateCenterOnScreen('three.png', grayscale=True, confidence=0.8, region=(1097, 615, 50, 40)) != None:
            print("3")
            command.append('three()\n')
            pass
        elif pyautogui.locateCenterOnScreen('four.png', grayscale=True, confidence=0.8, region=(1097, 615, 50, 40)) != None:
            print("4")
            command.append('four()\n')
            pass
        else:
            pass
        pass
    else:
        # 単一
        if pyautogui.locateCenterOnScreen('one.png', grayscale=True, confidence=0.8, region=(932, 615, 50, 40)) != None:
            print("1")
            command.append('one()\n')
            pass
        elif pyautogui.locateCenterOnScreen('two.png', grayscale=True, confidence=0.8, region=(932, 615, 50, 40)) != None:
            print("2")
            command.append('two()\n')
            pass
        elif pyautogui.locateCenterOnScreen('three.png', grayscale=True, confidence=0.8, region=(932, 615, 50, 40)) != None:
            print("3")
            command.append('three()\n')
            pass
        elif pyautogui.locateCenterOnScreen('four.png', grayscale=True, confidence=0.8, region=(932, 615, 50, 40)) != None:
            print("4")
            command.append('four()\n')
            pass
        else:
            pass
        pass

    if len(command) > 0:
        pyautogui.typewrite('def main():\n')
        pyautogui.typewrite('time.sleep(1)\n')
        for cmd in command:
            pyautogui.typewrite(cmd)
            pass
        pyautogui.typewrite('reset()\n')
        pyautogui.typewrite('\n\n\n')
        pyautogui.typewrite('main()\n')
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        time.sleep(6)
        pass

