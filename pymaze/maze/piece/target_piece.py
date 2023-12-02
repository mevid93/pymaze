"""
Created on 4 Mar 2016

@author: Martin Vidjeskog
"""


from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget

from pymaze.maze.piece.piece import Piece
from pymaze.maze.piece.piece_type import PieceType


class TargetPiece(Piece):
    """Target piece."""

    def get_piece_type(self) -> PieceType:
        return PieceType.TARGET_PIECE

    def is_allowed_to_move_up(self) -> bool:
        return False

    def is_allowed_to_move_down(self) -> bool:
        return False

    def is_allowed_to_move_right(self) -> bool:
        return False

    def is_allowed_to_move_left(self) -> bool:
        return False

    def paint(self, window: QWidget) -> None:
        painter = QPainter()
        painter.begin(window)
        painter.fillRect(self._x, self._y, self._w, self._h, QColor(0, 255, 0))
        painter.end()
