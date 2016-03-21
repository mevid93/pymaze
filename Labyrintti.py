'''
Created on 5 Mar 2016

@author: Martin Vidjeskog
'''


import Luontialgoritmi1
import Luontialgoritmi2


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

    def getTyyppi(self):
        pass
    
    def getLeveys(self):
        return self.leveys
    
    def getKorkeus(self):
        return self.korkeus
    
    def getPala(self, x, y):
        return self.lista[y][x]
    
    def getPalat(self):
        return self.lista
    
    

class KaksiDLabyrintti(Labyrintti):
    
    def __init__(self, leveys, korkeus):
        super().__init__(leveys, korkeus)
        self.luoLabyrintti()
        
    def luoLabyrintti(self):
        self.lista = Luontialgoritmi1.luo2Dlabyrintti(self.leveys, self.korkeus)
        
    def piirraPelialueeseen(self, window):
        for y in range(self.leveys):
            for x in range(self.korkeus):
                if(self.lista[y][x]):
                    self.lista[y][x].paintPala(window)
                    
    def getTyyppi(self):
        return "KaksiDLabyrintti"
      
      
      
class WeaveLabyrintti(Labyrintti):
    
    def __init__(self, leveys, korkeus):
        super().__init__(leveys, korkeus)
        self.luoLabyrintti()
        
    def luoLabyrintti(self):
        self.lista = Luontialgoritmi2.luoWeaveLabyrintti(self.leveys, self.korkeus)
        
    def piirraPelialueeseen(self, window):
        for y in range(self.leveys):
            for x in range(self.korkeus):
                if(self.lista[y][x]):
                    self.lista[y][x].paintPala(window)
                    
    def getTyyppi(self):
        return "WeaveLabyrintti"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    