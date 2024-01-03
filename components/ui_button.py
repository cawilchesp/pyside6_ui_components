from PySide6.QtWidgets import QToolButton, QWidget
from PySide6.QtCore import Qt, QSize

from icon_color import icon_color


class UI_Button(QToolButton):
    """
    PySide6 Button component
    """
    def __init__(
        self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 32,
        type: str = 'standard',
        icon_name: str = None,
        labels: tuple[str, str] = None,
        enabled: bool = True,
        theme_color: str = 'blue',
        language: int = 0
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            clicked_signal (callable): Button 'clicked' method name
            position (tuple[int, int]): Button top left corner position (x, y)
            width (int): Button width
            type (str): Button type
                Options: 'standard', 'accent', 'outlined', 'hyperlink'
            icon_name (str): Icon name
            labels (tuple[str, str]): Button labels (label_spanish, label_english)
            enabled (bool): Button enabled / disabled
            theme_color (str): App theme color name
            language (int): App language
                Options: 0 = Spanish, 1 = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 32)
        self.setEnabled(enabled)
        self.type = type
        self.labels = labels

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setAutoRaise(True)
        
        self.set_icon(theme_color, icon_name) if icon_name is not None else None
        self.set_language(language) if self.labels is not None else None
        self.setProperty('type', self.type)

        self.clicked.connect(clicked_signal)


    def set_icon( self, theme_color: str, icon_name: str) -> None:
        """ Change button icon """
        if self.type == 'standard':
            color = 'white'
        elif self.type == 'accent':
            color = 'black'
        elif self.type in ['outlined', 'hyperlink']:
            color = theme_color
        colorized_icon = icon_color(color, icon_name)
        self.setIcon(colorized_icon)


    def set_language(self, language: int) -> None:
        """ Change language of button label """
        if self.labels is not None:
            if language == 0:   self.setText(self.labels[0])
            elif language == 1: self.setText(self.labels[1])