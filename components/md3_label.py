"""
PySide6 Label component adapted to follow Material Design 3 guidelines


"""

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

import sys

# ------
# Labels
# ------
class MD3Label(QtWidgets.QLabel):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Label

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Card position
                (x, y) -> x, y: upper left corner
            width: int
                Label width
            type: str
                Label type
                For text: 'subtitle', 'value'
                For indicators: 'icon', 'color'
            align: str 
                Text align
                'center', 'left', 'right'
            icon: str
                Icon file without extension
            color: str
                Label color
                Format hex: '#RRGGBB'
            border_color: str
                Border color
                Format hex: '#RRGGBB'
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
        super(MD3Label, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        h = 16 if attributes['type'] == 'subtitle' else 32
        self.setGeometry(x, y, w, h)

        if 'align' in attributes:
            alignment_dict = { 'center': Qt.AlignmentFlag.AlignCenter, 'right': Qt.AlignmentFlag.AlignRight }
            if attributes['align'] in alignment_dict: label_alignment = alignment_dict[attributes['align']]
            else: label_alignment = Qt.AlignmentFlag.AlignLeft
        else:
            label_alignment = Qt.AlignmentFlag.AlignLeft
        self.setAlignment(label_alignment | Qt.AlignmentFlag.AlignVCenter)

        self.setProperty(attributes['type'], True)
        if 'icon' in attributes:
            self.setIconLabel(attributes['icon'], attributes['theme'])
        if 'language' in attributes:
            self.setLanguage(attributes['language'])
        

    def setIconLabel(self, icon: str, theme: bool) -> None:
        """ Update icon corresponding to the theme """

        self.attributes['icon'] = icon
        icon_theme = 'L' if theme else 'D'
        self.setPixmap(QtGui.QIcon(f'icons/{self.attributes["icon"]}_{icon_theme}.png').pixmap(24))
        

    # def setColorLabel(self, color: str, theme: bool) -> None:
    #     """ Apply custom color to component """

    #     border_color = colors(theme, 'outline')
    #     self.setStyleSheet(f'QLabel#{self.name} {{ '
    #             f'border: 2px solid {border_color};'
    #             f'border-radius: 16px;'
    #             f'background-color: {color} '
    #             f'}}')


    def setLanguage(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.setText(self.attributes['labels'][0])
            elif language == 1: self.setText(self.attributes['labels'][1])