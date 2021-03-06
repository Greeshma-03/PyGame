from os import system
from typing_extensions import Self
from colorama import Back, Style, Fore
import random
from src.King import king
from src.Queen import queen
from src.barbarian import barbars
from src.archer import archers
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
        self.lred = Back.LIGHTRED_EX+' '+Style.RESET_ALL
        self.lmag = Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL
        

        #replay of games
        self.num_files = len(os.listdir('replays'))
        self.outp=-1;
        self.running=1  #currently the game is running
        self.main='k'

        #Initialsing boundaries of village
        self.rows=40 
        self.cols=200        

        #Co-ordinates of components        
        #townhall
        self.townhallx=int(self.rows/2) 
        self.townhally=int(self.cols/2)
        self.townhealth=20
        self.town_max_health=self.townhealth
        
        #spawning points
        self.spx=[5,30,8] 
        self.spy=[10,180,196] 

        #huts
        self.hutsx=[12,10,10,10,10] 
        self.hutsy=[38,46,50,120,170] 
        self.hhpoints=[10,10,10,10,10] 
        self.hut_max_health=self.hhpoints[0] 

        #canons
        self.cx=[12,37]
        self.cy=[44,151]
        self.crange = random.randint(1,5)
        self.cdamage = 4
        self.canon_attacked=[0,0]
        self.level=1
        
        #tower wizard
        self.tx=[11,14]
        self.ty=[42,42]
        #did that tower choose some attack point
        self.tower_attacked=[0,0]
       
        #coordinates of choosen tower target
        self.targetx=[-1,-1]
        self.targety=[-1,-1]


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


        #King and Queen
        self.kx=39 
        self.ky=100 
        self.kdamage=2
        self.khealth=50
        self.king=king(self.kx,self.ky) 

        self.qx=39
        self.qy=100
        self.qdamage=1
        self.qhealth=40
        self.queen=queen(self.qx,self.qy)
        
        #troops
        self.maxtroops=5
        self.barbs=[]   
        self.archer=[]    
        self.ballon=[]

        self.bardam=4
        self.barhealth=20
        self.archdam=self.bardam/2
        self.balldam=self.bardam*2
        self.archealth=self.barhealth/2
        self.ballhealth=self.barhealth

         #colors of components
        self.townhall_col=self.magenta
        self.can_col=[]
        self.huts_col=[]
        self.wall1_col=[]
        self.wall2_col=[]
        self.wall3_col=[]
        self.wall4_col=[]

       
        for i in range(len(self.cx)):
            self.can_col.append(self.blue) 
        
        for i in range(len(self.hutsx)):
            self.huts_col.append(self.green) 

        for i in range(9):
            self.wall1_col.append(self.green) 
            self.wall2_col.append(self.green) 
            self.wall3_col.append(self.green) 
            self.wall4_col.append(self.green) 
        
        
        self.king_col=self.red 
        self.queen_col=self.red 
        self.bg_col=self.black 
        self.tower_col=[self.lred,self.lred]

        #king health bar colors
        self.bar_col=self.white 
        self.level_col = Back.LIGHTWHITE_EX+' '+Style.RESET_ALL
        self.spawn_col=self.yellow 
        self.sleep=0

        

    def render(self):
        if(self.sleep!=-1):
         self.queen.spl_attack(self)

        for i in range(len(self.tower_col)):
         self.tower_attacked[i]=0

        for i in range(len(self.tower_col)):
            self.canon_attacked[i]=0
        
        for i in range(len(self.targetx)):
            self.targetx[i]=-1
            self.targety[i]=-1

        
        #Do the barbarian work
        index=0
        for obj in self.barbs:
            obj.move(self)
            if(obj.health==0):
                self.barbs.pop(index)
            index+=1


        for obj in self.barbs:
             obj.wizard_target_attack(obj.barx,obj.bary,self)
                         
        
        index=0
        for obj in self.archer:
            #doubling the movement speed
            obj.move(self)
            obj.move(self)
            if(obj.health==0):
                self.archer.pop(index)
            index+=1
    
        for obj in self.archer:
            obj.wizard_target_attack(obj.barx,obj.bary,self)            

        index=0    
        for obj in self.ballon:
            #doubling the movement speed
            obj.move(self)
            obj.move(self)
            if(obj.health==0):
                self.ballon.pop(index)
            index+=1   

        index=0
        for obj in self.ballon:
            if(self.tower_attacked==1):
             obj.wizard_target_attack(obj.barx,obj.bary,self)
            else:
                break 
            index+=1             
    
        #Do canon and wizard work
        if(self.main=='q'):
          for i in range(len(self.cx)):
            if(((self.qx-self.cx[i])**2 + (self.qy-self.cy[i])**2) < (self.cdamage**2) and self.can_col[i] != self.black):
                self.qhealth -= self.cdamage
                if(self.qhealth<=40 and self.qhealth>=30):
                    self.queen_col=self.lred
                elif(self.qhealth<=30 and self.qhealth>=20):
                    self.queen_col=self.blue
                elif(self.qhealth<=20 and self.qhealth>=10):
                    self.queen_col=self.lmag
                elif(self.qhealth<=10 and self.qhealth>=0):
                    self.queen_col=self.yellow   
                elif(self.qhealth<=0):
                    self.queen_col=self.black 
                    self.qhealth=0
                    
          for i in range(len(self.tx)):
             if(((self.qx-self.tx[i])**2 + (self.qy-self.ty[i])**2) < (self.cdamage**2) and self.tower_col[i] != self.black):
                self.qhealth -= self.cdamage
                if(self.qhealth<=40 and self.qhealth>=30):
                    self.queen_col=self.lred
                elif(self.qhealth<=30 and self.qhealth>=20):
                    self.queen_col=self.blue
                elif(self.qhealth<=20 and self.qhealth>=10):
                    self.queen_col=self.lmag
                elif(self.qhealth<=10 and self.qhealth>=0):
                    self.queen_col=self.yellow   
                elif(self.qhealth<=0):
                    self.queen_col=self.black 
                    self.qhealth=0        

          if(self.qhealth <=0):
             self.running = 0 

        else:
          for i in range(2):
            if(((self.kx-self.cx[i])**2 + (self.ky-self.cy[i])**2) < (self.cdamage**2) and self.can_col[i] != self.black):
                self.khealth -= self.cdamage
                if(self.khealth<=40 and self.khealth>=30):
                    self.king_col=self.lred
                elif(self.khealth<=30 and self.khealth>=20):
                    self.king_col=self.blue
                elif(self.khealth<=20 and self.khealth>=10):
                    self.king_col=self.lmag
                elif(self.khealth<=10 and self.khealth>=0):
                    self.king_col=self.yellow   
                elif(self.khealth<=0):
                    self.king_col=self.black 
                    self.khealth=0

            if(((self.kx-self.tx[i])**2 + (self.ky-self.ty[i])**2) < (self.cdamage**2) and self.can_col[i] != self.black):
                self.khealth -= self.cdamage
                if(self.khealth<=40 and self.khealth>=30):
                    self.king_col=self.lred
                elif(self.khealth<=30 and self.khealth>=20):
                    self.king_col=self.blue
                elif(self.khealth<=20 and self.khealth>=10):
                    self.king_col=self.lmag
                elif(self.khealth<=10 and self.khealth>=0):
                    self.king_col=self.yellow   
                elif(self.khealth<=0):
                    self.king_col=self.black 
                    self.khealth=0        

          if(self.khealth <= 0):
             self.running = 0     

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
        for i in range(len(self.can_col)):
            self.board[self.cx[i]][self.cy[i]]=self.can_col[i] 

        #fill tower wizards
        for i in range(len(self.tower_col)):  
         self.board[self.tx[i]][self.ty[i]]=self.tower_col[i]

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
        for obj in self.archer:
            self.board[obj.barx][obj.bary]=obj.barb_col
        for obj in self.ballon:
            self.board[obj.barx][obj.bary]=obj.barb_col    

        #fill king/queen
        if(self.main=='k'):
         self.board[self.kx][self.ky]=self.king_col 
        else: 
         self.board[self.qx][self.qy]=self.queen_col 
 

        #fill health bar
        title="Health Bar"
        title_offset = (self.cols+1-len(title)) // 2
        for j in range(0, len(title)):
            self.board[1][80+title_offset+j] = Back.WHITE + \
                Fore.RED+title[j]+Style.RESET_ALL

        title="Level - "+str(self.level)
        title_offset = (self.cols+1-len(title)) // 2
        for j in range(0, len(title)):
            self.board[1][title_offset+j] = Back.WHITE + \
                Fore.GREEN+title[j]+Style.RESET_ALL        
        

        if(self.main=='k'):
         for i in range(25):
            self.board[3][170+i] = self.bar_col

         for i in range(int(self.khealth/2)):
            self.board[3][170+i] = self.yellow 
        else:
          for i in range(20):
                self.board[3][170+i] = self.bar_col

          for i in range(int(self.qhealth/2)):
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