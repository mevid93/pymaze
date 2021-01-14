'''
Created on 12 Mar 2016

@author: Martin Vidjeskog
'''


from PyQt5 import QtGui, QtCore


class Player(object):

    def __init__(self, piece, x, y):
        self.pala = piece
        self.x = x
        self.y = y

    def movePlayer(self, piece, x, y):
        self.pala = piece
        self.x = x
        self.y = y

    def drawPlayer(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.pala.getX() + self.pala.getW()/4+1, self.pala.getY() +
                         self.pala.getH()/4+1, self.pala.getW()/2-2, self.pala.getH()/2-2, QtCore.Qt.red)
        painter.end()

    def getLocation(self):
        return self.x, self.y
