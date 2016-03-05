'''
Created on 5 Mar 2016

@author: Martin Vidjeskog

Tama moduuli sisaltaa algoritmeja labyrinttien luomiseksi.
'''


from Pala import MuuriPala, KaytavaPala

 
def luo2Dlabyrintti(leveys, korkeus):
    xc = 275
    xy = 25
    lista = [[0 for leveys in range(leveys)] for y in range(korkeus)]
    for y in range(korkeus):
        for x in range(leveys):
            if(x % 2 == 0):
                lista[y][x] = MuuriPala(xc, xy, 25, 25)
            else:
                lista[y][x] = KaytavaPala(xc, xy, 25, 25)
            xc += 25
        xy += 25
        xc = 275
    return lista