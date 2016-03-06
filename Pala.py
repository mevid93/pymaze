'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
'''


from PyQt4 import QtGui, QtCore


class Pala(object):
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
        
    def paintPala(self):
        pass

        
     
class VaakasuoraPala(Pala):
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
        painter.fillRect(self.x, self.y + self.y/4, self.w, self.h/2, QtCore.Qt.white)
        painter.end() 


class VaakasuoraVasenPaatyPala(Pala):
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
        
        
class VaakasuoraOikeaPaatyPala(Pala):
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


class PystysuoraPala(Pala):
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
        
        
class PystysuoraYlapaatyPala(Pala):
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
        
        
class PystysuoraAlapaatyPala(Pala):
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
        
        
class KaannosNEPala(Pala):
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
        
        
class KaannosSEPala(Pala):
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
        
        
class KaannosSWPala(Pala):
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
        
        
class KaannosNWPala(Pala):
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
        
        
class TRisteysVasemmallePala(Pala):
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
        
        
class TRisteysYlosPala(Pala):
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
        
        
class TRisteysOikeallePala(Pala):
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
        
        
class TRisteysAlasPala(Pala):
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
        
        
class YlikulkuPystysuuntaPala(Pala):
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
        painter.drawLine(self.x + self.w/4, self.y, self.x + self.w/4, self.y + self.h -1)
        painter.drawLine(self.x + self.w/4*3, self.y, self.x + self.w/4*3, self.y + self.h -1)
        painter.end()
        
        
class YlikulkuVaakasuuntaPala(Pala):
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
        painter.drawLine(self.x, self.y + self.h/4, self.x + self.w-1, self.y + self.h/4)
        painter.drawLine(self.x, self.y + self.h/4*3, self.x + self.w-1, self.y + self.h/4*3)
        painter.end()
        
        
        
        
        