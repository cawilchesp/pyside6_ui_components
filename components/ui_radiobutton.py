from PySide6.QtWidgets import QRadioButton, QWidget, QButtonGroup
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from components.icons import icons


class UI_RadioButton(QRadioButton):
    """ Check box component """
    def __init__(
        self,
        parent: QWidget,
        state_changed_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 40,
        icon_name: str = None,
        texts: tuple[str, str] = None,
        state: int = 0,
        enabled: bool = True,
        group: QButtonGroup = None,
        language: str = 'es'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Check box top left corner position (x, y)
            width (int): Check box width
            icon_name (str): Icon name
            texts (tuple[str, str]): Check box texts (text_spanish, text_english)
            state (bool): Check box toggle State of activation
                Options: True: On, False: Off
            enabled (bool): Check box enabled / disabled
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setFont(QFont('Segoe Fluent Icons', 10))
        self.setEnabled(enabled)
        self.icon_code = icons[icon_name] if icon_name is not None else ''
        self.texts = texts
        self.state = state

        self.set_language(language)
        self.setChecked(self.state)
        group.addButton(self) if group is not None else None

        self.toggled.connect(state_changed_signal)

    
    def set_language(self, language: str) -> None:
        """ Change language of button text """
        button_text = self.icon_code
        space = ' ' if button_text != '' and self.texts is not None else ''
        if self.texts is not None:
            if language == 'es':
                button_text = f"{button_text}{space}{self.texts[0]}"
            elif language == 'en':
                button_text = f"{button_text}{space}{self.texts[1]}"
        self.setText(button_text)