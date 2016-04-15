'''
Created on 13 Apr 2016

@author: Marski
'''

from Labyrintti import *
from Pala import *

class WallFollower(object):
    
    def __init__(self, window, labyrintti):
        self.window = window
        self.labyrintti = labyrintti
        self.palalista = []
        
    def selvitaReitti(self):
        eteenpain = "N"
        x = int(self.labyrintti.getLeveys()/2) -1
        y = int(self.labyrintti.getKorkeus()/2) -1
        self.palalista.append(self.labyrintti.getPala(x,y))
        if(self.labyrintti.getPala(x, y).voiLiikkuaYlos()):
            y = y-1
            self.palalista.append(self.labyrintti.getPala(x, y))
        elif(self.labyrintti.getPala(x, y).voiLiikkuaOikealle()):
            x = x+1
            self.palalista.append(self.labyrintti.getPala(x,y))
            eteenpain = "E"
        elif(self.labyrintti.getPala(x,y).voiLiikkuaAlas()):
            y = y+1
            self.palalista.append(self.labyrintti.getPala(x,y))
            eteenpain = "S"
        elif(self.labyrintti.getPala(x,y).voiLiikkuaVasemmalle()):
            x = x -1
            eteenpain = "W"
            self.palalista.append(self.labyrintti.getPala(x, y))
    
    def piirraReitti(self):
        painter = QtGui.QPainter()
        painter.begin(self.window)
        painter.setPen(QtCore.Qt.red)
        x1, y1 = self.palalista[0].getKeskipiste()
        x2, y2 = self.palalista[1].getKeskipiste()
        painter.drawLine(x1, y1, x2, y2)
        painter.end()
    