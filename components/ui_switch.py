from PySide6.QtWidgets import QFrame, QToolButton, QWidget, QPushButton
from PySide6.QtCore import Qt, QSize

from icon_color import icon_color


class UI_Switch(QFrame):
    """
    PySide6 Switch component
    """
    def __init__(self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        state: bool = False,
        enabled: bool = True,
        theme_style: bool = True,
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            clicked_signal (callable): Button 'clicked' method name
            position (tuple[int, int]): Button top left corner position (x, y)
            state (bool): State of activation
                Options: True: On, False: Off
            enabled (bool): Button enabled / disabled
            theme_style (bool): App theme style name
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(40, 20)
        self.state = state

        self.left_switch = QToolButton(self)
        self.left_switch.setGeometry(0, 0, 20, 20)
        self.left_switch.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.left_switch.setCheckable(True)
        self.left_switch.setEnabled = enabled

        self.right_switch = QToolButton(self)
        self.right_switch.setGeometry(20, 0, 20, 20)
        self.right_switch.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.right_switch.setCheckable(True)
        self.right_switch.setEnabled = enabled

        self.left_switch.setProperty('side', 'left')
        self.right_switch.setProperty('side', 'right')
        self.set_state(self.state, theme_style)

        self.left_switch.clicked.connect(clicked_signal)
        self.right_switch.clicked.connect(clicked_signal)
        

    def set_state(self, state: bool, theme_style: bool) -> None:
        """ Set button state and corresponding icon """
        
        self.left_switch.setChecked(state)
        self.right_switch.setChecked(state)
        icon_state = {
            True: { 'left': 'none', 'right': 'circle' },
            False: { 'left': 'circle', 'right': 'none' }
        }
        icon_left_name = icon_state[state]['left']
        icon_right_name = icon_state[state]['right']
        color_style = {
            True: { 'left': 'black', 'right': 'white' },
            False: { 'left': 'white', 'right': 'black' }
        }
        color_left_name = color_style[theme_style]['left']
        color_right_name = color_style[theme_style]['right']
        colorized_left_icon = icon_color(color_left_name, icon_left_name)
        colorized_right_icon = icon_color(color_right_name, icon_right_name)
        self.left_switch.setIcon(colorized_left_icon)
        self.right_switch.setIcon(colorized_right_icon)