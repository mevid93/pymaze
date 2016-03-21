'''
Created on 20 Mar 2016

@author: Martin Vidjeskog
'''


from Labyrintti import Labyrintti
from Pala import SuperPala
import PyQt4.QtGui

class Tallentaja(object):

    def __init__(self, window, labyrintti):
        self.window = window
        self.leveys = labyrintti.getLeveys()
        self.korkeus = labyrintti.getKorkeus()
        self.lista = labyrintti.getPalat()
        self.tyyppi = labyrintti.getTyyppi()
        
    def tallennaLabyrintti(self):
        name = PyQt4.QtGui.QFileDialog.getSaveFileName(self.window, 'Save File', filter = '*.maze')
        if(name != '' and name != None):
            file = open(name, 'w')
            file.write("#Tyyppi: " + self.tyyppi)
            file.write("\n\n")
            file.write("#Labyrintin leveys: " + str(self.leveys))
            file.write("\n\n")
            file.write("#Labyrintin korkeus: " + str(self.korkeus))
            file.write("\n\n")
            file.write("#Palan leveys: " + str(self.lista[0][0].getW()))
            file.write("\n\n")
            file.write("#Palan korkeus: " + str(self.lista[0][0].getY()))
            file.write("\n\n")
            file.write("#Palat: \n")
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    file.write(str(self.lista[y][x].getX()) + " " + str(self.lista[y][x].getY()) + " " + type(self.lista[y][x]).__name__)
                    file.write("\n")
            file.close()