'''
Created on 20 Mar 2016

@author: Martin Vidjeskog
'''


from src.maze import *
from src.piece import *
from PyQt5 import QtGui, QtWidgets


class Saver(object):

    def __init__(self, window):
        self.window = window
        self.leveys = window.maze.getWidth()
        self.korkeus = window.maze.getHeigth()
        self.lista = window.maze.getPieces()
        self.tyyppi = window.maze.getType()

    def saveMazeIntoFile(self):
        ''' Open save file dialog and save the maze into a file '''
        name = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save File', filter='*.maze')
        if(name != '' and name != None):
            name = name[0]
            if not name.lower().endswith(".maze"):
                name += ".maze"
            file = open(name, 'w')
            file.write("#Tyyppi: " + self.tyyppi)
            file.write("\n\n")
            file.write("#Labyrintin leveys: " + str(self.leveys))
            file.write("\n\n")
            file.write("#Labyrintin korkeus: " + str(self.korkeus))
            file.write("\n\n")
            file.write("#Palan leveys: " + str(self.lista[0][0].getW()))
            file.write("\n\n")
            file.write("#Palan korkeus: " + str(self.lista[0][0].getH()))
            file.write("\n\n")
            file.write("#Palat: \n")
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    file.write(str(self.lista[y][x].getX(
                    )) + " " + str(self.lista[y][x].getY()) + ": " + type(self.lista[y][x]).__name__)
                    file.write("\n")
            file.close()


