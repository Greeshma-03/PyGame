from src.village import village
from src.input_to import *
from os import system
from src.King import king
from src.Queen import queen
from src.barbarian import barbars
from src.archer import archers
from src.ballon import ballons

import os
import time

win=1

while(1):
 inp=input("Do you want to play with King or Archer Queen(k/q)?")
 if(inp.lower()=='k'):
    main='k'
    break
 elif(inp.lower()=='q'):
    main='q'
    break 

while(win>0 and win<4):
 game = village()
 if(main=='k'):
     game.main='k'
 elif(main=='q'):
     game.main='q'
 game.level=win
 if(win>=2):
        game.tx.append(12)
        game.ty.append(40)
        game.tower_attacked.append(0)
        game.tower_col.append(game.lred)
        game.targetx.append(-1)
        game.targety.append(-1)

        game.cx.append(20)
        game.cy.append(20)
        game.canon_attacked.append(0)
        game.can_col.append(game.blue)
        

 if(win==3):
        game.tx.append(14)
        game.ty.append(20)
        game.tower_attacked.append(0)
        game.tower_col.append(game.lred)
        game.targetx.append(-1)
        game.targety.append(-1)

        game.cx.append(30)
        game.cy.append(30)
        game.canon_attacked.append(0)
        game.can_col.append(game.blue)


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
          game.barbs.append(barbars(5,170,game.barhealth,game.bardam))
    elif(input=='g'):
        if(len(game.barbs)<game.maxtroops):
         game.barbs.append(barbars(20,15,game.barhealth,game.bardam))
    elif(input=='n'):
        if(len(game.barbs)<game.maxtroops):
         game.barbs.append(barbars(30,160,game.barhealth,game.bardam))
    elif(input=='t'):
        if(len(game.archer)<game.maxtroops):
         game.archer.append(archers(5,170,game.archealth,game.archdam))
    elif(input=='h'):
        if(len(game.archer)<game.maxtroops):
         game.archer.append(archers(20,15,game.archealth,game.archdam))
    elif(input=='m'):
        if(len(game.archer)<game.maxtroops):
         game.archer.append(archers(30,160,game.archealth,game.archdam))
    elif(input=='e'):
        if(len(game.ballon)<game.maxtroops):
         game.ballon.append(ballons(5,170,game.ballhealth,game.balldam))
    elif(input=='f'):
        if(len(game.ballon)<game.maxtroops):
         game.ballon.append(ballons(20,15,game.ballhealth,game.balldam))
    elif(input=='v'):
        if(len(game.ballon)<game.maxtroops):
         game.ballon.append(ballons(30,160,game.ballhealth,game.balldam))     
    elif(input=='p'):
        game.sleep=time.time()

    if(input == 'q'):
        game.running=2
        break
    else:
        game.render()
        

 if(game.running==0):
    win=0
 elif(game.running==-1):    
    win+=1     
 else:
    win=-1

if(win==0):
    print("You are defeated!!!")
    win=0
elif(win==4):    
    print("You won the match!!!")   
    win+=1 
else:
    print("You quitted the match!!")    
  
