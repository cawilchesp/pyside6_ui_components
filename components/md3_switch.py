"""
PyQt Icon Button component adapted to follow Material Design 3 guidelines


"""

from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt

from components.style_color import colors

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
            theme: bool
                App theme
                True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(MD3Switch, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (0, 0)
        self.setGeometry(x, y, 26, 32)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setCheckable(True)

        self.apply_styleSheet(attributes['theme'])
        self.set_state(attributes['state'], attributes['theme'])
        

    def set_state(self, state: bool, theme: bool) -> None:
        """ Set button state and corresponding icon """

        if theme: icon_theme = 'L'
        else: icon_theme = 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'
        if state:
            if self.attributes['side'] == 'left':
                self.setIcon(QtGui.QIcon(f'{images_path}/none_{icon_theme}.png'))
            else:
                self.setIcon(QtGui.QIcon(f'{images_path}/circle_checked_{icon_theme}.png'))
            self.setChecked(True)
        else:
            if self.attributes['side'] == 'left':
                self.setIcon(QtGui.QIcon(f'{images_path}/circle_{icon_theme}.png'))
            else:
                self.setIcon(QtGui.QIcon(f'{images_path}/none_{icon_theme}.png'))
            self.setChecked(False)
        self.setIconSize(QtCore.QSize(16,16))

        self.apply_styleSheet(self.attributes['theme'])


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        
        background_color = colors(theme, 'surface_variant')
        checked_background_color = colors(theme, 'secondary_container')
        border_color = colors(theme, 'outline')

        border_outline = (f'border-top: 2px solid {border_color}; '
                          f'border-{self.attributes["side"]}: 2px solid {border_color}; '
                          f'border-bottom: 2px solid {border_color}')
        border_position = (f'border-top-{self.attributes["side"]}-radius: 16; '
                           f'border-bottom-{self.attributes["side"]}-radius: 16')
        
        self.setStyleSheet(f'QToolButton#{self.name} {{ '
                           f'{border_outline}; '
                           f'{border_position};'
                           f'background-color: {background_color}; '
                           f'}}'
                           f'QToolButton#{self.name}:checked {{ '
                           f'border: 0px solid; '
                           f'{border_position};'
                           f'background-color: {checked_background_color};'
                           f'}}')


    def language_text(self, language: int) -> None:
        """ Change language of switch text """
        return 0