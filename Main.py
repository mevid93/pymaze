'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
@version: 0.2.3
'''


import sys
from PyQt4 import QtGui
from GraphicalUI import GraphUI


if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    app = QtGui.QApplication(sys.argv)    
    window = GraphUI()
    window.showWindow()
