"""
PySide6 Card component adapted to follow Material Design 3 guidelines

"""
from PySide6 import QtGui, QtWidgets

# ----
# Card
# ----
class MD3Card(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Card

        Parameters
        ----------
        attributes: dict
            position: tuple
                Card position
                (x, y) -> x, y: upper left corner
            size: tuple
                Card size
                (w, h) -> w: width, h: height
            titles: tuple
                Card title text (Optional)
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            type: str
                Card type
                'filled', 'outlined'
            language: int
                App language
                0: Spanish, 1: English
        
        Returns
        -------
        None
        """
        super(MD3Card, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w, h = attributes['size'] if 'size' in attributes else (96, 96)
        self.setGeometry(x, y, w, h)

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(8, 8, 32, 32)
        self.title.setFont(QtGui.QFont('Segoe UI', 14))

        self.setProperty(self.attributes['type'], True)
        self.setLanguage(attributes['language'])


    def setLanguage(self, language: int) -> None:
        """ Change language of title text """
        if 'titles' in self.attributes:
            if language == 0:   self.title.setText(self.attributes['titles'][0])
            elif language == 1: self.title.setText(self.attributes['titles'][1])
            self.title.adjustSize()