from PySide6.QtWidgets import QDateEdit, QTimeEdit, QCalendarWidget, QWidget, QMenu, QFrame, QToolButton
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

        self.setCalendarWidget(UI_CalendarView(self))


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


class UI_CalendarView(QCalendarWidget):
    """ Calendar View component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        theme_color: str = 'blue',
        theme_style: bool = False
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Calendar top left corner position (x, y)
            theme_color (str): App theme color name
            theme_style (bool): App theme style name
        """
        super().__init__(parent)
        
        self.parent = parent
        self.move(position[0], position[1])
        self.setMinimumSize(300, 350)
        self.setMaximumSize(300, 350)
        self.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setWindowFlags(self.windowFlags() | Qt.NoDropShadowWindowHint)

        month_menu = self.findChild(QMenu)
        month_menu.setWindowFlags(month_menu.windowFlags() | Qt.NoDropShadowWindowHint)

        self.set_header(theme_style)
        self.set_weekend_color(theme_color)

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

    def set_weekend_color(self, theme_color: str) -> None:
        """ Change weekend days text color """        
        colors = {
            'blue': [200/360, 1.0, 0.50],
            'yellow': [48/360, 1.0, 0.67],
            'red': [0, 0.9, 0.40],
            # 'green': []
        }
        h, s, l = colors[theme_color]
        format = QTextCharFormat()
        format.setFont(QFont('Segoe Fluent Icons', 10))
        format.setForeground(QBrush(QColor.fromHslF(h, s, l)))
        self.setWeekdayTextFormat(Qt.DayOfWeek.Saturday, format)
        self.setWeekdayTextFormat(Qt.DayOfWeek.Sunday, format)


class UI_DatePicker(QFrame):
    """ Date Picker component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        enabled: bool = True,
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Calendar top left corner position (x, y)
            theme_color (str): App theme color name
            theme_style (bool): App theme style name
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(300, 40)
        self.setEnabled(enabled)
        self.setFont(QFont('Segoe Fluent Icons', 10))

        month_names = {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre'
        }

        today = QDate.currentDate()        

        day_button = QToolButton(self)
        day_button.setObjectName('date_day_button')
        month_button = QToolButton(self)
        month_button.setObjectName('date_month_button')
        year_button = QToolButton(self)
        year_button.setObjectName('date_year_button')

        day_button.move(4,4)
        day_button.resize(80,32)
        day_button.setText(str(today.day()))
        month_button.move(83,4)
        month_button.resize(134,32)
        month_button.setText(month_names[today.month()])
        year_button.move(216,4)
        year_button.resize(80,32)
        year_button.setText(str(today.year()))

