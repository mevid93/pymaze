"""
Created on 13 Apr 2016

@author: Martin Vidjeskog
"""


import copy
from typing import List, Optional

from pymaze.maze.generator.maze import Maze
from pymaze.maze.piece.piece import Piece
from pymaze.maze.piece.piece_type import PieceType


def solve_maze(input_maze: Optional[Maze]) -> Optional[Maze]:
    """Solve maze and draw the solution to game window."""
    # check input
    if input_maze is None:
        return None

    # create copy of the input maze
    maze = copy.deepcopy(input_maze)

    # define starting position
    x = int(maze.get_width() / 2)
    y = int(maze.get_height() / 2)

    # find target position
    end_x = 0
    end_y = 0
    target_found = False
    for i in range(maze.get_height()):
        for j in range(maze.get_width()):
            if maze.get_piece(j, i).get_piece_type() == PieceType.TARGET_PIECE:
                end_x = j
                end_y = i
                target_found = True
                break
        if target_found is True:
            break

    # do depth first search until target is found
    visit_piece((x, y), (end_x, end_y), maze)

    # return modified maze, where solution path is visible
    return maze


def visit_piece(current: tuple[int, int], target: tuple[int, int], maze: Maze) -> bool:
    """Visit a piece."""
    # extract coordinates of current piece and target piece
    x, y = current
    end_x, end_y = target

    # if target is reached, end recursion and return true
    if x == end_x and y == end_y:
        return True

    # get current piece
    current_piece = maze.get_piece(x, y)

    # if current piece is a bridge piece, it is possible that it has been visited before
    # if this is the case, then we need to make sure that we do not reset its state
    bridge_piece_already_visited = False
    if is_bridge_piece(current_piece) and current_piece.is_part_of_solution():
        bridge_piece_already_visited = True

    # if current piece is not a bridge piece and it is aready marked as part of solution,
    # then return False, since no solution was found from this path
    if not is_bridge_piece(current_piece) and current_piece.is_part_of_solution():
        return False

    # include current piece to the possible solution path (mark it as visited)
    current_piece.set_part_of_solution(True)

    # 1. handle up direction
    if current_piece.is_allowed_to_move_up():
        visited_pieces: List[Piece] = []
        visited_already: List[bool] = []
        next_y = y - 1
        # visits pieces until next piece is not of type BRIDGE_HORIZONTAL_PIECE
        while True:
            next_piece = maze.get_piece(x, next_y)
            visited_pieces.append(next_piece)
            visited_already.append(next_piece.is_part_of_solution())
            if next_piece.get_piece_type() != PieceType.BRIDGE_HORIZONTAL_PIECE:
                break
            next_piece.set_part_of_solution(True)
            next_y -= 1
        # try to visit next piece
        result = visit_piece((x, next_y), target, maze)
        if result:
            return True
        # solution was not found, so we need to undo visits
        while len(visited_pieces) != 0:
            next_piece = visited_pieces.pop()
            if not visited_already.pop():
                next_piece.set_part_of_solution(False)

    # 2. handle right direction
    if current_piece.is_allowed_to_move_right():
        visited_pieces: List[Piece] = []
        visited_already: List[bool] = []
        next_x = x + 1
        # visits pieces until next piece is not of type BRIDGE_VERTICAL_PIECE
        while True:
            next_piece = maze.get_piece(next_x, y)
            visited_pieces.append(next_piece)
            visited_already.append(next_piece.is_part_of_solution())
            if next_piece.get_piece_type() != PieceType.BRIDGE_VERTICAL_PIECE:
                break
            next_piece.set_part_of_solution(True)
            next_x += 1
        # try to visit next piece
        result = visit_piece((next_x, y), target, maze)
        if result:
            return True
        # solution was not found, so we need to undo visits
        while len(visited_pieces) != 0:
            next_piece = visited_pieces.pop()
            if not visited_already.pop():
                next_piece.set_part_of_solution(False)

    # 3. handle down direction
    if current_piece.is_allowed_to_move_down():
        visited_pieces: List[Piece] = []
        visited_already: List[bool] = []
        next_y = y + 1
        # visits pieces until next piece is not of type BRIDGE_HORIZONTAL_PIECE
        while True:
            next_piece = maze.get_piece(x, next_y)
            visited_pieces.append(next_piece)
            visited_already.append(next_piece.is_part_of_solution())
            if next_piece.get_piece_type() != PieceType.BRIDGE_HORIZONTAL_PIECE:
                break
            next_piece.set_part_of_solution(True)
            next_y += 1
        # try to visit next piece
        result = visit_piece((x, next_y), target, maze)
        if result:
            return True
        # solution was not found, so we need to undo visits
        while len(visited_pieces) != 0:
            next_piece = visited_pieces.pop()
            if not visited_already.pop():
                next_piece.set_part_of_solution(False)

    # 4. handle left direction
    if current_piece.is_allowed_to_move_left():
        visited_pieces: List[Piece] = []
        visited_already: List[bool] = []
        next_x = x - 1
        # visits pieces until next piece is not of type BRIDGE_VERTICAL_PIECE
        while True:
            next_piece = maze.get_piece(next_x, y)
            visited_pieces.append(next_piece)
            visited_already.append(next_piece.is_part_of_solution())
            if next_piece.get_piece_type() != PieceType.BRIDGE_VERTICAL_PIECE:
                break
            next_piece.set_part_of_solution(True)
            next_x -= 1
        # try to visit next piece
        result = visit_piece((next_x, y), target, maze)
        if result:
            return True
        # solution was not found, so we need to undo visits
        while len(visited_pieces) != 0:
            next_piece = visited_pieces.pop()
            if not visited_already.pop():
                next_piece.set_part_of_solution(False)

    # ending up here means that no solution was found
    if not bridge_piece_already_visited:
        current_piece.set_part_of_solution(False)
    return False


def is_bridge_piece(piece: Piece) -> bool:
    """Return true if piece is bridge piece."""
    return piece.get_piece_type() in [
        PieceType.BRIDGE_HORIZONTAL_PIECE,
        PieceType.BRIDGE_VERTICAL_PIECE,
    ]
