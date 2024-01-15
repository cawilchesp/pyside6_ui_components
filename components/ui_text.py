from PySide6.QtWidgets import QFrame, QLineEdit, QLabel, QWidget
from PySide6.QtGui import QFont, QIcon, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression, Qt

from icon_color import icon_color


class UI_TextBox(QLineEdit):
    """ Text Box component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8, 8),
        width: int = 64,
        placeholder_texts: tuple[str, str] = None,
        input: str = None,
        max_length: int = 32767,
        enabled: bool = True,
        language: str = 'es'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Text box top left corner position (x, y)
            width (int): Text box width
            placeholder_texts (tuple[str, str]): Text box placeholder texts (text_spanish, text_english)
            input (str): Characters allowed
                Options:
                    'alphabet': letters and accents
                    'numeric': numbers
                    'alphanumeric': letters and numbers
            max_length (int): Number of characters allowed
            enabled (bool): Text box enabled / disabled
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setClearButtonEnabled(True)
        self.setMaxLength(max_length)
        self.setEnabled = enabled
        self.placeholder_texts = placeholder_texts

        patterns_dict = {
            'alphabet': r"[\p{L}\s]+",
            'numeric': r"[+-]?\d+",
            'alphanumeric': r"[\p{L}\s\d]+"
        }
        if input is not None:
            input_pattern = patterns_dict[input]
            reg_exp = QRegularExpressionValidator(QRegularExpression(input_pattern))
            self.setValidator(reg_exp)

        self.set_language(language) if self.placeholder_texts is not None else None

    def set_language(self, language: str) -> None:
        """ Change language of button label """
        if language == 'es':   self.setPlaceholderText(self.placeholder_texts[0])
        elif language == 'en': self.setPlaceholderText(self.placeholder_texts[1])


class UI_PasswordBox(QLineEdit):
    """ Password Box component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8, 8),
        width: int = 64,
        placeholder_texts: tuple[str, str] = None,
        max_length: int = 32767,
        enabled: bool = True,
        theme_style: bool = True,
        language: str = 'es'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Password box top left corner position (x, y)
            width (int): Password box width
            placeholder_texts (tuple[str, str]): Password box placeholder texts (text_spanish, text_english)
            max_length (int): Number of characters allowed
            enabled (bool): Password box enabled / disabled
            theme_style (bool): App theme style name
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setClearButtonEnabled(True)
        self.setMaxLength(max_length)
        self.setEnabled = enabled
        self.placeholder_texts = placeholder_texts
        self.password_visible = False
        self.setEchoMode(QLineEdit.EchoMode.Password)

        self.toggle_password = self.addAction(QIcon('icons/none.png'), QLineEdit.ActionPosition.TrailingPosition)
        self.toggle_password.triggered.connect(self.password_action)
        
        self.set_icon(theme_style)
        self.set_language(language) if self.placeholder_texts is not None else None
    
    def set_icon(self, theme_style: bool) -> None:
        """ Change button icon """
        color = 'black' if theme_style else 'white'
        self.visible_icon = icon_color(color, 'eye')
        self.hidden_icon = icon_color(color, 'eye_off')
        if self.password_visible:
            self.toggle_password.setIcon(self.visible_icon)
        else:
            self.toggle_password.setIcon(self.hidden_icon)

    def password_action(self) -> None:
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_password.setIcon(self.visible_icon)
        else:
            self.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_password.setIcon(self.hidden_icon)

    def set_language(self, language: str) -> None:
        """ Change language of button label """
        if language == 'es':   self.setPlaceholderText(self.placeholder_texts[0])
        elif language == 'en': self.setPlaceholderText(self.placeholder_texts[1])



























class MD3TextField(QFrame):
    """
    PySide6 Text Field component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        width: int = 96,
        type: str = 'filled',
        input: str = None,
        length: int = 32767,
        labels: tuple[str, str] = None,
        enabled: bool = True,
        theme_color: str = 'blue',
        language: int = 0,
        return_pressed_signal: callable = None,
        text_edited_signal: callable = None,
        text_changed_signal: callable = None
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            return_pressed_signal (callable): Text field 'return pressed' method name
            text_edited_signal (callable): Text field 'text edited' method name
            text_changed_signal (callable): Text field 'text changed' method name
            position (tuple[int, int]): Text field top left corner position (x, y)
            width (int): Text field width
            type (str): Text field type
                Options: 'filled', 'outlined'
            input: str (optional, any character allowed if not specified)
                Text field type
                    'text':      only letters and accents
                    'integer':   only integer numbers
                    'double':    allow decimal point
                    'weight':    double values from 0.00 to 999.99
                    'height_si': double values from 0.00 to 2.99
                    'height_us': number in format [ft]'[in]" (ex. 5'12")
                    'email':     text in email format
                    'ip':        numbers in ip format (0.0.0.0 - 255.255.255.255)
            length (int): Number of characters allowed
            labels (tuple[str, str]): Text field labels (label_spanish, label_english)
            enabled (bool): Button enabled / disabled
            theme_color (str): App theme color name
            language (int): App language
                Options: 0 = Spanish, 1 = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 52)
        self.setEnabled = enabled
        self.labels = labels

        self.text_field = QLineEdit(self)
        self.text_field.setGeometry(0, 8, width, 44)
        self.text_field.setClearButtonEnabled(True)
        self.text_field.setMaxLength(length)

        if input is not None:
            patterns_dict = {
                'text': r"[\p{L}\s]+",
                'integer': r'[+-]?\d+',
                'double': r'[+-]?\d+\.\d+',
                'weight': r'([0-9]\d{0,2})\.(\d{1,2})',
                'height_si': r'[0-3]\.(\d{1,2})',
                'height_us': r'[0-9]\'([0-9]|10|11|12)\"',
                'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
                'ip': r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
            }
            if input in patterns_dict:
                pattern = patterns_dict[input]
                reg_exp = QRegularExpressionValidator(QRegularExpression(pattern))
                self.text_field.setValidator(reg_exp)
            elif input == 'password':
                self.visible_icon = icon_color(theme_color, 'eye')
                self.hidden_icon = icon_color(theme_color, 'eye_off')
                                
                self.text_field.setEchoMode(QLineEdit.EchoMode.Password)
                self.toggle_password = self.text_field.addAction(self.visible_icon, QLineEdit.ActionPosition.TrailingPosition)
                self.toggle_password.triggered.connect(self.password_action)
                self.toggle_password_state = False

        self.label_field = QLabel(self)
        self.label_field.move(8, 0)
        self.label_field.setMargin(4)
        self.label_field.setFont(QFont('Segoe UI', 9))
        self.label_field.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.set_language(language) if self.labels is not None else None
        self.setProperty(type, True)

        self.text_field.returnPressed.connect(return_pressed_signal)
        self.text_field.textEdited.connect(text_edited_signal)
        self.text_field.textChanged.connect(text_changed_signal)
          

    def password_action(self) -> None:
        if not self.toggle_password_state:
            self.text_field.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_password_state = True
            self.toggle_password.setIcon(self.hidden_icon)
        else:
            self.text_field.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_password_state = False
            self.toggle_password.setIcon(self.visible_icon)


    def set_language(self, language: int) -> None:
        """ Change language of label field text """
        if language == 0:   self.label_field.setText(self.labels[0])
        elif language == 1: self.label_field.setText(self.labels[1])
        self.label_field.adjustSize()
        self.label_field.resize(self.label_field.width(), 20)