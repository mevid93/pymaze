"""
Created on 5 Mar 2016

@author: Martin Vidjeskog
"""

import random
from typing import List, Optional

from pymaze.maze.direction import Direction
from pymaze.maze.piece.horizontal_left_blocked_piece import HorizontalLeftBlockedPiece
from pymaze.maze.piece.horizontal_piece import HorizontalPiece
from pymaze.maze.piece.horizontal_right_blocked_piece import HorizontalRightBlockedPiece
from pymaze.maze.piece.intersection_down_piece import IntersectionDownPiece
from pymaze.maze.piece.intersection_left_piece import IntersectionLeftPiece
from pymaze.maze.piece.intersection_piece import IntersectionPiece
from pymaze.maze.piece.intersection_right_piece import IntersectionRightPiece
from pymaze.maze.piece.intersection_up_piece import IntersectionUpPiece
from pymaze.maze.piece.piece import Piece
from pymaze.maze.piece.target_piece import TargetPiece
from pymaze.maze.piece.turn_ne_piece import TurnNEPiece
from pymaze.maze.piece.turn_nw_piece import TurnNWPiece
from pymaze.maze.piece.turn_se_piece import TurnSEPiece
from pymaze.maze.piece.turn_sw_piece import TurnSWPiece
from pymaze.maze.piece.vertical_bottom_blocked_piece import VerticalBottomBlockedPiece
from pymaze.maze.piece.vertical_piece import VerticalPiece
from pymaze.maze.piece.vertical_top_blocked_piece import VerticalTopBlockedPiece


def generate_two_dimensional_maze(width: int, height: int) -> List[List[Piece]]:
    """Generate two dimensional maze.

    width: maze width (number of pieces)
    height: maze height (number of pieces)
    """
    # initialize global variables
    pixels_side: int = int((775 - 275) / width)
    directions: List[List[List[Direction]]] = [
        [[] for x in range(width)] for y in range(height)
    ]

    # starting point
    begin_x = int(width / 2)
    begin_y = int(height / 2)

    # generate end point
    goal_x = random.randint(0, width - 1)
    goal_y = random.choice([0, height - 1])

    if random.randint(0, 1) == 1:
        goal_x = random.choice([0, width - 1])
        goal_y = random.randint(0, height - 1)

    # generate maze
    current_coordinate = (begin_x, begin_y)
    end_coordinate = (goal_x, goal_y)
    size = (width, height)
    __recursive_backtracking(size, current_coordinate, end_coordinate, None, directions)
    return __transform_directions_to_pieces(
        size, end_coordinate, directions, pixels_side
    )


def __recursive_backtracking(
    size: tuple[int, int],
    current_coordinate: tuple[int, int],
    end_coordinate: tuple[int, int],
    direction: Optional[Direction],
    directions: List[List[List[Direction]]],
) -> None:
    """Visit all map coordinates and generate a list of directions for each coordinate."""
    x, y = current_coordinate
    if direction == Direction.NORTH:
        directions[y][x].append(Direction.SOUTH)
    elif direction == Direction.SOUTH:
        directions[y][x].append(Direction.NORTH)
    elif direction == Direction.EAST:
        directions[y][x].append(Direction.WEST)
    elif direction == Direction.WEST:
        directions[y][x].append(Direction.EAST)

    goal_x, goal_y = end_coordinate
    if x == goal_x and y == goal_y:
        return

    possible_directions = [
        Direction.NORTH,
        Direction.SOUTH,
        Direction.EAST,
        Direction.WEST,
    ]

    random.shuffle(possible_directions)

    for i in range(0, 4):
        next_x = 0
        next_y = 0
        direction = possible_directions[i]

        if direction == Direction.NORTH:
            next_x = x
            next_y = y - 1
        elif direction == Direction.SOUTH:
            next_x = x
            next_y = y + 1
        elif direction == Direction.EAST:
            next_x = x + 1
            next_y = y
        elif direction == Direction.WEST:
            next_x = x - 1
            next_y = y

        max_width = size[0]
        max_height = size[1]
        if next_x < max_width and next_x >= 0 and next_y < max_height and next_y >= 0:
            if not directions[next_y][next_x]:
                directions[y][x].append(direction)
                __recursive_backtracking(
                    size, (next_x, next_y), end_coordinate, direction, directions
                )


