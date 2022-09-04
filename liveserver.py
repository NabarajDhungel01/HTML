import pyautogui
import time

import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

time.sleep(0.5)









pyautogui.hotkey("ctrl", "k")
pyautogui.hotkey("ctrl", "q")

time.sleep(3)

pyautogui.hotkey("ctrl", "l")
pyautogui.hotkey("ctrl", "c")

time.sleep(0.5)

pyautogui.hotkey("win", "altleft" )

time.sleep(0.5)

pyautogui.hotkey("ctrl", "l")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")


time.sleep(5)
exit()