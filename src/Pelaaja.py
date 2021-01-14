'''
Created on 12 Mar 2016

@author: Martin Vidjeskog

 Tama luokka kuvaa pelaajaa (punainen nelio). Luokka
 piirtaa ja tietaa pelaajan paikan labyrintissa.
 Saa parametreina kokonaisluvut x ja y, jotka kuvaavat pelaajan 
 paikkaa 2-dimensioisessa labyrintti taulukossa.

'''


from PyQt4 import QtGui, QtCore


class Hahmo(object):

    ''' Konstruktori, joka saa parametreina palan, johon hahmo laitetaan.
        Lisaksi x ja y jotka kertovat sijainnin 2-dimensioisessa labyrintti taulukossa. '''

    def __init__(self, superpala, x, y):
        self.pala = superpala
        self.x = x
        self.y = y
        
    
    
    ''' Metodi, joka liikutaa hahmon uuteen palaan '''    

    def liikutaHahmoa(self, superpala, x, y):
        self.pala = superpala
        self.x = x
        self.y = y
        
        
        
    ''' Metodi, jota kutsumalla hahmo piirretaan '''
        
    def piirraHahmo(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.pala.getX() + self.pala.getW()/4+1, self.pala.getY() + self.pala.getH()/4+1, self.pala.getW()/2-2, self.pala.getH()/2-2, QtCore.Qt.red)
        painter.end()
        
        
    
    ''' Getteri-metodi, joka palauttaa hahmon sijainnin 2-dimensioisessa labyrintti taulukossa. '''
        
    def getSijainti(self):
        return self.x, self.y
    

        
    