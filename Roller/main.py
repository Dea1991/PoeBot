import pyautogui as pg
# python -m pip install pyautogui
import pyperclip as pc
# python -m pip install pyperclip
import time
import keyboard
txt = 0


def roll_alt():
    pg.moveTo(121, 277, 0.1)
    pg.click(button='right')
    pg.moveTo(361, 471, 0.1)
    pg.click(button='left')
    time.sleep(0.2)
    pg.hotkey('ctrl', 'alt', 'c')
    file = open('data.txt', "w", encoding='utf-8')
    file.write(pc.paste())
    file.close()
    file1 = open('data.txt')
    read_txt = file1.read()

    if "Prefix" not in read_txt:
        pg.moveTo(224, 325, 0.1)
        pg.click(button='right')
        pg.moveTo(361, 471, 0.1)
        pg.click(button='left')
        time.sleep(0.2)
        pg.hotkey('ctrl', 'alt', 'c')
        file1.close()
        file2 = open('data.txt', "w", encoding='utf-8')
        file2.write(pc.paste())
        file2.close()


a = 0
count_alt = 0
roll_alt()

file3 = open('data.txt')
read_txt1 = file3.read()
if "Dictator's" in read_txt1:
    a = 1
    print("Merciless")
if "Merciless" in read_txt1:
    a = 1
    print("Merciless")

while a != 1:
    roll_alt()
    count_alt += 1
    file3 = open('data.txt')
    read_txt1 = file3.read()
    if "Merciless" in read_txt1:
        a = 1
        print("Merciless")
    if "Dictator's" in read_txt1:
        a = 1
        print("Dictator's")
    print(count_alt)
