'''
Created on 13 Apr 2016

@author: Marski

 Ratkaisualgoritmi-luokka. Luokka osaa ratkaista kaikki satunnaisesti generoidut labyrintit.
 Algoritmi on yksinkertainen "WallFollower". Luokka osaa oikean reitin etsimisen lisaksi 
 piirtaa sen kayttoliittymaan (punainen viiva lahtopisteesta maaliin).

'''

from Labyrintti import *
from Pala import *


class WallFollower(object):
    
    ''' Konstruktori, joka saa parametrina kayttoliittyman ikkunan '''
    
    def __init__(self, window):
        self.window = window
        self.labyrintti = window.labyrintti
        self.palalista = []
        self.x = 0
        self.y = 0
        self.suunta = "N"
    
    ''' Metodi, joka selvittaa oikean reitin labyrintissa '''
        
    def selvitaReitti(self):
        # Asetetaan aloituspala ja suunta johon lahdetaan kulkemaan
        self.x = int(self.labyrintti.getLeveys()/2) -1
        self.y = int(self.labyrintti.getKorkeus()/2) -1
        if(type(self.labyrintti.getPala(self.x, self.y)).__name__ == "YlikulkuVaakasuuntaPala"):
            self.suunta = "E"
        # palalistaan laitetaan muistiin kaikki palat, jossa kaydaan ennen maalipalaa
        self.palalista.append(self.labyrintti.getPala(self.x, self.y))
        # Jatketaan suunnan valitsemista ja palojen muistiin laittamista niin kauan kunnes paastaan maaliin
        while(type(self.labyrintti.getPala(self.x, self.y)).__name__ != "MaaliPala"):
            pala = self.__valitseSuuntaJaLiiku()
            self.__palassaVierailtuToimenpiteet(pala)
    
    
    
    ''' Private-metodi, joka valitsee suunnan johon seuraavaksi liikutaan ja siirtaa tarkastelun tahan uuteen sijaintiin.
        Palauttaa palan, uudesta sijainnista. '''
    
    def __valitseSuuntaJaLiiku(self):
        tyyppi = type(self.labyrintti.getPala(self.x, self.y)).__name__ 
        if(tyyppi == "YlikulkuPystysuuntaPala" or tyyppi == "YlikulkuVaakasuuntaPala"):
            if(self.suunta == "N"):
                self.y = self.y-1
            elif(self.suunta == "W"):
                self.x = self.x-1
            elif(self.suunta == "S"):
                self.y = self.y+1
            else:
                self.x = self.x+1
        elif(self.suunta == "N"):
            if(self.labyrintti.getPala(self.x, self.y).voiLiikkuaOikealle()):
                self.x = self.x+1
                self.suunta = "E"
            elif(self.labyrintti.getPala(self.x, self.y).voiLiikkuaYlos()):
                self.y = self.y-1
            elif(self.labyrintti.getPala(self.x, self.y).voiLiikkuaVasemmalle()):
                self.x = self.x-1
                self.suunta = "W"
            else:
                self.suunta = "S"
                self.y = self.y+1
        elif(self.suunta == "W"):
            if(self.labyrintti.getPala(self.x, self.y).voiLiikkuaYlos()):
                self.y = self.y-1
                self.suunta = "N"
            elif(self.labyrintti.getPala(self.x, self.y).voiLiikkuaVasemmalle()):
                self.x = self.x-1
            elif(self.labyrintti.getPala(self.x, self.y).voiLiikkuaAlas()):
                self.y = self.y+1
                self.suunta = "S"
            else:
                self.suunta = "E"
                self.x = self.x+1
        elif(self.suunta == "S"):
            if(self.labyrintti.getPala(self.x, self.y).voiLiikkuaVasemmalle()):
                self.x = self.x-1
                self.suunta = "W"
            elif(self.labyrintti.getPala(self.x, self.y).voiLiikkuaAlas()):
                self.y = self.y+1
            elif(self.labyrintti.getPala(self.x, self.y).voiLiikkuaOikealle()):
                self.x = self.x+1
                self.suunta = "E"
            else:
                self.y = self.y-1
                self.suunta = "N"         
        elif(self.suunta == "E"):
            if(self.labyrintti.getPala(self.x, self.y).voiLiikkuaAlas()):
                self.y = self.y+1
                self.suunta = "S"
            elif(self.labyrintti.getPala(self.x, self.y).voiLiikkuaOikealle()):
                self.x = self.x+1
            elif(self.labyrintti.getPala(self.x, self.y).voiLiikkuaYlos()):
                self.y = self.y-1
                self.suunta = "N"
            else:
                self.suunta = "W"
                self.x = self.x-1
        return self.labyrintti.getPala(self.x, self.y)
    
    
    
    ''' Private-metodi, joka suorittaa tarvittavat toimenpiteet, jos pala johon siirryttiin on jo vierailtujen palojen listassa ''' 
    
    def __palassaVierailtuToimenpiteet(self, pala):
        tyyppi = type(pala).__name__ 
        if(pala in self.palalista):
            if(tyyppi == "YlikulkuPystysuuntaPala" or tyyppi == "YlikulkuVaakasuuntaPala"):
                vieruspalat = []
                vieruspalat.append(self.labyrintti.getPala(self.x-1, self.y))
                vieruspalat.append(self.labyrintti.getPala(self.x+1, self.y))
                vieruspalat.append(self.labyrintti.getPala(self.x, self.y-1))
                vieruspalat.append(self.labyrintti.getPala(self.x, self.y+1))
                kpl = 0
                for vieruspala in vieruspalat:
                    if(vieruspala in self.palalista):
                        kpl += 1
                if(kpl == 1):
                    index = self.__rindex(self.palalista, pala)
                    self.palalista = self.palalista[0:index+1]
                if(kpl == 2 and (vieruspalat[0] in self.palalista) and (vieruspalat[1] in self.palalista)):
                    index = self.__rindex(self.palalista, pala)
                    self.palalista = self.palalista[0:index+1]
                elif(kpl == 2 and len(vieruspalat) == 4 and (vieruspalat[2] in self.palalista) and (vieruspalat[3] in self.palalista)):
                    index = self.__rindex(self.palalista, pala)
                    self.palalista = self.palalista[0:index+1]
                elif(kpl == 4):
                    index = self.__rindex(self.palalista, pala)
                    self.palalista = self.palalista[0:index+1]
                else:
                    self.palalista.append(pala)
            else:
                index = self.__rindex(self.palalista, pala)
                self.palalista = self.palalista[0:index+1]
        else:
            self.palalista.append(pala)
            
            
    
    ''' Private-metodi, joka palauttaa viimeisen indeksin listassa, joka sisaltaa haettavan arvon '''            

    def __rindex(self, hakuLista, haettavaArvo):
        return len(hakuLista) - hakuLista[::-1].index(haettavaArvo) - 1



    ''' Metodi, joka piirtaa demoreitin kayttoliittymaan '''
    
    def piirraReitti(self):
        painter = QtGui.QPainter()
        painter.begin(self.window)
        painter.setPen(QtCore.Qt.red)
        for i in range(0, len(self.palalista)-1):
            x1, y1 = self.palalista[i].getKeskipiste()
            x2, y2 = self.palalista[i+1].getKeskipiste()
            painter.drawLine(x1, y1, x2, y2)
        painter.end()
    