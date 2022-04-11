from sys import breakpointhook
from colorama import Back, Style
import os
from src.input_to import *
from colorama import Back, Style
import math
import time

class queen():

    def __init__(self,qx,qy):

        #Initalsing colors and king
        self.black = Back.BLACK+' '+Style.RESET_ALL
        self.green = Back.GREEN+' '+Style.RESET_ALL
        self.magenta = Back.MAGENTA+' '+Style.RESET_ALL
        self.blue = Back.BLUE+' '+Style.RESET_ALL
        self.red = Back.RED+' '+Style.RESET_ALL
        self.yellow = Back.YELLOW+' '+Style.RESET_ALL
        self.white = Back.WHITE+' '+Style.RESET_ALL

        self.qx=qx 
        self.qy=qy 
        self.last_mom='a'

    def move(self,board,moment):
        
        if(moment=='a'):
            temp=self.last_mom
            self.last_mom=moment
            board.qy-=1 

            #iterating through each hut
            for i in range(5):
                if((((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2))==0):
                    if(board.huts_col[i]!=self.black):
                        board.qy +=1
                        self.last_mom=temp

                    continue
            
            #iterating through each wall
            for i in range(36):
                if((((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2))==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          self.last_mom=temp
                          board.qy +=1
                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           self.last_mom=temp
                           board.qy +=1
                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           self.last_mom=temp
                           board.qy +=1        
                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               self.last_mom=temp
                               board.qy +=1

                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.qx-board.townhallx-i)**2 + (board.qy-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            self.last_mom=temp
                            board.qy +=1
                    continue

            #iterating through canons
            for i in range(2):
                if(((board.qx-board.cx[i])**2 + (board.qy-board.cy[i])**2)==0):
                    self.last_mom=temp
                    board.qy +=1
                    continue
                
        elif(moment=='d'):
            temp=self.last_mom
            self.last_mom=moment
            board.qy+=1 

            #iterating through each hut
            for i in range(5):
                if(((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2)==0):
                    if(board.huts_col[i]!=self.black):
                        board.qy -=1
                        self.last_mom=temp

                    continue
            
            #iterating through each wall
            for i in range(36):
                if(((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2)==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.qy -=1
                          self.last_mom=temp

                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.qy -=1
                           self.last_mom=temp

                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.qy -=1  
                           self.last_mom=temp

                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                               board.qy -=1
                               self.last_mom=temp


                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.qx-board.townhallx-i)**2 + (board.qy-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.qy -=1
                            self.last_mom=temp

                    continue

            #iterating through canons
            for i in range(2):
                if(((board.qx-board.cx[i])**2 + (board.qy-board.cy[i])**2)==0):
                    board.qy -=1
                    self.last_mom=temp

                    continue   

        
        elif(moment=='s'):
            temp=self.last_mom
            self.last_mom=moment
            board.qx+=1 

            #iterating through each hut
            for i in range(5):
                if((((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2))==0):
                    if(board.huts_col[i]!=self.black):
                        board.qx -=1
                        self.last_mom=temp

                    continue
            
            #iterating through each wall
            for i in range(36):
                if((((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2))==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.qx -=1
                          self.last_mom=temp

                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.qx -=1
                           self.last_mom=temp

                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.qx-=1   
                           self.last_mom=temp

                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                           board.qx-=1
                           self.last_mom=temp


                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.qx-board.townhallx-i)**2 + (board.qy-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.qx -=1
                            self.last_mom=temp

                    continue

            #iterating through canons
            for i in range(2):
                if(((board.qx-board.cx[i])**2 + (board.qy-board.cy[i])**2)==0):
                    board.qx -=1
                    self.last_mom=temp

                    continue


        elif(moment=='w'):
            temp=self.last_mom
            self.last_mom=moment
            board.qx-=1 

            #iterating through each hut
            for i in range(5):
                if(((board.qx-board.hutsx[i])**2 + (board.qy-board.hutsy[i])**2)==0):
                    if(board.huts_col[i]!=self.black):
                        board.qx +=1
                        self.last_mom=temp

                    continue
            
            #iterating through each wall
            for i in range(36):
                if(((board.qx-board.wallsx[i])**2 + (board.qy-board.wallsy[i])**2)==0):
                    if(i%4==0):
                       if(board.wall1_col[int(i/4)]!=self.black):
                          board.qx +=1
                          self.last_mom=temp

                    elif(i%4==1):
                        if(board.wall2_col[int((i-1)/4)]!=self.black):
                           board.qx +=1
                           self.last_mom=temp

                    elif(i%4==2):
                        if(board.wall3_col[int((i-2)/4)]!=self.black):
                           board.qx +=1   
                           self.last_mom=temp

                    else:
                         if(board.wall4_col[int((i-3)/4)]!=self.black):
                           board.qx +=1
                           self.last_mom=temp


                    continue
            
            #iterating through townhall
            for i in range(4):
                for j in range(3):
                    if(((board.qx-board.townhallx-i)**2 + (board.qy-board.townhally-j)**2)==0):
                        if(board.townhall_col!=self.black):
                            board.qx +=1
                            self.last_mom=temp

                    continue

            #iterating through canons
            for i in range(2):
                if(((board.qx-board.cx[i])**2 + (board.qy-board.cy[i])**2)==0):
                    board.qx +=1
                    self.last_mom=temp

                    continue

        elif(moment == ' '):
            #attack on huts
            if(self.last_mom=='a'):
                x=board.qx
                y=board.qy+8
            elif(self.last_mom=='d'):
                x=board.qx
                y=board.qy-8
            elif(self.last_mom=='s'):
                x=board.qx-8
                y=board.qy
            elif(self.last_mom=='w'):
                x=board.qx+8
                y=board.qy           

            for i in range(5):
                if(((x-board.hutsx[i])**2 + (y-board.hutsy[i])**2)<=25):                      
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
                if(((x-board.wallsx[i])**2 + (y-board.wallsy[i])**2)<=25):

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
                 if(board.khealth >= board.townhealth):
                    if(board.townhall_col!=self.black and (((x-(board.townhallx+i))**2 + (y-(board.townhally+j))**2)<=25)):
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
                    

        if(board.qy == board.cols):
            board.qx = 39
            board.qy = 100

        if(board.qx == board.rows):
            board.qx = 39
            board.qy = 100


    def spl_attack(self,board):
        if(time.time()-board.sleep>1):
            board.sleep=-1
            if(self.last_mom=='a'):
                x=board.qx
                y=board.qy+16
            elif(self.last_mom=='d'):
                x=board.qx
                y=board.qy-16
            elif(self.last_mom=='s'):
                x=board.qx-16
                y=board.qy
            elif(self.last_mom=='w'):
                x=board.qx+16
                y=board.qy    

            for i in range(5):
                if(((x-board.hutsx[i])**2 + (y-board.hutsy[i])**2)<=81):                      
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
                if(((x-board.wallsx[i])**2 + (y-board.wallsy[i])**2)<=81):

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
                 if(board.khealth >= board.townhealth):
                    if(board.townhall_col!=self.black and (((x-(board.townhallx+i))**2 + (y-(board.townhally+j))**2)<=81)):
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

            return