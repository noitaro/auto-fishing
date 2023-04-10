# pip install pywin32
import win32api
import win32con
import ctypes
import time
ULONG_PTR = ctypes.POINTER(ctypes.c_ulong)
import pyautogui
import pydirectinput

time.sleep(5)

# # 'C'キーを押す
# win32api.keybd_event(0x43, 0, 0, 0)
# time.sleep(0.1)
# # 'C'キーを離す
# win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)


# マウスイベントの情報
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ULONG_PTR)]

class CTYPESINPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("mi", MOUSEINPUT)]

# #マウス制御初期化諸々
# LPINPUT = ctypes.POINTER(CTYPESINPUT)
# SendInput = ctypes.windll.user32.SendInput
# SendInput.argtypes = (ctypes.c_uint, LPINPUT, ctypes.c_int)
# SendInput.restype = ctypes.c_uint

# #座標指定
# for i in range(800):
#     x, y = i, i
#     x = x * 65536 // 1920
#     y = y * 65536 // 1080
#     # MOUSEINPUT(x座標, y座標, ホイールの回転量, マウスイベント, 0, None)
#     _mi = MOUSEINPUT(x, y, 0, (0x0001 | 0x8000), 0, None)
#     # SendInput(1, CTYPESINPUT(入力の種類, _mi), ctypes.sizeof(CTYPESINPUT))
#     SendInput(1, CTYPESINPUT(0, _mi), ctypes.sizeof(CTYPESINPUT))
#     time.sleep(0.0001)


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_long),
                ("wScan", ctypes.c_long),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ULONG_PTR)]


class CTYPESKEYINPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ki", KEYBDINPUT)]


LPINPUT = ctypes.POINTER(CTYPESKEYINPUT)
SendInput = ctypes.windll.user32.SendInput
SendInput.argtypes = (ctypes.c_uint, LPINPUT, ctypes.c_int)
SendInput.restype = ctypes.c_uint

_ki = KEYBDINPUT(0x43, 0, 0x0001, 0, None)
SendInput(1, CTYPESKEYINPUT(1, _ki), ctypes.sizeof(CTYPESKEYINPUT))

time.sleep(0.1)

_ki = KEYBDINPUT(0x43, 0, 0x0002, 0, None)
SendInput(1, CTYPESKEYINPUT(1, _ki), ctypes.sizeof(CTYPESKEYINPUT))
