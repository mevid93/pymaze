'''
Created on 5 May 2016

@author: Marski

 Tama luokka sisaltaa testeja tiedoston lataamiselle. Testeilla
 testataan siis Tallentaja-luokan toimintaa. Normaalia toimintaa ei ole
 testattu (tiedetaan etta toimii oikein). Vain virheellisia tiedostoja
 on pyritty testaamaan

'''


import sys
import unittest
from PyQt4 import QtGui
from Tiedostonkasittelija import Lataaja
from Grafiikka import Kayttoliittyma


class TestLataaja(unittest.TestCase):
    
    def test_labyrintinTyyppiEiTuettu(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: EITUETTU", "#Labyrintin leveys: 50\n", "#Labyrintin korkeus: 50\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()
        
    def test_labyrintinTyyppiPuuttuu(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Labyrintin leveys: 50\n", "#Labyrintin korkeus: 50\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()
        
    def test_labyrintinTyyppiEiOleEnsin(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Labyrintin leveys: 50\n", "#Tyyppi: WeaveLabyrintti", "#Labyrintin korkeus: 50\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()
        
    def test_labyrintinLeveysLiianPieni(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Labyrintin leveys: 14\n", "#Labyrintin korkeus: 50\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()        
    
    def test_labyrintinLeveysLiianSuuri(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Labyrintin leveys: 51\n", "#Labyrintin korkeus: 50\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()       
        
    def test_labyrintinKorkeusLiianPieni(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Labyrintin leveys: 50\n", "#Labyrintin korkeus: 14\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()        
    
    def test_labyrintinKorkeusLiianSuuri(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Labyrintin leveys: 50\n", "#Labyrintin korkeus: 51\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()
        
    def test_palanLeveysLiianPieni(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan leveys: 8\n", "#Labyrintin korkeus: 51\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 
        
    def test_palanLeveysLiianSuuri(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan leveys: 35\n", "#Labyrintin korkeus: 51\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 

    def test_palanKorkeusLiianPieni(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 8\n", "#Labyrintin korkeus: 51\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 
        
    def test_palanKorkeusLiianSuuri(self):
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 35\n", "#Labyrintin korkeus: 51\n"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 
        
    def test_virheellinenPalanKoordinaatti1(self):    
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 25", "#Palan leveys: 25", "#Palat:", "a 25: KaannosSEPala", "285 25: VaakasuoraPala"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 
        
    def test_virheellinenPalanKoordinaatti2(self):    
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 25", "#Palan leveys: 25", "#Palat:",  "22 22 25: KaannosSEPala", "285 25: VaakasuoraPala"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()
        
    def test_virheellinenPalanKoordinaatti3(self):    
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 25", "#Palan leveys: 25", "#Palat:", "22 25: KaannosSEPala", "285 25: VaakasuoraPala"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 
        
    def test_virheellinenPalanKoordinaatti4(self):    
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 25", "#Palan leveys: 25", "#Palat:",  "776 40: KaannosSEPala", "285 25: VaakasuoraPala"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 
    
    def test_virheellinenPalanKoordinaatti5(self):    
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 25", "#Palan leveys: 25", "#Palat:", "300 24: KaannosSEPala", "285 25: VaakasuoraPala"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 
        
    def test_virheellinenPalanKoordinaatti6(self):    
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 25", "#Palan leveys: 25", "#Palat:",  "300 530: KaannosSEPala", "285 25: VaakasuoraPala"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit()         
        
    def test_virheellinenPalanTyyppi(self):    
        app = QtGui.QApplication(sys.argv)
        window = Kayttoliittyma()
        lataaja = Lataaja(window)
        tiedosto = ["#Tyyppi: WeaveLabyrintti", "#Palan korkeus: 25", "#Palan leveys: 25", "#Palat:", "275 25: TuntematonPala", "285 25: VaakasuoraPala"]
        self.assertFalse(lataaja.lueTiedostoRiviRivilta(tiedosto))
        app.exit() 
        
        
        

if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    