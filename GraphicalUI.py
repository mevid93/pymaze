'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
'''


import sys
from PyQt4 import QtGui


class GraphUI(QtGui.QWidget):

    def __init__(self):
        super(GraphUI, self).__init__()
        self.initUI()
    
    def initUI(self):
        #ikkunan alustaminen
        self.setFixedSize(825, 700)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#808080"))
        self.setPalette(p)
        self.setWindowTitle("Labyrintti V.0.0.3")
        self.center_screen()
        #tekstiboxin alustaminen
        self.textbox = QtGui.QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.move(50, 551)
        self.textbox.resize(725, 125)
        self.textbox.setText("Tervetuloa Labyrintti-pelin pariin.")
        #exit-napin alustaminen
        self.exitButton = QtGui.QPushButton("Exit", self)
        self.exitButton.clicked.connect(lambda: sys.exit())
        self.exitButton.resize(200, 50)
        self.exitButton.move(50, 476)   
            
    def center_screen(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showWindow(self):
        app = QtGui.QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())
    
    def paintEvent(self, event):
        '''
        Metodia kutsutaan heti alussa kun sovellus kaynnistyy.
        Piirtaa pelialueen rajat.
        '''
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawRect(274, 24, 501, 501)
        painter.end()    
        self.tyhjennaPelialue()
        
    def setTextboxText(self, string):
        self.textbox.setText(string)

    def tyhjennaPelialue(self):
        painter = QtGui.QPainter()
        painter.begin(self)
        y = 24
        x = 274
        painter.fillRect(275, 25, 500, 500, QtGui.QColor("#E0E0E0"))
        painter.end() 
        

        