"""
Created on 2 May 2016

@author: Martin Vidjeskog
"""


from PyQt5.QtCore import Qt

from pymaze.gui.maze_painter import MazePainter
from pymaze.maze.piece.piece_type import PieceType


def handle_key_press_event(e, maze_drawing_widget: MazePainter):
    """Handle key press event."""
    # make sure that player exists
    if maze_drawing_widget.player is None:
        return

    # check event type
    if e.key() == Qt.Key_W:  # type: ignore
        __move_up(maze_drawing_widget)
    elif e.key() == Qt.Key_S:  # type: ignore
        __move_down(maze_drawing_widget)
    elif e.key() == Qt.Key_A:  # type: ignore
        __move_left(maze_drawing_widget)
    elif e.key() == Qt.Key_D:  # type: ignore
        __move_right(maze_drawing_widget)

    maze_drawing_widget.update()


def __move_up(maze_drawing_widget: MazePainter):
    """Move player up."""
    if maze_drawing_widget.player is None or maze_drawing_widget.maze is None:
        return

    x, y = maze_drawing_widget.player.get_location()

    if maze_drawing_widget.maze.get_piece(x, y).is_allowed_to_move_up():
        piece = maze_drawing_widget.maze.get_piece(x, y - 1)
        maze_drawing_widget.player.move_player(piece, x, y - 1)
        y -= 1

        while piece.get_piece_type() == PieceType.BRIDGE_HORIZONTAL_PIECE:
            piece = maze_drawing_widget.maze.get_piece(x, y - 1)
            maze_drawing_widget.player.move_player(piece, x, y - 1)
            y -= 1


def __move_down(maze_drawing_widget: MazePainter):
    """Move player down."""
    if maze_drawing_widget.player is None or maze_drawing_widget.maze is None:
        return

    x, y = maze_drawing_widget.player.get_location()

    if maze_drawing_widget.maze.get_piece(x, y).is_allowed_to_move_down():
        piece = maze_drawing_widget.maze.get_piece(x, y + 1)
        maze_drawing_widget.player.move_player(piece, x, y + 1)
        y += 1

        while piece.get_piece_type() == PieceType.BRIDGE_HORIZONTAL_PIECE:
            piece = maze_drawing_widget.maze.get_piece(x, y + 1)
            maze_drawing_widget.player.move_player(piece, x, y + 1)
            y += 1


def __move_left(maze_drawing_widget: MazePainter):
    """Move player left."""
    if maze_drawing_widget.player is None or maze_drawing_widget.maze is None:
        return

    x, y = maze_drawing_widget.player.get_location()

    if maze_drawing_widget.maze.get_piece(x, y).is_allowed_to_move_left():
        piece = maze_drawing_widget.maze.get_piece(x - 1, y)
        maze_drawing_widget.player.move_player(piece, x - 1, y)
        x -= 1

        while piece.get_piece_type() == PieceType.BRIDGE_VERTICAL_PIECE:
            piece = maze_drawing_widget.maze.get_piece(x - 1, y)
            maze_drawing_widget.player.move_player(piece, x - 1, y)
            x -= 1


def __move_right(maze_drawing_widget: MazePainter):
    """Move player right."""
    if maze_drawing_widget.player is None or maze_drawing_widget.maze is None:
        return

    x, y = maze_drawing_widget.player.get_location()

    if maze_drawing_widget.maze.get_piece(x, y).is_allowed_to_move_right():
        piece = maze_drawing_widget.maze.get_piece(x + 1, y)
        maze_drawing_widget.player.move_player(piece, x + 1, y)
        x += 1

        while piece.get_piece_type() == PieceType.BRIDGE_VERTICAL_PIECE:
            piece = maze_drawing_widget.maze.get_piece(x + 1, y)
            maze_drawing_widget.player.move_player(piece, x + 1, y)
            x += 1
