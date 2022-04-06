
from time import sleep, time
import sys
import os
from os import system

sys.path.insert(0, './replays')

nons = int(input("Which game u want to see: "))
hui = len( os.listdir('replays') )

replay = 'replays/replay' + str(hui - nons + 1) + '.txt'


with open( replay, "r") as replayo:
    for i in replayo:
        if i.strip() == "hello":
            sleep(0.1)
            system('clear')
        else:
            print(i, end="")
