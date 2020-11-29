import sys
import os
import time

def main():
    os.system("cls")

    for i in range(10):
        for i in range(10-i):
            print('X', end='')
        print()
    pass
    time.sleep(0.3)

    os.system("cls")
    for i in range(10):
        for i in range(i):
            print('X', end='')
        print()
    pass
    os.system("cls")
    time.sleep(0.3)
    for i in range(10):
        for i in range(i):
            print('.', end='')
        for i in range(10-i):
            print('X', end='')
        print()
    pass
    time.sleep(0.3)

    os.system("cls")
    for i in range(10):
        for i in range(10-i):
            print('.', end='')
        for i in range(10-i):
            time.sleep(0.01)
            print('X', end='')
        print()
    pass
    os.system("cls")
    for i in range(10):
        for i in range(i+1):
            time.sleep(0.003)

            print('.', end='')
        for i in range(10):
            print('X', end='')
        print()
    pass
    time.sleep(0.03)
    
    os.system("cls")
    for i in range(10):
        time.sleep(0.01)

        for i in range(i+1):
            time.sleep(0.01)

            print('.', end='')
        for i in range(i-1):
            print('X', end='')

            print('X', end='')
        print()
    pass
    time.sleep(0.08)
    os.system("cls")
    for i in range(10):
        time.sleep(0.008)

        for i in range(i+1):
            time.sleep(0.02)

            print('.', end='')
        for i in range(i*i-i*6):
            print('X', end='')

            print('X', end='')
        print()
    pass
    time.sleep(0.3)

if __name__ == "__main__":
    main()
    pass
