"""
PyQt Button component adapted to follow Material Design 3 guidelines

"""

from PyQt6 import QtGui, QtWidgets

from components.style_color import colors

import sys

# --------------
# Common Buttons
# --------------
class MD3Button(QtWidgets.QPushButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Common Buttons

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Button position
                (x, y) -> x, y: upper left corner
            width: tuple
                Button width
            type: str
                Button type
                'elevated', 'filled', 'tonal', 'outlined', 'text'
            icon: str (Optional)
                Icon file without extension ('icon')
            labels: tuple
                Item label text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
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
        super(MD3Button, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        self.setThemeStyle(attributes['theme'])
        self.setLanguage(attributes['language'])

        self.clicked.connect(attributes['clicked'])


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.attributes['type'] == 'filled':
            background_color = colors(theme, 'primary')
            color = colors(theme, 'on_primary')
            hover_background_color = colors(theme, 'hover_primary')
            hover_color = colors(theme, 'on_primary')
        elif self.attributes['type'] == 'tonal':
            background_color = colors(theme, 'secondary_container')
            color = colors(theme, 'on_secondary_container')
            hover_background_color = colors(theme, 'hover_secondary_container')
            hover_color = colors(theme, 'on_secondary_container')
        elif self.attributes['type'] in ('outlined', 'text'):
            if self.parent.attributes['type'] == 'filled':
                background_color = colors(theme, 'surface_tint')
            elif self.parent.attributes['type'] == 'outlined':
                background_color = colors(theme, 'background')
            color = colors(theme, 'primary')
            hover_background_color = colors(theme, 'primary_container')
            hover_color = colors(theme, 'primary')
        disabled_color = colors(theme, 'surface_variant')

        thickness = 2 if self.attributes['type'] == 'outlined' else 0
        border_color = colors(theme, 'outline') if self.attributes['type'] == 'outlined' else None

        if 'icon' in self.attributes:
            if theme: icon_theme = 'L'
            else: icon_theme = 'D'
            current_path = sys.path[0].replace("\\","/")
            images_path = f'{current_path}/icons'
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_{icon_theme}.png'))

        self.setStyleSheet(f'QPushButton#{self.name} {{ '
                f'border: {thickness}px solid {border_color};'
                f'border-radius: 16;'
                f'background-color: {background_color};'
                f'color: {color};'
                f'}}'
                f'QPushButton#{self.name}:hover {{ '
                f'background-color: {hover_background_color};'
                f'color: {hover_color};'
                f'}}'
                f'QPushButton#{self.name}:!enabled {{ '
                f'color: {disabled_color}'
                f'}}')
              

    def setLanguage(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.setText(self.attributes['labels'][0])
            elif language == 1: self.setText(self.attributes['labels'][1])