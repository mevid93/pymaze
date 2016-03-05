'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
'''


from PyQt4 import QtGui, QtCore


class Pala(object):
    '''
    Pala on superluokka, jonka muut 4 alaluokkaa perivat
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

        
     
class MuuriPala(Pala):
    '''
    Mustan varinen muuriPala
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.end()
        


class KaytavaPala(Pala):
    '''
    Valkoisen varinen kaytavaPala
    '''
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    
    def paintPala(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.white)
        painter.end()
        
        
        
        
        
        
        