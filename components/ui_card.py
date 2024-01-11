from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QWidget


class UI_Card(QFrame):
    """ Card component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (16, 16),
        size: tuple[int, int] = (96, 96),
        titles: tuple[str, str] = None,
        language: str = 'es'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Card top left corner position (x, y)
            size (tuple[int, int]): Card size (width, height)
            titles (tuple[str, str]): Card titles (title_spanish, title_english)
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(size[0], size[1])
        self.titles = titles
        
        if self.titles is not None:
            self.title = QLabel(self)
            self.title.setGeometry(16, 16, size[0], 32)
            self.title.setFont(QFont('Segoe UI', 14))

        self.set_language(language)


    def set_language(self, language: int) -> None:
        """ Change language of title text """
        if self.titles is not None:
            if language == 'es':   self.title.setText(self.titles[0])
            elif language == 'en': self.title.setText(self.titles[1])
            self.title.adjustSize()