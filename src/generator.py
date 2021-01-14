'''
Created on 5 Mar 2016

@author: Martin Vidjeskog
'''


import random
from src.piece import *


class TwoDimMazeGenerator(object):

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.pixelX = 275
        self.pixelY = 25
        self.pixelSivu = int((775-275)/self.width)
        self.lista = [[[] for x in range(self.width)]
                      for x in range(self.heigth)]

    def generate(self):
        # generate staring point
        alkuX = int(self.width/2)
        alkuY = int(self.heigth/2)
        # generate end point
        valinta = random.randint(0, 1)
        if(valinta == 1):
            maaliX = random.choice([0, self.width-1])
            maaliY = random.randint(0, self.heigth-1)
        else:
            maaliX = random.randint(0, self.width-1)
            maaliY = random.choice([0, self.heigth-1])
        # create algorithm
        self.__recursiveBactracking(alkuX, alkuY, maaliX, maaliY, None)
        self.__directionsToPieces(maaliX, maaliY)
        return self.lista

    def __recursiveBactracking(self, x, y, maaliX, maaliY, suunta):
        if(suunta == 'N'):
            self.lista[int(y)][int(x)].append('S')
        if(suunta == 'S'):
            self.lista[int(y)][int(x)].append('N')
        if(suunta == 'E'):
            self.lista[int(y)][int(x)].append('W')
        if(suunta == 'W'):
            self.lista[int(y)][int(x)].append('E')
        directions = ['N', 'S', 'E', 'W']
        random.shuffle(directions, random.random)
        if(x == maaliX and y == maaliY):
            return
        for i in range(0, 4):
            seuraavaX = 0
            seuraavaY = 0
            suunta = directions[i]
            if(suunta == 'N'):
                seuraavaX = x
                seuraavaY = y-1
            elif(suunta == 'S'):
                seuraavaX = x
                seuraavaY = y+1
            elif(suunta == 'E'):
                seuraavaX = x+1
                seuraavaY = y
            elif(suunta == 'W'):
                seuraavaX = x-1
                seuraavaY = y
            if(seuraavaX < self.width and seuraavaX >= 0 and seuraavaY >= 0 and seuraavaY < self.heigth):
                if not self.lista[int(seuraavaY)][int(seuraavaX)]:
                    self.lista[int(y)][int(x)].append(suunta)
                    self.__recursiveBactracking(
                        seuraavaX, seuraavaY, maaliX, maaliY, suunta)
        return

    def __directionsToPieces(self, maaliX, maaliY):
        for y in range(self.heigth):
            for x in range(self.width):
                if(y == maaliY and x == maaliX):
                    self.lista[y][x] = FinnishLinePiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N'], self.lista[y][x])):
                    self.lista[y][x] = VerticalBottomBlockedPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['E'], self.lista[y][x])):
                    self.lista[y][x] = HorizontalLeftBlockedPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['S'], self.lista[y][x])):
                    self.lista[y][x] = VerticalTopBlockedPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['W'], self.lista[y][x])):
                    self.lista[y][x] = HorizontalRightBlockedPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'E'], self.lista[y][x])):
                    self.lista[y][x] = TurnNEPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'S'], self.lista[y][x])):
                    self.lista[y][x] = VerticalPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'W'], self.lista[y][x])):
                    self.lista[y][x] = TurnNWPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['E', 'S'], self.lista[y][x])):
                    self.lista[y][x] = TurnSEPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['E', 'W'], self.lista[y][x])):
                    self.lista[y][x] = HorizontalPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['S', 'W'], self.lista[y][x])):
                    self.lista[y][x] = TurnSWPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'E', 'S'], self.lista[y][x])):
                    self.lista[y][x] = IntersectionToRightPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'E', 'W'], self.lista[y][x])):
                    self.lista[y][x] = IntersectionToUpPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'W', 'S'], self.lista[y][x])):
                    self.lista[y][x] = IntersectionToLeftPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['S', 'W', 'E'], self.lista[y][x])):
                    self.lista[y][x] = IntersectionToDownPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                else:
                    self.lista[y][x] = IntersectionPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                self.pixelX += self.pixelSivu
            self.pixelX = 275
            self.pixelY += self.pixelSivu

    def __containsDirections(self, suunnat, palalista):
        if(len(suunnat) != len(palalista)):
            return False
        for i in suunnat:
            if i not in palalista:
                return False
        return True


