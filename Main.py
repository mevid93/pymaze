'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
@version: 0.2.6

HUOM!!!!!
 Ohjelman suorittaminen vaatii pythonin asentamista.
 Suoritus vaatii myos PyQT4 kayttoliittymakirjastojen
 lataamista. Ne eivat sisally pythonin peruskirjastoihin.
'''


import sys
from PyQt4 import QtGui
from Grafiikka import Kayttoliittyma


''' Tama on paaohjelma, jonka ajamalla varsinainen kayttoliittyma
    luodaan ja kaynnistetaan.    '''

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    app = QtGui.QApplication(sys.argv)    
    window = Kayttoliittyma()
    window.showWindow()
