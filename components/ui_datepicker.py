from PySide6.QtWidgets import QDateEdit, QTimeEdit, QCalendarWidget, QWidget, QToolButton, QMenu
from PySide6.QtCore import QDate, QTime, Qt
from PySide6.QtGui import QFont, QTextCharFormat, QBrush, QColor


class UI_DateEdit(QDateEdit):
    """ Date Edit component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        width: int = 96,
        enabled: bool = True
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Date picker top left corner position (x, y)
            width (int): Date picker width
            enabled (bool): Date picker enabled / disabled
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setFont(QFont('Segoe Fluent Icons', 10))
        self.setEnabled(enabled)
        
        self.setCalendarPopup(True)
        self.setDate(QDate.currentDate())


class UI_TimeEdit(QTimeEdit):
    """ Date Edit component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        width: int = 96,
        range: tuple[tuple[int,int,int], tuple[int,int,int]] = ((0,0,0), (23,59,59)),
        enabled: bool = True
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Time picker top left corner position (x, y)
            width (int): Time picker width
            range (tuple[int, int, int], tuple[int, int, int]): Time picker range (min, max) -> (hour, minute, second)
            enabled (bool): Time picker enabled / disabled
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setFont(QFont('Segoe Fluent Icons', 10))
        self.setEnabled(enabled)
        
        min_time = QTime(range[0][0], range[0][1], range[0][2])
        max_time = QTime(range[1][0], range[1][1], range[1][2])

        self.setTime(QTime.currentTime())
        self.setTimeRange(min_time, max_time)


class UI_Calendar(QCalendarWidget):
    """ Calendar component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        theme_style: bool = False
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Calendar top left corner position (x, y)
        """
        super().__init__(parent)
        
        self.parent = parent
        self.move(position[0], position[1])
        self.resize(300, 350)
        self.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        
        month_menu = self.findChild(QMenu)
        month_menu.setWindowFlags(month_menu.windowFlags() | Qt.NoDropShadowWindowHint)
        
        self.set_header(theme_style)

    def set_header(self, theme_style: bool) -> None:
        """ Change header format """
        format = QTextCharFormat()
        format.setFont(QFont('Segoe Fluent Icons', 10))
        if theme_style:
            format.setBackground(QBrush(QColor.fromHslF(0, 0, 0.93)))
            format.setForeground(QBrush(QColor.fromHslF(0, 0, 0.13)))
        else:
            format.setBackground(QBrush(QColor.fromHslF(0, 0, 0.2)))
            format.setForeground(QBrush(QColor.fromHslF(0, 0, 0.93)))
        self.setHeaderTextFormat(format)
        