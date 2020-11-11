import time
import pyautogui
import keyboard
import colorama
from colorama import Fore
from colors import green, red, white

def spammerv2():
    time.sleep(2)
    print(red())
    print("""

    █▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀█   █░█ ▀█
    ▄█ █▀▀ █▀█ █░▀░█ █░▀░█ ██▄ █▀▄   ▀▄▀ █▄
    \n\nby Alfo

    """)



    print("[+] The spam is starting...", white())
    print("[?] If you want to change the word write them in spammer.txt", white())
    print("Good Trolling, by alfo", green())

    try:
        f = open("spammer.txt", 'r')
    except IOError:
        print("[-] No file named spammer.txt creating new", red())
        f = open("spammer.txt", "x")

    for word in f:
       keyboard.write(word, 0.01)
       keyboard.press('enter')
       time.sleep(0.5)
       print("[+] Succesfully Writed" + " " + word, green())

spammerv2()