class Loader(object):

    def __init__(self, window):
        self.window = window
        # list of possible pieces
        self.palojenTyypit = ["HorizontalPiece", "HorizontalLeftBlockedPiece", "HorizontalRightBlockedPiece",
                              "VerticalPiece", "VerticalTopBlockedPiece", "VerticalBottomBlockedPiece"]
        self.palojenTyypit += ["TurnNEPiece", "TurnSEPiece", "TurnSWPiece",
                               "TurnNWPiece", "IntersectionToLeftPiece", "IntersectionToUpPiece"]
        self.palojenTyypit += ["IntersectionToDownPiece", "IntersectionToRightPiece", "IntersectionPiece",
                               "BridgeVerticalPiece", "BridgeHorizontalPiece", "FinnishLinePiece"]
        # check flags
        self.checkTyyppi = False
        self.checkLeveys = False
        self.checkKorkeus = False
        self.checkPalat = False
        self.checkPalanLeveys = False
        self.checkPalanKorkeus = False
        # maze info
        self.tyyppi = ""
        self.leveys = -1
        self.korkeus = -1
        self.palanKorkeus = 0
        self.palanLeveys = 0
        self.palalista = []

    def loadMazeFromFile(self):
        # avataan open-file-dialog ja valitaan tiedosto
        name = QtWidgets.QFileDialog.getOpenFileName(
            self.window, 'Open File', filter='*.maze')
        if(name != '' and name != None):
            name = name[0]
            # Avaa tiedosto lukemista varten
            file = None
            try:
                file = open(name, 'r')
            except OSError:
                # Tiedosta ei ole olemassa. Ei pitaisi olla koskaan mahdollista
                self.window.textbox.clear()
                self.window.textbox.setText("Tiedostoa ei ole olemassa.")
            else:
                jatka = self.readFileLineByLine(file)
            file.close()
            # Tarkista etta kaikki tiedot on luettu
            if(jatka != True or self.checkTyyppi != True or self.checkLeveys != True or self.checkKorkeus != True or self.checkPalanLeveys != True or self.checkPalanKorkeus != True):
                return None
            if(self.tyyppi == "WeaveLabyrintti" and len(self.palalista) == self.korkeus*self.leveys):
                lista = self.__piecesInto2dList()
                return WeaveMaze(self.leveys, self.korkeus, lista)
            if(self.tyyppi == "KaksiDLabyrintti" and len(self.palalista) == self.korkeus*self.leveys):
                lista = self.__piecesInto2dList()
                return TwoDimMaze(self.leveys, self.korkeus, lista)
            return None
        return None

    def readFileLineByLine(self, file):
        # lue tiedoston sisalto
        for line in file:
            osat = line.split(":")
            if len(osat) == 2:
                osat[0] = osat[0].strip()
                osat[1] = osat[1].strip()
                if(osat[0] == "#Tyyppi"):
                    self.tyyppi = osat[1]
                    if(self.tyyppi != "WeaveLabyrintti" and self.tyyppi != "KaksiDLabyrintti"):
                        self.window.textbox.clear()
                        self.window.textbox.setText(
                            "Labyrintin Tyyppi ei ole tuettu!")
                        return False
                    self.checkTyyppi = True
                elif(osat[0] == "#Labyrintin leveys"):
                    self.leveys = self.__stringToInt(osat[1])
                    if(self.leveys < 15 or self.leveys > 50 or self.checkTyyppi == False):
                        return False
                    self.checkLeveys = True
                elif(osat[0] == "#Labyrintin korkeus"):
                    self.korkeus = self.__stringToInt(osat[1])
                    if(self.korkeus < 15 or self.korkeus > 50 or self.checkTyyppi == False):
                        return False
                    self.checkKorkeus = True
                elif(osat[0] == "#Palan korkeus"):
                    self.palanKorkeus = self.__stringToInt(osat[1])
                    if(self.palanKorkeus < 9 or self.palanKorkeus > 34 or self.checkTyyppi == False):
                        return False
                    self.checkPalanKorkeus = True
                elif(osat[0] == "#Palan leveys"):
                    self.palanLeveys = self.__stringToInt(osat[1])
                    if(self.palanLeveys < 9 or self.palanLeveys > 34 or self.checkTyyppi == False):
                        return False
                    self.checkPalanLeveys = True
                elif(osat[0] == "#Palat"):
                    self.checkPalat = True
                # Tarkoittaa sita etta nyt luetaan palojen dataa. Palojen jarjestyksella ei valia.
                elif(self.checkPalat == True and self.checkPalanLeveys == True and self.checkPalanKorkeus == True):
                    palatyyppi = osat[1]
                    if(palatyyppi in self.palojenTyypit):
                        koordinaatit = osat[0].split(" ")
                        if(len(koordinaatit) == 2):
                            x = -1
                            y = -1
                            koordinaatit[0] = koordinaatit[0].strip()
                            koordinaatit[1] = koordinaatit[1].strip()
                            x = self.__stringToInt(koordinaatit[0])
                            y = self.__stringToInt(koordinaatit[1])
                            if(x == -1 or y == -1 or x < 275 or x > 775 or y < 25 or y > 525):
                                self.window.textbox.clear()
                                self.window.textbox.setText(
                                    "Labyrintti sisaltaa virheellisen palan.")
                                return False
                            else:
                                self.palalista.append(self._createPiece(
                                    palatyyppi, x, y, self.palanLeveys, self.palanKorkeus))
                        else:
                            self.window.textbox.clear()
                            self.window.textbox.setText(
                                "Labyrintti sisaltaa virheellisen palan.")
                            return False
                    else:
                        self.window.textbox.clear()
                        self.window.textbox.setText(
                            "Labyrintti sisaltaa virheellisen palan.")
                        return False

            else:
                continue
        # Jos paasty tanne niin labyrintti tiedoston rivit eivat olleet virheellisia
        return True

    def __stringToInt(self, strInt):
        try:
            luku = int(strInt)
            return luku
        except ValueError:
            # merkkijono ei ole luku
            return -1

    def _createPiece(self, palatyyppi, x, y, w, h):
        if(palatyyppi == "HorizontalPiece"):
            return HorizontalPiece(x, y, w, h)
        elif(palatyyppi == "HorizontalLeftBlockedPiece"):
            return HorizontalLeftBlockedPiece(x, y, w, h)
        elif(palatyyppi == "HorizontalRightBlockedPiece"):
            return HorizontalRightBlockedPiece(x, y, w, h)
        elif(palatyyppi == "VerticalPiece"):
            return VerticalPiece(x, y, w, h)
        elif(palatyyppi == "VerticalTopBlockedPiece"):
            return VerticalTopBlockedPiece(x, y, w, h)
        elif(palatyyppi == "VerticalBottomBlockedPiece"):
            return VerticalBottomBlockedPiece(x, y, w, h)
        elif(palatyyppi == "TurnNEPiece"):
            return TurnNEPiece(x, y, w, h)
        elif(palatyyppi == "TurnSEPiece"):
            return TurnSEPiece(x, y, w, h)
        elif(palatyyppi == "TurnSWPiece"):
            return TurnSWPiece(x, y, w, h)
        elif(palatyyppi == "TurnNWPiece"):
            return TurnNWPiece(x, y, w, h)
        elif(palatyyppi == "IntersectionToLeftPiece"):
            return IntersectionToLeftPiece(x, y, w, h)
        elif(palatyyppi == "IntersectionToUpPiece"):
            return IntersectionToUpPiece(x, y, w, h)
        elif(palatyyppi == "IntersectionToRightPiece"):
            return IntersectionToRightPiece(x, y, w, h)
        elif(palatyyppi == "IntersectionToDownPiece"):
            return IntersectionToDownPiece(x, y, w, h)
        elif(palatyyppi == "IntersectionPiece"):
            return IntersectionPiece(x, y, w, h)
        elif(palatyyppi == "BridgeVerticalPiece"):
            return BridgeVerticalPiece(x, y, w, h)
        elif(palatyyppi == "BridgeHorizontalPiece"):
            return BridgeHorizontalPiece(x, y, w, h)
        elif(palatyyppi == "FinnishLinePiece"):
            return FinnishLinePiece(x, y, w, h)

 
    def __piecesInto2dList(self):
        lista = [[0 for x in range(self.leveys)] for x in range(self.korkeus)]
        sija = 0
        for j in range(self.korkeus):
            for i in range(self.leveys):
                lista[j][i] = self.palalista[sija]
                sija += 1
        return lista
