'''
Created on 4 Mar 2016

@author: Martin Vidjeskog

 SuperPala (muiden palojen ylaluokka) ja muut 18 erilaista pala luokkaa. Jokainen pala tietaa 
 sijaintinsa ja kokonsa (pikseleina). Lisaksi osaavat piirtaa itsensa ja palauttaa tiedot
 siita mihin suuntiin palasta voi liikkua. 
 
HUOM!
 Jokaisella luokalla on samat metodit, joten niiden toiminta on selitetty vain superluokassa.

'''


from PyQt4 import QtGui, QtCore


class SuperPala(object):
    
    '''
    Konstruktori, joka saa parametreina palan vasemman ylareunan sijainnin naytolla (x,y),
    seka leveyden ja korkeuden w, h. '''
       
    def __init__(self, x, y , w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
 
    
    
    ''' Metodi, joka palatuttaa palan sijainnin (pikseleina) x-akselilla '''
    
    def getX(self):
        return self.x
    
    
    
    ''' Metodi, joka palauttaa palan sijainnin (pikseleina) y-akselilla. Huom! Kaanteinen y-akseli '''
    
    def getY(self):
        return self.y
    
    
    
    ''' Metodi, joka palauttaa palan leveyden pikseleina '''
    
    def getW(self):
        return self.w
    
    
    
    ''' Metodi, joka palauttaa palan korkeuden pikseleina '''
    
    def getH(self):
        return self.h     
    
    
    
    ''' Metodi, joka palauttaa palan keskipisteen (pikseleina) '''
    
    def getKeskipiste(self):
        x = self.x + self.w/2;
        y = self.y + self.h/2;
        return x, y
    
    
    
    ''' Metodi, joka palauttaa tiedon voiko palasta liikkua ylos. Toteutus
        on jatetty alaluokkille. '''
    
    def voiLiikkuaYlos(self):
        pass
    
    
    
    ''' Metodi, joka palauttaa tiedon voiko palasta liikkua alas. Toteutus
        on jatetty alaluokille. '''
    
    def voiLiikkuaAlas(self):
        pass
    
    
    
    ''' Metodi, joka palauttaa tiedon voiko palasta liikkua oikealle. Toteutus
        on jatetty alaluokille. '''
    
    def voiLiikkuaOikealle(self):
        pass
    
    
    
    ''' Metodi, joka palauttaa tiedon voiko palasta liikkua vasemmalle. Toteutus
        on jatetty alaluokille. '''
    
    def voiLiikkuaVasemmalle(self):
        pass
       
    
    
    ''' Metodi, joka piirtaa palan kayttoliittymaan. Toteutus jatetty alaluokille. '''
        
    def paintPala(self):
        pass






""" Alaluoka alkavat tasta eteenpain. Jokaiseen luokkaan on pyritty 
    hahmottelemaan minka tyyppinen pala on kyseessa. """

        
     
class VaakasuoraPala(SuperPala):
    '''
    ---------------------------------------
    ######
    
    ######
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, self.w, self.h/2, QtCore.Qt.white)
        painter.end() 

    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return True



class VaakasuoraVasenPaatyPala(SuperPala):
    '''
    ---------------------------------------
    ######
    ##  
    ######
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        leveys = self.w/4*3    
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h/4, leveys, self.h/2, QtCore.Qt.white)
        painter.end()
        
    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return False
        
        
        
class VaakasuoraOikeaPaatyPala(SuperPala):
    '''
    ---------------------------------------
    ######
        ## 
    ######
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, self.w/4*3, self.h/2, QtCore.Qt.white)
        painter.end()         

    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return True



class PystysuoraPala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
    ##  ##
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return False               
        
        
        
class PystysuoraYlapaatyPala(SuperPala):
    '''
    ---------------------------------------
    ######
    ##  ##
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        korkeus = self.h/4*3    
        while(True):
            if(self.y + self.h/4 + korkeus == self.y + self.h):
                korkeus += 1
                break
            korkeus += 1
        painter.fillRect(self.x+ self.w/4, self.y + self.h/4, self.w/2, korkeus, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return False       
        
        
        
class PystysuoraAlapaatyPala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
    ##  ##
    ######
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h/4*3, QtCore.Qt.white)
        painter.end()  
        
    def getKeskipiste(self):
        return super().getKeskipiste()
        
    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return False
        
        
        
