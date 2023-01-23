"""
PyQt Segmented Button component adapted to follow Material Design 3 guidelines


"""

from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt

from components.style_color import colors

import sys

# ----------------
# Segmented Button
# ----------------
class MD3Segmented(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Segmented Button

        Parameters
        ----------
        name: str
            Widget name
        position: tuple
                Button position
                (x, y) -> x, y: upper left corner
        width: tuple
            Button width
        labels: tuple
            Segmented button text
            (label_es, label_en) -> label_es: label in spanish, label_en: label in english
        icon: str
            Icon file without extension ('icon')
        location: str
            Position of the segmented button in the group
            Options: 'left', 'center', 'right'
        state: bool
            State of activation
            True: On, False: Off
        theme: bool
            App theme
            True: Light theme, False: Dark theme
        language: int
            App language
            0: Spanish, 1: English
        
        Returns
        -------
        None
        """
        super(MD3Segmented, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 300
        self.setGeometry(x, y, w, 32)

        