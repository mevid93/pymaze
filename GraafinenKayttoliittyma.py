'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
'''


import sys
from PyQt4 import QtGui


class Kayttoliittyma(QtGui.QWidget):

    def __init__(self):
        super(Kayttoliittyma, self).__init__()
        self.initUI()

    
    def initUI(self):
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle("Labyrintti V.0.0.1")
        self.center_screen()
        
            
    def center_screen(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def naytaIkkuna(self):
        app = QtGui.QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())

    
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawRect(100, 100, 150, 150)
        painter.end()
    
        

        