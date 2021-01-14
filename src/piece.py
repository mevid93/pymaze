'''
Created on 4 Mar 2016

@author: Martin Vidjeskog
'''


from PyQt5 import QtGui, QtCore


class Piece(object):

    def __init__(self, x, y, w, h):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate
        self.w = w  # width
        self.h = h  # height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getW(self):
        ''' get width in pixels '''
        return self.w

    def getH(self):
        ''' get heigth in pixels '''
        return self.h

    def getCenter(self):
        ''' get center of piece in pixels '''
        x = self.x + self.w/2
        y = self.y + self.h/2
        return x, y

    def isAllowedToMoveUp(self):
        pass

    def isAllowedToMoveDown(self):
        pass

    def isAllowedToMoveRight(self):
        pass

    def isAllowedToMoveLeft(self):
        pass

    def paintPiece(self, window):
        pass


class HorizontalPiece(Piece):
    '''
    ---------------------------------------
    ######

    ######
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4,
                         self.w, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return True


class HorizontalLeftBlockedPiece(Piece):
    '''
    ---------------------------------------
    ######
    ##  
    ######
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        leveys = self.w/4*3
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h /
                         4, leveys, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return False


class HorizontalRightBlockedPiece(Piece):
    '''
    ---------------------------------------
    ######
        ## 
    ######
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, self.w /
                         4*3, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return True


class VerticalPiece(Piece):
    '''
    ---------------------------------------
    ##  ##
    ##  ##
    ##  ##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y,
                         self.w/2, self.h, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return False


class VerticalTopBlockedPiece(Piece):
    '''
    ---------------------------------------
    ######
    ##  ##
    ##  ##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        korkeus = self.h/4*3
        while(True):
            if(self.y + self.h/4 + korkeus == self.y + self.h):
                korkeus += 1
                break
            korkeus += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h /
                         4, self.w/2, korkeus, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return False


class VerticalBottomBlockedPiece(Piece):
    '''
    ---------------------------------------
    ##  ##
    ##  ##
    ######
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y, self.w /
                         2, self.h/4*3, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return False


class TurnNEPiece(Piece):
    '''
    ---------------------------------------
    ##  ##
    ##  
    ######
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y, self.w /
                         2, self.h/2, QtCore.Qt.white)
        leveys = self.w/4*3
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h /
                         4, leveys, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return False


class TurnSEPiece(Piece):
    '''
    ---------------------------------------
    ######
    ##  
    ##  ##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        leveys = self.w/4*3
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h /
                         4, leveys, self.h/2, QtCore.Qt.white)
        alkuY = self.y + self.h/2
        while(True):
            if(alkuY + self.h/2 == self.y + self.h):
                alkuY += 1
                break
            alkuY += 1
        painter.fillRect(self.x + self.w/4, alkuY, self.w /
                         2, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return False


class TurnSWPiece(Piece):
    '''
    ---------------------------------------
    ######
        ##
    ##  ##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, int(self.w/4) +
                         int(self.w/2), self.h/2, QtCore.Qt.white)
        alkuY = self.y + self.h/2
        while(True):
            if(alkuY + self.h/2 == self.y + self.h):
                alkuY += 1
                break
            alkuY += 1
        painter.fillRect(self.x + self.w/4, alkuY, self.w /
                         2, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return True


class TurnNWPiece(Piece):
    '''
    ---------------------------------------
    ##  ##
        ##
    ######
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, int(self.w/4) +
                         int(self.w/2), self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y, self.w /
                         2, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return True


class IntersectionToLeftPiece(Piece):
    '''
    ---------------------------------------
    ##  ##
        ##
    ##  ##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4, int(self.w/4) +
                         int(self.w/2), self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y,
                         self.w/2, self.h, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return True


class IntersectionToUpPiece(Piece):
    '''
    ---------------------------------------
    ##  ##

    ######
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4,
                         self.w, self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y, self.w /
                         2, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return True


class IntersectionToRightPiece(Piece):
    '''
    ---------------------------------------
    ##  ##
    ##
    ##  ##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y,
                         self.w/2, self.h, QtCore.Qt.white)
        leveys = self.w/4*3
        while(True):
            if(self.x + self.w/4 + leveys == self.x + self.w):
                leveys += 1
                break
            leveys += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h /
                         4, leveys, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return False


class IntersectionToDownPiece(Piece):
    '''
    ---------------------------------------
    ######

    ##  ##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4,
                         self.w, self.h/2, QtCore.Qt.white)
        korkeus = self.h/4*3
        while(True):
            if(self.y + self.h/4 + korkeus == self.y + self.h):
                korkeus += 1
                break
            korkeus += 1
        painter.fillRect(self.x + self.w/4, self.y + self.h /
                         4, self.w/2, korkeus, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return True


class IntersectionPiece(Piece):
    '''
    ---------------------------------------
    ##  ##

    ##  ##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x + self.w/4, self.y,
                         self.w/2, self.h, QtCore.Qt.white)
        painter.fillRect(self.x, self.y + self.h/4,
                         self.w, self.h/2, QtCore.Qt.white)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return True


class BridgeVerticalPiece(Piece):
    '''
    ---------------------------------------
    ##|  |##
      |  |
    ##|  |##
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4,
                         self.w, self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y,
                         self.w/2, self.h, QtCore.Qt.white)
        painter.drawLine(self.x + self.w/4-1, self.y,
                         self.x + self.w/4-1, self.y + self.h - 1)
        painter.drawLine(self.x + int(self.w/4)+int(self.w/2), self.y,
                         self.x + int(self.w/4)+int(self.w/2), self.y + self.h - 1)
        painter.end()

    def isAllowedToMoveUp(self):
        return True

    def isAllowedToMoveDown(self):
        return True

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return False


class BridgeHorizontalPiece(Piece):
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

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.black)
        painter.fillRect(self.x, self.y + self.h/4,
                         self.w, self.h/2, QtCore.Qt.white)
        painter.fillRect(self.x + self.w/4, self.y,
                         self.w/2, self.h, QtCore.Qt.white)
        painter.drawLine(self.x, self.y + self.h/4-1,
                         self.x + self.w-1, self.y + self.h/4-1)
        painter.drawLine(self.x, self.y + int(self.h/4)+int(self.h/2),
                         self.x + self.w-1, self.y + int(self.h/4)+int(self.h/2))
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return True

    def isAllowedToMoveLeft(self):
        return True


class FinnishLinePiece(Piece):
    '''
    ---------------------------------------
    Green cube
    ---------------------------------------
    '''

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def paintPiece(self, window):
        painter = QtGui.QPainter()
        painter.begin(window)
        painter.fillRect(self.x, self.y, self.w, self.h, QtCore.Qt.green)
        painter.end()

    def isAllowedToMoveUp(self):
        return False

    def isAllowedToMoveDown(self):
        return False

    def isAllowedToMoveRight(self):
        return False

    def isAllowedToMoveLeft(self):
        return False
