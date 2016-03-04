'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
@version: 0.0.1
'''


import sys
from PyQt4 import QtGui
from GraafinenKayttoliittyma import Kayttoliittyma


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ohjelmaruutu = Kayttoliittyma()
    ohjelmaruutu.naytaIkkuna()
