"""
PySide6 Icon Button component adapted to follow Material Design 3 guidelines

"""
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from icon_color import icon_color

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
            theme_style: bool
                App theme style
                True: Light theme, False: Dark theme
            theme_color: str
                App theme color name
            clicked: def
                Icon button 'clicked' method name
        
        Returns
        -------
        None
        """
        super(MD3IconButton, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent
        x, y = attributes['position'] if 'position' in attributes else (8,8)
        self.setGeometry(x, y, 32, 32)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setAutoRaise(True)

        # Icon Button Styling
        if attributes['type'] in ['filled', 'tonal']:
            color = 'black'
        elif attributes['type'] in ['outlined', 'standard']:
            color = self.attributes['theme_style']
        colorized_icon = icon_color(color, self.attributes['icon'])

        self.setIcon(QtGui.QIcon(f"{icon_path}"))
        self.setProperty(self.attributes['type'], True)
        
        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True
        self.clicked.connect(attributes['clicked'])