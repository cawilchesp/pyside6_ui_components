from PySide6.QtWidgets import QFrame, QToolButton, QWidget
from PySide6.QtGui import QFont

from components.icons import icons


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
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(40, 20)
        self.state = state

        self.left_switch = QToolButton(self)
        self.left_switch.setGeometry(0, 0, 20, 20)
        self.left_switch.setCheckable(True)
        self.left_switch.setFont(QFont('Segoe Fluent Icons', 9))
        self.left_switch.setEnabled(enabled)

        self.right_switch = QToolButton(self)
        self.right_switch.setGeometry(20, 0, 20, 20)
        self.right_switch.setCheckable(True)
        self.right_switch.setFont(QFont('Segoe Fluent Icons', 9))
        self.right_switch.setEnabled(enabled)

        self.left_switch.setProperty('side', 'left')
        self.right_switch.setProperty('side', 'right')
        self.set_state(self.state)

        self.left_switch.clicked.connect(clicked_signal)
        self.right_switch.clicked.connect(clicked_signal)
        
    def set_state(self, state: bool) -> None:
        """ Set button state and corresponding icon """
        self.left_switch.setChecked(state)
        self.right_switch.setChecked(state)
        if state:
            self.left_switch.setText("")
            self.right_switch.setText(f"{icons['FullCircleMask']}")
        else:
            self.left_switch.setText(f"{icons['FullCircleMask']}")
            self.right_switch.setText("")