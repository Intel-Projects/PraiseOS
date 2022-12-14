import getpass, hashlib

from simple_term_menu import TerminalMenu
from art import tprint

import os, time

os.system('clear')

tprint('PraiseOS')

print('='*48)

print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ Login Page\n')

print('(HELP): (Use UP and DOWN keys to make a selection. \n Once you are ready, press ENTER to finalise your choice)\n')

urname = os.listdir('../../global/users')[TerminalMenu(os.listdir('../../global/users')).show()]

with open(f'../../global/users/{urname}/.pass') as f:
    paswrd = f.read()

tries = 0

while True:
    os.system('clear')

    tprint('PraiseOS')

    print('='*48)

    print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ Login Page\n')

    print(f'(HELP): (Type in the passcode to account "{urname}")\n')

    getpas = getpass.getpass('Passcode ?: ')

    encpass = hashlib.sha256(getpas.encode()).hexdigest()

    if encpass == paswrd:
        break
    elif tries == 3:
        os.system('clear')
        for i in range(0,15):
            print(f'NO TRIES LEFT WAIT {15-i} MORE SECONDS')
            time.sleep(1)
        tries = 0
    else:
        os.system('clear')
        print('Incorrect Password')
        time.sleep(2)
        tries += 1

os.system('python3 home.py')