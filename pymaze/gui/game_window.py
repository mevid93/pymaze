"""
Created on 4 Mar 2016

@author: Martin Vidjeskog
"""


import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from pymaze.file.file_manager import FileManager

from pymaze.gui.game_state import GameState
from pymaze.gui.key_press_handler import handle_key_press_event
from pymaze.gui.maze_painter import MazePainter
from pymaze.maze.generator.two_dim_maze import TwoDimMaze
from pymaze.maze.generator.weave_maze import WeaveMaze
from pymaze.maze.player import Player
from pymaze.maze.solver import solve_maze


PROGRAM_VERSION = "PyMaze V.0.4.0"
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720


class GameWindow(QtWidgets.QWidget):
    """Game window class."""

    def __init__(self):
        """Constructor."""
        super().__init__()
        self.__maze = None
        self.__gamestate = GameState.DEFAULT
        self.__init_view()
        self.__init_buttons_menu_widget()
        self.__init_program_info_widget()
        self.__init_maze_settings_widget()
        self.__init_maze_drawing_widget()
        self.__reset_main_area()

    def __init_view(self):
        # create window
        self.setMinimumSize(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        self.setAutoFillBackground(True)
        self.setUpdatesEnabled(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#808080"))
        self.setPalette(p)
        self.setWindowTitle(PROGRAM_VERSION)
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # different widgets
        self.__buttons_menu_widget = QtWidgets.QWidget()
        self.__program_info_widget = QtWidgets.QWidget()
        self.__maze_settings_widget = QtWidgets.QWidget()
        self.__maze_drawing_widget = MazePainter()

        # maze area widget
        main_area = QtWidgets.QWidget()
        p1 = main_area.palette()
        p1.setColor(main_area.backgroundRole(), QtGui.QColor("#E0E0E0"))
        main_area.setPalette(p1)
        main_area.setAutoFillBackground(True)
        main_area_layout = QtWidgets.QGridLayout()
        main_area_layout.addWidget(self.__program_info_widget, 0, 0)
        main_area_layout.addWidget(self.__maze_settings_widget, 0, 0)
        main_area_layout.addWidget(self.__maze_drawing_widget, 0, 0)
        main_area.setLayout(main_area_layout)

        # game window main layout
        self.__layout = QtWidgets.QHBoxLayout()
        self.__layout.addWidget(self.__buttons_menu_widget)
        self.__layout.addWidget(main_area, 2)
        self.setLayout(self.__layout)

    def __init_buttons_menu_widget(self):
        # layouy for button menu
        button_menu_layout = QtWidgets.QVBoxLayout()

        # button for generating maze
        button_min_width = 200
        button_min_height = 50
        button_max_width = 300
        button_max_height = 75
        generate_button = QtWidgets.QPushButton("Generate maze", self)
        generate_button.setMinimumSize(button_min_width, button_min_height)
        generate_button.setMaximumSize(button_max_width, button_max_height)
        generate_button.clicked.connect(self.__show_maze_generation_menu)
        button_menu_layout.addWidget(generate_button)

        # button for loading a maze
        load_button = QtWidgets.QPushButton("Load maze", self)
        load_button.setMinimumSize(button_min_width, button_min_height)
        load_button.setMaximumSize(button_max_width, button_max_height)
        load_button.clicked.connect(self.__load_maze)
        button_menu_layout.addWidget(load_button)

        # button for saving a maze
        save_button = QtWidgets.QPushButton("Save maze", self)
        save_button.setMinimumSize(button_min_width, button_min_height)
        save_button.setMaximumSize(button_max_width, button_max_height)
        save_button.clicked.connect(self.__save_maze)
        button_menu_layout.addWidget(save_button)

        # button for playing
        play_button = QtWidgets.QPushButton("Play", self)
        play_button.setMinimumSize(button_min_width, button_min_height)
        play_button.setMaximumSize(button_max_width, button_max_height)
        play_button.clicked.connect(self.__play_game)
        button_menu_layout.addWidget(play_button)

        # button for drawing solution
        demo_button = QtWidgets.QPushButton("Show solution", self)
        demo_button.setMinimumSize(button_min_width, button_min_height)
        demo_button.setMaximumSize(button_max_width, button_max_height)
        demo_button.clicked.connect(self.__show_solution)
        button_menu_layout.addWidget(demo_button)

        # button for showing program information
        info_button = QtWidgets.QPushButton("About", self)
        info_button.setMinimumSize(button_min_width, button_min_height)
        info_button.setMaximumSize(button_max_width, button_max_height)
        info_button.clicked.connect(self.__show_program_information)
        button_menu_layout.addWidget(info_button)

        # exit button
        exit_button = QtWidgets.QPushButton("Quit", self)
        exit_button.setMinimumSize(button_min_width, button_min_height)
        exit_button.setMaximumSize(button_max_width, button_max_height)
        exit_button.clicked.connect(sys.exit)
        button_menu_layout.addWidget(exit_button)

        # set layout for buttons
        self.__buttons_menu_widget.setLayout(button_menu_layout)

    def __init_program_info_widget(self):
        program_info_layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(PROGRAM_VERSION)
        label.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        label.setFont(QtGui.QFont("Arial", 20))
        program_info_layout.addWidget(label)

        label2 = QtWidgets.QLabel(
            "1. Press Generate maze button to open a settings menu for generating a new maze."
        )
        label2.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        program_info_layout.addWidget(label2)

        labelx = QtWidgets.QLabel(
            "2. Press Load maze button to load an existing maze from file."
        )
        labelx.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        program_info_layout.addWidget(labelx)

        label7 = QtWidgets.QLabel(
            "3. Press Save maze button to save the maze into a file."
        )
        label7.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        program_info_layout.addWidget(label7)

        text = "4. Press Play button to play the game."
        text += " Try to find the path to the green square.\n\n"
        text += "Keyboard mappings for moving the player in the maze.\n\n"
        text += "W = move up\n\n"
        text += "A = move left\n\n"
        text += "S = move down\n\n"
        text += "D = move right\n\n"
        label3 = QtWidgets.QLabel(text)
        label3.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        program_info_layout.addWidget(label3)

        label6 = QtWidgets.QLabel(
            "5. Press Show solution button to see the model solution."
        )
        label6.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        program_info_layout.addWidget(label6)

        label5 = QtWidgets.QLabel("6. Press About button to view program information.")
        label5.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        program_info_layout.addWidget(label5)

        label8 = QtWidgets.QLabel("7. Press Quit button to exit the application.")
        label8.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        program_info_layout.addWidget(label8)

        self.__program_info_widget.setLayout(program_info_layout)

    def __init_maze_settings_widget(self):
        maze_settings_layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Generate new maze")
        label.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        label.setFont(QtGui.QFont("Arial", 20))
        maze_settings_layout.addWidget(label)

        # section for maze type
        maze_type_widget = QtWidgets.QWidget()
        maze_type_layout = QtWidgets.QVBoxLayout()
        label2 = QtWidgets.QLabel("Select maze type")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        label2.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        label2.setFont(font)
        maze_type_layout.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        maze_type_layout.addWidget(label2)

        self.__check_box_2d_type = QtWidgets.QCheckBox("Standard 2D Maze", self)
        self.__check_box_2d_type.clicked.connect(lambda: self.__change_selection(False))
        maze_type_layout.addWidget(self.__check_box_2d_type)

        self.__check_box_weave_type = QtWidgets.QCheckBox("Weave Maze", self)
        self.__check_box_weave_type.clicked.connect(
            lambda: self.__change_selection(True)
        )
        maze_type_layout.addWidget(self.__check_box_weave_type)
        maze_type_widget.setLayout(maze_type_layout)
        maze_settings_layout.addWidget(maze_type_widget)

        # section for maze size
        maze_size_widget = QtWidgets.QWidget()
        maze_size_layout = QtWidgets.QVBoxLayout()
        label3 = QtWidgets.QLabel("Select maze width\n (min = 15, max = 50)")
        label3.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        label3.setFont(font)
        maze_size_layout.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        maze_size_layout.addWidget(label3)

        self.__size_spin_box = QtWidgets.QSpinBox()
        self.__size_spin_box.setMinimumHeight(30)
        self.__size_spin_box.setMinimum(15)
        self.__size_spin_box.setMaximum(50)
        self.__size_spin_box.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        maze_size_layout.addWidget(self.__size_spin_box)
        maze_size_widget.setLayout(maze_size_layout)

        maze_settings_layout.addWidget(maze_size_widget)

        # section for maze generation button
        maze_button_widget = QtWidgets.QWidget()
        maze_button_layout = QtWidgets.QVBoxLayout()
        generate_button = QtWidgets.QPushButton("Generate", self)
        generate_button.setMinimumSize(100, 40)
        generate_button.setMaximumSize(200, 65)
        generate_button.clicked.connect(self.__generate_maze)
        maze_button_layout.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        maze_button_layout.addWidget(generate_button)
        maze_button_widget.setLayout(maze_button_layout)
        maze_settings_layout.addWidget(maze_button_widget)

        maze_settings_layout.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        maze_settings_layout.setSpacing(50)
        self.__maze_settings_widget.setLayout(maze_settings_layout)

    def __init_maze_drawing_widget(self):
        pass

    def show_window(self) -> None:
        """Show game window."""
        self.show()

    def __save_maze(self) -> None:
        """Save maze to file."""
        if self.__maze is None:
            return

        FileManager.save_file(self, self.__maze)

    def __load_maze(self) -> None:
        """Load maze from file."""
        loaded_maze = FileManager.load_file(self)

        if loaded_maze is None:
            return

        self.__maze = loaded_maze
        self.__gamestate = GameState.MAZE
        self.__show_maze()
        self.update()

    def __reset_main_area(self):
        self.__program_info_widget.hide()
        self.__maze_settings_widget.hide()
        self.__maze_drawing_widget.hide()

    def __show_program_information(self) -> None:
        self.__reset_main_area()
        self.__program_info_widget.show()

    def __show_maze_generation_menu(self) -> None:
        self.__reset_main_area()
        self.__gamestate = GameState.DEFAULT
        self.__maze = None
        self.__maze_settings_widget.show()

    def __show_maze(self) -> None:
        if self.__maze is None:
            return
        self.__reset_main_area()
        self.__maze_drawing_widget.maze = self.__maze
        self.__maze_drawing_widget.player = None
        self.__maze_drawing_widget.show()

    def __show_solution(self) -> None:
        """Show solution for maze."""
        if self.__maze is None or self.__maze_drawing_widget.maze is None:
            return

        self.__gamestate = GameState.SOLUTION
        self.__show_maze()
        solved_maze = solve_maze(self.__maze)
        self.__maze_drawing_widget.maze = solved_maze
        self.update()

    def __change_selection(self, weave_selected: bool) -> None:
        self.__check_box_2d_type.setChecked(not weave_selected)
        self.__check_box_weave_type.setChecked(weave_selected)

    def __generate_maze(self) -> None:
        # validate that input had been given
        if (
            not self.__check_box_2d_type.isChecked()
            and not self.__check_box_weave_type.isChecked()
        ):
            return

        width = self.__size_spin_box.value()
        if width is None or width < 15 or width > 50:
            return

        # calculate maze height based on the given width
        height = int(0.67 * width)

        if self.__check_box_2d_type.isChecked():
            self.__maze = TwoDimMaze(width, height)
            self.__gamestate = GameState.MAZE
            self.__show_maze()
            self.update()
        elif self.__check_box_weave_type.isChecked():
            self.__maze = WeaveMaze(width, height)
            self.__gamestate = GameState.MAZE
            self.__show_maze()
            self.update()

    def __play_game(self) -> None:
        """Start the game."""
        if self.__maze is None or self.__maze_drawing_widget.maze is None:
            return

        self.__gamestate = GameState.GAME
        self.__show_maze()
        begin_x = int(self.__maze.get_width() / 2)
        begin_y = int(self.__maze.get_height() / 2)
        piece = self.__maze_drawing_widget.maze.get_piece(begin_x, begin_y)

        player = Player(piece, begin_x, begin_y)
        self.__maze_drawing_widget.player = player
        self.update()

    # pylint: disable-next=invalid-name
    def paintEvent(self, event):  # pylint: disable=unused-argument
        """Draw game window."""
        if self.__gamestate == GameState.DEFAULT:
            pass
        else:
            self.__maze_drawing_widget.update()

    # pylint: disable-next=invalid-name
    def keyPressEvent(self, e):
        """Handle keyboard inputs."""
        # check that objects are initialized
        if (
            self.__maze_drawing_widget.maze is None
            or self.__maze_drawing_widget.player is None
        ):
            return

        # if in game state, then handle key press event
        if self.__gamestate == GameState.GAME:
            handle_key_press_event(e, self.__maze_drawing_widget)

        # check if game ended
        # if it did, then show message to user
        # also reset the status after showing the message
        player = self.__maze_drawing_widget.player
        if not player.has_reached_target_piece():
            return

        msg = QtWidgets.QMessageBox(self)

        msg.setText(
            '<p style="font-size:30pt; color: #FF0000;"><center>Good job!</center></p>'
        )
        msg.setStyleSheet("QLabel {min-width: 300px; min-height: 125px;}")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        retval = msg.exec_()

        if retval == QtWidgets.QMessageBox.Ok:
            self.__gamestate = GameState.MAZE
            self.__show_maze()
