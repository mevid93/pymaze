'''
Created on 20 Mar 2016

@author: Martin Vidjeskog

 Tanne on toteutettu tiedostonkasittelyyn tarvittavat luokat Tallentaja ja Lataaja.
 Lataaja luokalle oo tehty testeja, mutta Tallentaja on sen verran yksinkertainen luokka, 
 etta sita ei tarvitse testata. Se toimii aina samalla tavalla.

'''


from Labyrintti import *
from Pala import *
import PyQt4.QtGui


class Tallentaja(object):

    ''' Konstruktori, joka saa parametrina kayttoliittyma ikkunan '''

    def __init__(self, window):
        self.window = window
        self.leveys = window.labyrintti.getLeveys()
        self.korkeus = window.labyrintti.getKorkeus()
        self.lista = window.labyrintti.getPalat()
        self.tyyppi = window.labyrintti.getTyyppi()
    
    
    
    ''' Metodi, joka avaa save-file-dialogin ja kirjoittaa tarvittavat tiedot .maze tiedostoon '''
        
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
            file.write("#Palan korkeus: " + str(self.lista[0][0].getH()))
            file.write("\n\n")
            file.write("#Palat: \n")
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    file.write(str(self.lista[y][x].getX()) + " " + str(self.lista[y][x].getY()) + ": " + type(self.lista[y][x]).__name__)
                    file.write("\n")
            file.close()
            




            
            
