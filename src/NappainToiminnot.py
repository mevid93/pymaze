'''
Created on 2 May 2016

@author: Marski

 Luokka, joka sisaltaa komennot, jotka suoritetaan kun nappaimia painetaa. 
 (Pelaajan liikuttamiseen suunniteltu pelilogiikka). Pelaajan liikuttaminen
 on mahdollista vain pelitilassa, jolloin pelaaja on piirrettyna kayttoliittymassa
 olevaan labyrinttiin. 

'''


from PyQt4 import QtCore


class NappainKuuntelija(object):
    
    '''
    Konstruktori, joka saa parametrina kayttoliittyman ikkunan.
    '''

    def __init__(self, window):
        self.window = window
    
    
    
    ''' Meotodi, joka selvittaa mita nappainta on painettu ja kutsuu sen perusteella liikuttamista
        varten suunniteltuja metodeja.'''
    
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
    


    ''' Metodi, joka liikuttaa pelaajaa labyrintissa ylospain, mikali siirtyma on sallittu. '''
    
    def liikuYlosKomento(self, x, y, liikuta):
        if(y > 0 and self.window.labyrintti.getPala(x, y).voiLiikkuaYlos()):
            while(type(self.window.labyrintti.getPala(x, y-liikuta)).__name__ == "YlikulkuVaakasuuntaPala"):
                liikuta += 1
            y = y - liikuta 
            pala = self.window.labyrintti.getPala(x, y)
            self.window.hahmo.liikutaHahmoa(pala, x, y)
            self.window.update()



    ''' Metodi, joka liikuttaa pelaajaa alaspain, mikali siirtyma on sallittu. '''

    def liikuAlasKomento(self, x, y, liikuta):
        if(y < self.window.labyrintti.getKorkeus()-1 and self.window.labyrintti.getPala(x, y).voiLiikkuaAlas()):
            while(type(self.window.labyrintti.getPala(x, y+liikuta)).__name__ == "YlikulkuVaakasuuntaPala"):
                liikuta += 1
            y = y + liikuta 
            pala = self.window.labyrintti.getPala(x, y)
            self.window.hahmo.liikutaHahmoa(pala, x, y)
            self.window.update()
    
    
    
    ''' Metodi, joka liikuttaa pelaajaa vasemmalle, mikali siirtyma on sallittu. '''
    
    def liikuVasemmalleKomento(self, x, y, liikuta):
        if(x > 0 and self.window.labyrintti.getPala(x, y).voiLiikkuaVasemmalle()):
            while(type(self.window.labyrintti.getPala(x-liikuta, y)).__name__ == "YlikulkuPystysuuntaPala"):
                liikuta += 1
            x = x - liikuta 
            pala = self.window.labyrintti.getPala(x, y)
            self.window.hahmo.liikutaHahmoa(pala, x, y)
            self.window.update()



    ''' Metodi, joka liikuttaa pelaajaa oikealle, mikali siirtyma on sallittu. '''

    def liikuOikealleKomento(self, x, y, liikuta):
        if(x < self.window.labyrintti.getLeveys()-1 and self.window.labyrintti.getPala(x, y).voiLiikkuaOikealle()):
            while(type(self.window.labyrintti.getPala(x+liikuta, y)).__name__ == "YlikulkuPystysuuntaPala"):
                liikuta += 1
            x = x + liikuta 
            pala = self.window.labyrintti.getPala(x, y)
            self.window.hahmo.liikutaHahmoa(pala, x, y)
            self.window.update()



    ''' Metodi, joka suoritetaan kun pelaaja saavuttaa maaliruudun. Pelitila vaihtuu pois jne. '''

    def maaliKomento(self):
        self.window.tila = 1
        self.window.textbox.clear()
        self.window.textbox.setText("SELVITIT LABYRINTIN!!")


    
    