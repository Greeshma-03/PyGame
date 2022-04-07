from sys import breakpointhook
from colorama import Back, Style
import os
from src.input_to import *
from colorama import Back, Style
import math


class barbars():

    def __init__(self,barx,bary):

        #Initalsing colors and king
        self.black = Back.BLACK+' '+Style.RESET_ALL
        self.green = Back.GREEN+' '+Style.RESET_ALL
        self.magenta = Back.MAGENTA+' '+Style.RESET_ALL
        self.blue = Back.BLUE+' '+Style.RESET_ALL
        self.red = Back.RED+' '+Style.RESET_ALL
        self.yellow = Back.YELLOW+' '+Style.RESET_ALL
        self.white = Back.WHITE+' '+Style.RESET_ALL
        self.lit=Back.LIGHTCYAN_EX+' '+Style.RESET_ALL

        self.barx=barx
        self.bary=bary
        self.barb_col=self.yellow
        self.health=20

    def shortest_dist(self,x,y,board):
        tx=board.townhallx
        ty=board.townhally

        mini=10000000

        #huts nearest
        for i in range(5):
            if(board.huts_col[i]==self.black):
                continue
            if( mini>((x-board.hutsx[i])**2+(y-board.hutsy[i])**2)):                    
                mini=(x-board.hutsx[i])**2+(y-board.hutsy[i])**2
                if(mini==1):
                    if(board.huts_col[i]==self.green):
                       board.huts_col[i]=self.blue
                    elif(board.huts_col[i]==self.blue):
                        board.huts_col[i]=self.yellow 
                    elif(board.huts_col[i]==self.yellow):
                        board.huts_col[i]=self.black   
                    return 1          

        #townhall nearest
        if(board.townhall_col!=self.black):
            for i in range(4):
                for j in range(3):
                   if(mini>((x-tx-i)**2+(y-ty-j)**2)):
                      mini=(x-tx-i)**2+(y-ty-j)**2

                      if(mini==1):
                        if(board.townhall_col==self.magenta):
                           board.townhall_col=self.blue
                        elif(board.townhall_col==self.blue):
                            board.townhall_col=self.yellow 
                        elif(board.townhall_col==self.yellow):
                             board.townhall_col=self.lit
                        elif(board.townhall_col==self.lit):
                             board.townhall_col=self.red   
                        elif(board.townhall_col==self.red):
                             board.townhall_col=self.black       
                        return 1             
        return mini


    def canon_attack(self,x,y,board):
        for i in range(2):
            if(((x-board.cx[i])**2+(y-board.cy[i])**2)<=(board.crange)**2):
                self.health-=board.cdamage
                if(self.health<20):
                    self.barb_col=self.magenta
                elif(self.health<=15 and self.health>=10):
                    self.barb_col=self.blue
                elif(self.health<=10 and self.health>=5):
                    self.barb_col=self.yellow
                elif(self.health<=5 and self.health>=0):
                    self.barb_col=self.red 
                elif(self.health<=0):
                    self.barb_col=self.black 
                    self.health=0



    def break_walls(self,x,y,board,addx,addy):

        for i in range(36):
                if(((x-board.wallsx[i])**2 + (y-board.wallsy[i])**2)==0):
                    if(i%4==0):
                      if(board.wall1_col[int(i/4)] == self.green):
                        board.wall1_col[int((i)/4)]=self.blue
                        self.barx+=addx
                        self.bary+=addy
                        break
                      elif(board.wall1_col[int((i)/4)] == self.blue):
                            board.wall1_col[int((i)/4)]=self.yellow
                            self.barx+=addx
                            self.bary+=addy
                            break
                      elif(board.wall1_col[int((i)/4)] == self.yellow):
                        board.wall1_col[int((i)/4)]=self.black    
                        self.barx+=addx
                        self.bary+=addy                
                        break
                                                    
                    elif(i%4==1):  
                      if(board.wall2_col[int((i-1)/4)] == self.green):
                            board.wall2_col[int((i-1)/4)]=self.blue
                            self.barx+=addx
                            self.bary+=addy
                            break
                      elif(board.wall2_col[int((i-1)/4)] == self.blue):
                            board.wall2_col[int((i-1)/4)]=self.yellow
                            self.barx+=addx
                            self.bary+=addy
                            break
                      elif(board.wall2_col[int((i-1)/4)] == self.yellow):
                        board.wall2_col[int((i-1)/4)]=self.black   
                        self.barx+=addx
                        self.bary+=addy                 
                        break
                      

                    elif(i%4==2):  
                      if(board.wall3_col[int((i-2)/4)] == self.green):
                            board.wall3_col[int((i-2)/4)]=self.blue
                            self.barx+=addx
                            self.bary+=addy
                            break
                      elif(board.wall3_col[int((i-2)/4)] == self.blue):
                            board.wall3_col[int((i-2)/4)]=self.yellow
                            self.barx+=addx
                            self.bary+=addy
                            break
                      elif(board.wall3_col[int((i-2)/4)] == self.yellow):
                        board.wall3_col[int((i-2)/4)]=self.black   
                        self.barx+=addx
                        self.bary+=addy                   
                        break
 

                    elif(i%4==3):  
                      if(board.wall4_col[int((i-3)/4)] == self.green):
                            board.wall4_col[int((i-3)/4)]=self.blue
                            self.barx+=addx
                            self.bary+=addy
                            break
                      elif(board.wall4_col[int((i-3)/4)] == self.blue):
                            board.wall4_col[int((i-3)/4)]=self.yellow
                            self.barx+=addx
                            self.bary+=addy
                            break
                      elif(board.wall4_col[int((i-3)/4)] == self.yellow):
                        board.wall4_col[int((i-3)/4)]=self.black    
                        self.barx+=addx
                        self.bary+=addy                                          
                        break
                      

    def move(self,board):
        
        dist=[]
        #find the shortest dist among huts,townhall for 4 possibilities
        dist.append(self.shortest_dist(self.barx+1,self.bary,board))
        dist.append(self.shortest_dist(self.barx,self.bary+1,board))
        dist.append(self.shortest_dist(self.barx-1,self.bary,board))
        dist.append(self.shortest_dist(self.barx,self.bary-1,board))
      

        #follow the path that gives least among the 4            
        if(min(dist)==dist[0]):
            self.barx+=1
            self.break_walls(self.barx,self.bary,board,-1,0)
        elif(min(dist)==dist[1]):
            self.bary+=1
            self.break_walls(self.barx,self.bary,board,0,-1)
        elif(min(dist)==dist[2]):
            self.barx-=1
            self.break_walls(self.barx,self.bary,board,1,0)
        else:
            self.bary-=1        
            self.break_walls(self.barx,self.bary,board,0,1)
        self.canon_attack(self.barx,self.bary,board)

    
