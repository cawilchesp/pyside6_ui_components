"""
PySide6 Icon Button component adapted to follow Material Design 3 guidelines

"""

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

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
                Icon button position
                (x, y) -> x, y: upper left corner
            type: str
                Icon button type
                'filled', 'tonal', 'outlined', 'standard'
            icon: str
                Icon file without extension
            enabled: bool
                Icon button enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            clicked: def
                Icon button 'clicked' method name
        
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

        icon_theme = 'L' if self.attributes['theme'] else 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'
        self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_{icon_theme}.png'))

        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True
        
        self.setProperty(self.attributes['type'], True)

        self.clicked.connect(attributes['clicked'])

    #     elif self.attributes['type'] in ('outlined','standard'):
    #         if self.parent.attributes['type'] == 'filled':
    #             background_color = colors(theme, 'surface_tint')
    #         elif self.parent.attributes['type'] == 'outlined':
    #             background_color = colors(theme, 'background')