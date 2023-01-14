from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget, QApplication, QStyle
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QSettings

import sys
import pathlib

from ui import UI


class App(QWidget):
    def __init__(self):
        super().__init__()
        # --------
        # Settings
        # --------
        # self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        # self.language_value = int(self.settings.value('language'))
        # self.theme_value = eval(self.settings.value('theme'))
        # self.default_path = self.settings.value('default_path')

        # ----------------
        # Generación de UI
        # ----------------
        self.ui = UI(self)


if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec())
