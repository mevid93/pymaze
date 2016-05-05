'''
Created on 5 Mar 2016

@author: Martin Vidjeskog

 Labyrintti-luokat. Huolehtivat labyrintin kuvaamisesta. Tietavat koon ja niihin
 kuuluvat palat. Palat on tallennettuna 2d-taulukkoon (lista). 

'''


from Luontialgoritmi1 import luo2Dlabyrintti 
import Luontialgoritmi2


''' Labyrintti luokka on abstrakti ylaluokka, jonka muut labyrintin tyypit perivat '''

class Labyrintti(object):

    ''' Konstruktori. Saa parametreina labyrintin leveyden ja korkeuden '''

    def __init__(self, leveys, korkeus):
        self.lista = [] 
        self.leveys = leveys
        self.korkeus = korkeus 
        
    
    
    ''' Metodi, jota kutsumalla labyrintti piirretaan kayttoliittymaan. 
        window = kayttoliittyma-olio '''    
        
    def piirraPelialueeseen(self, window):
        for y in range(self.leveys):
            for x in range(self.korkeus):
                if(self.lista[y][x]):
                    self.lista[y][x].paintPala(window)
    
    
    
    ''' Getteri-metodi, joka palauttaa labyrintin leveyden '''
                    
    def getLeveys(self):
        return self.leveys
    
    
    
    ''' Getteri-metodi, joka palauttaa labyrintin korkeuden '''
    
    def getKorkeus(self):
        return self.korkeus
    
    
    
    ''' Getteri-metodi, joka palauttaa palan taulukon kohdasta (x,y) '''
    
    def getPala(self, x, y):
        return self.lista[y][x]
    
    
    
    ''' Getteri-metodi, joka palauttaa taulukon, johon palat on tallennettu '''
    
    def getPalat(self):
        return self.lista
    
    
    
    ''' Metodi, jolla labyrintti luodaan. Jatetaan alaluokkien toteutettavaksi. '''
    
    def luoLabyrintti(self):
        pass
    
    
    
    ''' Getteri-metodi, joka palauttaa tiedon siita, minka tyyppinen labyrintti on. 
        Toteutus jatetaan alaluokille. '''

    def getTyyppi(self):
        pass
     
    
    
    

''' KaksiDLabyrintti-luokka, joka perii Labyrintti-luokan '''

class KaksiDLabyrintti(Labyrintti):
    
    ''' Konstruktori, joka saa parametreina leveyden, korkeuden ja listan. 
        Jos listaa ei anneta oliota luotaessa, niin konstruktori kutsuu 
        luoLabyrintti-metodia. Jos lista annetaan ja se ei ole tyhja niin
        labyrintti on listan sisaltamien palojen muotoinen. (labyrintin lataus) '''
    
    def __init__(self, leveys, korkeus, lista = []):
        super().__init__(leveys, korkeus)
        if(len(lista) == 0):
            self.luoLabyrintti()
        else:
            self.lista = lista
    
    
    
    ''' Metodi, joka kutsuu luontialgoritmia ja asettaa luodun labyrintin olion atribuutiksi '''
        
    def luoLabyrintti(self):
        luoja = luo2Dlabyrintti(self.leveys, self.korkeus)
        self.lista = luoja.suoritaLabyrintinLuonti()
    
    
    
    ''' Getteri-metodi palauttaa labyrintin tyypin '''
                    
    def getTyyppi(self):
        return "KaksiDLabyrintti"
      



''' WeaveLabyrintti-luokka, joka perii Labyrintti-luokan '''      
      
class WeaveLabyrintti(Labyrintti):
    
    ''' Konstruktori, joka saa parametreina leveyden, korkeuden ja listan. 
        Jos listaa ei anneta oliota luotaessa, niin konstruktori kutsuu 
        luoLabyrintti-metodia. Jos lista annetaan ja se ei ole tyhja niin
        labyrintti on listan sisaltamien palojen muotoinen. (labyrintin lataus) '''
    
    def __init__(self, leveys, korkeus, lista = []):
        super().__init__(leveys, korkeus)
        if(len(lista) == 0):
            self.luoLabyrintti()
        else:
            self.lista = lista



    ''' Metodi, joka kutsuu luontialgoritmia ja asettaa luodun labyrintin olion atribuutiksi '''
     
    def luoLabyrintti(self):
        self.lista = Luontialgoritmi2.luoWeaveLabyrintti(self.leveys, self.korkeus)
        
        
        
    ''' Getteri-metodi palauttaa labyrintin tyypin '''        
                    
    def getTyyppi(self):
        return "WeaveLabyrintti"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    