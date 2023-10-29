"""
PySide6 Menu component adapted to follow Material Design 3 guidelines


"""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from components.style_color import colors

import sys

# ----
# Menú
# ----
class MD3Menu(QtWidgets.QComboBox):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Menu

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Button position
                (x, y) -> x, y: upper left corner
            width: int
                Menu width
            type: str
                Card type
                'filled', 'outlined'
            options: dict
                Menu options with translations
                Format: {0: ('es_1', 'en_1'), 1: ('es_2', 'en_2')}
            set: int
                Selected option
                -1: No option selected
            enabled: bool
                Menu enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            language: int
                App language
                0: Spanish, 1: English
            index_changed: def
                Menu 'index changed' method name
            text_activated: def
                Menu 'text activated' method name
        
        Returns
        -------
        None
        """
        super(MD3Menu, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        if 'options' in attributes:
            self.max_items = len(attributes['options']) if len(attributes['options']) < 6 else 10
            self.setLanguage(attributes['language'])
        else:
            self.max_items = 10

        self.setMaxVisibleItems(self.max_items)
        self.setMaxCount(self.max_items)
        self.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.setCurrentIndex(attributes['set'])
        self.view().window().setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        self.view().window().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.setProperty(attributes['type'], True)

        if 'index_changed' in attributes:
            self.currentIndexChanged.connect(attributes['index_changed'])
        if 'text_activated' in attributes:
            self.textActivated.connect(attributes['text_activated'])
        if 'activated' in attributes:
            self.activated.connect(attributes['activated'])
        

    def setLanguage(self, language: int) -> None:
        """ Change language of label text """
        if 'options' in self.attributes:
            for key, value in self.attributes['options'].items():
                self.addItem('')
                if language == 0:   self.setItemText(key, value[0])
                elif language == 1: self.setItemText(key, value[1])