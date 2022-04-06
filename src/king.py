from colorama import Back, Style
import os
from src.input_to import *
from colorama import Back, Style
import math


class king():

    def __init__(self, kx, ky):
        self.kx = kx
        self.ky = ky
        self.green=Back.GREEN+' '+Style.RESET_ALL
        self.yellow=Back.YELLOW+' '+Style.RESET_ALL
        self.blue=Back.BLUE+' '+Style.RESET_ALL
        self.black=Back.BLACK+' '+Style.RESET_ALL

    def modify(self, kx, ky):
        self.kx = kx
        self.ky = ky

    def move(self, board,moment):


        if(moment == ' '):
            

            


           




            

            for ii in range(12):
                if(math.sqrt(((board.kx-board.help[ii][0])**2 + (board.ky-board.help[ii][1])**2))==1):

                    for i in range(12):
                        if(board.townhall_col[i] == self.green):
                            board.townhall_col[i]=self.blue
                            continue

                        if(board.townhall_col[i] == self.blue):
                            board.townhall_col[i]=self.yellow
                            continue

                        if(board.townhall_col[i] == self.yellow):
                            board.townhall_col[i]=self.black
                            continue


            

        if(board.ky == board.cols):
            board.kx = 39
            board.ky = 100

        if(board.kx == board.rows):
            board.kx = 39
            board.ky = 100

