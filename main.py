
import sys
from unicodedata import name
import list
import stack_delete


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'list':
            list.main()
        elif sys.argv[1] == 'delete':
            stack_delete.main()
        else:
            print('Invalid argument')
            print('Usage: python main.py [list|delete]')
    else:
        print('Invalid argument')
        print('Usage: python main.py [list|delete]')



