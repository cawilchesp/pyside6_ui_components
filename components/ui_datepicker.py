from PySide6.QtWidgets import QFrame, QDateEdit, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import QDate


class UI_DatePicker(QDateEdit):
    """ Date Picker component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        width: int = 96,
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
        
        self.setCalendarPopup(True)
        self.setFrame(False)
        self.setSpecialValueText('')
        self.setDate(QDate.currentDate())
        
        # self.set_language(language) if self.labels is not None else None


    def set_language(self, language: int) -> None:
        """ Change language of date picker text """
        if language == 0:   self.label_field.setText(self.labels[0])
        elif language == 1: self.label_field.setText(self.labels[1])
        self.label_field.adjustSize()
        self.label_field.resize(self.label_field.width(), 20)