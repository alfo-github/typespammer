import pyautogui
import keyboard
import string
import time

print("""

░██████╗██████╗░░█████╗░███╗░░░███╗  ██████╗░██╗░░░██╗  ░█████╗░██╗░░░░░███████╗░█████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║  ██╔══██╗╚██╗░██╔╝  ██╔══██╗██║░░░░░██╔════╝██╔══██╗
╚█████╗░██████╔╝███████║██╔████╔██║  ██████╦╝░╚████╔╝░  ███████║██║░░░░░█████╗░░██║░░██║
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║  ██╔══██╗░░╚██╔╝░░  ██╔══██║██║░░░░░██╔══╝░░██║░░██║
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║  ██████╦╝░░░██║░░░  ██║░░██║███████╗██║░░░░░╚█████╔╝
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░
""")

print("[1] For Spam one phrase")

a = int(input("Key: "))

if a == 1:
    k = input("Insert the word to spam")
    count = int(input("How many Times do you want to spam?"))
    print("You have five seconds")
    time.sleep(5)
    for i in range(count):
        keyboard.write(k)
        keyboard.press("enter")
        time.sleep(0.1)
         
