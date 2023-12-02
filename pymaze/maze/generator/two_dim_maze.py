"""
Created on 5 Mar 2016

@author: Martin Vidjeskog
"""


from pymaze.maze.generator.maze import Maze
from pymaze.maze.generator.maze_type import MazeType
from pymaze.maze.generator.two_dim_maze_generator import generate_two_dimensional_maze


class TwoDimMaze(Maze):
    """Two dimensional maze class."""

    def __init__(self, width, height) -> None:
        super().__init__(width, height)
        self._pieces = generate_two_dimensional_maze(self._width, self._height)

    def get_type(self) -> MazeType:
        return MazeType.TWO_DIM
