from PySide6.QtWidgets import QToolButton, QWidget
from PySide6.QtCore import Qt

from icon_color import icon_color


class MD3Chip(QToolButton):
    """
    PySide6 Chip component
    """
    def __init__(self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 32,
        icon_name: str = None,
        labels: tuple[str, str] = None,
        state: bool = False,
        enabled: bool = True,
        theme_color: str = 'blue',
        language: int = 0
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            clicked_signal (callable): Chip 'clicked' method name
            position (tuple[int, int]): Chip top left corner position (x, y)
            width (int): Chip width
            labels (tuple[str, str]): Chip labels (label_spanish, label_english)
            icon_name (str): Icon name
            state (bool): State of activation
                Options: True: On, False: Off
            enabled (bool): Chip enabled / disabled
            theme_color (str): App theme color name
            language (int): App language
                Options: 0 = Spanish, 1 = English
        """
        super().__init__(parent)

        self.parent = parent

        self.move(position[0], position[1])
        self.resize(width, 32)
        self.setEnabled = enabled
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)
        self.icon_name = icon_name
        self.labels = labels
        
        self.set_state(state, theme_color)
        self.set_language(language) if self.labels is not None else None

        self.clicked.connect(clicked_signal)

        
    def set_state(self, state: bool, theme_color: str) -> None:
        """ Set chip state and corresponding icon """
        self.setChecked(state)
        active_icon = self.icon_name
        if state:
            active_icon = 'done'
            color = 'black'
        else:
            color = theme_color
        colorized_icon = icon_color(color, active_icon)
        self.setIcon(colorized_icon)


    def set_language(self, language: int) -> None:
        """ Change language of chip label """
        if self.labels is not None:
            if language == 0:   self.setText(self.labels[0])
            elif language == 1: self.setText(self.labels[1])