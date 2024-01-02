from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

from icon_color import icon_color


class MD3Label(QLabel):
    """
    PySide6 Label component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        width: int = 32,
        type: str = 'filled',
        align: str = 'left',
        icon_name: str = None,
        color: str = '#FFFFFF',
        border_color: str = '#FFFFFF',
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
            type (str): Label type
                Text options: 'subtitle', 'value'
                Indicator options: 'icon', 'color'
            align (str): Text align
                Options: 'center', 'left', 'right'
            icon_name (str): Icon name
            color (str): Label indicator color in hexadecimal format: '#RRGGBB'
            border_color (str): Label border color in hexadecimal format: '#RRGGBB'
            labels (tuple[str, str]): Button labels (label_spanish, label_english)
            theme_color (str): App theme color name
            language (int): App language
                Options: 0 = Spanish, 1 = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        height = 16 if type == 'subtitle' else 32
        self.resize(width, height)
        self.icon_name = icon_name
        self.labels = labels

        if type in {'subtitle', 'value'}:
            alignment_dict = {
                'left': Qt.AlignmentFlag.AlignLeft,
                'center': Qt.AlignmentFlag.AlignHCenter,
                'right': Qt.AlignmentFlag.AlignRight
            }
            label_H_alignment = alignment_dict[align]
            self.setAlignment(label_H_alignment | Qt.AlignmentFlag.AlignVCenter)

        self.setProperty(type, True)
        
        self.setStyleSheet(f"MD3Label[value=true] {{ border-color: {border_color} }}") if type == 'value' else None
        self.set_color_label(color) if type == 'color' else None
        self.set_icon_label(self.icon_name, theme_color) if icon_name is not None else None
        self.set_language(language) if self.labels is not None else None
        

    def set_icon_label(self, icon_name: str, color_name: str) -> None:
        """ Update icon corresponding to the theme """

        self.icon_name = icon_name
        colorized_icon = icon_color(color_name, icon_name)
        self.setPixmap(colorized_icon.pixmap(24))
        

    def set_color_label(self, color: str) -> None:
        """ Apply custom background color to label indicator """
        self.setStyleSheet(f"MD3Label[color=true] {{ background-color: {color} }}")


    def set_language(self, language: int) -> None:
        """ Change language of label """
        if self.labels is not None:
            if language == 0:   self.setText(self.labels[0])
            elif language == 1: self.setText(self.labels[1])