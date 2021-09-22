from pynput.keyboard import Key, Controller
import os           
import pyautogui
import keyboard
import time
import pyautogui

path = os.getcwd() and __file__
file = 'raadeens'


os.system(f'start cmd {path}')
time.sleep(0.1)
keyboard.write(f'py {file}.py')
pyautogui.press('enter')