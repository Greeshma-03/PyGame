from sys import breakpointhook
from colorama import Back, Style
import os
from src.input_to import *
from colorama import Back, Style
import math


class king():

    def __init__(self,kx,ky):

        #Initalsing colors and king
        self.black = Back.BLACK+' '+Style.RESET_ALL
        self.green = Back.GREEN+' '+Style.RESET_ALL
        self.magenta = Back.MAGENTA+' '+Style.RESET_ALL
        self.blue = Back.BLUE+' '+Style.RESET_ALL
        self.red = Back.RED+' '+Style.RESET_ALL
        self.yellow = Back.YELLOW+' '+Style.RESET_ALL
        self.white = Back.WHITE+' '+Style.RESET_ALL

        self.kx=kx 
        self.ky=ky 

    def move(self,board,moment):
        if(moment=='a'):
            board.ky-=1 

            #iterating through each hut
            for i in range(5):
                if((((board.kx-board.hutsx[i])**2 + (board.ky-board.hutsy[i])**2))==0):
                    if(board.huts_col[i]!=self.black):
                        board.ky +=1
                    continue
            
            #iterating through each wall
            for i in range(36):
                if((((board.kx-board.wallsx[i])**2 + (board.ky-board.wallsy[i])**2))==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.ky +=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.ky +=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.ky +=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.ky +=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.kx-board.townhallx-i)**2 + (board.ky-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.ky +=1
                    continue

            #iterating through canons
            for i in range(len(board.can_col)):
                if(((board.kx-board.cx[i])**2 + (board.ky-board.cy[i])**2)==0):
                    board.ky +=1
                    continue

            #iterating through tower wizard
            for i in range(len(board.targetx)):
                if(((board.kx-board.tx[i])**2 + (board.ky-board.ty[i])**2)==0):
                    board.ky +=1
                    continue    
                
        elif(moment=='d'):
            board.ky+=1 

            #iterating through each hut
            for i in range(5):
                if(((board.kx-board.hutsx[i])**2 + (board.ky-board.hutsy[i])**2)==0):
                    if(board.huts_col[i]!=self.black):
                        board.ky -=1
                    continue
            
            #iterating through each wall
            for i in range(36):
                if(((board.kx-board.wallsx[i])**2 + (board.ky-board.wallsy[i])**2)==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.ky -=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.ky -=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.ky -=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.ky -=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.kx-board.townhallx-i)**2 + (board.ky-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.ky -=1
                    continue

            #iterating through canons
            for i in range(2):
                if(((board.kx-board.cx[i])**2 + (board.ky-board.cy[i])**2)==0):
                    board.ky -=1
                    continue   

        
        elif(moment=='s'):
            board.kx+=1 

            #iterating through each hut
            for i in range(5):
                if((((board.kx-board.hutsx[i])**2 + (board.ky-board.hutsy[i])**2))==0):
                    if(board.huts_col[i]!=self.black):
                        board.kx -=1
                    continue
            
            #iterating through each wall
            for i in range(36):
                if((((board.kx-board.wallsx[i])**2 + (board.ky-board.wallsy[i])**2))==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.kx -=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.kx -=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.kx-=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.kx-=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.kx-board.townhallx-i)**2 + (board.ky-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.kx -=1
                    continue

            #iterating through canons
            for i in range(2):
                if(((board.kx-board.cx[i])**2 + (board.ky-board.cy[i])**2)==0):
                    board.kx -=1
                    continue


        elif(moment=='w'):
            board.kx-=1 

            #iterating through each hut
            for i in range(5):
                if(((board.kx-board.hutsx[i])**2 + (board.ky-board.hutsy[i])**2)==0):
                    if(board.huts_col[i]!=self.black):
                        board.kx +=1
                    continue
            
            #iterating through each wall
            for i in range(36):
                if(((board.kx-board.wallsx[i])**2 + (board.ky-board.wallsy[i])**2)==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.kx +=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.kx +=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.kx +=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.kx +=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.kx-board.townhallx-i)**2 + (board.ky-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.kx +=1
                    continue

            #iterating through canons
            for i in range(2):
                if(((board.kx-board.cx[i])**2 + (board.ky-board.cy[i])**2)==0):
                    board.kx +=1
                    continue

        elif(moment == ' '):
            #attack on huts
            for i in range(5):
                if(((board.kx-board.hutsx[i])**2 + (board.ky-board.hutsy[i])**2)==1):                      
                 if(board.khealth >= board.hhpoints[i]):
                    board.hhpoints[i] -= board.kdamage
                    if 2*board.hhpoints[i] in range(board.hut_max_health, 2*board.hut_max_health+1):
                            board.huts_col[i] =self.green
                            continue
                    elif(10*board.hhpoints[i] in range(2*board.hut_max_health, 5*board.hut_max_health+1)):
                            board.huts_col[i] = self.yellow
                            continue
                    elif(5*board.hhpoints[i] in range(0, board.hut_max_health+1)):
                            board.huts_col[i] = self.red
                            continue
                    else:
                            board.huts_col[i] = self.black

            #attackon townwall
            for i in range(36):
                if(((board.kx-board.wallsx[i])**2 + (board.ky-board.wallsy[i])**2)==1):

                    if(i%4==0):
                      if(board.wall1_col[int(i/4)] == self.green):
                        board.wall1_col[int((i)/4)]=self.blue
                        break
                      elif(board.wall1_col[int((i)/4)] == self.blue):
                            board.wall1_col[int((i)/4)]=self.yellow
                            break
                      elif(board.wall1_col[int((i)/4)] == self.yellow):
                        board.wall1_col[int((i)/4)]=self.black                        
                        break
                            
                          

                    elif(i%4==1):  
                      if(board.wall2_col[int((i-1)/4)] == self.green):
                            board.wall2_col[int((i-1)/4)]=self.blue
                            break
                      elif(board.wall2_col[int((i-1)/4)] == self.blue):
                            board.wall2_col[int((i-1)/4)]=self.yellow
                            break
                      elif(board.wall2_col[int((i-1)/4)] == self.yellow):
                        board.wall2_col[int((i-1)/4)]=self.black                    
                        break
                      

                    elif(i%4==2):  
                      if(board.wall3_col[int((i-2)/4)] == self.green):
                            board.wall3_col[int((i-2)/4)]=self.blue
                            break
                      elif(board.wall3_col[int((i-2)/4)] == self.blue):
                            board.wall3_col[int((i-2)/4)]=self.yellow
                            break
                      elif(board.wall3_col[int((i-2)/4)] == self.yellow):
                        board.wall3_col[int((i-2)/4)]=self.black                      
                        break
 

                    elif(i%4==3):  
                      if(board.wall4_col[int((i-3)/4)] == self.green):
                            board.wall4_col[int((i-3)/4)]=self.blue
                            break
                      elif(board.wall4_col[int((i-3)/4)] == self.blue):
                            board.wall4_col[int((i-3)/4)]=self.yellow
                            break
                      elif(board.wall4_col[int((i-3)/4)] == self.yellow):
                        board.wall4_col[int((i-3)/4)]=self.black                                              
                        break
                      
        #attack on townhall
            for i in range(4):
                for j in range(3):
                 if(board.khealth >= board.townhealth):
                    if(board.townhall_col!=self.black and (((board.kx-(board.townhallx+i))**2 + (board.ky-(board.townhally+j))**2)==1)):
                        board.townhealth-=board.kdamage
                        if 2*board.townhealth in range(board.town_max_health, 2*board.town_max_health):
                            board.townhall_col=self.magenta
                        elif 10*board.townhealth in range(2*board.town_max_health, 5*board.town_max_health+1):
                            board.townhall_col=self.yellow
                        elif 5*board.townhealth in range(0, board.town_max_health+1):
                            board.townhall_col=self.red
                        else:
                            board.townhall_col=self.black              
                        break
                    

        if(board.ky == board.cols):
            board.kx = 39
            board.ky = 100

        if(board.kx == board.rows):
            board.kx = 39
            board.ky = 100

                    