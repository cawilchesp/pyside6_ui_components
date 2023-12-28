from PySide6.QtWidgets import QFrame, QDateEdit, QLabel, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import QDate


class MD3DatePicker(QFrame):
    """
    PySide6 Date Picker component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        width: int = 96,
        type: str = 'filled',
        labels: tuple[str, str] = None,
        enabled: bool = True,
        language: int = 0
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Date picker top left corner position (x, y)
            width (int): Date picker width
            type (str): Date picker type
                Options: 'filled', 'outlined'
            labels: tuple
                Date field labels
                (label_spanish, label_english)
            enabled (bool): Date picker enabled / disabled
            language (int): App language
                Options: 0 = Spanish, 1 = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 52)
        self.setEnabled = enabled
        self.labels = labels

        self.text_field = QDateEdit(self)
        self.text_field.setGeometry(0, 8, width, 44)
        
        self.text_field.setCalendarPopup(True)
        self.text_field.setFrame(False)
        self.text_field.setSpecialValueText('')
        self.text_field.setDate(QDate.currentDate())
        
        self.label_field = QLabel(self)
        self.label_field.move(8, 0)
        self.label_field.setMargin(4)
        self.label_field.setFont(QFont('Segoe UI', 9))

        self.set_language(language) if self.labels is not None else None
        self.setProperty(type, True)


    def set_language(self, language: int) -> None:
        """ Change language of date picker text """
        if language == 0:   self.label_field.setText(self.labels[0])
        elif language == 1: self.label_field.setText(self.labels[1])
        self.label_field.adjustSize()
        self.label_field.resize(self.label_field.width(), 20)