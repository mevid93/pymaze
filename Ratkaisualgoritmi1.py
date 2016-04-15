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
        x = int(self.labyrintti.getLeveys()/2) -1
        y = int(self.labyrintti.getKorkeus()/2) -1
        suunta = "N"
        self.palalista.append(self.labyrintti.getPala(x,y))
        while(type(self.labyrintti.getPala(x, y)).__name__ != "MaaliPala"):
            tyyppi = type(self.labyrintti.getPala(x,y)).__name__ 
            if(tyyppi == "YlikulkuPystysuuntaPala" or tyyppi == "YlikulkuVaakasuuntaPala"):
                if(suunta == "N"):
                    y = y-1
                elif(suunta == "W"):
                    x = x-1
                elif(suunta == "S"):
                    y = y+1
                else:
                    x = x+1
            elif(suunta == "N"):
                if(self.labyrintti.getPala(x, y).voiLiikkuaOikealle()):
                    x = x+1
                    suunta = "E"
                elif(self.labyrintti.getPala(x, y).voiLiikkuaYlos()):
                    y = y-1
                elif(self.labyrintti.getPala(x, y).voiLiikkuaVasemmalle()):
                    x = x-1
                    suunta = "W"
                else:
                    suunta = "S"
                    y = y+1
            elif(suunta == "W"):
                if(self.labyrintti.getPala(x, y).voiLiikkuaYlos()):
                    y = y-1
                    suunta = "N"
                elif(self.labyrintti.getPala(x, y).voiLiikkuaVasemmalle()):
                    x = x-1
                elif(self.labyrintti.getPala(x, y).voiLiikkuaAlas()):
                    y = y+1
                    suunta = "S"
                else:
                    suunta = "E"
                    x = x+1
            elif(suunta == "S"):
                if(self.labyrintti.getPala(x, y).voiLiikkuaVasemmalle()):
                    x = x-1
                    suunta = "W"
                elif(self.labyrintti.getPala(x, y).voiLiikkuaAlas()):
                    y = y+1
                elif(self.labyrintti.getPala(x, y).voiLiikkuaOikealle()):
                    x = x+1
                    suunta = "E"
                else:
                    y = y-1
                    suunta = "N"         
            elif(suunta == "E"):
                if(self.labyrintti.getPala(x, y).voiLiikkuaAlas()):
                    y = y+1
                    suunta = "S"
                elif(self.labyrintti.getPala(x, y).voiLiikkuaOikealle()):
                    x = x+1
                elif(self.labyrintti.getPala(x, y).voiLiikkuaYlos()):
                    y = y-1
                    suunta = "N"
                else:
                    suunta = "W"
                    x = x-1
            self.palalista.append(self.labyrintti.getPala(x, y))

    
    def piirraReitti(self):
        painter = QtGui.QPainter()
        painter.begin(self.window)
        painter.setPen(QtCore.Qt.red)
        for i in range(0, len(self.palalista)-1):
            x1, y1 = self.palalista[i].getKeskipiste()
            x2, y2 = self.palalista[i+1].getKeskipiste()
            painter.drawLine(x1, y1, x2, y2)
        painter.end()
    