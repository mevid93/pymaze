'''
Created on 5 Mar 2016

@author: Martin Vidjeskog

Tama moduuli sisaltaa algoritmeja labyrinttien luomiseksi.
'''


from random import randint
from Pala import *

 
def luo2Dlabyrintti(leveys, korkeus):
    lista = []
    lista.append(VaakasuoraPala(275, 25, 25, 25))
    lista.append(PystysuoraPala(300, 50, 25, 25))
    lista.append(PystysuoraYlapaatyPala(325, 75, 25, 25))
    lista.append(PystysuoraAlapaatyPala(350, 100, 25, 25))
    lista.append(VaakasuoraVasenPaatyPala(375, 125, 25, 25))
    lista.append(VaakasuoraOikeaPaatyPala(400, 150, 25, 25))
    lista.append(KaannosNEPala(425, 175, 25, 25))
    lista.append(KaannosSEPala(450, 200, 25, 25))
    lista.append(KaannosSWPala(475, 225, 25, 25))
    lista.append(KaannosNWPala(500, 250, 25, 25))
    lista.append(TRisteysVasemmallePala(525, 275, 25, 25))
    lista.append(TRisteysYlosPala(550, 300, 25, 25))
    lista.append(TRisteysOikeallePala(575, 325, 25, 25))
    lista.append(TRisteysAlasPala(600, 350, 25, 25))
    lista.append(YlikulkuPystysuuntaPala(625, 375, 25, 25))
    lista.append(YlikulkuVaakasuuntaPala(650, 400, 25, 25))
    return lista

def recursiveBactracking(leveys, korkeus):
    print("Seuraava vaihe")

        