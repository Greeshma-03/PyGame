from sys import breakpointhook
from colorama import Back, Style
import os
from src.input_to import *
from colorama import Back, Style
import math


class ballons():

    def __init__(self, barx, bary, heal, dam):

        # Initalising colors and king
        self.black = Back.BLACK+' '+Style.RESET_ALL
        self.green = Back.GREEN+' '+Style.RESET_ALL
        self.magenta = Back.MAGENTA+' '+Style.RESET_ALL
        self.blue = Back.BLUE+' '+Style.RESET_ALL
        self.red = Back.RED+' '+Style.RESET_ALL
        self.yellow = Back.YELLOW+' '+Style.RESET_ALL
        self.white = Back.WHITE+' '+Style.RESET_ALL
        self.lit = Back.LIGHTCYAN_EX+' '+Style.RESET_ALL
        self.lred = Back.LIGHTRED_EX+' '+Style.RESET_ALL
        self.lgreen = Back.LIGHTGREEN_EX+' '+Style.RESET_ALL
        

        self.barx = barx
        self.bary = bary
        self.barb_col = self.lgreen
        self.health = heal
        self.damage = dam

    def shortest_dist(self, x, y, board):

        tx = board.townhallx
        ty = board.townhally

        mini = 10000000
        
        use2=0
        for i in range(len(board.can_col)):
                if(board.can_col[i] == self.black):
                    use2+=1
                    continue
                if(mini > ((x-board.cx[i])**2+(y-board.cy[i])**2)):
                    mini = (x-board.cx[i])**2+(y-board.cy[i])**2
                    if(mini <= 1):
                        if(board.can_col[i] == self.blue):
                            board.can_col[i] = self.lit
                        elif(board.can_col[i] == self.lit):
                            board.can_col[i] = self.yellow
                        elif(board.can_col[i] == self.yellow):
                            board.can_col[i] = self.red
                        elif(board.can_col[i] == self.red):
                            board.can_col[i] = self.black    
                        return 1 

        use=0              
        for i in range(len(board.tower_col)):
         if(board.tower_col[i]!=self.black):
            if(mini > ((x-board.tx[i])**2+(y-board.ty[i])**2)):
                    mini = (x-board.tx[i])**2+(y-board.ty[i])**2
                    #attack by baloon
                    if(mini <= 1):
                        if(board.tower_col[i] == self.lred):
                            board.tower_col[i] = self.lit
                        elif(board.tower_col[i] == self.lit):
                            board.tower_col[i] = self.yellow
                        elif(board.tower_col[i] == self.yellow):
                            board.tower_col[i] = self.red
                        elif(board.tower_col[i] == self.red):
                            board.tower_col[i] = self.black    
                        return 1             
         else:
             use+=1

        if(use==len(board.tower_col) and use2==len(board.can_col)):
            # huts nearest
            destroy = 0
            for i in range(5):
                if(board.huts_col[i] == self.black):
                    destroy += 1
                    continue
                if(mini > ((x-board.hutsx[i])**2+(y-board.hutsy[i])**2)):
                    mini = (x-board.hutsx[i])**2+(y-board.hutsy[i])**2
                    if(mini <= 1):
                        if(board.huts_col[i] == self.green):
                            board.huts_col[i] = self.blue
                        elif(board.huts_col[i] == self.blue):
                            board.huts_col[i] = self.yellow
                        elif(board.huts_col[i] == self.yellow):
                            board.huts_col[i] = self.black
                        return 1

            # townhall nearest
            if(destroy == 5):
                if(board.townhall_col != self.black):
                    for i in range(4):
                        for j in range(3):
                            if(mini > ((x-tx-i)**2+(y-ty-j)**2)):
                                mini = (x-tx-i)**2+(y-ty-j)**2

                                if(mini <= 1):
                                    if(board.townhall_col == self.magenta):
                                        board.townhall_col = self.blue
                                    elif(board.townhall_col == self.blue):
                                        board.townhall_col = self.yellow
                                    elif(board.townhall_col == self.yellow):
                                        board.townhall_col = self.lit
                                    elif(board.townhall_col == self.lit):
                                        board.townhall_col = self.red
                                    elif(board.townhall_col == self.red):
                                        board.townhall_col = self.black
                                    return 1

        return mini

    def wizard_tower_attack(self, x, y, board):
        use=0
        for i in range(len(board.tower_col)):
            if(board.tower_col[i]==self.black or board.tower_attacked[i]==1):
                use+=1
        if(use==len(board.tower_col)):
            return

        for i in range(len(board.tower_col)):
         if(((x-board.tx[i])**2+(y-board.ty[i])**2) <= (board.crange)**2):            
            self.health -= board.cdamage
            board.tower_attacked[i] = 1
            board.targetx[i] = x
            board.targety[i] = y
            if(self.health < 20):
                self.barb_col = self.magenta
            elif(self.health <= 15 and self.health >= 10):
                self.barb_col = self.blue
            elif(self.health <= 10 and self.health >= 5):
                self.barb_col = self.yellow
            elif(self.health <= 5 and self.health >= 0):
                self.barb_col = self.red
            elif(self.health <= 0):
                self.barb_col = self.black
                self.health = 0
            break    

    def wizard_target_attack(self, x, y, board):
        if(board.tower_col==self.black):
            return        
        if((x-board.targetx)**2+(y-board.targety)**2 <= 9):
            self.health -= board.cdamage
            if(self.health < 20):
                self.barb_col = self.magenta
            elif(self.health <= 15 and self.health >= 10):
                self.barb_col = self.blue
            elif(self.health <= 10 and self.health >= 5):
                self.barb_col = self.yellow
            elif(self.health <= 5 and self.health >= 0):
                self.barb_col = self.red
            elif(self.health <= 0):
                self.barb_col = self.black
                self.health = 0

    def move(self, board):

        dist = []
        # find the shortest dist among huts,townhall for 4 possibilities
        dist.append(self.shortest_dist(self.barx+1, self.bary, board))
        dist.append(self.shortest_dist(self.barx, self.bary+1, board))
        dist.append(self.shortest_dist(self.barx-1, self.bary, board))
        dist.append(self.shortest_dist(self.barx, self.bary-1, board))

        # follow the path that gives least among the 4
        if(min(dist) == dist[0]):
            self.barx += 1
        elif(min(dist) == dist[1]):
            self.bary += 1
        elif(min(dist) == dist[2]):
            self.barx -= 1
        else:
            self.bary -= 1

        self.wizard_tower_attack(self.barx, self.bary, board)
