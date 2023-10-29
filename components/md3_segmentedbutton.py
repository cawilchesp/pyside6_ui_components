"""
PySide6 Segmented Button component adapted to follow Material Design 3 guidelines


"""
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

# ----------------
# Segmented Button
# ----------------
class MD3SegmentedButton(QtWidgets.QToolButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Segmented Button

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                    Button position
                    (x, y) -> x, y: upper left corner
            width: int
                Button width
            labels: tuple
                Segmented button text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            icon: str
                Icon file without extension ('icon')
            check_icon: bool
                Use check icon for selected option
            location: str
                Position of the segmented button in the group
                Options: 'left', 'center', 'right'
            state: bool
                State of activation
                True: On, False: Off
            enabled: bool
                Segmented button enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            language: int
                App language
                0: Spanish, 1: English
            clicked: def
                Segmented button 'clicked' method name
        
        Returns
        -------
        None
        """
        super(MD3SegmentedButton, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)

        self.setProperty(self.attributes['location'], True)
        self.setState(attributes['state'], attributes['theme'])
        self.setLanguage(attributes['language'])

        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.clicked.connect(attributes['clicked'])
        

    def setState(self, state: bool, theme: bool) -> None:
        """ Set button state and corresponding icon """

        self.setChecked(state)
        icon_theme = 'L' if theme else 'D'
        icon_image = self.attributes['icon'] if 'icon' in self.attributes else 'none'
        if state and self.attributes['check_icon']:
            icon_image = 'done'
        icon_path = f"icons/{icon_image}_{icon_theme}.png"
        self.setIcon(QtGui.QIcon(f"{icon_path}"))


    def setLanguage(self, language: int) -> None:
        """ Change language of label text """
        if 'labels' in self.attributes:
            if language == 0:   self.setText(self.attributes['labels'][0])
            elif language == 1: self.setText(self.attributes['labels'][1])