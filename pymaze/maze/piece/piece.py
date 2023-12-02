"""
Created on 4 Mar 2016

@author: Martin Vidjeskog
"""


from abc import ABCMeta, abstractmethod
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from pymaze.maze.piece.piece_type import PieceType


class Piece(metaclass=ABCMeta):
    """Abstract base class for pieces."""

    COLOR_BASE = QColor(255, 255, 255)
    COLOR_SOLUTION_PATH = QColor(255, 50, 150)

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        """Constructor.

        x: x coordinate of the piece in pixels
        y: y coordinate of the piece in pixels.
        w: piece width in pixels.
        h: piece heigth in pixels.
        """
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._part_of_solution = False
        self._path_color = Piece.COLOR_BASE

    def get_x_coordinate(self) -> int:
        """Get x coordinate of the piece in pixels."""
        return self._x

    def get_y_coordinate(self) -> int:
        """Get y coordinate of the piece in pixels."""
        return self._y

    def get_width_in_pixels(self) -> int:
        """Get piece width in pixels."""
        return self._w

    def get_height_in_pixels(self) -> int:
        """Get piece heigth in pixels."""
        return self._h

    def set_width_in_pixels(self, width: int) -> None:
        """Set piece width in pixels."""
        self._w = width

    def set_height_in_pixels(self, height: int) -> None:
        """Set piece height in pixels."""
        self._h = height

    def set_x_coordinate(self, x: int) -> None:
        """Set new x coordinate for piece."""
        self._x = x

    def set_y_coordinate(self, y: int) -> None:
        """Set new y coordinate for piece."""
        self._y = y

    def set_part_of_solution(self, part_of_solution: bool) -> None:
        """Set flag that tells if piece if part of maze solution."""
        self._part_of_solution = part_of_solution

    def is_part_of_solution(self) -> bool:
        """Return true if piece is part of solution."""
        return self._part_of_solution

    def _paint_solution_path(self, painter: QPainter):
        """Paint solution path mark."""
        if not self._part_of_solution:
            return
        if self._part_of_solution:
            painter.setBrush(QBrush(self.COLOR_SOLUTION_PATH, Qt.SolidPattern))  # type: ignore
            painter.drawEllipse(
                self._x + int(self._w / 3),
                self._y + int(self._h / 3),
                int(self._w / 3),
                int(self._h / 3),
            )

    @abstractmethod
    def get_piece_type(self) -> PieceType:
        """Return the type of the piece."""

    @abstractmethod
    def is_allowed_to_move_up(self) -> bool:
        """Returns boolean value indicating whether player can move up or not."""

    @abstractmethod
    def is_allowed_to_move_down(self) -> bool:
        """Returns boolean value indicating whether player can move down or not."""

    @abstractmethod
    def is_allowed_to_move_right(self) -> bool:
        """Returns boolean value indicating whether player can move right or not."""

    @abstractmethod
    def is_allowed_to_move_left(self) -> bool:
        """Returns boolean value indicating whether player can move left or not."""

    @abstractmethod
    def paint(self, window: QWidget) -> None:
        """Paint piece."""
