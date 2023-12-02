"""
Created on 4 Mar 2016

@author: Martin Vidjeskog
"""


from typing import Optional
from PyQt5 import QtWidgets

from pymaze.maze.generator.maze import Maze
from pymaze.maze.player import Player


class MazePainter(QtWidgets.QWidget):
    """Maze painter class."""

    maze: Optional[Maze] = None
    player: Optional[Player] = None

    def __init__(self) -> None:
        super().__init__()
        self.__previous_width = 0
        self.__previous_height = 0

    def __update_maze_pieces(self, width: int, height: int) -> None:
        """Update sizes of maze pieces."""
        if self.maze is None:
            return

        # calculate new width and height for pieces
        maze_width = self.maze.get_width()
        maze_height = self.maze.get_height()

        piece_width = int((width - 10) / maze_width)
        piece_height = int((height - 10) / maze_height)

        # get frame area corner
        x = self.frameGeometry().topLeft().x()
        y = self.frameGeometry().topLeft().y()

        # update each piece and their location
        self.maze.update_piece_size_and_location(piece_width, piece_height, x, y)

    # pylint: disable-next=invalid-name
    def paintEvent(self, event):  # pylint: disable=unused-argument
        """Draw maze."""
        if self.maze is None:
            return

        # get maze painter widget area and update the maze size
        area_width = self.size().width()
        area_height = self.size().height()

        if self.__previous_width != area_width or self.__previous_height != area_height:
            self.__update_maze_pieces(area_width, area_height)

        # draw maze
        self.maze.draw_maze(self)

        # draw player
        if self.player is not None:
            self.player.draw_player(self)
