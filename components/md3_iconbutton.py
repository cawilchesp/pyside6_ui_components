"""
PyQt Icon Button component adapted to follow Material Design 3 guidelines

"""

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt

from components.style_color import colors

import sys

# -----------
# Icon Button
# -----------
class MD3IconButton(QtWidgets.QToolButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Icon Button

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Card position
                (x, y) -> x, y: upper left corner
            type: str
                Label type
                'filled', 'tonal', 'outlined', 'standard'
            icon: str
                Icon file without extension ('icon')
            theme: bool
                App theme
                True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(MD3IconButton, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        self.setGeometry(x, y, 32, 32)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setAutoRaise(True)
        
        self.setThemeStyle(attributes['theme'])


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.attributes['type'] == 'filled':
            background_color = colors(theme, 'primary')
            hover_background_color = colors(theme, 'hover_primary')
        elif self.attributes['type'] == 'tonal':
            background_color = colors(theme, 'secondary_container')
            hover_background_color = colors(theme, 'hover_secondary_container')
        elif self.attributes['type'] == 'outlined':
            if self.parent.attributes['type'] == 'filled':
                background_color = colors(theme, 'surface_tint')
            elif self.parent.attributes['type'] == 'outlined':
                background_color = colors(theme, 'background')
            hover_background_color = colors(theme, 'primary_container')
        elif self.attributes['type'] == 'standard':
            if self.parent.attributes['type'] == 'filled':
                background_color = colors(theme, 'surface_tint')
            elif self.parent.attributes['type'] == 'outlined':
                background_color = colors(theme, 'background')
            hover_background_color = colors(theme, 'primary_container')
        thickness = 2 if self.attributes['type'] == 'outlined' else 0
        border_color = colors(theme, 'outline') if self.attributes['type'] == 'outlined' else None

        if theme: icon_theme = 'L'
        else: icon_theme = 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'
        self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_{icon_theme}.png'))
            
        self.setStyleSheet(f'QToolButton#{self.name} {{ '
                f'border: {thickness}px solid {border_color};'
                f'border-radius: 16;'
                f'background-color: {background_color};'
                f'}}'
                f'QToolButton#{self.name}:hover {{ '
                f'background-color: {hover_background_color};'
                f'}}')
