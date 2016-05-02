'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
'''


import sys
from PyQt4 import QtGui, QtCore
from Kuuntelija import NappienKuuntelija

class GraphUI(QtGui.QWidget):
    '''
    Kayttoliittyma-luokka, joka huolehtii kayttoliittyman piirtamisesta
    ja komentojen vastaanottamisesta. 
    '''

    def __init__(self):
        super(GraphUI, self).__init__()
        self.initUI()
        self.labyrintti = None
        self.hahmo = None
        self.demo = None
        self.tila = 0
        self.nappienKuuntelija = NappienKuuntelija(self)

    
    
    def initUI(self):
        #ikkunan alustaminen
        self.setFixedSize(825, 700)
        self.setAutoFillBackground(True)
        self.setUpdatesEnabled(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#808080"))
        self.setPalette(p)
        self.setWindowTitle("Labyrintti V.0.2.4")
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
        #Lataa-labyrintti nappi
        self.loadButton = QtGui.QPushButton("Lataa Labyrintti", self)
        self.loadButton.resize(200, 50)
        self.loadButton.move(50, 100)
        self.loadButton.clicked.connect(lambda: self.buttonClicked())
        #Tallenna-labyrintti nappi
        self.saveButton = QtGui.QPushButton("Tallenna Labyrintti", self)
        self.saveButton.resize(200, 50)
        self.saveButton.move(50, 175)
        self.saveButton.clicked.connect(lambda: self.buttonClicked())
        #Pelaa nappi
        self.playButton = QtGui.QPushButton("Pelaa", self)
        self.playButton.resize(200, 50)
        self.playButton.move(50, 250)
        self.playButton.clicked.connect(lambda: self.buttonClicked())
        #Demoratkaisu nappi
        self.demoButton = QtGui.QPushButton("Luovuta ja anna ratkaisu", self)
        self.demoButton.resize(200, 50)
        self.demoButton.move(50, 325)
        self.demoButton.clicked.connect(lambda: self.buttonClicked())
        #tietoja-nappi
        self.exitButton = QtGui.QPushButton("Tietoja ohjelmasta", self)
        self.exitButton.clicked.connect(lambda: self.buttonClicked())
        self.exitButton.resize(200, 50)
        self.exitButton.move(50, 401)
        #exit-napin alustaminen
        self.exitButton = QtGui.QPushButton("Lopeta", self)
        self.exitButton.clicked.connect(lambda: self.buttonClicked())
        self.exitButton.resize(200, 50)
        self.exitButton.move(50, 476)
        #labyrintin asetusvalikko
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        self.label1 = QtGui.QLabel("Valitse labyrintin tyyppi", self)
        self.label1.setFont(font)
        self.label1.move(290, 40)
        self.label1.setVisible(False)
        self.checkBox1 = QtGui.QCheckBox("Tavallinen 2DLabyrintti", self)
        self.checkBox1.move(300, 70)
        self.checkBox1.setVisible(False)
        self.checkBox2 = QtGui.QCheckBox("WeaveLabyrintti", self)
        self.checkBox2.move(300, 100)
        self.checkBox2.setVisible(False)
        self.checkBox2.clicked.connect(lambda: self.vaihdaValintaa())
        self.checkBox1.clicked.connect(lambda: self.vaihdaValintaa())
        self.generoi = QtGui.QPushButton("Generoi", self)
        self.generoi.clicked.connect(lambda: self.buttonClicked())
        self.generoi.resize(100, 30)
        self.generoi.move(290, 200)
        self.generoi.setStyleSheet("border: 2px solid black")
        self.generoi.setVisible(False)
        self.leveysBox = QtGui.QSpinBox(self)
        self.leveysBox.move(300, 160)
        self.leveysBox.resize(70, 30)
        self.leveysBox.setMinimum(15)
        self.leveysBox.setMaximum(50)
        self.leveysBox.setVisible(False)
        self.label2 = QtGui.QLabel("Anna leveys/korkeus", self)
        self.label2.setFont(font)
        self.label2.move(290, 130)
        self.label2.setVisible(False)
        self.label3 = QtGui.QLabel("Leveys/korkeus (min = 15, max = 50)", self)
        self.label3.move(380, 170)
        self.label3.setVisible(False)     
          


    def showWindow(self):
        app = QtGui.QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())



    def vaihdaValintaa(self):
        sender = self.sender()
        if(sender.text() == "Tavallinen 2DLabyrintti"):
            self.checkBox1.setChecked(True)
            self.checkBox2.setChecked(False)
        else:
            self.checkBox1.setChecked(False)
            self.checkBox2.setChecked(True)



    def asetusvalikko(self):
        if not(self.checkBox1.isVisible()):
            self.checkBox1.setVisible(True)
            self.checkBox2.setVisible(True)
            self.label1.setVisible(True)
            self.label2.setVisible(True)
            self.label3.setVisible(True)
            self.leveysBox.setVisible(True)
            self.generoi.setVisible(True)
        else:
            self.checkBox1.setVisible(False)
            self.checkBox2.setVisible(False)
            self.label1.setVisible(False)
            self.label2.setVisible(False)
            self.label3.setVisible(False)
            self.leveysBox.setVisible(False)
            self.generoi.setVisible(False)



    def keyPressEvent(self, e):
        if(self.tila == 2):
            x, y = self.hahmo.getSijainti()
            liikuta = 1
            if (e.key() == QtCore.Qt.Key_W):
                if(y > 0 and self.labyrintti.getPala(x, y).voiLiikkuaYlos()):
                    while(type(self.labyrintti.getPala(x, y-liikuta)).__name__ == "YlikulkuVaakasuuntaPala"):
                        liikuta += 1
                    y = y - liikuta 
                    pala = self.labyrintti.getPala(x, y)
                    self.hahmo.liikutaHahmoa(pala, x, y)
                    self.update()
            elif(e.key() == QtCore.Qt.Key_S):
                if(y < self.labyrintti.getKorkeus()-1 and self.labyrintti.getPala(x, y).voiLiikkuaAlas()):
                    while(type(self.labyrintti.getPala(x, y+liikuta)).__name__ == "YlikulkuVaakasuuntaPala"):
                        liikuta += 1
                    y = y + liikuta 
                    pala = self.labyrintti.getPala(x, y)
                    self.hahmo.liikutaHahmoa(pala, x, y)
                    self.update()
            elif(e.key() == QtCore.Qt.Key_A):
                if(x > 0 and self.labyrintti.getPala(x, y).voiLiikkuaVasemmalle()):
                    while(type(self.labyrintti.getPala(x-liikuta, y)).__name__ == "YlikulkuPystysuuntaPala"):
                        liikuta += 1
                    x = x - liikuta 
                    pala = self.labyrintti.getPala(x, y)
                    self.hahmo.liikutaHahmoa(pala, x, y)
                    self.update()
            elif(e.key() == QtCore.Qt.Key_D):
                if(x < self.labyrintti.getLeveys()-1 and self.labyrintti.getPala(x, y).voiLiikkuaOikealle()):
                    while(type(self.labyrintti.getPala(x+liikuta, y)).__name__ == "YlikulkuPystysuuntaPala"):
                        liikuta += 1
                    x = x + liikuta 
                    pala = self.labyrintti.getPala(x, y)
                    self.hahmo.liikutaHahmoa(pala, x, y)
                    self.update()
            if(type(self.labyrintti.getPala(x,y)).__name__ == "MaaliPala"):
                self.tila = 1
                self.textbox.clear()
                self.textbox.setText("SELVITIT LABYRINTIN!!")


    
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        if(self.tila == 0):
            painter.drawRect(274, 24, 501, 501)
            painter.fillRect(275, 25, 500, 500, QtGui.QColor("#E0E0E0"))
        if(self.tila == 1):
            self.labyrintti.piirraPelialueeseen(self)
        if(self.tila == 2):
            self.labyrintti.piirraPelialueeseen(self)
            self.hahmo.piirraHahmo(self)
        if(self.tila == 3):
            self.labyrintti.piirraPelialueeseen(self)
            self.demo.piirraReitti()
        painter.end()      

   
        
    def buttonClicked(self):
        sender = self.sender()
        self.nappienKuuntelija.suoritaNapinToiminnot(sender)

                
                

            
            
            
            
            
            
            
            
            
        