class Lataaja(object):
    
    ''' Konstruktori, joka saa parametrina kayttoliittyman '''
    
    def __init__(self, window):
        self.window = window
        #lista, joka sisaltaa kaikki tuetut palatyypit
        self.palojenTyypit = ["VaakasuoraPala", "VaakasuoraVasenPaatyPala", "VaakasuoraOikeaPaatyPala", "PystysuoraPala", "PystysuoraYlapaatyPala", "PystysuoraAlapaatyPala"]
        self.palojenTyypit += ["KaannosNEPala", "KaannosSEPala", "KaannosSWPala", "KaannosNWPala", "TRisteysVasemmallePala", "TRisteysYlosPala"]
        self.palojenTyypit += ["TRisteysOikeallePala", "TRisteysAlasPala", "XRisteysPala", "YlikulkuPystysuuntaPala", "YlikulkuVaakasuuntaPala", "MaaliPala"]
        #Tiedostosta tarkistettavat asiat
        self.checkTyyppi = False
        self.checkLeveys = False
        self.checkKorkeus = False
        self.checkPalat = False
        self.checkPalanLeveys = False
        self.checkPalanKorkeus = False
        #Labyrintin tiedot
        self.tyyppi = ""
        self.leveys = -1
        self.korkeus = -1
        self.palanKorkeus = 0
        self.palanLeveys = 0
        self.palalista = []

    
    ''' Metodi, joka avaa open-file-dialogin ja lukee labyrintin tiedot .maze tiedostosta. Virhetilanteille on poikkeukset,
        silla ladattava tiedosto voi olla "rikki". '''
        
    def lataaLabyrintti(self):
        #avataan open-file-dialog ja valitaan tiedosto
        name = PyQt4.QtGui.QFileDialog.getOpenFileName(self.window, 'Open File', filter = '*.maze')
        if(name != '' and name != None):
            #Avaa tiedosto lukemista varten
            file = None
            try:
                file = open(name, 'r')
            except OSError:
                #Tiedosta ei ole olemassa. Ei pitaisi olla koskaan mahdollista
                self.window.textbox.clear()
                self.window.textbox.setText("Tiedostoa ei ole olemassa.")
            else:
                jatka = self.__lueTiedostoRiviRivilta(file)
            file.close()
            #Tarkista etta kaikki tiedot on luettu
            if(jatka != True or self.checkTyyppi != True or self.checkLeveys != True or self.checkKorkeus != True or self.checkPalanLeveys != True or self.checkPalanKorkeus != True):
                return None
            if(self.tyyppi == "WeaveLabyrintti" and len(self.palalista) == self.korkeus*self.leveys):
                lista = self.__palat2Dlistaan()
                return WeaveLabyrintti(self.leveys, self.korkeus, lista)
            if(self.tyyppi == "KaksiDLabyrintti" and len(self.palalista) == self.korkeus*self.leveys):
                lista = self.__palat2Dlistaan()
                return WeaveLabyrintti(self.leveys, self.korkeus, lista)
            return None
        return None
    
    
    
    ''' Private-metodi, jolla luetaan tiedosto rivi rivilta. Lukemisen aikana merkitaan muistiin
        etta tarvittavia tietoja on loydetty tiedostosta. '''
    
    def __lueTiedostoRiviRivilta(self, file):
        #lue tiedoston sisalto
        for line in file:
            osat = line.split(":")
            if len(osat) == 2:
                osat[0] = osat[0].strip()
                osat[1] = osat[1].strip()
                if(osat[0] == "#Tyyppi"):
                    self.tyyppi = osat[1]
                    if(self.tyyppi != "WeaveLabyrintti" and self.tyyppi != "KaksiDLabyrintti"):
                        self.window.textbox.clear()
                        self.window.textbox.setText("Labyrintin Tyyppi ei ole tuettu!")
                        file.close()
                        return False
                    self.checkTyyppi = True
                elif(osat[0] == "#Labyrintin leveys"):
                    self.leveys = self.__stringToInt(osat[1])
                    if(self.leveys < 15 or self.leveys > 50 or self.checkTyyppi == False):             
                        return False
                    self.checkLeveys = True
                elif(osat[0] == "#Labyrintin korkeus"):
                    self.korkeus = self.__stringToInt(osat[1])
                    if(self.korkeus < 15 or self.korkeus > 50 or self.checkTyyppi == False):               
                        return False
                    self.checkKorkeus = True
                elif(osat[0] == "#Palan korkeus"):
                    self.palanKorkeus = self.__stringToInt(osat[1])
                    if(self.palanKorkeus < 9 or self.palanKorkeus > 34 or self.checkTyyppi == False):               
                        return False
                    self.checkPalanKorkeus = True
                elif(osat[0] == "#Palan leveys"):
                    self.palanLeveys = self.__stringToInt(osat[1])
                    if(self.palanLeveys < 9 or self.palanLeveys > 34 or self.checkTyyppi == False):               
                        return False
                    self.checkPalanLeveys = True
                elif(osat[0] == "#Palat"):
                    self.checkPalat = True
                #Tarkoittaa sita etta nyt luetaan palojen dataa. Palojen jarjestyksella ei valia.
                elif(self.checkPalat == True and self.checkPalanLeveys == True and self.checkPalanKorkeus == True):                     
                    palatyyppi = osat[1]
                    if(palatyyppi in self.palojenTyypit):
                        koordinaatit = osat[0].split(" ")
                        if(len(koordinaatit) == 2):
                            x = -1
                            y = -1
                            koordinaatit[0] = koordinaatit[0].strip()
                            koordinaatit[1] = koordinaatit[1].strip()
                            x = self.__stringToInt(koordinaatit[0])
                            y = self.__stringToInt(koordinaatit[1])
                            if(x == -1 or y == -1 ):
                                self.window.textbox.clear()
                                self.window.textbox.setText("Labyrintti sisaltaa virheellisen palan.")
                                return False
                            else:
                                self.palalista.append(self.__luoPala(palatyyppi, x, y, self.palanLeveys, self.palanKorkeus))
                        else:
                            self.window.textbox.clear()
                            self.window.textbox.setText("Labyrintti sisaltaa virheellisen palan.")
                    else:
                        self.window.textbox.clear()
                        self.window.textbox.setText("Labyrintti sisaltaa virheellisen palan.")
                        return False   
            else:
                continue
        #Jos paasty tanne niin labyrintti tiedoston rivit eivat olleet virheellisia 
        return True
        
        
        
    ''' Private-metodi, jolla tiedostosta luettu string tyyppinen luku muutetaan int tyypiksi,
        jos se on mahdollista. Virhetilanteissa palautetaan -1 '''
        
    def __stringToInt(self, strInt):
        try:
            luku = int(strInt)
            return luku
        except ValueError:
            #merkkijono ei ole luku
            return -1
        


    ''' Private-metodi, jolla luetut tiedot muutetaan pala-olioiksi '''
        
    def __luoPala(self, palatyyppi, x, y, w, h):
        if(palatyyppi == "VaakasuoraPala"):
            return VaakasuoraPala(x,y,w,h)
        elif(palatyyppi == "VaakasuoraVasenPaatyPala"):
            return VaakasuoraVasenPaatyPala(x,y,w,h)
        elif(palatyyppi == "VaakasuoraOikeaPaatyPala"):
            return VaakasuoraOikeaPaatyPala(x,y,w,h)
        elif(palatyyppi == "PystysuoraPala"):
            return PystysuoraPala(x,y,w,h)
        elif(palatyyppi == "PystysuoraYlapaatyPala"):
            return PystysuoraYlapaatyPala(x,y,w,h)
        elif(palatyyppi == "PystysuoraAlapaatyPala"):
            return PystysuoraAlapaatyPala(x,y,w,h)
        elif(palatyyppi == "KaannosNEPala"):
            return KaannosNEPala(x,y,w,h)
        elif(palatyyppi == "KaannosSEPala"):
            return KaannosSEPala(x,y,w,h)
        elif(palatyyppi == "KaannosSWPala"):
            return KaannosSWPala(x,y,w,h)
        elif(palatyyppi == "KaannosNWPala"):
            return KaannosNWPala(x,y,w,h)
        elif(palatyyppi == "TRisteysVasemmallePala"):
            return TRisteysVasemmallePala(x,y,w,h)
        elif(palatyyppi == "TRisteysYlosPala"):
            return TRisteysYlosPala(x,y,w,h)
        elif(palatyyppi == "TRisteysOikeallePala"):
            return TRisteysOikeallePala(x,y,w,h)
        elif(palatyyppi == "TRisteysAlasPala"):
            return TRisteysAlasPala(x,y,w,h)
        elif(palatyyppi == "XRisteysPala"):
            return XRisteysPala(x,y,w,h)
        elif(palatyyppi == "YlikulkuPystysuuntaPala"):
            return YlikulkuPystysuuntaPala(x,y,w,h)
        elif(palatyyppi == "YlikulkuVaakasuuntaPala"):
            return YlikulkuVaakasuuntaPala(x,y,w,h)
        elif(palatyyppi == "MaaliPala"):
            return MaaliPala(x,y,w,h)
        
        
    
    ''' Private-metodi, jolla luetut palat siirretaan listasta 2-dimensioiseen listaan,
        jollaista labyrintti luokka kayttaa '''
       
    def __palat2Dlistaan(self):
        lista = [[0 for x in range(self.leveys)] for x in range(self.korkeus)]
        sija = 0
        for j in range(self.korkeus):
            for i in range(self.leveys):
                lista[j][i] = self.palalista[sija]
                sija += 1         
        return lista
        
        