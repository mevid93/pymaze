'''
Created on 4 Mar 2016

@author: Martin Vidjeskog

 Kayttoliittyma-luokka, joka huolehtii kayttoliittyman piirtamisesta
 ja komentojen vastaanottamisesta ja muiden luokkien toimintojen 
 kutsumisesta.

'''


import sys
from PyQt4 import QtGui
from NappienToiminnot import NappienKuuntelija
from NappainToiminnot import NappainKuuntelija


class Kayttoliittyma(QtGui.QWidget):

    ''' Konstruktori '''

    def __init__(self):
        super(Kayttoliittyma, self).__init__()
        self.__alustaNakyma()
        self.labyrintti = None
        self.hahmo = None
        self.demo = None
        self.tila = 0
        self.nappienKuuntelija = NappienKuuntelija(self)
        self.nappainKuuntelija = NappainKuuntelija(self)
    
    
    
    ''' Private-metodi, joka alustaa kayttoliittyman komponentit '''
    
    def __alustaNakyma(self):
        ''' ikkunan alustaminen '''  
        self.setFixedSize(825, 700)
        self.setAutoFillBackground(True)
        self.setUpdatesEnabled(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#808080"))
        self.setPalette(p)
        self.setWindowTitle("Labyrintti V.0.2.7")
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        ''' kayttoliittyman tekstikentan alustaminen ''' 
        self.textbox = QtGui.QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.move(50, 551)
        self.textbox.resize(725, 125)
        self.textbox.setText("Tervetuloa Labyrintti-pelin pariin.")
        
        ''' labyrintin luonti-napin alustaminen '''
        self.genButton = QtGui.QPushButton("Generoi Labyrintti", self)
        self.genButton.resize(200, 50)
        self.genButton.move(50, 25)
        self.genButton.clicked.connect(lambda: self.buttonClicked())
        
        ''' labyrintin lataus-napin alustaminen ''' 
        self.loadButton = QtGui.QPushButton("Lataa Labyrintti", self)
        self.loadButton.resize(200, 50)
        self.loadButton.move(50, 100)
        self.loadButton.clicked.connect(lambda: self.buttonClicked())
        
        ''' labyrintin tallentamis-napin alustaminen '''
        self.saveButton = QtGui.QPushButton("Tallenna Labyrintti", self)
        self.saveButton.resize(200, 50)
        self.saveButton.move(50, 175)
        self.saveButton.clicked.connect(lambda: self.buttonClicked())
        
        ''' Pelin aloitus-napin alustaminen '''
        self.playButton = QtGui.QPushButton("Pelaa", self)
        self.playButton.resize(200, 50)
        self.playButton.move(50, 250)
        self.playButton.clicked.connect(lambda: self.buttonClicked())
        
        ''' pelin luovutus/demoratkaisu-napin alustaminen '''
        self.demoButton = QtGui.QPushButton("Luovuta ja anna ratkaisu", self)
        self.demoButton.resize(200, 50)
        self.demoButton.move(50, 325)
        self.demoButton.clicked.connect(lambda: self.buttonClicked())
        
        ''' ohejelman info-napin alustaminen'''
        self.infoButton = QtGui.QPushButton("Tietoja ohjelmasta", self)
        self.infoButton.clicked.connect(lambda: self.buttonClicked())
        self.infoButton.resize(200, 50)
        self.infoButton.move(50, 401)
        
        ''' ohjelman lopteus-napin alustaminen '''
        self.exitButton = QtGui.QPushButton("Lopeta", self)
        self.exitButton.clicked.connect(lambda: self.buttonClicked())
        self.exitButton.resize(200, 50)
        self.exitButton.move(50, 476)
        
        ''' labyrintin generointiin liittyva asetusvalikon alustaminen. '''
        
        ''' valikon ensimmainen iso otsikko '''
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        self.label1 = QtGui.QLabel("Valitse labyrintin tyyppi", self)
        self.label1.setFont(font)
        self.label1.move(290, 40)
        self.label1.setVisible(False)
        
        ''' valikon valintaboxien alustaminen '''
        self.checkBox1 = QtGui.QCheckBox("Tavallinen 2DLabyrintti", self)
        self.checkBox1.move(300, 70)
        self.checkBox1.setVisible(False)
        self.checkBox2 = QtGui.QCheckBox("WeaveLabyrintti", self)
        self.checkBox2.move(300, 100)
        self.checkBox2.setVisible(False)
        self.checkBox2.clicked.connect(lambda: self.__vaihdaValintaa())
        self.checkBox1.clicked.connect(lambda: self.__vaihdaValintaa())
        
        ''' valikon labyrintin generointi-nappi'''
        self.generoi = QtGui.QPushButton("Generoi", self)
        self.generoi.clicked.connect(lambda: self.buttonClicked())
        self.generoi.resize(100, 30)
        self.generoi.move(290, 200)
        self.generoi.setStyleSheet("border: 2px solid black")
        self.generoi.setVisible(False)
        
        ''' valikon labyrintin koko-napin alustaminen '''
        self.leveysBox = QtGui.QSpinBox(self)
        self.leveysBox.move(300, 160)
        self.leveysBox.resize(70, 30)
        self.leveysBox.setMinimum(15)
        self.leveysBox.setMaximum(50)
        self.leveysBox.setVisible(False)
        
        ''' valikon toinen iso otsikko '''
        self.label2 = QtGui.QLabel("Anna leveys/korkeus", self)
        self.label2.setFont(font)
        self.label2.move(290, 130)
        self.label2.setVisible(False)
        
        ''' labyrintin kokoon liittyva infobox '''
        self.label3 = QtGui.QLabel("Leveys/korkeus (min = 15, max = 50)", self)
        self.label3.move(380, 170)
        self.label3.setVisible(False)     
          


    ''' Metodi, jota kutsumalla ikkuna kutsutaan nakyviin '''

    def showWindow(self):
        app = QtGui.QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())



    ''' Private-metodi, joka pitaa huolen, etta kahta labyrintin valikkoboksia ei voi painaa samanaikaisesti '''

    def __vaihdaValintaa(self):
        sender = self.sender()
        if(sender.text() == "Tavallinen 2DLabyrintti"):
            self.checkBox1.setChecked(True)
            self.checkBox2.setChecked(False)
        else:
            self.checkBox1.setChecked(False)
            self.checkBox2.setChecked(True)


    
    ''' Metodi, jota kutsumalla labyrintin generointiin liittyva valikko voidaan piilottaa tai kutsua nakyviin '''
    
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



    ''' Metodi jota kutsumalla kayttoliittyma, pelaaja ja demoratkaisu voidaan piirretaa '''

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

   
   
    ''' Metodi, joka rekisteroi nappien klikkailut. Kutsuu nappienKuuntelijaa joka paattaa miten toimia '''
        
    def buttonClicked(self):
        sender = self.sender()
        self.nappienKuuntelija.suoritaNapinToiminnot(sender)



    ''' Metodi, joka rekisteroi nappainten painallukset. Kutsuu nappainKuuntelijaa joka paattaa miten toimia '''

    def keyPressEvent(self, e):
        if(self.tila == 2):
            self.nappainKuuntelija.suoritaNappaimenToiminto(e)
                
                

            
            
            
            
            
            
            
            
            
        