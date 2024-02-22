from PySide6.QtWidgets import QPushButton, QToolButton, QMenu, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QColor

from components.icons import icons

import qtawesome as qta
from themes.colors import light_colors, dark_colors, theme_colors

from icecream import ic

class UI_Button(QPushButton):
    """ Button component """
    def __init__(
        self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8, 8),
        width: int = 40,
        type: str = 'standard',
        icon_name: str = None,
        texts: tuple[str, str] = None,
        enabled: bool = True,
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
            texts (tuple[str, str]): Button texts (label_spanish, label_english)
            enabled (bool): Button enabled / disabled
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setEnabled(enabled)
        self.type = type
        self.texts = texts
        self.icon_name = icon_name

        self.set_language(language)
        self.setProperty('type', self.type)
        self.set_icon()

        self.clicked.connect(clicked_signal)

    def set_icon(self) -> None:
        if self.icon_name is not None:
            color = self.parent.parent.theme_color
            style = self.parent.parent.theme_style
            button_types = {
                'standard': (light_colors['@text_active'], dark_colors['@text_active']),
                'accent': (light_colors['@background_full'], dark_colors['@background_full']),
                'outlined': (theme_colors[color]['@theme_active'], theme_colors[color]['@theme_active']),
                'hyperlink': (theme_colors[color]['@theme_active'], theme_colors[color]['@theme_active'])
            }
            h, s, l = button_types[self.type][0] if style else button_types[self.type][1]
            icon = qta.icon(f"mdi6.{self.icon_name}", color=QColor.fromHslF(h/360, s/100, l/100))
            self.setIcon(icon)


    def set_language(self, language: str) -> None:
        """ Change language of button text """
        if self.texts is not None:
            if language == 'es': self.setText(self.texts[0])
            elif language == 'en': self.setText(self.texts[1])


class UI_ToggleButton(QPushButton):
    """ Toggle Button component """
    def __init__(
        self,
        parent: QWidget,
        clicked_signal: callable,
        position: tuple[int, int] = (8,8),
        width: int = 40,
        icon_name: str = None,
        texts: tuple[str, str] = None,
        state: bool = False,
        enabled: bool = True,
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
            texts (tuple[str, str]): Button texts (label_spanish, label_english)
            state (bool): Button toggle State of activation
                Options: True: On, False: Off
            enabled (bool): Button enabled / disabled
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setEnabled(enabled)
        self.setCheckable(True)
        self.icon_code = icons[icon_name] if icon_name is not None else ''
        self.texts = texts
        self.state = state
        
        self.set_language(language)

        self.clicked.connect(clicked_signal)

    def set_language(self, language: str) -> None:
        """ Change language of button text """
        button_text = self.icon_code
        space = ' ' if button_text != '' and self.texts is not None else ''
        if self.texts is not None:
            if language == 'es':
                button_text = f"{button_text}{space}{self.texts[0]}"
            elif language == 'en':
                button_text = f"{button_text}{space}{self.texts[1]}"
        self.setText(button_text)


class UI_ThemeButton(QPushButton):
    """ Theme Button component """
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
        self.resize(40, 40)
        self.setEnabled(enabled)
        
        self.set_state(state)

        self.clicked.connect(clicked_signal)

    def set_state(self, state: bool) -> None:
        """ Set button state and corresponding icon """
        icon_theme = qta.icon('ph.sun') if state else qta.icon('ph.moon')
        self.setIcon(icon_theme)


class UI_DropDownButton(QToolButton):
    """ Drop Down Button component """
    def __init__(
        self,
        parent: QWidget,
        clicked_signal: callable,
        actions_list: dict[str, tuple[callable, str]],
        position: tuple[int, int] = (8,8),
        width: int = 64,
        icon_name: str = None,
        texts: tuple[str, str] = None,
        enabled: bool = True,
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
            texts (tuple[str, str]): Button texts (label_spanish, label_english)
            enabled (bool): Button enabled / disabled
            theme_color (str): App theme color name
            language (str): App language
                Options: 'es' = Español, 'en' = English
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(width, 40)
        self.setEnabled(enabled)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        self.texts = texts
        self.icon_code = icons[icon_name] if icon_name is not None else ''
        self.actions_list = actions_list

        self.set_language(language)
        
        self.dropdown_menu = QMenu(self)
        self.dropdown_menu.setWindowFlags(self.dropdown_menu.windowFlags() | Qt.NoDropShadowWindowHint)

        self.set_actions_menu(language)
        self.dropdown_menu.setStyleSheet(f"UI_DropDownButton QMenu::item {{ padding-right: {width-82} }}")
        
        self.clicked.connect(clicked_signal)

    def set_actions_menu(self, language: str) -> None:
        """ Set action buttons for drop down menu """
        for name_es, name_en, action, icon_name in self.actions_list:
            icon_code = icons[icon_name] if icon_name is not None else ''
            space = ' ' if icon_code != '' and name_es is not None else ''
            if language == 'es':
                action_name = f"{icon_code}{space}{name_es}"
            elif language == 'en':
                action_name = f"{icon_code}{space}{name_en}"
            action_item = QAction(action_name)
            action_item.triggered.connect(action)
            self.dropdown_menu.insertAction(None, action_item)
        self.setMenu(self.dropdown_menu)

    def set_language(self, language: str) -> None:
        """ Change language of button text """
        button_text = self.icon_code
        space = ' ' if button_text != '' and self.texts is not None else ''
        if self.texts is not None:
            if language == 'es':
                button_text = f"{button_text}{space}{self.texts[0]}"
            elif language == 'en':
                button_text = f"{button_text}{space}{self.texts[1]}"
        self.setText(button_text)