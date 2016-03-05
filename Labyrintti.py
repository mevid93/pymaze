'''
Created on 5 Mar 2016

@author: Martin Vidjeskog
'''


import LuontiAlgoritmit
from Pala import MuuriPala, KaytavaPala


class Labyrintti(object):
    '''
    Labyrintti-luokka, jossa jokainen labyrintin pala
    on tallennettuna 2d-taulukkoon (lista). 
    '''

    def __init__(self, leveys, korkeus):
        self.lista = [] 
        self.leveys = leveys
        self.korkeus = korkeus 
    
    def luoLabyrintti(self):
        pass
    
    def piirraPelialueeseen(self, window):
        pass
    
    

class KaksiDLabyrintti(Labyrintti):
    
    def __init__(self, leveys, korkeus):
        super().__init__(leveys, korkeus)
        self.luoLabyrintti()
        
    def luoLabyrintti(self):
        self.lista = LuontiAlgoritmit.luo2Dlabyrintti(self.leveys, self.korkeus)
        
    def piirraPelialueeseen(self, window):
        for y in range(self.leveys):
            for x in range(self.korkeus):
                self.lista[y][x].paintPala(window)
    
        