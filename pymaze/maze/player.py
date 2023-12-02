"""
Created on 12 Mar 2016

@author: Martin Vidjeskog
"""


from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtWidgets

from pymaze.maze.piece.piece import Piece
from pymaze.maze.piece.piece_type import PieceType


class Player:
    """Player class."""

    def __init__(self, piece: Piece, x: int, y: int):
        self.__piece = piece
        self.__x = x
        self.__y = y

    def move_player(self, piece: Piece, x: int, y: int):
        """Set player location to x and y."""
        self.__piece = piece
        self.__x = x
        self.__y = y

    def draw_player(self, window: QtWidgets.QWidget):
        """Draw player to game window."""
        painter = QPainter()
        painter.begin(window)
        player_width = int(self.__piece.get_width_in_pixels() / 2) - 2
        player_height = int(self.__piece.get_height_in_pixels() / 2) - 2
        painter.fillRect(
            self.__piece.get_x_coordinate()
            + int(self.__piece.get_width_in_pixels() / 4)
            + 1,
            self.__piece.get_y_coordinate()
            + int(self.__piece.get_height_in_pixels() / 4)
            + 1,
            player_width,
            player_height,
            QColor(255, 0, 0),
        )
        painter.end()

    def has_reached_target_piece(self) -> bool:
        """Return true if player has reached targer piece."""
        if self.__piece is None:
            return False

        return self.__piece.get_piece_type() == PieceType.TARGET_PIECE

    def get_location(self):
        """Get player x and y location."""
        return self.__x, self.__y
