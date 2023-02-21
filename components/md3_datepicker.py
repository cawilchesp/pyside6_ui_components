"""
PyQt Date Picker component adapted to follow Material Design 3 guidelines


"""

from PyQt6 import QtGui, QtWidgets, QtCore

from components.style_color import colors

import sys

# -----------
# Date Picker
# -----------
class MD3DatePicker(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Date Field

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Button position
                (x, y) -> x, y: upper left corner
            width: int
                Button width
            labels: tuple
                Date field text
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
        super(MD3DatePicker, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 96
        self.setGeometry(x, y, w, 52)

        self.text_field = QtWidgets.QDateEdit(self)
        self.text_field.setGeometry(0, 8, w, 44)
        
        self.text_field.setCalendarPopup(True)
        self.text_field.setFrame(False)
        self.text_field.setSpecialValueText('')
        self.text_field.setDate(QtCore.QDate.currentDate())
        
        self.label_field = QtWidgets.QLabel(self)
        self.label_field.setGeometry(8, 0, 16, 16)
        self.label_field.setFont(QtGui.QFont('Segoe UI', 9))

        self.setThemeStyle(attributes['theme'])
        self.setLanguage(attributes['language'])


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        color = colors(theme, 'on_surface')
        drop_background_color = colors(theme, 'primary')

        if theme: icon_theme = 'L'
        else: icon_theme = 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'

        self.setStyleSheet(f'QFrame {{ '
                f'background-color: {background_color} }}'
                
                f'QDateEdit {{ '
                f'border: 1px solid {color}; '
                f'border-radius: 4; '
                f'padding: 0 8 0 8;'
                f'background-color: {background_color}; '
                f'color: {color}; }}'

                f'QDateEdit::drop-down {{ '
                f'background-color: {drop_background_color};'
                f'width: 32; '
                f'height: 32; '
                f'subcontrol-position: center right; '
                f'left: -4;'
                f'border-radius: 16 }}'
                
                f'QDateEdit::down-arrow {{ '
                f'image: url({images_path}/calendar_{icon_theme}.png);'
                f'width: 16; height: 16 }}'
                
                f'QLabel {{ border: 0px solid; '
                f'padding: 0 4 0 4;'
                f'background-color: {background_color}; '
                f'color: {color} }}')

    def setLanguage(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.label_field.setText(self.attributes['labels'][0])
        elif language == 1: self.label_field.setText(self.attributes['labels'][1])
        self.label_field.adjustSize()