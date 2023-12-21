from PySide6.QtWidgets import QPushButton

from icon_color import icon_color


class MD3Button(QPushButton):
    """
    PySide6 Button component
    """
    def __init__(
        self,
        parent,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 32,
        enabled: bool = True,
        type: str = 'filled',
        icon_name: str = None,
        labels: tuple[str, str] = None,
        theme_color: str = 'blue',
        language: int = 0
    ):
        """
        Parameters
        ----------
            position (tuple[int, int]): Button top left corner position (x, y)
            width (int): Button width
            type (str): Button type
                Options: 'filled', 'tonal', 'outlined', 'standard'
            icon (str): Icon name
            labels (tuple[str, str]): Button labels (label_spanish, label_english)
            enabled (bool): Button enabled / disabled
            theme_color (str): App theme color name
            language (int): App language
                Options: 0 = Spanish, 1 = English
            clicked (any): Button 'clicked' method name
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 32)
        self.setEnabled = enabled
        self.type = type
        self.labels = labels

        self.set_icon(theme_color, icon_name) if icon_name is not None else None
        self.set_language(language) if self.labels is not None else None
        self.setProperty(self.type, True)

        self.clicked.connect(clicked_signal)


    def set_icon( self, theme_color: str, icon_name: str) -> None:
        """ Change button icon """
        if self.type in ['filled', 'tonal']:
            color = 'black'
        elif self.type in ['outlined', 'standard']:
            color = theme_color
        colorized_icon = icon_color(color, icon_name)
        self.setIcon(colorized_icon)


    def set_language(self, language: int) -> None:
        """ Change language of button label """
        if self.labels is not None:
            if language == 0:   self.setText(self.labels[0])
            elif language == 1: self.setText(self.labels[1])