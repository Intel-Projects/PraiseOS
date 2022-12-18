from bin import *
from bin import __all__
import os

ops  = ['+', '-', '/', '*', '^', '**']
cmds = ['file-explorer', 'pkgm-gui', './', 'tree', 'dir', 'ls', 'add-package', 'text-editor']

bin_list = os.listdir('bin')

del bin_list[bin_list.index('__init__.py')]

del bin_list[bin_list.index('__pycache__')]

def check(cmd, usr):
    math = 0
    for op in ops:
        if op in cmd:
            try:
                math = 1
                exec(f'print(str({cmd}).split(\'.\')[0])')
                break
            except (NameError, SyntaxError):
                math = 0
    if cmd.lower() == "":
        pass
    elif cmd.lower() == "help":
        print()
        for item in bin_list:
            exec(f'print(\'{item.replace(".py", "")} - \' + {item.replace(".py", "")}.description())')
        print()
    elif cmd.lower().split(' ')[0]+'.py' in bin_list:
        exec(f"{cmd.lower().split(' ')[0].removesuffix('.py')}.run(cmd)", {})
    else:
        if math == 0:print("Command not found run help for list of commands")
        math = 1
