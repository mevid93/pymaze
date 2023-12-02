"""
Created on 21 Oct 2023

@author: Martin Vidjeskog
"""


from enum import Enum


class Direction(Enum):
    """Different movement directions."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH_BRIDGE = 4
    EAST_BRIDGE = 5
    SOUTH_BRIDGE = 6
    WEST_BRIDGE = 7
