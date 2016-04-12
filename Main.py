'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
@version: 0.1.5
'''


import sys
from PyQt4 import QtGui
from GraphicalUI import GraphUI


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)    
    window = GraphUI()
    window.showWindow()
