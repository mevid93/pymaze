'''
Created on 13 Apr 2016

@author: Martin Vidjeskog
'''

from src.maze import *
from src.piece import *


class WallFollower(object):

    def __init__(self, window):
        self.window = window
        self.maze = window.maze
        self.pieces = []
        self.x = 0
        self.y = 0
        self.direction = "N"

    def solve(self):
        self.x = int(self.maze.getWidth()/2) - 1
        self.y = int(self.maze.getHeigth()/2) - 1
        if(type(self.maze.getPiece(self.x, self.y)).__name__ == "BridgeHorizontalPiece"):
            self.direction = "E"
        self.pieces.append(self.maze.getPiece(self.x, self.y))
        while(type(self.maze.getPiece(self.x, self.y)).__name__ != "FinnishLinePiece"):
            pala = self.__chooseAndMove()
            self.__visitPiece(pala)

    def __chooseAndMove(self):
        tyyppi = type(self.maze.getPiece(self.x, self.y)).__name__
        if(tyyppi == "BridgeVerticalPiece" or tyyppi == "BridgeHorizontalPiece"):
            if(self.direction == "N"):
                self.y = self.y-1
            elif(self.direction == "W"):
                self.x = self.x-1
            elif(self.direction == "S"):
                self.y = self.y+1
            else:
                self.x = self.x+1
        elif(self.direction == "N"):
            if(self.maze.getPiece(self.x, self.y).isAllowedToMoveRight()):
                self.x = self.x+1
                self.direction = "E"
            elif(self.maze.getPiece(self.x, self.y).isAllowedToMoveUp()):
                self.y = self.y-1
            elif(self.maze.getPiece(self.x, self.y).isAllowedToMoveLeft()):
                self.x = self.x-1
                self.direction = "W"
            else:
                self.direction = "S"
                self.y = self.y+1
        elif(self.direction == "W"):
            if(self.maze.getPiece(self.x, self.y).isAllowedToMoveUp()):
                self.y = self.y-1
                self.direction = "N"
            elif(self.maze.getPiece(self.x, self.y).isAllowedToMoveLeft()):
                self.x = self.x-1
            elif(self.maze.getPiece(self.x, self.y).isAllowedToMoveDown()):
                self.y = self.y+1
                self.direction = "S"
            else:
                self.direction = "E"
                self.x = self.x+1
        elif(self.direction == "S"):
            if(self.maze.getPiece(self.x, self.y).isAllowedToMoveLeft()):
                self.x = self.x-1
                self.direction = "W"
            elif(self.maze.getPiece(self.x, self.y).isAllowedToMoveDown()):
                self.y = self.y+1
            elif(self.maze.getPiece(self.x, self.y).isAllowedToMoveRight()):
                self.x = self.x+1
                self.direction = "E"
            else:
                self.y = self.y-1
                self.direction = "N"
        elif(self.direction == "E"):
            if(self.maze.getPiece(self.x, self.y).isAllowedToMoveDown()):
                self.y = self.y+1
                self.direction = "S"
            elif(self.maze.getPiece(self.x, self.y).isAllowedToMoveRight()):
                self.x = self.x+1
            elif(self.maze.getPiece(self.x, self.y).isAllowedToMoveUp()):
                self.y = self.y-1
                self.direction = "N"
            else:
                self.direction = "W"
                self.x = self.x-1
        return self.maze.getPiece(self.x, self.y)

    def __visitPiece(self, pala):
        tyyppi = type(pala).__name__
        if(pala in self.pieces):
            if(tyyppi == "BridgeVerticalPiece" or tyyppi == "BridgeHorizontalPiece"):
                vieruspalat = []
                vieruspalat.append(self.maze.getPiece(self.x-1, self.y))
                vieruspalat.append(self.maze.getPiece(self.x+1, self.y))
                vieruspalat.append(self.maze.getPiece(self.x, self.y-1))
                vieruspalat.append(self.maze.getPiece(self.x, self.y+1))
                kpl = 0
                for vieruspala in vieruspalat:
                    if(vieruspala in self.pieces):
                        kpl += 1
                if(kpl == 1):
                    index = self.__rindex(self.pieces, pala)
                    self.pieces = self.pieces[0:index+1]
                if(kpl == 2 and (vieruspalat[0] in self.pieces) and (vieruspalat[1] in self.pieces)):
                    index = self.__rindex(self.pieces, pala)
                    self.pieces = self.pieces[0:index+1]
                elif(kpl == 2 and len(vieruspalat) == 4 and (vieruspalat[2] in self.pieces) and (vieruspalat[3] in self.pieces)):
                    index = self.__rindex(self.pieces, pala)
                    self.pieces = self.pieces[0:index+1]
                elif(kpl == 4):
                    index = self.__rindex(self.pieces, pala)
                    self.pieces = self.pieces[0:index+1]
                else:
                    self.pieces.append(pala)
            else:
                index = self.__rindex(self.pieces, pala)
                self.pieces = self.pieces[0:index+1]
        else:
            self.pieces.append(pala)


    def __rindex(self, hakuLista, haettavaArvo):
        return len(hakuLista) - hakuLista[::-1].index(haettavaArvo) - 1

    def drawRoute(self):
        painter = QtGui.QPainter()
        painter.begin(self.window)
        painter.setPen(QtCore.Qt.red)
        for i in range(0, len(self.pieces)-1):
            x1, y1 = self.pieces[i].getCenter()
            x2, y2 = self.pieces[i+1].getCenter()
            painter.drawLine(x1, y1, x2, y2)
        painter.end()
