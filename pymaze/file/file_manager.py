"""
Created on 20 Mar 2016

@author: Martin Vidjeskog
"""


from typing import Optional
import pickle
from PyQt5 import QtWidgets

from pymaze.maze.generator.maze import Maze


FILE_EXTENSION = ".maze"


class FileManager:
    """File manager class for handling maze files."""

    @staticmethod
    def save_file(parent_window: QtWidgets.QWidget, maze: Maze):
        """Open file save dialog and save file."""

        # first select output file
        name = QtWidgets.QFileDialog.getSaveFileName(
            parent_window, "Save File", filter="*.maze"
        )

        if name is None:
            return

        try:
            # try to get file name
            filename = name[0]

            if filename is None or filename == "":
                return

            if not filename.lower().endswith(".maze"):
                filename += ".maze"

            # dump maze content into the output file
            with open(filename, "wb") as file:
                pickle.dump(maze, file)

        # pylint: disable-next=bare-except
        except:
            print("Failed to save maze!")

    @staticmethod
    def load_file(parent_window: QtWidgets.QWidget) -> Optional[Maze]:
        """Open file open dialog and load file."""

        # first select input file
        name = QtWidgets.QFileDialog.getOpenFileName(
            parent_window, "Open File", filter="*.maze"
        )

        if name is None:
            return None

        # try to read maze from file
        try:
            # try to get file name
            filename = name[0]

            if filename is None or filename == "":
                return None

            if not filename.lower().endswith(".maze"):
                filename += ".maze"

            # dump maze content into the output file
            with open(filename, "rb") as file:
                maze = pickle.load(file)
                return maze

        # pylint: disable-next=bare-except
        except:
            print("Failed to load maze!")
            return None
