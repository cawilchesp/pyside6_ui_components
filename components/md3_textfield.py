"""
PyQt Text Field component adapted to follow Material Design 3 guidelines


"""

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

from components.style_color import colors

import sys

# ----------
# Text Field
# ----------
class MD3TextField(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Text Field

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Text field position
                (x, y) -> x, y: upper left corner
            width: int
                Text field width
            labels: tuple
                Text field text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            enabled: bool
                Text field enabled / disabled
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
        super(MD3TextField, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 96
        self.setGeometry(x, y, w, 52)

        self.text_field = QtWidgets.QLineEdit(self)
        self.text_field.setGeometry(0, 8, w, 44)
        self.text_field.setClearButtonEnabled(True)

        if 'type' in attributes:
            pattern = None
            if attributes['type'] == 'integer':
                pattern = r"^[-+]?\d+$"
            elif attributes['type'] == 'double':
                pattern = r"^[-+]?\d+\.\d{2}$"
            
            elif attributes['type'] == 'text':
                pattern = r"[\p{L}\s]"
            elif attributes['type'] == 'email':
                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            elif attributes['type'] == 'ip':
                pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"


            pattern_size = ''
            if 'size' in attributes:
                pattern_size = f'{{1,{attributes["size"]}}}'
                

            regExp = QRegularExpressionValidator(QRegularExpression(f'{pattern}{pattern_size}'))
            
            self.text_field.setValidator(regExp)






        self.label_field = QtWidgets.QLabel(self)
        self.label_field.setGeometry(8, 0, 16, 16)
        self.label_field.setFont(QtGui.QFont('Segoe UI', 9))

        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.setThemeStyle(attributes['theme'])
        self.setLanguage(attributes['language'])


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        color = colors(theme, 'on_surface')

        disabled_background_color = colors(theme, 'surface_variant')
        disabled_color = colors(theme, 'on_surface_variant')
            
        self.setStyleSheet(f'QFrame {{ '
                f'border: 0px solid; '
                f'border-radius: 4; '
                f'background-color: {background_color} }}'
                f'QFrame:!enabled {{ '
                f'background-color: {disabled_background_color};'
                f'color: {disabled_color}'
                f'}}'

                f'QLineEdit {{ '
                f'border: 1px solid {color}; '
                f'border-radius: 4;'
                f'padding: 0 8 0 8; '
                f'background-color: {background_color}; '
                f'color: {color} }}'
                f'QLineEdit:!enabled {{ '
                f'background-color: {disabled_background_color};'
                f'color: {disabled_color}'
                f'}}'

                f'QLabel {{ '
                f'border: 0px solid; '
                f'padding: 0 4 0 4;'
                f'background-color: {background_color}; '
                f'color: {color} }}')


    def setLanguage(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.label_field.setText(self.attributes['labels'][0])
        elif language == 1: self.label_field.setText(self.attributes['labels'][1])
        self.label_field.adjustSize()