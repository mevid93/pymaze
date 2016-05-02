'''
Created on 2 May 2016

@author: Marski
'''


from PyQt4 import QtCore


class NappainKuuntelija(object):
    '''
    Luokka, joka sisaltaa komennot, jotka suoritetaan kun nappaimia painetaa. 
    (Pelaajan liikuttamiseen suunniteltu logiikka).
    '''

    def __init__(self, window):
        self.window = window
    
    
    
    def suoritaNappaimenToiminto(self, e):
        x, y = self.window.hahmo.getSijainti()
        liikuta = 1
        if (e.key() == QtCore.Qt.Key_W):
            self.liikuYlosKomento(x, y, liikuta)
        elif(e.key() == QtCore.Qt.Key_S):
            self.liikuAlasKomento(x, y, liikuta)
        elif(e.key() == QtCore.Qt.Key_A):
            self.liikuVasemmalleKomento(x, y, liikuta)
        elif(e.key() == QtCore.Qt.Key_D):
            self.liikuOikealleKomento(x, y, liikuta)
        x, y = self.window.hahmo.getSijainti()
        if(type(self.window.labyrintti.getPala(x,y)).__name__ == "MaaliPala"):
            self.maaliKomento()  
    
    
    
    def liikuYlosKomento(self, x, y, liikuta):
        if(y > 0 and self.window.labyrintti.getPala(x, y).voiLiikkuaYlos()):
            while(type(self.window.labyrintti.getPala(x, y-liikuta)).__name__ == "YlikulkuVaakasuuntaPala"):
                liikuta += 1
            y = y - liikuta 
            pala = self.window.labyrintti.getPala(x, y)
            self.window.hahmo.liikutaHahmoa(pala, x, y)
            self.window.update()



    def liikuAlasKomento(self, x, y, liikuta):
        if(y < self.window.labyrintti.getKorkeus()-1 and self.window.labyrintti.getPala(x, y).voiLiikkuaAlas()):
            while(type(self.window.labyrintti.getPala(x, y+liikuta)).__name__ == "YlikulkuVaakasuuntaPala"):
                liikuta += 1
            y = y + liikuta 
            pala = self.window.labyrintti.getPala(x, y)
            self.window.hahmo.liikutaHahmoa(pala, x, y)
            self.window.update()
    
    
    
    def liikuVasemmalleKomento(self, x, y, liikuta):
        if(x > 0 and self.window.labyrintti.getPala(x, y).voiLiikkuaVasemmalle()):
            while(type(self.window.labyrintti.getPala(x-liikuta, y)).__name__ == "YlikulkuPystysuuntaPala"):
                liikuta += 1
            x = x - liikuta 
            pala = self.window.labyrintti.getPala(x, y)
            self.window.hahmo.liikutaHahmoa(pala, x, y)
            self.window.update()



    def liikuOikealleKomento(self, x, y, liikuta):
        if(x < self.window.labyrintti.getLeveys()-1 and self.window.labyrintti.getPala(x, y).voiLiikkuaOikealle()):
            while(type(self.window.labyrintti.getPala(x+liikuta, y)).__name__ == "YlikulkuPystysuuntaPala"):
                liikuta += 1
            x = x + liikuta 
            pala = self.window.labyrintti.getPala(x, y)
            self.window.hahmo.liikutaHahmoa(pala, x, y)
            self.window.update()



    def maaliKomento(self):
        self.window.tila = 1
        self.window.textbox.clear()
        self.window.textbox.setText("SELVITIT LABYRINTIN!!")


    
    