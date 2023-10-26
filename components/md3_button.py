"""
PySide6 Button component adapted to follow Material Design 3 guidelines

"""
from PySide6 import QtGui, QtWidgets

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
            width: int
                Button width
            type: str
                Button type
                'elevated', 'filled', 'tonal', 'outlined', 'standard'
            icon: str (Optional)
                Icon file without extension ('icon')
            labels: tuple
                Item label text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            enabled: bool
                Button enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            language: int
                App language
                0: Spanish, 1: English
            clicked: def
                Button 'clicked' method name
        
        Returns
        -------
        None
        """
        super(MD3Button, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        if 'icon' in self.attributes:
            icon_theme = 'L' if self.attributes['theme'] else 'D'
            icon_path = f"icons/{self.attributes['icon']}_{icon_theme}.png"
            self.setIcon(QtGui.QIcon(f"{icon_path}"))

        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.setProperty(attributes['type'], True)
        self.setLanguage(attributes['language'])

        self.clicked.connect(attributes['clicked'])
              

    def setLanguage(self, language: int) -> None:
        """ Change language of title text """
        if language == 0:   self.setText(self.attributes['labels'][0])
        elif language == 1: self.setText(self.attributes['labels'][1])