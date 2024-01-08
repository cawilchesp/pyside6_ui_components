from PySide6.QtWidgets import QToolButton, QWidget, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

from icon_color import icon_color


class UI_Button(QToolButton):
    """ Button component """
    def __init__(
        self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 32,
        type: str = 'standard',
        icon_name: str = None,
        labels: tuple[str, str] = None,
        enabled: bool = True,
        theme_color: str = 'blue',
        theme_style: bool = True,
        language: str = 'es'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            clicked_signal (callable): Button 'clicked' method name
            position (tuple[int, int]): Button top left corner position (x, y)
            width (int): Button width
            type (str): Button type
                Options: 'standard', 'accent', 'outlined', 'hyperlink'
            icon_name (str): Icon name
            labels (tuple[str, str]): Button labels (label_spanish, label_english)
            enabled (bool): Button enabled / disabled
            theme_color (str): App theme color name
            theme_style (bool): App theme style name
            language (int): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 32)
        self.setEnabled(enabled)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.type = type
        self.labels = labels
        self.icon_name = icon_name

        self.set_icon(theme_style, theme_color) if icon_name is not None else None
        self.set_language(language) if self.labels is not None else None
        self.setProperty('type', self.type)

        self.clicked.connect(clicked_signal)


    def set_icon(self, theme_style: bool, theme_color: str) -> None:
        """ Change button icon """
        if self.type == 'standard':
            color = 'black' if theme_style else 'white'
        elif self.type == 'accent':
            color = 'black'
        elif self.type in ['outlined', 'hyperlink']:
            color = theme_color
        colorized_icon = icon_color(color, self.icon_name)
        self.setIcon(colorized_icon)


    def set_language(self, language: str) -> None:
        """ Change language of button label """
        if self.labels is not None:
            if language == 'es':   self.setText(self.labels[0])
            elif language == 'en': self.setText(self.labels[1])


class UI_ToggleButton(QToolButton):
    """
    Toggle Button component
    """
    def __init__(
        self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 32,
        icon_name: str = None,
        labels: tuple[str, str] = None,
        state: bool = False,
        enabled: bool = True,
        theme_style: bool = True,
        language: str = 'es'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            triggered_signal (callable): Button 'clicked' method name
            position (tuple[int, int]): Button top left corner position (x, y)
            width (int): Button width
            icon_name (str): Icon name
            labels (tuple[str, str]): Button labels (label_spanish, label_english)
            state (bool): Button toggle State of activation
                Options: True: On, False: Off
            enabled (bool): Button enabled / disabled
            theme_style (bool): App theme style name
            language (int): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 32)
        self.setEnabled(enabled)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)
        self.icon_name = icon_name
        self.labels = labels
        self.state = state
        
        self.set_icon(state, theme_style) if icon_name is not None else None
        self.set_language(language) if self.labels is not None else None

        self.clicked.connect(clicked_signal)


    def set_icon(self, state: bool, theme_style: bool) -> None:
        """ Change button icon """
        if state:
            color = 'black'
        else:
            color = 'black' if theme_style else 'white'
        colorized_icon = icon_color(color, self.icon_name)
        self.setIcon(colorized_icon)


    def set_language(self, language: str) -> None:
        """ Change language of button label """
        if self.labels is not None:
            if language == 'es':   self.setText(self.labels[0])
            elif language == 'en': self.setText(self.labels[1])


class UI_ThemeButton(QToolButton):
    """
    Theme Button component
    """
    def __init__(self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        state: bool = False,
        enabled: bool = True
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            clicked_signal (callable): Button 'clicked' method name
            position (tuple[int, int]): Button top left corner position (x, y)
            state (bool): State of activation
                Options: True: On, False: Off
            enabled (bool): Button enabled / disabled
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(32, 32)
        self.setEnabled(enabled)
        
        self.set_state(state)

        self.clicked.connect(clicked_signal)


    def set_state(self, state: bool) -> None:
        """ Set button state and corresponding icon """
        icon_name = 'light_mode' if state else 'dark_mode'
        color = 'black'
        colorized_icon = icon_color(color, icon_name)
        self.setIcon(colorized_icon)


class UI_DropDownButton(QToolButton):
    """
    Drop Down Button component
    """
    def __init__(
        self,
        parent: QWidget,
        clicked_signal: callable,
        actions_list: dict[str, tuple[callable, str]],
        position: tuple[int, int] = (8,8),
        width: int = 64,
        icon_name: str = None,
        labels: tuple[str, str] = None,
        enabled: bool = True,
        theme_style: bool = True,
        language: str = 'es'
    ):
        """
        Parameters
        ----------
            parent (QWidget): UI Parent object
            clicked_signal (callable): Button 'clicked' method name
            position (tuple[int, int]): Button top left corner position (x, y)
            width (int): Button width
            icon_name (str): Icon name
            labels (tuple[str, str]): Button labels (label_spanish, label_english)
            
            enabled (bool): Button enabled / disabled
            theme_color (str): App theme color name
            theme_style (bool): App theme style name
            language (int): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setEnabled(enabled)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        self.labels = labels
        self.icon_name = icon_name
        self.actions_list = actions_list

        self.set_icon(theme_style) if icon_name is not None else None
        self.set_language(language) if self.labels is not None else None
        
        self.dropdown_menu = QMenu(self)
        self.dropdown_menu.setWindowFlags(self.dropdown_menu.windowFlags() | Qt.NoDropShadowWindowHint)
        
        self.none_icons = not any([item[2] for item in self.actions_list])
        self.set_actions_menu(self.none_icons, theme_style)
        menu_width = width-62 if self.none_icons else width-86
        self.dropdown_menu.setStyleSheet(f"UI_DropDownButton QMenu::item {{ padding-right: {menu_width} }}")
        

        self.clicked.connect(clicked_signal)


    def set_icon(self, theme_style: bool) -> None:
        """ Change button icon """
        color = 'black' if theme_style else 'white'
        colorized_icon = icon_color(color, self.icon_name)
        self.setIcon(colorized_icon)


    def set_actions_menu(self, none_icons: list, theme_style: bool) -> None:
        for name, action, icon_name in self.actions_list:
            action_item = QAction(name)
            action_item.triggered.connect(action)
            if not none_icons:
                color = 'black' if theme_style else 'white'
                colorized_icon = icon_color(color, icon_name)
                action_item.setIcon(colorized_icon)
            self.dropdown_menu.insertAction(None, action_item)
        self.setMenu(self.dropdown_menu)


    def set_language(self, language: str) -> None:
        """ Change language of button label """
        if self.labels is not None:
            if language == 'es':   self.setText(self.labels[0])
            elif language == 'en': self.setText(self.labels[1])