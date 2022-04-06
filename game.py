from src.village import village
from src.input_to import *
from os import system
from src.King import king
import os

game = village()

while(game.running==1):
    input=input_to()

    if(input == 'a' or input == 'w' or input == 's' or input == 'd'):
            os.system("aplay -q ./src/move.wav &")
    elif(input == ' '):
            os.system("aplay -q ./src/attack.wav &")

    if(input=='a' or input=='s' or input=='d' or input=='w' or input==' '):
        game.king.move(game,input)
    # elif(input=='r' or input=='n' or input=='b'):
    #     game.barbs.move()
   

    if(input == 'q'):
        game.running=2
        break
    else:
        game.render()

if(game.running==0):
    print("You are defeated!!!")
elif(game.running==-1):    
    print("You won the match!!!")    
else:
    print("You quitted the match!!")    
