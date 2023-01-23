"""
PyQt Main Window

"""

from components.style_color import colors

# ------
# Window
# ------
class MD3Window:
    def __init__(self, attributes):
        self.attributes = attributes

        self.parent = attributes['parent']

        w, h = attributes['size'] if 'size' in attributes else (1300, 700)
        screen_x = int(self.parent.screen().availableGeometry().width() / 2 - (w / 2))
        screen_y = int(self.parent.screen().availableGeometry().height() / 2 - (h / 2))
        x, y = attributes['position'] if 'position' in attributes else (screen_x,screen_y)
        self.parent.setGeometry(x, y, w, h)
        self.parent.setMinimumSize(w, h)

        self.setThemeStyle(attributes['theme'])
        self.setLanguage(attributes['language'])
            

    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        
        background_color = colors(theme, 'background')
        color = colors(theme, 'on_background')
        menu_color = colors(theme, 'on_surface')
        menu_border_color = colors(theme, 'on_background')
        menu_background_color = colors(theme, 'surface')

        self.parent.setStyleSheet(f'QWidget {{ '
                f'background-color: {background_color};'
                f'color: {color} }}'
                f'QComboBox QListView {{ '
                f'border: 1px solid {menu_border_color}; '
                f'border-radius: 4;'
                f'background-color: {menu_background_color}; '
                f'color: {menu_color} }}')


    def setLanguage(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.parent.setWindowTitle(self.attributes['labels'][0])
            elif language == 1: self.parent.setWindowTitle(self.attributes['labels'][1])