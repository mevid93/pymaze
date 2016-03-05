'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
'''


import sys
from PyQt4 import QtGui
from Labyrintti import KaksiDLabyrintti


class GraphUI(QtGui.QWidget):

    def __init__(self):
        super(GraphUI, self).__init__()
        self.initUI()
        self.Labyrintti = None
        self.tila = 0
    
    def initUI(self):
        #ikkunan alustaminen
        self.setFixedSize(825, 700)
        self.setAutoFillBackground(True)
        self.setUpdatesEnabled(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#808080"))
        self.setPalette(p)
        self.setWindowTitle("Labyrintti V.0.0.4")
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        #tekstiboxin alustaminen
        self.textbox = QtGui.QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.move(50, 551)
        self.textbox.resize(725, 125)
        self.textbox.setText("Tervetuloa Labyrintti-pelin pariin.")
        #Labyrintin luontinappi
        self.genButton = QtGui.QPushButton("Generoi Labyrintti", self)
        self.genButton.resize(200, 50)
        self.genButton.move(50, 25)
        self.genButton.clicked.connect(lambda: self.buttonClicked())
        #exit-napin alustaminen
        self.exitButton = QtGui.QPushButton("Exit", self)
        self.exitButton.clicked.connect(lambda: sys.exit())
        self.exitButton.resize(200, 50)
        self.exitButton.move(50, 476)   
        
    def showWindow(self):
        app = QtGui.QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())
    
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        if (self.tila == 0):
            painter.drawRect(274, 24, 501, 501)
            self.tyhjennaPelialue()
        if (self.tila == 1):
            self.Labyrintti.piirraPelialueeseen(self)
        painter.end()      
        
    def setTextboxText(self, string):
        self.textbox.setText(string)

    def tyhjennaPelialue(self):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.fillRect(275, 25, 500, 500, QtGui.QColor("#E0E0E0"))
        painter.end() 
        
    def buttonClicked(self):
        sender = self.sender()
        if(sender.text() == "Generoi Labyrintti"):
            self.Labyrintti = KaksiDLabyrintti(20, 20)
            self.tila = 1
            self.update()

        