#!/usr/bin/python3
# SurePWD v.1.0.0
# Coded by esiquiel
# Github: https://github.com/esiquiel/surepwd

# Dependencies

import secrets
import random
import string
import os


# Configuration

class Colors:
    WHITE = '\033[37m'
    YELLOW = '\033[93m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'

colors_dict = {
    0: Colors.YELLOW,
    1: Colors.BLUE,
    2: Colors.RED,
    3: Colors.GREEN,
    4: Colors.MAGENTA,
    5: Colors.CYAN
}

color = colors_dict[random.randint(0, 5)]

sh = color + '#~: '


# Clear terminal

def refresh():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(color + open('banner.txt', 'r').read())


# Print a password

def generate(save):
    alphabet = string.ascii_letters + string.digits + '@#$@'
    password = ''.join(secrets.choice(alphabet) for i in range(24))

    if save:
        print(f'\n{password}\n')
        pass_file = open('pass.txt', 'w').write(password)
    else:
        print(f'\n{password}\n')


# Main

if __name__ == '__main__':
    refresh()

    while True:

        print(sh, end='')
        cmd = str(input(Colors.WHITE))

        # Help commands
        if cmd == 'help':
            refresh()
            print(Colors.WHITE + '\nhelp > Show help commands')
            print('clear > Clear the terminal')
            print('generate > Generate a password')
            print('generate -s > Generate a password and save\n' + color)
        
        # Clear the terminal
        elif cmd == 'clear' or cmd =='cls':
            refresh()
        
        # Generate a password
        elif cmd == 'generate' or cmd == 'g':
            generate(False)
        
        # Generate a password and save
        elif cmd == 'generate -s' or cmd == 'generate --save':
            generate(True)
        else:
            refresh()
            print(f'\n{Colors.RED}Command not found :(')
            print('Please type help to see commands\n')
