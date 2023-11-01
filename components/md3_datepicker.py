"""
PySide6 Date Picker component adapted to follow Material Design 3 guidelines


"""

from PySide6 import QtGui, QtWidgets, QtCore

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
                Date field position
                (x, y) -> x, y: upper left corner
            width: int
                Date field width
            type: str
                Date field type
                'filled', 'outlined'
            labels: tuple
                Date field text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            enabled: bool
                Date field enabled / disabled
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
        self.label_field.move(8, 0)
        self.label_field.setMargin(4)
        self.label_field.setFont(QtGui.QFont('Segoe UI', 9))

        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.setProperty(attributes['type'], True)
        self.set_language(attributes['language'])


    def set_language(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.label_field.setText(self.attributes['labels'][0])
        elif language == 1: self.label_field.setText(self.attributes['labels'][1])
        self.label_field.adjustSize()
        self.label_field.resize(self.label_field.width(), 20)