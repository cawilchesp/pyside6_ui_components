"""
PySide6 Chip component adapted to follow Material Design 3 guidelines

"""

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

import sys

# ----
# Chip
# ----
class MD3Chip(QtWidgets.QToolButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Chip

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Chip position
                (x, y) -> x, y: upper left corner
            width: int
                Chip width
            labels: tuple
                Chip text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            icon: str (Optional)
                Icon file without extension ('icon')
            state: bool
                State of activation
                True: On, False: Off
            enabled: bool
                Chip enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            language: int
                App language
                0: Spanish, 1: English
            clicked: def
                Chip 'clicked' method name
        
        Returns
        -------
        None
        """
        super(MD3Chip, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)

        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.set_state(attributes['state'], attributes['theme'])
        self.set_language(attributes['language'])

        self.clicked.connect(attributes['clicked'])

        
    def set_state(self, state: bool, theme: bool) -> None:
        """ Set button state and corresponding icon """
        
        self.setChecked(state)
        icon_theme = 'L' if theme else 'D'
        icon_image = self.attributes['icon'] if 'icon' in self.attributes else 'none'
        if state:
            icon_image = 'done'
        self.setIcon(QtGui.QIcon(f'icons/{icon_image}_{icon_theme}.png'))


    def set_language(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.setText(self.attributes['labels'][0])
        elif language == 1: self.setText(self.attributes['labels'][1])