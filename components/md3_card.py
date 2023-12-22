from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QWidget


class MD3Card(QFrame):
    """
    PySide6 Card component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        size: tuple[int, int] = (96,96),
        type: str = 'filled',
        titles: tuple[str, str] = None,
        language: int = 0
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Card top left corner position (x, y)
            size (tuple[int, int]): Card size (width, height)
            type (str): Card type
                Options: 'filled', 'outlined'
            titles (tuple[str, str]): Card titles (title_spanish, title_english)
            language (int): App language
                Options: 0 = Spanish, 1 = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(size[0], size[1])
        self.type = type
        self.titles = titles
        
        self.title = QLabel(self)
        self.title.setGeometry(8, 8, 32, 32)
        self.title.setFont(QFont('Segoe UI', 14))

        self.set_language(language) if self.titles is not None else None
        self.setProperty(self.type, True)


    def set_language(self, language: int) -> None:
        """ Change language of title text """
        if self.titles is not None:
            if language == 0:   self.title.setText(self.titles[0])
            elif language == 1: self.title.setText(self.titles[1])
            self.title.adjustSize()