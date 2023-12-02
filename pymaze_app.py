"""
Created on 4 Mar 2016

@author: Martin Vidjeskog
@version: 0.4.0
"""


import sys
from PyQt5 import QtWidgets

from pymaze.gui.game_window import GameWindow


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow()
    window.show_window()
    sys.exit(app.exec_())
