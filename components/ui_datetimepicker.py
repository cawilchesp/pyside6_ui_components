from PySide6.QtWidgets import QDateEdit, QTimeEdit, QCalendarWidget, QWidget, QMenu, QFrame
from PySide6.QtCore import QDate, QTime, Qt
from PySide6.QtGui import QFont, QTextCharFormat, QBrush, QColor

from components.ui_combobox import UI_ComboBox


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
        language: str = 'es',
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

        self.month_names = {
            0: ['Enero','January'],
            1: ['Febrero','February'],
            2: ['Marzo','March'],
            3: ['Abril','April'],
            4: ['Mayo','May'],
            5: ['Junio','June'],
            6: ['Julio','July'],
            7: ['Agosto','August'],
            8: ['Septiembre','September'],
            9: ['Octubre','October'],
            10: ['Noviembre','November'],
            11: ['Diciembre','December']
        }

        today = QDate.currentDate()

        day_options = {
            0: ('1','1'),
            1: ('2','2'),
            2: ('3','3'),
            3: ('4','4'),
            4: ('5','5'),
            5: ('6','6'),
            6: ('7','7'),
            7: ('8','8'),
            8: ('9','9'),
            9: ('10','10'),
            10: ('11','11'),
            11: ('12','12'),
            12: ('13','13'),
            13: ('14','14'),
            14: ('15','15'),
            15: ('16','16'),
            16: ('17','17'),
            17: ('18','18'),
            18: ('19','19'),
        }

        year_options = {
            0: ('2020','2020'),
            1: ('2021','2021'),
            2: ('2022','2022'),
            3: ('2023','2023'),
            4: ('2024','2024')
        }

        self.day_button = UI_ComboBox(
            parent=self,
            position=(0, 0),
            width=80,
            texts=('Día', 'Day'),
            options=day_options,
            set=today.day()-1,
            language=language
        )
        self.month_button = UI_ComboBox(
            parent=self,
            position=(72,0),
            width=140,
            texts=('Mes', 'Month'),
            options=self.month_names,
            set=today.month()-1,
            language=language
        )
        self.year_button = UI_ComboBox(
            parent=self,
            position=(204,0),
            width=96,
            texts=('Año', 'Year'),
            options=year_options,
            set=today.year()-2020,
            language=language
        )





        