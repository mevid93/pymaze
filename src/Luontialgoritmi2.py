'''
Created on 19 Mar 2016

@author: Martin Vidjeskog

 Tama luokka sisaltaa Weave-labyrinttien luomiseksi suunnitellun algoritmin.
 Algoritmi perustuu "Recursive Backtrack"-algoritmiin. 
 
'''


import random 
from Pala import *

 
class LuoWeaveLabyrintti(object):
    
    ''' Konstruktori, joka saa parametreina labyrintin leveyden ja korkeuden. 
        Konstrukotirssa maaritellaan myos muuttuja, joita tarvitaan palan kuvaamiseen (sijainti ja koko) '''
    
    def __init__(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus
        self.pixelX = 275
        self.pixelY = 25
        self.pixelSivu = int((775-275)/leveys)
        self.lista = [[[] for x in range(leveys)] for x in range(korkeus)]
    
    
    
    ''' Metodi, jota kutsumalla voidaan luoda Weave-labyrintti. Metodissa luodaan aloituspiste
        ja kutsutaan rekursiivista algoritmi-metodia, jolla labyrintin suuntalista saadaan tehtya.
        Taman jalkeen kutsutaan metodia, jolla suuntalistat saadaan muutettua pala-olioiksi. '''
    
    def suoritaLabyrintinLuonti(self):
        #luodaan aloituspiste
        alkuX = int(self.leveys/2)
        alkuY = int(self.korkeus/2)
        #luodaan maalipiste
        valinta = random.randint(0, 1)
        if(valinta == 1):
            maaliX = random.choice([0, self.leveys-1])
            maaliY = random.randint(0, self.korkeus-1)
        else:
            maaliX = random.randint(0, self.leveys-1)
            maaliY = random.choice([0, self.korkeus-1])
        #kutsutaan luontialgoritmia
        self.__recursiveBactracking(alkuX, alkuY, maaliX, maaliY, None)
        #kutsutaan metodia, joka muuttaa suuntalistat pala-olioiksi
        self.__suuntalistatPalalistoiksi(maaliX, maaliY)
        return self.lista




    ''' Private-rekursiivinen algoritmi-metodi, joka luo satunnaisen labyrintin. Algoritmi laittaa muistiin
        suunnat johon "palan" indeksista voidaan siirtya. Algoritmi palauttaa lopulta 2-dimensioisen listan
        joka sisaltaa suunta-listoja. Suuntalistojen perusteella voidaan jokainen lista korvata pala-oliolla. '''

    def __recursiveBactracking(self, x, y, maaliX, maaliY, suunta):
        if(suunta == 'N'):
            self.lista[int(y)][int(x)].append('S')
        if(suunta == 'S'):
            self.lista[int(y)][int(x)].append('N')
        if(suunta == 'E'):
            self.lista[int(y)][int(x)].append('W')
        if(suunta == 'W'):
            self.lista[int(y)][int(x)].append('E')
        directions = ['N', 'S', 'E', 'W']
        random.shuffle(directions, random.random)
        if(x == maaliX and y == maaliY):
            return 
        for i in range(0,4):
            seuraavaX = 0
            seuraavaY = 0
            ylitysX = 0
            ylitysY = 0
            suunta = directions[i]
            if(suunta == 'N'):
                seuraavaX = x
                seuraavaY = y-1
                ylitysX = x
                ylitysY = y-2
            elif(suunta == 'S'):
                seuraavaX = x
                seuraavaY = y+1
                ylitysX = x
                ylitysY = y+2
            elif(suunta == 'E'):
                seuraavaX = x+1
                seuraavaY = y
                ylitysX = x+2
                ylitysY = y
            elif(suunta == 'W'):
                seuraavaX = x-1
                seuraavaY = y
                ylitysX = x-2
                ylitysY = y
            if(seuraavaX < self.leveys and seuraavaX >= 0 and seuraavaY >= 0 and seuraavaY < self.korkeus):
                if not self.lista[int(seuraavaY)][int(seuraavaX)]:
                    self.lista[int(y)][int(x)].append(suunta)
                    self.__recursiveBactracking(seuraavaX, seuraavaY, maaliX, maaliY, suunta)
                elif(ylitysX < self.leveys and ylitysX >= 0 and ylitysY >= 0 and ylitysY < self.korkeus):
                    if not self.lista[int(ylitysY)][int(ylitysX)]:
                        if(self.__sisaltaaSuunnat(self.lista[int(seuraavaY)][int(seuraavaX)], ['W', 'E']) and (suunta == 'N' or suunta == 'S')):
                            self.lista[int(y)][int(x)].append(suunta)
                            self.lista[int(seuraavaY)][int(seuraavaX)] = ['NY', 'SY', 'E', 'W']
                            self.__recursiveBactracking(ylitysX, ylitysY, maaliX, maaliY,suunta)
                        elif(self.__sisaltaaSuunnat(self.lista[int(seuraavaY)][int(seuraavaX)], ['N', 'S']) and (suunta == 'W' or suunta == 'E')):
                            self.lista[int(y)][int(x)].append(suunta)
                            self.lista[int(seuraavaY)][int(seuraavaX)] = ['N', 'S', 'EY', 'WY']
                            self.__recursiveBactracking(ylitysX, ylitysY, maaliX, maaliY, suunta)
        return 



    ''' Private-metodi, jolla jokainen labyrintin indeksi kaydaan lapi ja muutetaan pala-olioksi '''

    def __suuntalistatPalalistoiksi(self, maaliX, maaliY):
        for y in range(self.korkeus):
            for x in range(self.leveys):
                if(y == maaliY and x == maaliX):
                    self.lista[y][x] = MaaliPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['N'], self.lista[y][x])):
                    self.lista[y][x] = PystysuoraAlapaatyPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['E'], self.lista[y][x])):
                    self.lista[y][x] = VaakasuoraVasenPaatyPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['S'], self.lista[y][x])):
                    self.lista[y][x] = PystysuoraYlapaatyPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['W'], self.lista[y][x])):
                    self.lista[y][x] = VaakasuoraOikeaPaatyPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['N', 'E'], self.lista[y][x])):
                    self.lista[y][x] = KaannosNEPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['N', 'S'], self.lista[y][x])):
                    self.lista[y][x] = PystysuoraPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['N', 'W'], self.lista[y][x])):
                    self.lista[y][x] = KaannosNWPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['E', 'S'], self.lista[y][x])):
                    self.lista[y][x] = KaannosSEPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['E', 'W'], self.lista[y][x])):
                    self.lista[y][x] = VaakasuoraPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['S', 'W'], self.lista[y][x])):
                    self.lista[y][x] = KaannosSWPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['N', 'E', 'S'], self.lista[y][x])):
                    self.lista[y][x] = TRisteysOikeallePala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['N', 'E', 'W'], self.lista[y][x])):
                    self.lista[y][x] = TRisteysYlosPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['N', 'W', 'S'], self.lista[y][x])):
                    self.lista[y][x] = TRisteysVasemmallePala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['S', 'W', 'E'], self.lista[y][x])):
                    self.lista[y][x] = TRisteysAlasPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['SY', 'W', 'E', 'NY'], self.lista[y][x])):
                    self.lista[y][x] = YlikulkuPystysuuntaPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                elif(self.__sisaltaaSuunnat(['S', 'WY', 'EY', 'N'], self.lista[y][x])):
                    self.lista[y][x] = YlikulkuVaakasuuntaPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                else:
                    self.lista[y][x] = XRisteysPala(self.pixelX, self.pixelY, self.pixelSivu, self.pixelSivu)
                self.pixelX += self.pixelSivu
            self.pixelX = 275
            self.pixelY += self.pixelSivu
            
            
            
    ''' Private-metodi, joka tarkistaa etta sisaltaako labyrintin x,y indeksissa ollut suunta-lista 
        ne suunnat, jotka vaaditaan tietyn palan muodostamiseen.'''            

    def __sisaltaaSuunnat(self, suunnat, palalista):
        if(len(suunnat) != len(palalista)):
            return False
        for i in suunnat:
            if i not in palalista:
                return False
        return True
