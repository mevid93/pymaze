'''
Created on 5 Mar 2016

@author: Martin Vidjeskog
'''


from src.generator import TwoDimMazeGenerator, WeaveMazeGenerator


class Maze(object):

    def __init__(self, width, heigth):
        self.pieces = []
        self.width = width
        self.heigth = heigth

    def drawMaze(self, window):
        for y in range(self.width):
            for x in range(self.heigth):
                if(self.pieces[y][x]):
                    self.pieces[y][x].paintPiece(window)

    def getWidth(self):
        return self.width

    def getHeigth(self):
        return self.heigth

    def getPiece(self, x, y):
        return self.pieces[y][x]

    def getPieces(self):
        return self.pieces

    def generateMaze(self):
        pass

    def getType(self):
        pass


class TwoDimMaze(Maze):

    def __init__(self, width, heigth, pieces=[]):
        super().__init__(width, heigth)
        if(len(pieces) == 0):
            self.generateMaze()
        else:
            self.pieces = pieces

    def generateMaze(self):
        generator = TwoDimMazeGenerator(self.width, self.heigth)
        self.pieces = generator.generate()

    def getType(self):
        return "KaksiDLabyrintti"


class WeaveMaze(Maze):

    def __init__(self, width, heigth, pieces=[]):
        super().__init__(width, heigth)
        if(len(pieces) == 0):
            self.generateMaze()
        else:
            self.pieces = pieces

    def generateMaze(self):
        generator = WeaveMazeGenerator(self.width, self.heigth)
        self.pieces = generator.generate()

    def getType(self):
        return "WeaveLabyrintti"
