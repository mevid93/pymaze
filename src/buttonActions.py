'''
Created on 2 May 2016

@author: Martin Vidjeskog
'''


import sys
from src.fileManager import Saver, Loader
from src.player import Player
from src.maze import WeaveMaze, TwoDimMaze
from src.solver import WallFollower


class ButtonListener(object):

    def __init__(self, window):
        self.window = window

    def handleButtonClick(self, sender):
        if(sender.text() == "Generoi Labyrintti" and self.window.state != 2):
            self.generateMazeCommand()
        if(sender.text() == "Tietoja ohjelmasta" and self.window.state != 2):
            self.showInformationCommand()
        if(sender.text() == "Pelaa" and self.window.maze != None):
            self.playCommand()
        if(sender.text() == "Lopeta"):
            sys.exit()
        if(sender.text() == "Tallenna Labyrintti" and self.window.state != 2 and self.window.maze != None):
            self.saveMazeCommand()
        if(sender.text() == "Lataa Labyrintti" and self.window.state != 2):
            self.loadMazeCommand()
        if(sender.text() == "Luovuta ja anna ratkaisu" and self.window.state == 2):
            self.showSolutionCommand()
        if(sender.text() == "Generoi" and self.window.state != 2):
            self.generateComand()

    def generateMazeCommand(self):
        self.window.state = 0
        self.window.maze = None
        self.window.update()
        if not(self.window.label1.isVisible()):
            self.window.settingsMenu()

    def showInformationCommand(self):
        self.window.textbox.clear()
        self.window.textbox.setText("Labyrintti-peli V.0.3.0\n")
        self.window.textbox.append("Ohjeet:")
        self.window.textbox.append("1. Lataa tai luo ensin labyrintti.")
        self.window.textbox.append("2. Paina pelaa nappia.")
        self.window.textbox.append(
            "3. Yrita ohjata punainen nelio vihreaan ruutuun.")
        self.window.textbox.append("  W = liiku ylos")
        self.window.textbox.append("  S = liiku alas")
        self.window.textbox.append("  A = liiku vasemmalle")
        self.window.textbox.append("  D = liiku oikealle")
        self.window.textbox.append(
            "4. Voit lopettaa ja saada esimerkkiratkaisun painamalla \" Luovuta ja anna ratkaisu\"-nappia.")
        self.window.textbox.append(
            "5. Labyrintin voi tallentaa painamalla \"Tallenna labyrintti\"-nappia")
        self.window.textbox.append(
            "6. \"Lopeta\"-nappi sammuttaa sovelluksen.")

    def playCommand(self):
        self.window.state = 2
        x = int(self.window.maze.getWidth()/2)-1
        y = int(self.window.maze.getHeigth()/2)-1
        self.window.player = Player(self.window.maze.getPiece(x, y), x, y)
        self.window.textbox.clear()
        self.window.textbox.setText(
            "PELI ON KAYNNISSA! Etsi reitti ulos labyrintista.\nVoit aina luovuttaa jos et keksi ratkaisua.")
        self.window.update()

    def saveMazeCommand(self):
        tallentaja = Saver(self.window)
        tallentaja.saveMazeIntoFile()

    def loadMazeCommand(self):
        lataaja = Loader(self.window)
        labyrintti = lataaja.loadMazeFromFile()
        if(labyrintti != None):
            self.window.maze = labyrintti
            if (self.window.label1.isVisible()):
                self.window.settingsMenu()
            self.window.state = 1
            self.window.update()
            self.window.textbox.clear()
            self.window.textbox.setText("Labyrintin lataus onnistui.")

    ''' Metodi, jonka avulla peli voidaan luovuttaa ja samalla esitetaan demoratkaisu. '''

    def showSolutionCommand(self):
        self.window.state = 1
        self.window.update()
        self.window.state = 3
        self.window.demo = WallFollower(self.window)
        self.window.demo.solve()
        self.window.update()
        self.window.textbox.clear()
        self.window.textbox.setText("Luovutit. Tassa esimerkkiratkaisu.")

    def generateComand(self):
        ''' operations to execute when user wants to generate maze '''
        leveys = self.window.leveysBox.value()
        korkeus = leveys
        if(self.window.checkBox2.isChecked()):
            self.window.maze = WeaveMaze(leveys, korkeus)
            self.window.settingsMenu()
            self.window.state = 1
            self.window.update()
        if(self.window.checkBox1.isChecked()):
            self.window.maze = TwoDimMaze(leveys, korkeus)
            self.window.settingsMenu()
            self.window.state = 1
            self.window.update()
