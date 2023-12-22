from PySide6.QtWidgets import QToolButton, QWidget
from PySide6.QtCore import Qt

from icon_color import icon_color


class MD3SegmentedButton(QToolButton):
    """
    PySide6 Segmented Button component
    """
    def __init__(
        self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 32,
        icon_name: str = 'none',
        labels: tuple[str, str] = None,
        check_icon: bool = True,
        location: str = 'center',
        state: bool = False,
        enabled: bool = True,
        theme_color: str = 'blue',
        language: int = 0
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            clicked_signal (callable): Segmented button 'clicked' method name
            position (tuple[int, int]): Button top left corner position (x, y)
            width (int): Button width
            icon_name (str): Icon name
            labels (tuple[str, str]): Segmented button labels (label_spanish, label_english)
            check_icon (bool): Use "check" icon for selected option
            location (str): Position of the segmented button in the group
                Options: 'left', 'center', 'right'
            state (bool): State of activation
                Options: True: On, False: Off
            enabled (bool): Segmented button enabled / disabled
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
        self.check_icon = check_icon
        self.labels = labels

        self.set_state(state, theme_color)
        self.set_language(language) if self.labels is not None else None
        self.setProperty(location, True)

        self.clicked.connect(clicked_signal)
        

    def set_state(self, state: bool, theme_color: str) -> None:
        """ Set button state and corresponding icon """
        self.setChecked(state)
        active_icon = self.icon_name
        if state:
            if self.check_icon: active_icon = 'done'
            color = 'black'
        else:
            color = theme_color
        colorized_icon = icon_color(color, active_icon)
        self.setIcon(colorized_icon)


    def set_language(self, language: int) -> None:
        """ Change language of button label """
        if self.labels is not None:
            if language == 0:   self.setText(self.labels[0])
            elif language == 1: self.setText(self.labels[1])