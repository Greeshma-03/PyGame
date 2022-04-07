from src.village import village
from src.input_to import *
from os import system
from src.King import king
from src.Queen import queen
from src.barbarian import barbars
import os

game = village()

while(1):
 inp=input("Do you want to play with King or Archer Queen(k/q)?")
 if(inp.lower()=='k'):
    game.main='k'
    break
 elif(inp.lower()=='q'):
    game.main='q'
    break 

while(game.running==1):
    input=input_to()

    if(input == 'a' or input == 'w' or input == 's' or input == 'd'):
            os.system("aplay -q ./src/move.wav &")
    elif(input == ' '):
            os.system("aplay -q ./src/attack.wav &")

    if(input=='a' or input=='s' or input=='d' or input=='w' or input==' '):
        if(game.main=='k'):
         game.king.move(game,input)
        elif(game.main=='q'):
             game.queen.move(game,input) 
    elif(input=='r'):
        if(len(game.barbs)<game.maxtroops):
          game.barbs.append(barbars(5,170))
    elif(input=='g'):
        if(len(game.barbs)<game.maxtroops):
         game.barbs.append(barbars(20,15))
    elif(input=='n'):
        if(len(game.barbs)<game.maxtroops):
         game.barbs.append(barbars(30,160))
    elif(input=='t'):
        if(len(game.archer)<game.maxtroops):
         game.archer.append(barbars(5,170))
    elif(input=='h'):
        if(len(game.archer)<game.maxtroops):
         game.archer.append(barbars(20,15))
    elif(input=='m'):
        if(len(game.archer)<game.maxtroops):
         game.archer.append(barbars(30,160))
    elif(input=='e'):
        if(len(game.ballon)<game.maxtroops):
         game.ballon.append(barbars(5,170))
    elif(input=='f'):
        if(len(game.ballon)<game.maxtroops):
         game.ballon.append(barbars(20,15))
    elif(input=='v'):
        if(len(game.ballon)<game.maxtroops):
         game.ballon.append(barbars(30,160))        

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
