from os import system
from typing_extensions import Self
from colorama import Back, Style, Fore
import random
from src.King import king
from src.barbarian import barbars
import math
import os


class village():
    def __init__(self):
        
        #colors to use
        self.black = Back.BLACK+' '+Style.RESET_ALL
        self.green = Back.GREEN+' '+Style.RESET_ALL
        self.magenta = Back.MAGENTA+' '+Style.RESET_ALL
        self.blue = Back.BLUE+' '+Style.RESET_ALL
        self.red = Back.RED+' '+Style.RESET_ALL
        self.yellow = Back.YELLOW+' '+Style.RESET_ALL
        self.white = Back.WHITE+' '+Style.RESET_ALL

        #replay of games
        self.num_files = len(os.listdir('replays'))
        self.outp=-1;
        self.running=1  #currently the game is running


        #Initialsing boundaries of village
        self.rows=40 
        self.cols=200 

        #colors of components
        self.townhall_col=self.magenta
        self.can_col=[]
        self.huts_col=[]
        self.wall1_col=[]
        self.wall2_col=[]
        self.wall3_col=[]
        self.wall4_col=[]

       
        for i in range(2):
            self.can_col.append(self.blue) 
        
        for i in range(5):
            self.huts_col.append(self.green) 

        for i in range(9):
            self.wall1_col.append(self.green) 
            self.wall2_col.append(self.green) 
            self.wall3_col.append(self.green) 
            self.wall4_col.append(self.green) 
        
        
        self.king_col=self.red 
        self.bg_col=self.black 

        #king health bar colors
        self.bar_col=self.white 
        self.level_col = Back.LIGHTWHITE_EX+' '+Style.RESET_ALL
        self.spawn_col=self.yellow 


        #Co-ordinates of components
        
        #townhall
        self.townhallx=int(self.rows/2) 
        self.townhally=int(self.cols/2)
        
        #spawning points
        self.spx=[10,10,10] 
        self.spy=[10,180,196] 

        #huts
        self.hutsx=[10,10,10,10,10] 
        self.hutsy=[20,42,60,120,170] 
        self.hhpoints=[10,10,10,10,10] 
        self.hut_max_health=self.hhpoints[0] 

        #canons
        self.cx=[10,37]
        self.cy=[45,151]
        self.crange = random.randint(6, 10)
        self.cdamage = random.randint(1, 5)
        
        #walls
        self.wallsx=[]
        self.wallsy=[]

        wallx=self.townhallx-3 
        wally=self.townhally-3 

        for i in range(9):
            self.wallsx.append(wallx)
            self.wallsy.append(wally+i)

            self.wallsx.append(wallx+i)
            self.wallsy.append(wally+8)

            self.wallsx.append(wallx+8)
            self.wallsy.append(wally+i)

            self.wallsx.append(wallx+i)
            self.wallsy.append(wally)


        #King
        self.kx=39 
        self.ky=100 
        self.kdamage=2
        self.king=king(self.kx,self.ky) 
        self.khealth=25 
        
        #barbarians
        self.barbs=[]       
        

    def render(self):
        
        #Do the barbarian work
        for obj in self.barbs:
            obj.move(self)
            

        #Do canon work
            

        system("clear") 
        destroy=0
        #render all components with black background
        self.board = [[self.black for i in range(self.cols)] for j in range(self.rows)]

        # fill town hall(4*3)
        for i in range(4):
            for j in range(3):
                if(self.townhall_col==self.black):
                    destroy=1             
                self.board[self.townhallx+i][self.townhally+j]=self.townhall_col

        # #fill huts(1*1)
        for i in range(5):            
            self.board[self.hutsx[i]][self.hutsy[i]]=self.huts_col[i] 
            if(self.huts_col[i]==self.black):
                destroy+=1
        
        # #fill canons(1*1)
        for i in range(2):
            self.board[self.cx[i]][self.cy[i]]=self.can_col[i] 

        #fill walls    
        wallx=self.townhallx-3 
        wally=self.townhally-3 

        for i in range(9):
            self.board[wallx][wally+i]=self.wall1_col [i]
            self.board[wallx+i][wally+8]=self.wall2_col[i]
            self.board[wallx+8][wally+i]=self.wall3_col[i]
            self.board[wallx+i][wally]=self.wall4_col[i] 

        #fill barbarians
        for obj in self.barbs:
            self.board[obj.barx][obj.bary]=obj.barb_col

        #fill king
        self.board[self.kx][self.ky]=self.king_col 

        #fill health bar
        title="Health Bar"
        title_offset = (self.cols+1-len(title)) // 2
        for j in range(0, len(title)):
            self.board[1][80+title_offset+j] = Back.WHITE + \
                Fore.RED+title[j]+Style.RESET_ALL

        for i in range(25):
            self.board[3][170+i] = self.bar_col

        for i in range(self.khealth):
            self.board[3][170+i] = self.yellow 

        self.outp="\n".join(["".join(row) for row in self.board])
        print(self.outp)
        print("\n")

        replay_file = 'replays/replay' + str(self.num_files + 1) + '.txt'
        with open(replay_file, 'a+') as f:
            for i in self.outp:
                for j in i:
                    f.write(j)

            f.write("\n")
            f.write("hello\n")
        
        if(destroy==6):
            self.running=-1