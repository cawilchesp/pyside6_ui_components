"""
PyQt Segmented Button component adapted to follow Material Design 3 guidelines


"""

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt

from components.style_color import colors

import sys

# ----------------
# Segmented Button
# ----------------
class MD3SegmentedButton(QtWidgets.QToolButton):
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
        super(MD3SegmentedButton, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)

        self.apply_styleSheet(attributes['theme'])
        self.set_state(attributes['state'], attributes['theme'])
        self.language_text(attributes['language'])
        

    def set_state(self, state: bool, theme: bool) -> None:
        """ Set button state and corresponding icon """

        if theme: icon_theme = 'L'
        else: icon_theme = 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'
        if state:
            self.setIcon(QtGui.QIcon(f'{images_path}/done_{icon_theme}.png'))
            self.setChecked(True)
        else:
            if 'icon' in self.attributes:
                self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_{icon_theme}.png'))
            else:
                self.setIcon(QtGui.QIcon(f'{images_path}/none_{icon_theme}.png'))
            self.setChecked(False)


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        color = colors(theme, 'on_secondary_container')
        checked_background_color = colors(theme, 'secondary_container')
        checked_color = colors(theme, 'on_secondary_container')
        border_color = colors(theme, 'outline')

        if theme: icon_theme = 'L'
        else: icon_theme = 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'
        if 'icon' in self.attributes:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_{icon_theme}.png'))
        else:
            self.setIcon(QtGui.QIcon(f'{images_path}/none_{icon_theme}.png'))

        if self.attributes['location'] == 'left':
            border_position = 'border-top-left-radius: 16; border-bottom-left-radius: 16'
        elif self.attributes['location'] == 'center':
            border_position = 'border-radius: 0'
        elif self.attributes['location'] == 'right':
            border_position = 'border-top-right-radius: 16; border-bottom-right-radius: 16'
                
        self.setStyleSheet(f'QToolButton#{self.name} {{ '
                f'border: 1px solid {border_color};'
                f'{border_position};'
                f'padding: 0 8 0 8;'
                f'background-color: {background_color}; '
                f'color: {color} '
                f'}}'
                f'QToolButton#{self.name}:checked {{ '
                f'background-color: {checked_background_color};'
                f'color: {checked_color}'
                f'}}')


    def language_text(self, language: int) -> None:
        """ Change language of label text """
        if 'labels' in self.attributes:
            if language == 0:   self.setText(self.attributes['labels'][0])
            elif language == 1: self.setText(self.attributes['labels'][1])