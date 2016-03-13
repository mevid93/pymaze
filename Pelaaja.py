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

    def __init__(self, SuperPala):
        self.pala = SuperPala

    def liikutaHahmoa(self, SuperPala):
        self.pala = SuperPala
        
    def piirraHahmo(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.pala.getX() + self.pala.getW()/4 + 1, self.pala.getY() + self.pala.getH()/4 + 1, 10, 10, QtCore.Qt.red)
        painter.end() 