class WeaveMazeGenerator(object):

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.pixelX = 275
        self.pixelY = 25
        self.pixelSivu = int((775-275)/width)
        self.lista = [[[] for x in range(width)] for x in range(heigth)]

    def generate(self):
        # generate starting point
        alkuX = int(self.width/2)
        alkuY = int(self.heigth/2)
        # generate goal point
        valinta = random.randint(0, 1)
        if(valinta == 1):
            maaliX = random.choice([0, self.width-1])
            maaliY = random.randint(0, self.heigth-1)
        else:
            maaliX = random.randint(0, self.width-1)
            maaliY = random.choice([0, self.heigth-1])
        # use algorithm to create the maze
        self.__recursiveBactracking(alkuX, alkuY, maaliX, maaliY, None)
        self.__directionsToPieces(maaliX, maaliY)
        return self.lista

    def __recursiveBactracking(self, x, y, maaliX, maaliY, suunta):
        if(suunta == 'N'):
            self.lista[int(y)][int(x)].append('S')
        if(suunta == 'S'):
            self.lista[int(y)][int(x)].append('N')
        if(suunta == 'E'):
            self.lista[int(y)][int(x)].append('W')
        if(suunta == 'W'):
            self.lista[int(y)][int(x)].append('E')
        directions = ['N', 'S', 'E', 'W']
        random.shuffle(directions, random.random)
        if(x == maaliX and y == maaliY):
            return
        for i in range(0, 4):
            seuraavaX = 0
            seuraavaY = 0
            ylitysX = 0
            ylitysY = 0
            suunta = directions[i]
            if(suunta == 'N'):
                seuraavaX = x
                seuraavaY = y-1
                ylitysX = x
                ylitysY = y-2
            elif(suunta == 'S'):
                seuraavaX = x
                seuraavaY = y+1
                ylitysX = x
                ylitysY = y+2
            elif(suunta == 'E'):
                seuraavaX = x+1
                seuraavaY = y
                ylitysX = x+2
                ylitysY = y
            elif(suunta == 'W'):
                seuraavaX = x-1
                seuraavaY = y
                ylitysX = x-2
                ylitysY = y
            if(seuraavaX < self.width and seuraavaX >= 0 and seuraavaY >= 0 and seuraavaY < self.heigth):
                if not self.lista[int(seuraavaY)][int(seuraavaX)]:
                    self.lista[int(y)][int(x)].append(suunta)
                    self.__recursiveBactracking(
                        seuraavaX, seuraavaY, maaliX, maaliY, suunta)
                elif(ylitysX < self.width and ylitysX >= 0 and ylitysY >= 0 and ylitysY < self.heigth):
                    if not self.lista[int(ylitysY)][int(ylitysX)]:
                        if(self.__containsDirections(self.lista[int(seuraavaY)][int(seuraavaX)], ['W', 'E']) and (suunta == 'N' or suunta == 'S')):
                            self.lista[int(y)][int(x)].append(suunta)
                            self.lista[int(seuraavaY)][int(seuraavaX)] = [
                                'NY', 'SY', 'E', 'W']
                            self.__recursiveBactracking(
                                ylitysX, ylitysY, maaliX, maaliY, suunta)
                        elif(self.__containsDirections(self.lista[int(seuraavaY)][int(seuraavaX)], ['N', 'S']) and (suunta == 'W' or suunta == 'E')):
                            self.lista[int(y)][int(x)].append(suunta)
                            self.lista[int(seuraavaY)][int(seuraavaX)] = [
                                'N', 'S', 'EY', 'WY']
                            self.__recursiveBactracking(
                                ylitysX, ylitysY, maaliX, maaliY, suunta)
        return

    def __directionsToPieces(self, maaliX, maaliY):
        for y in range(self.heigth):
            for x in range(self.width):
                if(y == maaliY and x == maaliX):
                    self.lista[y][x] = FinnishLinePiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N'], self.lista[y][x])):
                    self.lista[y][x] = VerticalBottomBlocedPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['E'], self.lista[y][x])):
                    self.lista[y][x] = HorizontalLeftBlockedPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['S'], self.lista[y][x])):
                    self.lista[y][x] = VerticalTopBlockedPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['W'], self.lista[y][x])):
                    self.lista[y][x] = HorizontalRightBlockedPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'E'], self.lista[y][x])):
                    self.lista[y][x] = TurnNEPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'S'], self.lista[y][x])):
                    self.lista[y][x] = VerticalPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'W'], self.lista[y][x])):
                    self.lista[y][x] = TurnNWPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['E', 'S'], self.lista[y][x])):
                    self.lista[y][x] = TurnSEPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['E', 'W'], self.lista[y][x])):
                    self.lista[y][x] = HorizontalPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['S', 'W'], self.lista[y][x])):
                    self.lista[y][x] = TurnSWPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'E', 'S'], self.lista[y][x])):
                    self.lista[y][x] = IntersectionToRightPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'E', 'W'], self.lista[y][x])):
                    self.lista[y][x] = IntersectionToUpPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['N', 'W', 'S'], self.lista[y][x])):
                    self.lista[y][x] = IntersectionToLeftPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['S', 'W', 'E'], self.lista[y][x])):
                    self.lista[y][x] = IntersectionToDownPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['SY', 'W', 'E', 'NY'], self.lista[y][x])):
                    self.lista[y][x] = BridgeVerticalPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__containsDirections(['S', 'WY', 'EY', 'N'], self.lista[y][x])):
                    self.lista[y][x] = BridgeHorizontalPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                else:
                    self.lista[y][x] = IntersectionPiece(
                        self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                self.pixelX += self.pixelSivu
            self.pixelX = 275
            self.pixelY += self.pixelSivu

    def __containsDirections(self, suunnat, palalista):
        if(len(suunnat) != len(palalista)):
            return False
        for i in suunnat:
            if i not in palalista:
                return False
        return True
