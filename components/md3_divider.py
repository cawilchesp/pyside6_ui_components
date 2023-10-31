"""
PySide6 Divider component adapted to follow Material Design 3 guidelines

"""

from PySide6 import QtWidgets

import sys

# -------
# Divider
# -------
class MD3Divider(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Divider

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Divider position
                (x, y) -> x, y: upper left corner
            size: tuple
                Divider size
                (w, h) -> w: width, h: height
            theme: bool
                App theme
                True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(MD3Divider, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        if attributes['shape'] == 'horizontal':
            w = attributes['length'] if 'length' in attributes else 32
            h = 1
            self.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        elif attributes['shape'] == 'vertical':
            w = 1
            h = attributes['length'] if 'length' in attributes else 32
            self.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.setGeometry(x, y, w, h)

        self.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
