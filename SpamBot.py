from pynput.keyboard import Key, Controller
from colorama import Fore
import time
import colorama
colorama.init(autoreset=True)

title = (Fore.BLUE + """
______ _            _       _____                        ______       _   
| ___ \ |          ( )     /  ___|                       | ___ \     | |  
| |_/ / |_   _  ___|/ ___  \ `--. _ __   __ _ _ __ ___   | |_/ / ___ | |_ 
| ___ \ | | | |/ _ \ / __|  `--. \ '_ \ / _` | '_ ` _ \  | ___ \/ _ \| __|
| |_/ / | |_| |  __/ \__ \ /\__/ / |_) | (_| | | | | | | | |_/ / (_) | |_ 
\____/|_|\__,_|\___| |___/ \____/| .__/ \__,_|_| |_| |_| \____/ \___/ \__|
                                 | |                                      
                                 |_|                                      
""")

print(title)
print(Fore.RED + "Use at your own risk, I am not liable for any accounts being lost due to self botting or other reasons.")
print(Fore.RED + "You have been warned".upper())


spam = input(Fore.CYAN + "Enter the string you want to spam: " + Fore.WHITE)
length_input = input(Fore.CYAN + "Enter the amount of times you want the message to be spammed: " + Fore.WHITE)
delay_input = input(Fore.CYAN + "Enter the delay between sending each message in seconds: " + Fore.WHITE)
enter = input(Fore.CYAN + "Would you like it to press enter at the end of each message? Y/N " + Fore.WHITE)

length = int(length_input)
delay = int(delay_input)

keyboard = Controller()

time.sleep(1)

def message():
    keyboard.type(spam)
    if enter == "y":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(delay)
    else:
        time.sleep(delay)

print(Fore.RED + "You have 3 seconds to navigate to the desired spam location".upper())

time.sleep(3)

for x in range(0, length):
    message()


print(Fore.GREEN + "Spam Complete")

wait_for_ = input("Press any key to close...")
