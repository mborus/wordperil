from enum import Enum

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt


class ControllerMode(Enum):
    SETUP = 0
    PLAYERS = 1
    SCORE = 2
    PUZZLE = 3


class Controller(QWidget):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.window = parent
        self.setFocusPolicy(Qt.StrongFocus)

    def setMode(self, mode):
        if (
            mode != ControllerMode.SETUP and
            mode != ControllerMode.PLAYERS and
            mode != ControllerMode.SCORE and
            mode != ControllerMode.PUZZLE
        ):
            raise ValueError("Invalid ControllerMode specified.")

        self.mode = mode

    def keyPressEvent(self, event):
        if self.mode == ControllerMode.SETUP:
            self.setupControl(event)
        elif self.mode == ControllerMode.PLAYERS:
            self.playersControl(event)
        elif self.mode == ControllerMode.SCORE:
            self.scoreControl(event)
        elif self.mode == ControllerMode.PUZZLE:
            self.puzzleControl(event)

    def setupControl(self, event):
        if event.key() == Qt.Key_L:
            print("Load")
        # elif event.key() == Qt.Key_P:
        #     print("Players Toggle")
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.window.playersMode()

    def playersControl(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.window.scoreMode()
        elif event.key() == Qt.Key_Escape:
            self.window.setupMode()

    def scoreControl(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.window.puzzleMode()
        elif event.key() == Qt.Key_Escape:
            self.window.setupMode()

    def puzzleControl(self, event):
        letters = [
            Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E, Qt.Key_F,
            Qt.Key_G, Qt.Key_H, Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L,
            Qt.Key_M, Qt.Key_N, Qt.Key_O, Qt.Key_P, Qt.Key_Q, Qt.Key_R,
            Qt.Key_S, Qt.Key_T, Qt.Key_U, Qt.Key_V, Qt.Key_W, Qt.Key_X,
            Qt.Key_Y, Qt.Key_Z]

        if event.key() in letters:
            print(event.text())
        # elif event.key() == Qt.Key_Escape:
        #     print("Abort")
