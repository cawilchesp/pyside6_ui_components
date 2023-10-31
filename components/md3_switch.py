"""
PySide6 Icon Button component adapted to follow Material Design 3 guidelines


"""

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import Qt

import sys

# ------
# Switch
# ------
class MD3Switch(QtWidgets.QToolButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Switch

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Switch position
                (x, y) -> x, y: upper left corner
            side: str
                Switch button side
                'left', 'right'
            state: bool
                State of activation
                True: On, False: Off
            enabled: bool
                Switch enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            clicked: def
                Switch 'clicked' method name
        
        Returns
        -------
        None
        """
        super(MD3Switch, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        x, y = attributes['position'] if 'position' in attributes else (0, 0)
        self.setGeometry(x, y, 26, 32)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setCheckable(True)
        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.setProperty(attributes['side'], True)
        self.setState(attributes['state'], attributes['theme'])

        self.clicked.connect(attributes['clicked'])
        

    def setState(self, state: bool, theme: bool) -> None:
        """ Set button state and corresponding icon """
        self.setChecked(state)
        
        icon_theme = 'L' if theme else 'D'
        icon_state = {
            True: { 'left': 'none', 'right': 'circle_checked' },
            False: { 'left': 'circle', 'right': 'none' }
        }
        icon_image = icon_state[state][self.attributes['side']]
        self.setIcon(QtGui.QIcon(f'icons/{icon_image}_{icon_theme}.png'))
        self.setIconSize(QtCore.QSize(16,16))
