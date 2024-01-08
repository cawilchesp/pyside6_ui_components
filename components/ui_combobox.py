from PySide6.QtWidgets import QComboBox, QWidget, QFrame
from PySide6.QtCore import Qt

from icon_color import icon_color


class UI_ComboBox(QComboBox):
    """ Combo box component """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        width: int = 40,
        options: dict = None,
        # set: int = -1,
        enabled: bool = True,
        language: str = 'es',
        # index_changed_signal: callable = None,
        # text_activated_signal: callable = None,
        # activated_signal: callable = None
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            position (tuple[int, int]): Menu top left corner position (x, y)
            width (int): Menu width
            options (dict): Menu options with translations
                options = {
                    0: ('spanish_1', 'english_1'),
                    1: ('spanish_2', 'english_2')
                }
            set (int): Selected option
                -1: No option selected
            enabled (bool): Button enabled / disabled
            language (str): App language
                Options: 'es' = Español, 'en' = English
            index_changed_signal (callable): Menu 'index changed' method name
            text_activated_signal (callable): Menu 'text activated' method name
            activated_signal (callable): Menu 'activated' method name
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setEnabled = enabled
        self.view().window().setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        self.options = options

        self.set_language(language)

        self.setMaxVisibleItems(5)
        self.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        # self.setCurrentIndex(set)

        # self.currentIndexChanged.connect(index_changed_signal)
        # self.textActivated.connect(text_activated_signal)
        # self.activated.connect(activated_signal)
        

    def set_language(self, language: str) -> None:
        """ Change language of options text """
        for key, value in self.options.items():
            self.addItem('')
            if language == 'es':   self.setItemText(key, value[0])
            elif language == 'en': self.setItemText(key, value[1])