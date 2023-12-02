"""
Created on 21 Oct 2023

@author: Martin Vidjeskog
"""

from enum import Enum


class GameState(Enum):
    """Different game states."""

    DEFAULT = 0
    MAZE = 1
    GAME = 2
    SOLUTION = 3
