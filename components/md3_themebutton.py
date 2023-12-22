from PySide6.QtWidgets import QPushButton, QWidget

from icon_color import icon_color


class MD3ThemeButton(QPushButton):
    """
    PySide6 Theme Button component
    """
    def __init__(self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        type: str = 'filled',
        state: bool = False,
        enabled: bool = True,
        theme_color: str = 'blue',
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            clicked_signal (callable): Button 'clicked' method name
            position (tuple[int, int]): Button top left corner position (x, y)
            type (str): Button type
                Options: 'filled', 'tonal', 'outlined', 'standard'
            state (bool): State of activation
                Options: True: On, False: Off
            enabled (bool): Button enabled / disabled
            theme_color (str): App theme color name
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(32, 32)
        self.setEnabled = enabled
        self.type = type
        
        self.set_state(state, theme_color)
        self.setProperty(self.type, True)

        self.clicked.connect(clicked_signal)


    def set_state(self, state: bool, theme_color: str) -> None:
        """ Set button state and corresponding icon """
        icon_name = 'light_mode' if state else 'dark_mode'
        if self.type in ['filled', 'tonal']:
            color = 'black'
        elif self.type in ['outlined', 'standard']:
            color = theme_color
        colorized_icon = icon_color(color, icon_name)
        self.setIcon(colorized_icon)