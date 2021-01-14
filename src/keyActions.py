'''
Created on 2 May 2016

@author: Martin Vidjeskog
'''


from PyQt5 import QtCore


class KeyListener(object):

    def __init__(self, window):
        self.window = window

    def handleKeyPress(self, e):
        x, y = self.window.player.getLocation()
        liikuta = 1
        if (e.key() == QtCore.Qt.Key_W):
            self.moveUpCommand(x, y, liikuta)
        elif(e.key() == QtCore.Qt.Key_S):
            self.moveDownCommand(x, y, liikuta)
        elif(e.key() == QtCore.Qt.Key_A):
            self.moveLeftCommand(x, y, liikuta)
        elif(e.key() == QtCore.Qt.Key_D):
            self.moveRightCommand(x, y, liikuta)
        x, y = self.window.player.getLocation()
        if(type(self.window.maze.getPiece(x, y)).__name__ == "FinnishLinePiece"):
            self.finnishCommand()

    def moveUpCommand(self, x, y, liikuta):
        if(y > 0 and self.window.maze.getPiece(x, y).isAllowedToMoveUp()):
            while(type(self.window.maze.getPiece(x, y-liikuta)).__name__ == "BridgeHorizontalPiece"):
                liikuta += 1
            y = y - liikuta
            pala = self.window.maze.getPiece(x, y)
            self.window.player.movePlayer(pala, x, y)
            self.window.update()

    def moveDownCommand(self, x, y, liikuta):
        if(y < self.window.maze.getHeigth()-1 and self.window.maze.getPiece(x, y).isAllowedToMoveDown()):
            while(type(self.window.maze.getPiece(x, y+liikuta)).__name__ == "BridgeHorizontalPiece"):
                liikuta += 1
            y = y + liikuta
            pala = self.window.maze.getPiece(x, y)
            self.window.player.movePlayer(pala, x, y)
            self.window.update()

    def moveLeftCommand(self, x, y, liikuta):
        if(x > 0 and self.window.maze.getPiece(x, y).isAllowedToMoveLeft()):
            while(type(self.window.maze.getPiece(x-liikuta, y)).__name__ == "BridgeVerticalPiece"):
                liikuta += 1
            x = x - liikuta
            pala = self.window.maze.getPiece(x, y)
            self.window.player.movePlayer(pala, x, y)
            self.window.update()

    def moveRightCommand(self, x, y, liikuta):
        if(x < self.window.maze.getWidth()-1 and self.window.maze.getPiece(x, y).isAllowedToMoveRight()):
            while(type(self.window.maze.getPiece(x+liikuta, y)).__name__ == "BridgeVerticalPiece"):
                liikuta += 1
            x = x + liikuta
            pala = self.window.maze.getPiece(x, y)
            self.window.player.movePlayer(pala, x, y)
            self.window.update()

    def finnishCommand(self):
        self.window.state = 1
        self.window.textbox.clear()
        self.window.textbox.setText("SELVITIT LABYRINTIN!!")
