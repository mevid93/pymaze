'''
Created on 20 Mar 2016

@author: Martin Vidjeskog
'''


from Labyrintti import *
from Pala import *
import PyQt4.QtGui

class Tallentaja(object):

    def __init__(self, window, labyrintti):
        self.window = window
        self.leveys = labyrintti.getLeveys()
        self.korkeus = labyrintti.getKorkeus()
        self.lista = labyrintti.getPalat()
        self.tyyppi = labyrintti.getTyyppi()
        
    def tallennaLabyrintti(self):
        name = PyQt4.QtGui.QFileDialog.getSaveFileName(self.window, 'Save File', filter = '*.maze')
        if(name != '' and name != None):
            file = open(name, 'w')
            file.write("#Tyyppi: " + self.tyyppi)
            file.write("\n\n")
            file.write("#Labyrintin leveys: " + str(self.leveys))
            file.write("\n\n")
            file.write("#Labyrintin korkeus: " + str(self.korkeus))
            file.write("\n\n")
            file.write("#Palan leveys: " + str(self.lista[0][0].getW()))
            file.write("\n\n")
            file.write("#Palan korkeus: " + str(self.lista[0][0].getY()))
            file.write("\n\n")
            file.write("#Palat: \n")
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    file.write(str(self.lista[y][x].getX()) + " " + str(self.lista[y][x].getY()) + ": " + type(self.lista[y][x]).__name__)
                    file.write("\n")
            file.close()
            
            
            