class KaannosNEPala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
    ##  
    ######
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h/2, QtCore.Qt.white)
        leveys = self.w/4*3   
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h/4, leveys, self.h/2, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return False
        
        
        
class KaannosSEPala(SuperPala):
    '''
    ---------------------------------------
    ######
    ##  
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        leveys = self.w/4*3    
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h/4, leveys, self.h/2, QtCore.Qt.white)
        alkuY = self.y + self.h/2   
        while(True):
            if(alkuY + self.h/2 == self.y + self.h):
                alkuY += 1
                break
            alkuY += 1
        painter.fillRect(self.x + self.w/4, alkuY, self.w/2, self.h/2, QtCore.Qt.white)
        painter.end()  

    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return False 
        
        
        
class KaannosSWPala(SuperPala):
    '''
    ---------------------------------------
    ######
        ##
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, int(self.w/4)+int(self.w/2), self.h/2, QtCore.Qt.white)
        alkuY = self.y + self.h/2    
        while(True):
            if(alkuY + self.h/2 == self.y + self.h):
                alkuY += 1
                break
            alkuY += 1
        painter.fillRect(self.x + self.w/4, alkuY, self.w/2, self.h/2, QtCore.Qt.white)
        painter.end()  

    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return True
        
        
        
class KaannosNWPala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
        ##
    ######
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, int(self.w/4)+int(self.w/2), self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h/2, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return True
        
        
        
class TRisteysVasemmallePala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
        ##
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, int(self.w/4)+int(self.w/2), self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return True
        
        
        
class TRisteysYlosPala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
        
    ######
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, self.w, self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h/2, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return True
        
        
        
class TRisteysOikeallePala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
    ##
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h, QtCore.Qt.white)
        leveys = self.w/4*3   
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h/4, leveys, self.h/2, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return False
        
        
        
class TRisteysAlasPala(SuperPala):
    '''
    ---------------------------------------
    ######
    
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, self.w, self.h/2, QtCore.Qt.white)
        korkeus = self.h/4*3  
        while(True):
            if(self.y + self.h/4 + korkeus == self.y + self.h):
                korkeus += 1
                break
            korkeus += 1
        painter.fillRect(self.x+ self.w/4, self.y + self.h/4, self.w/2, korkeus, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return True



class XRisteysPala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
    
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h, QtCore.Qt.white)
        painter.fillRect(self.x, self.y + self.h/4, self.w, self.h/2, QtCore.Qt.white)
        painter.end()

    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return True

        
        
class YlikulkuPystysuuntaPala(SuperPala):
    '''
    ---------------------------------------
    ##|  |##
      |  |
    ##|  |##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, self.w, self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h, QtCore.Qt.white)
        painter.drawLine(self.x + self.w/4-1, self.y, self.x + self.w/4-1, self.y + self.h -1)
        painter.drawLine(self.x + int(self.w/4)+int(self.w/2), self.y, self.x + int(self.w/4)+int(self.w/2), self.y + self.h -1)
        painter.end()

    def voiLiikkuaYlos(self):
        return True
    
    def voiLiikkuaAlas(self):
        return True
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return False
        
        
        
class YlikulkuVaakasuuntaPala(SuperPala):
    '''
    ---------------------------------------
    ##  ##
    ------
    ______ 
    ##  ##
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, self.w, self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y, self.w/2, self.h, QtCore.Qt.white)
        painter.drawLine(self.x, self.y + self.h/4-1, self.x + self.w-1, self.y + self.h/4-1)
        painter.drawLine(self.x, self.y + int(self.h/4)+int(self.h/2), self.x + self.w-1, self.y + int(self.h/4)+int(self.h/2))
        painter.end()

    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return True
    
    def voiLiikkuaVasemmalle(self):
        return True
        
        

class MaaliPala(SuperPala):
    '''
    ---------------------------------------
    Vihree kuutio
    ---------------------------------------
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.green)
        painter.end()

    def voiLiikkuaYlos(self):
        return False
    
    def voiLiikkuaAlas(self):
        return False
    
    def voiLiikkuaOikealle(self):
        return False
    
    def voiLiikkuaVasemmalle(self):
        return False
        
        
        
        