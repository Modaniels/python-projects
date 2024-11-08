from colorama import Fore, Style, init
import random
import time
import os

init(autoreset=True)

message = Fore.GREEN + "Happy Birthday, Junior!"

ribbon_symbols = ["*", "~", "@", "#", "$", "!", "&", "^"]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_birthday_message():
    clear_console()
    
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX + "\n" + "="*60)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "🎉🎈 Developer's Special Birthday Banner 🎈🎉")
    print("="*60 + "\n")
    
    print(Style.BRIGHT + message + "\n")
    
    for _ in range(50): 
        x = random.randint(0, 10)  
        y = random.randint(0, 50)  
        symbol = random.choice(ribbon_symbols)
        color = random.choice([Fore.RED, Fore.YELLOW, Fore.MAGENTA, Fore.BLUE, Fore.CYAN, Fore.GREEN])
        
        
        print(f"\033[{x};{y}H" + color + symbol)  
        time.sleep(0.08)  

    
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "\n🎂 Happy  Birthday Junior!! **Python Developer** 🎂\n" + "="*60)

animated_birthday_message()
