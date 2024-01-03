from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

from icon_color import icon_color


class UI_Label(QLabel):
    """
    Label component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (16, 16),
        width: int = 32,
        align: str = 'left',
        border_color: str = None,
        labels: tuple[str, str] = None,
        theme_color: str = 'blue',
        language: int = 0
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Label top left corner position (x, y)
            width (int): Label width
            align (str): Text alignment
                Options: 'center', 'left', 'right'
            border_color (str): Label border color in hexadecimal format: '#RRGGBB'
            labels (tuple[str, str]): Button labels (label_spanish, label_english)
            theme_color (str): App theme color name
            language (int): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 32)
        self.labels = labels
        self.border_color = border_color if border_color is not None else 'transparent'

        alignment_dict = {
            'left': Qt.AlignmentFlag.AlignLeft,
            'center': Qt.AlignmentFlag.AlignHCenter,
            'right': Qt.AlignmentFlag.AlignRight
        }
        label_H_alignment = alignment_dict[align]
        self.setAlignment(label_H_alignment | Qt.AlignmentFlag.AlignVCenter)
        
        self.setStyleSheet(f"UI_Label {{ border-color: {self.border_color} }}")
        self.set_language(language) if self.labels is not None else None
        
    def set_language(self, language: int) -> None:
        """ Change language of label """
        if self.labels is not None:
            if language == 'es':   self.setText(self.labels[0])
            elif language == 'en': self.setText(self.labels[1])


class UI_IconLabel(QLabel):
    """
    Icon Label component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (16, 16),
        icon_name: str = None,
        theme_color: str = 'blue'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Label top left corner position (x, y)
            icon_name (str): Icon name
            theme_color (str): App theme color name
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(32, 32)
        self.icon_name = icon_name
        
        self.set_icon_label(self.icon_name, theme_color)
        

    def set_icon_label(self, icon_name: str, color_name: str) -> None:
        """ Update icon corresponding to the theme """
        self.icon_name = icon_name
        colorized_icon = icon_color(color_name, icon_name)
        self.setPixmap(colorized_icon.pixmap(24))


class UI_ColorLabel(QLabel):
    """
    Color Label component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (16, 16),
        width: int = 32,
        color: str = '#FFFFFF'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Label top left corner position (x, y)
            width (int): Color Label width
            color (str): Color Label indicator color in hexadecimal format: '#RRGGBB'
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 32)

        self.set_color_label(color)


    def set_color_label(self, color: str) -> None:
        """ Apply custom background color to label indicator """
        self.setStyleSheet(f"UI_ColorLabel {{ background-color: {color} }}")