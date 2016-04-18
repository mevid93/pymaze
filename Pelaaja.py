'''
Created on 12 Mar 2016

@author: Martin Vidjeskog
'''


from PyQt4 import QtGui, QtCore
from Pala import SuperPala

class Hahmo(object):
    '''
    Tama luokka piirtaa ja tietaa pelaajan paikan labyrintissa.
    Saa parametreina kokonaisluvut x ja y.
    '''

    def __init__(self, SuperPala, x, y):
        self.pala = SuperPala
        self.x = x
        self.y = y

    def liikutaHahmoa(self, SuperPala, x, y):
        self.pala = SuperPala
        self.x = x
        self.y = y
        
    def piirraHahmo(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.pala.getX() + self.pala.getW()/4+1, self.pala.getY() + self.pala.getH()/4+1, self.pala.getW()/2-2, self.pala.getH()/2-2, QtCore.Qt.red)
        painter.end()
        
    def getSijainti(self):
        return self.x, self.y
    

        
    