def __transform_directions_to_pieces(
    size: tuple[int, int],
    end_coordinate: tuple[int, int],
    directions: List[List[List[Direction]]],
    pixels_side: int,
) -> List[List[Piece]]:
    """Transform list of directions on each coordinate to corresponding piece."""
    width, height = size
    maze: List[List[Piece]] = [
        [TargetPiece(0, 0, 0, 0) for x in range(width)] for y in range(height)
    ]

    max_width = size[0]
    max_height = size[1]
    goal_x, goal_y = end_coordinate
    pixel_x = 275
    pixel_y = 25

    for y in range(max_height):
        for x in range(max_width):
            if x == goal_x and y == goal_y:
                maze[y][x] = TargetPiece(pixel_x, pixel_y, pixels_side, pixels_side)
            elif directions_list_are_equal([Direction.NORTH], directions[y][x]):
                maze[y][x] = VerticalBottomBlockedPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            elif directions_list_are_equal([Direction.EAST], directions[y][x]):
                maze[y][x] = HorizontalLeftBlockedPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            elif directions_list_are_equal([Direction.SOUTH], directions[y][x]):
                maze[y][x] = VerticalTopBlockedPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            elif directions_list_are_equal([Direction.WEST], directions[y][x]):
                maze[y][x] = HorizontalRightBlockedPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            elif directions_list_are_equal(
                [Direction.NORTH, Direction.EAST], directions[y][x]
            ):
                maze[y][x] = TurnNEPiece(pixel_x, pixel_y, pixels_side, pixels_side)
            elif directions_list_are_equal(
                [Direction.NORTH, Direction.SOUTH], directions[y][x]
            ):
                maze[y][x] = VerticalPiece(pixel_x, pixel_y, pixels_side, pixels_side)
            elif directions_list_are_equal(
                [Direction.NORTH, Direction.WEST], directions[y][x]
            ):
                maze[y][x] = TurnNWPiece(pixel_x, pixel_y, pixels_side, pixels_side)
            elif directions_list_are_equal(
                [Direction.EAST, Direction.SOUTH], directions[y][x]
            ):
                maze[y][x] = TurnSEPiece(pixel_x, pixel_y, pixels_side, pixels_side)
            elif directions_list_are_equal(
                [Direction.EAST, Direction.WEST], directions[y][x]
            ):
                maze[y][x] = HorizontalPiece(pixel_x, pixel_y, pixels_side, pixels_side)
            elif directions_list_are_equal(
                [Direction.SOUTH, Direction.WEST], directions[y][x]
            ):
                maze[y][x] = TurnSWPiece(pixel_x, pixel_y, pixels_side, pixels_side)
            elif directions_list_are_equal(
                [Direction.NORTH, Direction.EAST, Direction.SOUTH], directions[y][x]
            ):
                maze[y][x] = IntersectionRightPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            elif directions_list_are_equal(
                [Direction.NORTH, Direction.EAST, Direction.WEST], directions[y][x]
            ):
                maze[y][x] = IntersectionUpPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            elif directions_list_are_equal(
                [Direction.NORTH, Direction.WEST, Direction.SOUTH], directions[y][x]
            ):
                maze[y][x] = IntersectionLeftPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            elif directions_list_are_equal(
                [Direction.SOUTH, Direction.WEST, Direction.EAST], directions[y][x]
            ):
                maze[y][x] = IntersectionDownPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            else:
                maze[y][x] = IntersectionPiece(
                    pixel_x, pixel_y, pixels_side, pixels_side
                )
            pixel_x += pixels_side
        pixel_x = 275
        pixel_y += pixels_side
    return maze


def directions_list_are_equal(
    directions1: List[Direction], directions2: List[Direction]
):
    """Return true if the two arrays of directions are equal."""
    if len(directions1) != len(directions2):
        return False
    for i in directions1:
        if i not in directions2:
            return False
    return True
