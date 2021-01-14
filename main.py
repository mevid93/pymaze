'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
@version: 0.3.0
'''


import sys
from PyQt5 import QtGui, QtWidgets
from src.window import GameWindow


if __name__ == '__main__':
    '''Main function to start the program.'''
    sys.setrecursionlimit(2000)
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow()
    window.showWindow()
    sys.exit(app.exec_())
