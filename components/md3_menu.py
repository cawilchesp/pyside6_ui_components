from PySide6.QtWidgets import QComboBox, QWidget


class MD3Menu(QComboBox):
    """
    PySide6 Menu component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        width: int = 32,
        type: str = 'filled',
        options: dict = None,
        set: int = -1,
        enabled: bool = True,
        language: int = 0,
        index_changed_signal: callable = None,
        text_activated_signal: callable = None,
        activated_signal: callable = None
    ):
        """
        Parameters
        ----------
            position (tuple[int, int]): Menu top left corner position (x, y)
            width (int): Menu width
            type (str): Menu type
                Options: 'filled', 'outlined'
            options (dict): Menu options with translations
                Example:
                    options = {
                        0: ('spanish_1', 'english_1'),
                        1: ('spanish_2', 'english_2')
                    }
            set (int): Selected option
                -1: No option selected
            enabled (bool): Button enabled / disabled
            language (int): App language
                Options: 0 = Spanish, 1 = English
            index_changed_signal (callable): Menu 'index changed' method name
            text_activated_signal (callable): Menu 'text activated' method name
            activated_signal (callable): Menu 'activated' method name
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 32)
        self.setEnabled = enabled
        self.type = type
        self.options = options

        if self.options is not None:
            self.max_items = len(self.options) if len(self.options) < 6 else 10
            self.set_language(language)
        else:
            self.max_items = 10

        self.setMaxVisibleItems(self.max_items)
        self.setMaxCount(self.max_items)
        self.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.setCurrentIndex(set)
        self.setProperty(self.type, True)

        self.currentIndexChanged.connect(index_changed_signal)
        self.textActivated.connect(text_activated_signal)
        self.activated.connect(activated_signal)
        

    def set_language(self, language: int) -> None:
        """ Change language of options text """
        if self.options is not None:
            for key, value in self.options.items():
                self.addItem('')
                if language == 0:   self.setItemText(key, value[0])
                elif language == 1: self.setItemText(key, value[1])