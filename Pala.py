'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
'''


from PyQt4 import QtGui, QtCore


class SuperPala(object):
    '''
    Pala on superluokka, jonka muut alaluokkat perivat
    '''   
    def __init__(self, x, y , w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def voiLiikkuaYlos(self):
        pass
    
    def voiLiikkuaAlas(self):
        pass
    
    def voiLiikkuaOikealle(self):
        pass
    
    def voiLiikkuaVasemmalle(self):
        pass
    
    def getY(self):
        return self.y
    
    def getW(self):
        return self.w
    
    def getH(self):
        return self.h            
        
    def paintPala(self):
        pass

        
     
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
        leveys = self.w/4*3    # pieni laskutoimitus jolla varmistetaan etta ei jaa reunoja
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
        korkeus = self.h/4*3    # pieni laskutoimitus jolla varmistetaan etta ei jaa reunoja
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
        leveys = self.w/4*3    # pieni laskutoimitus jolla varmistetaan etta ei jaa reunoja
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
        leveys = self.w/4*3    # pieni laskutoimitus jolla varmistetaan etta ei jaa reunoja
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h/4, leveys, self.h/2, QtCore.Qt.white)
        alkuY = self.y + self.h/2    # pieni laskutoimitus jolla varmistetaan etta ei jaa reunoja
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
        painter.fillRect(self.x, self.y + self.h/4, self.w/4*3, self.h/2, QtCore.Qt.white)
        alkuY = self.y + self.h/2    # pieni laskutoimitus jolla varmistetaan etta ei jaa reunoja
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
        painter.fillRect(self.x, self.y + self.h/4, self.w/4*3, self.h/2, QtCore.Qt.white)
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
        painter.fillRect(self.x, self.y + self.h/4, self.w/4*3, self.h/2, QtCore.Qt.white)
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
        leveys = self.w/4*3    # pieni laskutoimitus jolla varmistetaan etta ei jaa reunoja
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
        korkeus = self.h/4*3    # pieni laskutoimitus jolla varmistetaan etta ei jaa reunoja
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
        painter.drawLine(self.x + self.w/4*3, self.y, self.x + self.w/4*3, self.y + self.h -1)
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
        painter.drawLine(self.x, self.y + self.h/4*3, self.x + self.w-1, self.y + self.h/4*3)
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
        
        
        
        