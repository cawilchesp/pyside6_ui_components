"""
PySide6 Label component adapted to follow Material Design 3 guidelines


"""

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from icon_color import icon_color

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
        if attributes['type'] == 'value':
            self.setStyleSheet(f"MD3Label[value=true] {{ border-color: {attributes['border_color']} }}")
        if attributes['type'] == 'color':
            self.set_color_label(attributes['color'])
        if 'icon' in attributes:
            self.set_icon_label(attributes['icon'], attributes['theme_color'])
        if 'language' in attributes:
            self.set_language(attributes['language'])
        

    def set_icon_label(self, icon_name: str, color_name: str) -> None:
        """ Update icon corresponding to the theme """

        self.attributes['icon'] = icon_name
        colorized_icon = icon_color(color_name, icon_name)
        self.setPixmap(colorized_icon.pixmap(24))
        

    def set_color_label(self, color: str) -> None:
        """ Apply custom color to component """

        self.setStyleSheet(f"MD3Label[color=true] {{ background-color: {color} }}")


    def set_language(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.setText(self.attributes['labels'][0])
            elif language == 1: self.setText(self.attributes['labels'][1])