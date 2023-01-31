"""
PyQt Text Field component adapted to follow Material Design 3 guidelines


"""

from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import QRegularExpression, Qt
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
        geometry: tuple
            Text Field position and width
            (x, y, w) -> x, y: upper left corner, w: width
        labels: tuple
            Text Field text
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
            if attributes['type'] == 'numbers':
                text_type = '[0-9]'
            elif attributes['type'] == 'text':
                text_type = '[\p{L}\s]'
            elif attributes['type'] == 'email':
                text_type = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            elif attributes['type'] == 'ip':
                text_type = '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
            

            text_size = f'1,{attributes["size"]}'# if attributes['type'] != 'ip' else None
            
            self.text_field.setValidator(QRegularExpressionValidator(QRegularExpression(f'{text_type}{{{text_size}}}'), self))






        self.label_field = QtWidgets.QLabel(self)
        self.label_field.setGeometry(8, 0, 16, 16)
        self.label_field.setFont(QtGui.QFont('Segoe UI', 9))

        self.apply_styleSheet(attributes['theme'])
        self.language_text(attributes['language'])


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        color = colors(theme, 'on_surface')
            
        self.setStyleSheet(f'QFrame {{ '
                f'background-color: {background_color} }}'
                f'QLineEdit {{ '
                f'border: 1px solid {color}; '
                f'border-radius: 4;'
                f'padding: 0 8 0 8; '
                f'background-color: {background_color}; '
                f'color: {color} }}'
                f'QLabel {{ '
                f'border: 0px solid; '
                f'padding: 0 4 0 4;'
                f'background-color: {background_color}; '
                f'color: {color} }}')


    def language_text(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.label_field.setText(self.attributes['labels'][0])
        elif language == 1: self.label_field.setText(self.attributes['labels'][1])
        self.label_field.adjustSize()