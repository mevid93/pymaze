'''
Created on 2 May 2016

@author: Marski

 Luokka, joka sisaltaa kayttoliittyman nappien toimintalogiikan.
 Jokaiselle komennolle on oma metodi, jota kutstuaan aina kun nappia painetaan.
 Nappeja ei voi kuitenkaan aina painaa, vaan toiminnon suorittaminen riippuu myos 
 ohjelman tilasta. Esim. Pelitilassa labyrinttia ei voi tallentaa ennen kuin peli 
 on pelattu loppuun, tai on painettu luovutus nappia.
    
'''


import sys
from Tiedostonkasittelija import Tallentaja
from Tiedostonkasittelija import Lataaja
from Pelaaja import Hahmo
from Labyrintti import WeaveLabyrintti
from Labyrintti import KaksiDLabyrintti
from Ratkaisualgoritmi1 import WallFollower


class NappienKuuntelija(object):
    
    '''
    Konstruktori, joka saa parametrina kayttoliittyma-ikkunan. 
    '''

    def __init__(self, window):
        self.window = window
             
    
    
    ''' Metodi joka tunnistaa mita nappia on painettu ja kutsuu sen perusteella komento-metodeja '''    
        
    def suoritaNapinToiminnot(self, sender):
        if(sender.text() == "Generoi Labyrintti" and self.window.tila != 2):
            self.generoiLabyrinttiKomento()
        if(sender.text() == "Tietoja ohjelmasta" and self.window.tila != 2):
            self.tietojaOhjelmastaKomento()
        if(sender.text() == "Pelaa" and self.window.labyrintti != None):
            self.pelaaKomento()
        if(sender.text() == "Lopeta"):
            sys.exit()
        if(sender.text() == "Tallenna Labyrintti" and self.window.tila != 2 and self.window.labyrintti != None):
            self.tallennaLabyrinttiKomento()
        if(sender.text() == "Lataa Labyrintti" and self.window.tila != 2):
            self.lataaLabyrinttiKomento()
        if(sender.text() == "Luovuta ja anna ratkaisu" and self.window.tila == 2):
            self.luovutusKomento()
        if(sender.text() == "Generoi" and self.window.tila != 2):
            self.generoiKomento()



    ''' Metodi, joka asettaa labyrintin generointiin liittyvan asetusalikon nakyville '''

    def generoiLabyrinttiKomento(self):
        self.window.tila = 0
        self.window.labyrintti = None
        self.window.update()
        if not(self.window.label1.isVisible()):
            self.window.asetusvalikko()
                    
    
    
    ''' Metodi, joka asettaa tekstikentan sisalloksi pelin tiedot ja ohjeet '''
            
    def tietojaOhjelmastaKomento(self):
        self.window.textbox.clear()
        self.window.textbox.setText("Labyrintti-peli V.0.2.5\n")
        self.window.textbox.append("Ohjelma on tehty Aalto-yliopiston kurssin Ohjelmoinnin peruskurssi Y2 suorittamiseksi.")
        self.window.textbox.append("Ohjelman lahdekoodi on vapaasti saatavissa GitHubista.")
        self.window.textbox.append("GitHub:  https://github.com/mevid93/PythonY2Labyrintti.git")
        self.window.textbox.append("Ohjelmoija: Martin Vidjeskog")
        self.window.textbox.append("\n")
        self.window.textbox.append("Ohjeet:")
        self.window.textbox.append("1. Lataa tai luo ensin labyrintti.")
        self.window.textbox.append("2. Paina pelaa nappia.")
        self.window.textbox.append("3. Yrita ohjata punainen nelio vihreaan ruutuun.")
        self.window.textbox.append("  W = liiku ylos")
        self.window.textbox.append("  S = liiku alas")
        self.window.textbox.append("  A = liiku vasemmalle")
        self.window.textbox.append("  D = liiku oikealle")
        self.window.textbox.append("4. Voit lopettaa ja saada esimerkkiratkaisun painamalla \" Luovuta ja anna ratkaisu\"-nappia.")
        self.window.textbox.append("5. Labyrintin voi tallentaa painamalla \"Tallenna labyrintti\"-nappia")
        self.window.textbox.append("6. \"Lopeta\"-nappi sammuttaa sovelluksen.")



    ''' Metodi, joka kaynnistaa pelitilan. Hahmo asetetaan labyrintin keskelle, tekstikentan teksi vaihdetaan ja hahmon liikuttaminen 
        nappaimiston syotteilla on mahdollista. '''
    
    def pelaaKomento(self):
        self.window.tila = 2
        x = int(self.window.labyrintti.getLeveys()/2)-1
        y = int(self.window.labyrintti.getKorkeus()/2)-1
        self.window.hahmo = Hahmo(self.window.labyrintti.getPala(x, y), x, y)
        self.window.textbox.clear()
        self.window.textbox.setText("PELI ON KAYNNISSA! Etsi reitti ulos labyrintista.\nVoit aina luovuttaa jos et keksi ratkaisua.")
        self.window.update()    
        
    
    
    ''' Metodi, jonka avulla kutsutaan save-file valikko. Labyrintti voidaan tallentaa .maze-tiedostoon. '''    
        
    def tallennaLabyrinttiKomento(self):
        tallentaja = Tallentaja(self.window, self.window.labyrintti)
        tallentaja.tallennaLabyrintti()
        
    
    
    ''' Metodi, jonka avulla kutsutaan open-file dialog. Labyrintti voidaan ladata .maze-tiedostosta. '''
        
    def lataaLabyrinttiKomento(self):
        lataaja = Lataaja(self.window)
        labyrintti = lataaja.lataaLabyrintti()
        if(labyrintti != None):
            self.window.labyrintti = labyrintti
            if (self.window.label1.isVisible()):
                self.window.asetusvalikko()
            self.window.tila = 1
            self.window.update()
            self.window.textbox.clear()
            self.window.textbox.setText("Labyrintin lataus onnistui.")
        
    
    
    ''' Metodi, jonka avulla peli voidaan luovuttaa ja samalla esitetaan demoratkaisu. '''    
        
    def luovutusKomento(self):    
        self.window.tila = 1
        self.window.update()
        self.window.tila = 3
        self.window.demo = WallFollower(self.window, self.window.labyrintti)
        self.window.demo.selvitaReitti()
        self.window.update()
        self.window.textbox.clear()
        self.window.textbox.setText("Luovutit. Tassa esimerkkiratkaisu.")
    
    
    
    ''' Asetuvalikon generoi-napppiin liitttyva metodi, jota painettaessa labyrintti luodaan ja asetetaan nakyviin'''
    
    def generoiKomento(self):
        leveys = self.window.leveysBox.value()
        korkeus = leveys
        if(self.window.checkBox2.isChecked()):
            self.window.labyrintti = WeaveLabyrintti(leveys, korkeus)
            self.window.asetusvalikko()
            self.window.tila = 1
            self.window.update()
        if(self.window.checkBox1.isChecked()):
            self.window.labyrintti = KaksiDLabyrintti(leveys, korkeus)
            self.window.asetusvalikko()
            self.window.tila = 1
            self.window.update()
    
    
    
        
        
        