'''
Created on 20 Mar 2016

@author: Martin Vidjeskog
'''


from Labyrintti import Labyrintti
from Pala import SuperPala
import PyQt4.QtGui

class Tallentaja(object):

    def __init__(self, window, Labyrintti):
        self.window = window
        self.leveys = Labyrintti.getLeveys()
        self.korkeus = Labyrintti.getKorkeus()
        self.lista = Labyrintti.getPalat()
        
    def tallennaLabyrintti(self):
        name = PyQt4.QtGui.QFileDialog.getSaveFileName(self.window, 'Save File', filter = '*.maze')
        if(name != '' and name != None):
            file = open(name, 'w')
            file.write("#Leveys: " + str(self.leveys))
            file.write("\n\n")
            file.write("#Korkeus: " + str(self.korkeus))
            file.write("\n\n")
            file.write("#Palat: \n")
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    file.write(str(self.lista[y][x].getX()) + " " + str(self.lista[y][x].getY()) + " " + str(self.lista[y][x].getW()) + " " + str(self.lista[y][x].getH()))
                    file.write("\n")
            file.close()