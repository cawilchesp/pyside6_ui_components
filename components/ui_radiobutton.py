from PySide6.QtWidgets import QRadioButton, QWidget
from PySide6.QtCore import Qt

from icon_color import icon_color


class UI_RadioButton(QRadioButton):
    """ Check box component """
    def __init__(
        self,
        parent: QWidget,
        state_changed_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 40,
        icon_name: str = None,
        labels: tuple[str, str] = None,
        state: int = 0,
        enabled: bool = True,
        theme_style: bool = True,
        language: str = 'es'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Check box top left corner position (x, y)
            width (int): Check box width
            icon_name (str): Icon name
            labels (tuple[str, str]): Check box labels (label_spanish, label_english)
            state (bool): Check box toggle State of activation
                Options: True: On, False: Off
            enabled (bool): Check box enabled / disabled
            theme_style (bool): App theme style name
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setEnabled(enabled)
        self.icon_name = icon_name
        self.labels = labels
        self.state = state

        self.set_icon(theme_style) if icon_name is not None else None
        self.set_language(language) if self.labels is not None else None
        self.setChecked(self.state)

        self.toggled.connect(state_changed_signal)



    def set_icon(self, theme_style: bool) -> None:
        """ Change button icon """
        color = 'black' if theme_style else 'white'
        colorized_icon = icon_color(color, self.icon_name)
        self.setIcon(colorized_icon)

    
    def set_language(self, language: str) -> None:
        """ Change language of button label """
        if self.labels is not None:
            if language == 'es':   self.setText(self.labels[0])
            elif language == 'en': self.setText(self.labels[1])