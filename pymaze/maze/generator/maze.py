"""
Created on 5 Mar 2016

@author: Martin Vidjeskog
"""


from abc import abstractmethod
from typing import List
from PyQt5.QtWidgets import QWidget

from pymaze.maze.generator.maze_type import MazeType
from pymaze.maze.piece.piece import Piece


class Maze:
    """Abstract Maze base class."""

    def __init__(self, width: int, height: int) -> None:
        """Constructor.

        width: maze width
        height: maze height
        """
        self._width = width
        self._height = height
        self._pieces: List[List[Piece]] = []

    def draw_maze(self, window: QWidget) -> None:
        """Draw maze into given game widget.

        window: QWidget into which pieces are drawn.
        """
        for y in range(self._height):
            for x in range(self._width):
                if self._pieces[y][x] is not None:
                    self._pieces[y][x].paint(window)

    def get_width(self) -> int:
        """Get maze width."""
        return self._width

    def get_height(self) -> int:
        """Get maze height."""
        return self._height

    def get_piece(self, x: int, y: int) -> Piece:
        """Get piece from (x, y) location."""
        return self._pieces[y][x]

    def get_pieces(self) -> List[List[Piece]]:
        """Get all pieces."""
        return self._pieces

    @abstractmethod
    def get_type(self) -> MazeType:
        """Get maze type."""

    def update_piece_size_and_location(
        self, piece_width: int, piece_height: int, start_x: int, start_y: int
    ) -> None:
        """Update size of each piece and their location."""
        current_x = start_x
        current_y = start_y

        for y in range(self._height):
            for x in range(self._width):
                if self._pieces[y][x] is not None:
                    self._pieces[y][x].set_width_in_pixels(piece_width)
                    self._pieces[y][x].set_height_in_pixels(piece_height)
                    self._pieces[y][x].set_x_coordinate(current_x)
                    self._pieces[y][x].set_y_coordinate(current_y)
                    current_x += piece_width
            current_x = start_x
            current_y += piece_height
