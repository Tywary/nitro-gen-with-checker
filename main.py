import os
import ctypes
import requests
import random
import string
import time
import colorama
from colorama import Fore,Back


colorama.init()

print(Fore.BLUE + """

 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░
         ░  ░              ░         ░ ░           ░    ░  ░         ░

             █     █░ ██▓▄▄▄█████▓ ██░ ██     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███
            ▓█░ █ ░█░▓██▒▓  ██▒ ▓▒▓██░ ██▒   ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
            ▒█░ █ ░█ ▒██▒▒ ▓██░ ▒░▒██▀▀██░   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
            ░█░ █ ░█ ░██░░ ▓██▓ ░ ░▓█ ░██    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄
            ░░██▒██▓ ░██░  ▒██▒ ░ ░▓█▒░██▓   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
            ░ ▓░▒ ▒  ░▓    ▒ ░░    ▒ ░░▒░▒   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
              ▒ ░ ░   ▒ ░    ░     ▒ ░▒░ ░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
              ░   ░   ▒ ░  ░       ░  ░░ ░   ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░
                ░     ░            ░  ░  ░   ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░
                                             ░                       ░
                                              _       ___
                                             |_)       |          _. ._
                                             |_) \/    | \/ \/\/ (_| | \/
                                                 /       /             /
""")
time.sleep(0.1)
print(Fore.GREEN + "For Help and Support Contact qazadi#7228")
time.sleep(0.1)
print(Fore.GREEN + "Source Code: https://github.com/Tywary/nitro-gen-with-checker ")
time.sleep(0.1)

num = int(input('Type the number of Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered a high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
        r = requests.get(url)
        if r.status_code == 200:
            print(Fore.GREEN + f"√ Valid | {nitro} ")
            break
        else:
            print(Fore.RED + f"X Invalid | {nitro} ")

time.sleep(0.2)

input(f"\nYou have generated {num} Nitro Codes, Now press any key to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you are too unlucky :(  ")
input(Fore.Blue + f"Join my Discord Server for fun. hehe - https://discord.gg/xJ8Ft8HVuv ")