class Lataaja(object):
    
    def __init__(self, window):
        self.window = window
        
    def lataaLabyrintti(self):
        
        palojenTyypit = ["VaakasuoraPala", "VaakasuoraVasenPaatyPala", "VaakasuoraOikeaPaatyPala", "PystysuoraPala", "PystysuoraYlapaatyPala", "PystysuoraAlapaatyPala"]
        palojenTyypit += ["KaannosNEPala", "KaannosSEPala", "KaannosSWPala", "KaannosNWPala", "TRisteysVasemmallePala", "TRisteysYlosPala"]
        palojenTyypit += ["TRisteysOikeallePala", "TRisteysAlasPala", "XRisteysPala", "YlikulkuPystysuuntaPala", "YlikulkuVaakasuuntaPala", "MaaliPala"]
        
        name = PyQt4.QtGui.QFileDialog.getOpenFileName(self.window, 'Open File', filter = '*.maze')
        if(name != '' and name != None):
            file = None
            checkTyyppi = False
            checkLeveys = False
            checkKorkeus = False
            checkPalat = False
            checkPalanLeveys = True         #Merkitaan tosiksi nyt testausvaiheessa
            checkPalanKorkeus = True
            tyyppi = ""
            leveys = -1
            korkeus = -1
            palalista = []
            try:
                file = open(name, 'r')
            except OSError:
                #Tiedosta ei ole olemassa. Ei mahdollista milloinkaan :)
                self.window.textbox.clear()
                self.window.textbox.setText("Tiedostoa ei ole olemassa.")
            else:
                for line in file:
                    osat = line.split(":")
                    if len(osat) == 2:
                        osat[0] = osat[0].strip()
                        osat[1] = osat[1].strip()
                        if(osat[0] == "#Tyyppi"):
                            tyyppi = osat[1]
                            if(tyyppi != "WeaveLabyrintti" and tyyppi != "KaksiDLabyrintti"):
                                self.window.textbox.clear()
                                self.window.textbox.setText("Labyrintin Tyyppi ei ole tuettu!")
                                file.close()
                                return None
                            checkTyyppi = True
                        elif(osat[0] == "#Labyrintin leveys"):
                            leveys = self.stringToInt(osat[1])
                            if(leveys < 10 or checkTyyppi == False):               #labyrintin minimileveys 10 ruutua! ja tyyppi on oltava luettu ensin
                                return None
                            checkLeveys = True
                        elif(osat[0] == "#Labyrintin korkeus"):
                            korkeus = self.stringToInt(osat[1])
                            if(korkeus < 10 or checkTyyppi == False):               #labyrintin minimikorkeus 10 ruutua! ja tyyppi on oltava luettu ensin
                                return None
                            checkKorkeus = True
                        elif(osat[0] == "#Palat"):
                            checkPalat = True
                        elif(checkPalat == True):                     #Tarkoittaa sita etta nyt luetaan palojen dataa. Palojen jarjestyksella ei valia.
                            palatyyppi = osat[1]
                            if(palatyyppi in palojenTyypit):
                                koordinaatit = osat[0].split(" ")
                                if(len(koordinaatit) == 2):
                                    x = -1
                                    y = -1
                                    koordinaatit[0] = koordinaatit[0].strip()
                                    koordinaatit[1] = koordinaatit[1].strip()
                                    x = self.stringToInt(koordinaatit[0])
                                    y = self.stringToInt(koordinaatit[1])
                                    if(x == -1 or y == -1 ):
                                        self.window.textbox.clear()
                                        self.window.textbox.setText("Labyrintti sisaltaa virheellisen palan.")
                                        return None
                                    else:
                                        palalista.append(self.luoPala(palatyyppi, x, y))
                                else:
                                    self.window.textbox.clear()
                                    self.window.textbox.setText("Labyrintti sisaltaa virheellisen palan.")
                            else:
                                self.window.textbox.clear()
                                self.window.textbox.setText("Labyrintti sisaltaa virheellisen palan.")
                                return None
                            
                    else:
                        continue
            file.close()
            if(checkTyyppi != True or checkLeveys != True or checkKorkeus != True or checkPalanLeveys != True or checkPalanKorkeus != True):
                return None
            if(tyyppi == "WeaveLabyrintti" and len(palalista) == korkeus*leveys):
                lista = [[0 for x in range(leveys)] for x in range(korkeus)]
                sija = 0
                for j in range(korkeus):
                    for i in range(leveys):
                        lista[j][i] = palalista[sija]
                        sija += 1 
                return WeaveLabyrintti(leveys, korkeus, lista)
            if(tyyppi == "KaksiDLabyrintti" and len(palalista) == korkeus*leveys):
                lista = [[0 for x in range(leveys)] for x in range(korkeus)]
                sija = 0
                for j in range(korkeus):
                    for i in range(leveys):
                        lista[j][i] = palalista[sija]
                        sija += 1 
                return WeaveLabyrintti(leveys, korkeus, lista)
            return None
        return None
        
        
    def stringToInt(self, strInt):
        try:
            luku = int(strInt)
            return luku
        except ValueError:
            #merkkijono ei ole luku
            return -1
        
        
    def luoPala(self, palatyyppi, x, y):
        if(palatyyppi == "VaakasuoraPala"):
            return VaakasuoraPala(x,y, 25, 25)
        elif(palatyyppi == "VaakasuoraVasenPaatyPala"):
            return VaakasuoraVasenPaatyPala(x,y, 25, 25)
        elif(palatyyppi == "VaakasuoraOikeaPaatyPala"):
            return VaakasuoraOikeaPaatyPala(x,y, 25, 25)
        elif(palatyyppi == "PystysuoraPala"):
            return PystysuoraPala(x,y, 25, 25)
        elif(palatyyppi == "PystysuoraYlapaatyPala"):
            return PystysuoraYlapaatyPala(x,y, 25, 25)
        elif(palatyyppi == "PystysuoraAlapaatyPala"):
            return PystysuoraAlapaatyPala(x,y, 25, 25)
        elif(palatyyppi == "KaannosNEPala"):
            return KaannosNEPala(x,y, 25, 25)
        elif(palatyyppi == "KaannosSEPala"):
            return KaannosSEPala(x,y, 25, 25)
        elif(palatyyppi == "KaannosSWPala"):
            return KaannosSWPala(x,y, 25, 25)
        elif(palatyyppi == "KaannosNWPala"):
            return KaannosNWPala(x,y, 25, 25)
        elif(palatyyppi == "TRisteysVasemmallePala"):
            return TRisteysVasemmallePala(x,y, 25, 25)
        elif(palatyyppi == "TRisteysYlosPala"):
            return TRisteysYlosPala(x,y, 25, 25)
        elif(palatyyppi == "TRisteysOikeallePala"):
            return TRisteysOikeallePala(x,y, 25, 25)
        elif(palatyyppi == "TRisteysAlasPala"):
            return TRisteysAlasPala(x,y, 25, 25)
        elif(palatyyppi == "XRisteysPala"):
            return XRisteysPala(x,y, 25, 25)
        elif(palatyyppi == "YlikulkuPystysuuntaPala"):
            return YlikulkuPystysuuntaPala(x,y, 25, 25)
        elif(palatyyppi == "YlikulkuVaakasuuntaPala"):
            return YlikulkuVaakasuuntaPala(x,y, 25, 25)
        elif(palatyyppi == "MaaliPala"):
            return MaaliPala(x,y, 25, 25)
         
        
        