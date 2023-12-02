"""
Created on 5 Mar 2016

@author: Martin Vidjeskog
"""


from pymaze.maze.generator.maze import Maze
from pymaze.maze.generator.maze_type import MazeType
from pymaze.maze.generator.weave_maze_generator import generate_weave_maze


class WeaveMaze(Maze):
    """Weave maze class."""

    def __init__(self, width, height) -> None:
        super().__init__(width, height)
        self._pieces = generate_weave_maze(self._width, self._height)

    def get_type(self) -> MazeType:
        return MazeType.WEAVE
