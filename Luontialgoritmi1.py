'''
Created on 5 Mar 2016

@author: Martin Vidjeskog

Tama moduuli sisaltaa 2D labyrinttien luomiseksi suunnitellun algoritmin.
'''


import random 
from Pala import *
 
def luo2Dlabyrintti(leveys, korkeus):
    pixelX = 275
    pixelY = 25
    pixelSivu = int((775-275)/leveys)
    lista = [[[] for x in range(leveys)] for x in range(korkeus)]
    #luodaan aloituspiste melko tarkasti keskelle labyrinttia 
    alkuX = int(leveys/2)
    alkuY = int(korkeus/2)
    #luodaan piste maalille johonkin labyrintin reunallle
    valinta = random.randint(0, 1)
    if(valinta == 1):
        maaliX = random.choice([0, leveys-1])
        maaliY = random.randint(0, korkeus-1)
    else:
        maaliX = random.randint(0, leveys-1)
        maaliY = random.choice([0, korkeus-1])
    lista = recursiveBactracking(leveys, korkeus, alkuX, alkuY, maaliX, maaliY, lista, None)
    for y in range(korkeus):
        for x in range(leveys):
            if(y == maaliY and x == maaliX):
                lista[y][x] = MaaliPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['N'], lista[y][x])):
                lista[y][x] = PystysuoraAlapaatyPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['E'], lista[y][x])):
                lista[y][x] = VaakasuoraVasenPaatyPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['S'], lista[y][x])):
                lista[y][x] = PystysuoraYlapaatyPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['W'], lista[y][x])):
                lista[y][x] = VaakasuoraOikeaPaatyPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['N', 'E'], lista[y][x])):
                lista[y][x] = KaannosNEPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['N', 'S'], lista[y][x])):
                lista[y][x] = PystysuoraPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['N', 'W'], lista[y][x])):
                lista[y][x] = KaannosNWPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['E', 'S'], lista[y][x])):
                lista[y][x] = KaannosSEPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['E', 'W'], lista[y][x])):
                lista[y][x] = VaakasuoraPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['S', 'W'], lista[y][x])):
                lista[y][x] = KaannosSWPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['N', 'E', 'S'], lista[y][x])):
                lista[y][x] = TRisteysOikeallePala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['N', 'E', 'W'], lista[y][x])):
                lista[y][x] = TRisteysYlosPala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['N', 'W', 'S'], lista[y][x])):
                lista[y][x] = TRisteysVasemmallePala(pixelX, pixelY, pixelSivu, pixelSivu)
            elif(sisaltaaSuunnat(['S', 'W', 'E'], lista[y][x])):
                lista[y][x] = TRisteysAlasPala(pixelX, pixelY, pixelSivu, pixelSivu)
            else:
                lista[y][x] = XRisteysPala(pixelX, pixelY, pixelSivu, pixelSivu)
            pixelX += pixelSivu
        pixelX = 275
        pixelY += pixelSivu

    return lista


def recursiveBactracking(leveys, korkeus, x, y, maaliX, maaliY, lista, suunta):
    if(suunta == 'N'):
        lista[int(y)][int(x)].append('S')
    if(suunta == 'S'):
        lista[int(y)][int(x)].append('N')
    if(suunta == 'E'):
        lista[int(y)][int(x)].append('W')
    if(suunta == 'W'):
        lista[int(y)][int(x)].append('E')
    directions = ['N', 'S', 'E', 'W']
    random.shuffle(directions, random.random)
    if(x == maaliX and y == maaliY):
        return lista
    for i in range(0,4):
        seuraavaX = 0
        seuraavaY = 0
        suunta = directions[i]
        if(suunta == 'N'):
            seuraavaX = x
            seuraavaY = y-1
        elif(suunta == 'S'):
            seuraavaX = x
            seuraavaY = y+1
        elif(suunta == 'E'):
            seuraavaX = x+1
            seuraavaY = y
        elif(suunta == 'W'):
            seuraavaX = x-1
            seuraavaY = y
        if(seuraavaX < leveys and seuraavaX >= 0 and seuraavaY >= 0 and seuraavaY < korkeus):
            if not lista[int(seuraavaY)][int(seuraavaX)]:
                lista[int(y)][int(x)].append(suunta)
                lista = recursiveBactracking(leveys, korkeus, seuraavaX, seuraavaY, maaliX, maaliY, lista, suunta)
    return lista


def sisaltaaSuunnat(suunnat, palalista):
    if(len(suunnat) != len(palalista)):
        return False
    for i in suunnat:
        if i not in palalista:
            return False
    return True

        