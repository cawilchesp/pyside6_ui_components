from PySide6.QtWidgets import QSpinBox, QDoubleSpinBox, QWidget

from icon_color import icon_color


class UI_NumberBox(QSpinBox):
    """ Number Box component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8, 8),
        width: int = 64,
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Text box top left corner position (x, y)
            width (int): Text box width
            placeholder_texts (tuple[str, str]): Text box placeholder texts (text_spanish, text_english)
            input (str): Characters allowed
                Options:
                    'alphabet': letters and accents
                    'numeric': numbers
                    'alphanumeric': letters and numbers
            max_length (int): Number of characters allowed
            enabled (bool): Text box enabled / disabled
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)


class UI_FloatBox(QDoubleSpinBox):
    """ Float Box component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8, 8),
        width: int = 64,
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Text box top left corner position (x, y)
            width (int): Text box width
            placeholder_texts (tuple[str, str]): Text box placeholder texts (text_spanish, text_english)
            input (str): Characters allowed
                Options:
                    'alphabet': letters and accents
                    'numeric': numbers
                    'alphanumeric': letters and numbers
            max_length (int): Number of characters allowed
            enabled (bool): Text box enabled / disabled
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)