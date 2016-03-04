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
        self.setWindowTitle("Labyrintti V.0.0.2")
        self.center_screen()
        #tekstiboxin alustaminen
        self.textbox = QtGui.QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.move(50, 550)
        self.textbox.resize(725, 125)
        self.textbox.setText("Tervetuloa Labyrintti-pelin pariin.")
        #exit-napin alustaminen
        self.exitButton = QtGui.QPushButton("Exit", self)
        self.exitButton.clicked.connect(lambda: sys.exit())
        self.exitButton.resize(200, 50)
        self.exitButton.move(50, 475)
        
            
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
        painter = QtGui.QPainter()
        painter.begin(self)
        y = 25
        for i in range(20):
            x = 275
            for j in range(20):
                painter.drawRect(x, y, 25, 25)
                x += 25
            y += 25
        painter.end()
        
        
    def setTextboxText(self, string):
        self.textbox.setText(string)

    
        

        