"""
Created on 4 Mar 2016

@author: Martin Vidjeskog
"""


from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget

from pymaze.maze.piece.piece import Piece
from pymaze.maze.piece.piece_type import PieceType


class TurnSWPiece(Piece):
    """Piece that allows player movement to south and west."""

    def get_piece_type(self) -> PieceType:
        return PieceType.TURN_SW_PIECE

    def is_allowed_to_move_up(self) -> bool:
        return False

    def is_allowed_to_move_down(self) -> bool:
        return True

    def is_allowed_to_move_right(self) -> bool:
        return False

    def is_allowed_to_move_left(self) -> bool:
        return True

    def paint(self, window: QWidget) -> None:
        painter = QPainter()
        painter.begin(window)
        painter.fillRect(self._x, self._y, self._w, self._h, QColor(0, 0, 0))
        painter.fillRect(
            self._x,
            self._y + int(self._h / 4),
            int(self._w / 4) + int(self._w / 2),
            int(self._h / 2),
            self._path_color,
        )
        painter.fillRect(
            self._x + int(self._w / 4),
            self._y + int(self._h / 2),
            int(self._w / 2),
            int(self._h / 2) + 3,
            self._path_color,
        )
        self._paint_solution_path(painter)
        painter.end()
