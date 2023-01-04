from time import sleep
from pynput.mouse import Controller

mouse = Controller()

while True:
    print("The mouse is at:")
    print(mouse.position)
    print()
    sleep(1.0)
