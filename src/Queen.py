from sys import breakpointhook
from colorama import Back, Style
import os
from src.input_to import *
import math


class queen():

    def __init__(self,qx,qy):

        #Initalsing colors and king
        self.black = Back.BLACK+' '+Style.RESET_ALL
        self.green = Back.GREEN+' '+Style.RESET_ALL
        self.magenta = Back.MAGENTA+' '+Style.RESET_ALL
        self.blue = Back.BLUE+' '+Style.RESET_ALL
        self.lblue = Back.LIGHTBLUE_EX+' '+Style.RESET_ALL
        self.red = Back.RED+' '+Style.RESET_ALL
        self.yellow = Back.YELLOW+' '+Style.RESET_ALL
        self.white = Back.WHITE+' '+Style.RESET_ALL

        self.qx=qx 
        self.qy=qy 
        self.moment='a'

    def move(self,board,moment):
        if(moment!=' '):
            temp1=self.qx
            temp2=self.qy

        if(moment=='a'):
            board.qy-=1 

            #iterating through each hut
            for i in range(5):
                if((((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2))==0):
                    if(board.huts_col[i]!=self.black):
                        board.qy +=1
                    continue
            
            #iterating through each wall
            for i in range(36):
                if((((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2))==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.qy +=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.qy +=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.qy +=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.qy +=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.qx-board.townhallx-i)**2 + (board.qy-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.qy +=1
                    continue

            #iterating through canons
            for i in range(2):
                if(((board.qx-board.cx[i])**2 + (board.qy-board.cy[i])**2)==0):
                    board.qy +=1
                    continue
                
        elif(moment=='d'):
            board.qy+=1 

            #iterating through each hut
            for i in range(5):
                if(((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2)==0):
                    if(board.huts_col[i]!=self.black):
                        board.qy -=1
                    continue
            
            #iterating through each wall
            for i in range(36):
                if(((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2)==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.qy -=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.qy -=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.qy -=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.qy -=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.qx-board.townhallx-i)**2 + (board.qy-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.qy -=1
                    continue

            #iterating through canons
            for i in range(2):
                if(((board.qx-board.cx[i])**2 + (board.qy-board.cy[i])**2)==0):
                    board.qy -=1
                    continue   

        
        elif(moment=='s'):
            board.qx+=1 

            #iterating through each hut
            for i in range(5):
                if((((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2))==0):
                    if(board.huts_col[i]!=self.black):
                        board.qx -=1
                    continue
            
            #iterating through each wall
            for i in range(36):
                if((((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2))==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.qx -=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.qx -=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.qx-=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.qx-=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.qx-board.townhallx-i)**2 + (board.qy-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.qx -=1
                    continue

            #iterating through canons
            for i in range(2):
                if(((board.qx-board.cx[i])**2 + (board.qy-board.cy[i])**2)==0):
                    board.qx -=1
                    continue


        elif(moment=='w'):
            board.qx-=1 

            #iterating through each hut
            for i in range(5):
                if(((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2)==0):
                    if(board.huts_col[i]!=self.black):
                        board.qx +=1
                    continue
            
            #iterating through each wall
            for i in range(36):
                if(((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2)==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.qx +=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.qx +=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.qx +=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.qx +=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.qx-board.townhallx-i)**2 + (board.qy-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.qx +=1
                    continue

            #iterating through canons
            for i in range(2):
                if(((board.qx-board.cx[i])**2 + (board.qy-board.cy[i])**2)==0):
                    board.qx +=1
                    continue

        elif(moment == ' '):
          
            
            if(moment=='a'):
                board.qy-=8
            elif(moment=='d'):
                board.qy+=8
            elif(moment=='s'):
                board.qx+=8
            elif(moment=='w'):
                board.qx-=8
            
            

            #attack on huts
            for i in range(5):
                if(((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2)<=25):                      
                 if(board.qhealth >= board.hhpoints[i]):
                    board.hhpoints[i] -= board.qdamage
                    if 2*board.hhpoints[i] in range(board.hut_max_health, 2*board.hut_max_health):
                            board.huts_col[i] =self.lblue
                    elif(10*board.hhpoints[i] in range(2*board.hut_max_health, 5*board.hut_max_health+1)):
                            board.huts_col[i] = self.yellow
                    elif(5*board.hhpoints[i] in range(0, board.hut_max_health+1)):
                            board.huts_col[i] = self.red
                    else:
                            board.huts_col[i] = self.black


            #attackon townwall
            for i in range(36):
                if(((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2)<=25):
                    if(i%4==0):
                      if(board.wall1_col[int(i/4)] == self.green):
                        board.wall1_col[int((i)/4)]=self.blue
                      elif(board.wall1_col[int((i)/4)] == self.blue):
                            board.wall1_col[int((i)/4)]=self.yellow
                      elif(board.wall1_col[int((i)/4)] == self.yellow):
                        board.wall1_col[int((i)/4)]=self.black                                                    
                          

                    elif(i%4==1):  
                      if(board.wall2_col[int((i-1)/4)] == self.green):
                            board.wall2_col[int((i-1)/4)]=self.blue
                      elif(board.wall2_col[int((i-1)/4)] == self.blue):
                            board.wall2_col[int((i-1)/4)]=self.yellow
                      elif(board.wall2_col[int((i-1)/4)] == self.yellow):
                        board.wall2_col[int((i-1)/4)]=self.black                    
                      

                    elif(i%4==2):  
                      if(board.wall3_col[int((i-2)/4)] == self.green):
                            board.wall3_col[int((i-2)/4)]=self.blue
                      elif(board.wall3_col[int((i-2)/4)] == self.blue):
                            board.wall3_col[int((i-2)/4)]=self.yellow
                      elif(board.wall3_col[int((i-2)/4)] == self.yellow):
                        board.wall3_col[int((i-2)/4)]=self.black                      

                    elif(i%4==3):  
                      if(board.wall4_col[int((i-3)/4)] == self.green):
                            board.wall4_col[int((i-3)/4)]=self.blue
                      elif(board.wall4_col[int((i-3)/4)] == self.blue):
                            board.wall4_col[int((i-3)/4)]=self.yellow
                      elif(board.wall4_col[int((i-3)/4)] == self.yellow):
                        board.wall4_col[int((i-3)/4)]=self.black                                              
                      
        #attack on townhall
            for i in range(4):
                for j in range(3):
                 if(board.qhealth >= board.townhealth):
                    if(board.townhall_col!=self.black and (((board.qx-(board.townhallx+i))**2 + (board.qy-(board.townhally+j))**2)<=25)):
                        board.townhealth-=board.qdamage
                        if 2*board.townhealth in range(board.town_max_health, 2*board.town_max_health):
                            board.townhall_col=self.blue
                        elif 10*board.townhealth in range(2*board.town_max_health, 5*board.town_max_health+1):
                            board.townhall_col=self.yellow
                        elif 5*board.townhealth in range(0, board.town_max_health+1):
                            board.townhall_col=self.red
                        else:
                            board.townhall_col=self.black              
                        break

            if(moment=='a'):
                board.qy+=8
            elif(moment=='d'):
                board.qy-=8
            elif(moment=='s'):
                board.qx-=8
            elif(moment=='w'):
                board.qx+=8
                  

        if(board.qy == board.cols):
            board.qx = 39
            board.qy = 100

        if(board.qx == board.rows):
            board.qx = 39
            board.qy = 100
        if(moment!=' '):
         if(temp1>self.qx):
            moment='w'
         elif(temp1<self.qx):
            moment='s'
         elif(temp2>self.qy):
            moment='a'
         elif(temp2<self.qy):
            moment='d'
                    
    