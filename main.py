from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow

import sys
import yaml

from main_ui import UI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings_file = 'settings.yaml'
        with open(self.settings_file, 'r') as file:
            self.config = yaml.safe_load(file)

        self.language_value = int(self.config['LANGUAGE'])
        self.theme_value = self.config['THEME']

        # ----------------
        # Generación de UI
        # ----------------
        self.ui = UI(self)
        theme_file = 'themes/light_theme.qss' if self.theme_value else 'themes/dark_theme.qss'
        with open(theme_file, "r") as theme_qss:
            self.setStyleSheet(theme_qss.read())



    # ---------------------
    # Icon Button Functions
    # ---------------------
    def on_icon1_button_clicked(self) -> None:
        print('Icon button 1 clicked')

    def on_icon2_button_clicked(self) -> None:
        print('Icon button 2 clicked')

    def on_icon3_button_clicked(self) -> None:
        print('Icon button 3 clicked')

    def on_icon4_button_clicked(self) -> None:
        print('Icon button 4 clicked')

    def on_icon5_button_clicked(self) -> None:
        print('Icon button 5 clicked')

    def on_icon6_button_clicked(self) -> None:
        print('Icon button 6 clicked')

    def on_icon7_button_clicked(self) -> None:
        print('Icon button 7 clicked')

    def on_icon8_button_clicked(self) -> None:
        print('Icon button 8 clicked')


    # ----------------
    # Button Functions
    # ----------------
    def on_boton1_button_clicked(self) -> None:
        self.ui.gui_widgets['icon1_label'].setIconLabel('calendar', self.theme_value)

    def on_boton2_button_clicked(self) -> None:
        selected_color = QtWidgets.QColorDialog.getColor()
        color = selected_color.name()
        self.ui.gui_widgets['color1_label'].setColorLabel(color, self.theme_value)

    def on_boton3_button_clicked(self) -> None:
        print('Button 3 clicked')

    def on_boton4_button_clicked(self) -> None:
        print('Button 4 clicked')

    def on_boton5_button_clicked(self) -> None:
        print('Button 5 clicked')

    def on_boton6_button_clicked(self) -> None:
        print('Button 6 clicked')

    def on_boton7_button_clicked(self) -> None:
        print('Button 7 clicked')

    def on_boton8_button_clicked(self) -> None:
        print('Button 8 clicked')


    # --------------------------
    # Segmented Button Functions
    # --------------------------
    def on_left_segmented1_button_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['left_segmented1_button'].setState(state, self.theme_value)
        
    def on_center1_segmented1_button_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['center1_segmented1_button'].setState(state, self.theme_value)

    def on_center2_segmented1_button_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['center2_segmented1_button'].setState(state, self.theme_value)

    def on_right_segmented1_button_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['right_segmented1_button'].setState(state, self.theme_value)

    def on_left_segmented2_button_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['left_segmented2_button'].setState(state, self.theme_value)

    def on_center1_segmented2_button_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['center1_segmented2_button'].setState(state, self.theme_value)

    def on_center2_segmented2_button_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['center2_segmented2_button'].setState(state, self.theme_value)

    def on_right_segmented2_button_clicked(self, state:bool) -> None:
        self.ui.gui_widgets['right_segmented2_button'].setState(state, self.theme_value)


    # ---------------------------------
    # Theme Segmented Buttons Functions
    # ---------------------------------
    def on_light_theme_clicked(self, state: bool) -> None:
        """ Light theme segmented control to change components stylesheet
        
        Parameters
        ----------
        state: bool
            State of light theme segmented control
        
        Returns
        -------
        None
        """
        if state: 
            # for key in self.ui.gui_widgets.keys():
            #     self.ui.gui_widgets[key].setThemeStyle(True)
            with open('themes/light_theme.qss', "r") as theme_qss:
                self.setStyleSheet(theme_qss.read())
            self.ui.gui_widgets['dark_theme_button'].setState(False, True)
            self.ui.gui_widgets['dark2_theme_button'].setState(False, True)
    
            # Save settings
            self.theme_value = True
            self.config['THEME'] = True
            with open(self.settings_file, 'w') as file:
                yaml.dump(self.config, file)
        
        self.ui.gui_widgets['light_theme_button'].setState(True, True)
        self.ui.gui_widgets['light2_theme_button'].setState(True, True)

    def on_dark_theme_clicked(self, state: bool) -> None:
        """ Dark theme segmented control to change components stylesheet
        
        Parameters
        ----------
        state: bool
            State of dark theme segmented control
        
        Returns
        -------
        None
        """
        if state: 
            # for key in self.ui.gui_widgets.keys():
            #     self.ui.gui_widgets[key].setThemeStyle(False)
            with open('themes/dark_theme.qss', "r") as theme_qss:
                self.setStyleSheet(theme_qss.read())
            self.ui.gui_widgets['light_theme_button'].setState(False, False)
            self.ui.gui_widgets['light2_theme_button'].setState(False, False)

            # Save settings
            self.theme_value = False
            self.config['THEME'] = False
            with open(self.settings_file, 'w') as file:
                yaml.dump(self.config, file)

        self.ui.gui_widgets['dark_theme_button'].setState(True, False)
        self.ui.gui_widgets['dark2_theme_button'].setState(True, False)


    # ---------------
    # Chips Functions
    # ---------------
    def on_chip1_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['chip1_button'].setState(state, self.theme_value)

    def on_chip2_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['chip2_button'].setState(state, self.theme_value)

    def on_chip3_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['chip3_button'].setState(state, self.theme_value)

    def on_chip4_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['chip4_button'].setState(state, self.theme_value)

    def on_chip5_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['chip5_button'].setState(state, self.theme_value)

    def on_chip6_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['chip6_button'].setState(state, self.theme_value)


    # ----------------
    # Switch Functions
    # ----------------
    def on_test1_switch_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['test1_on_switch'].setState(state, self.theme_value)
        self.ui.gui_widgets['test1_off_switch'].setState(state, self.theme_value)
        
    def on_test2_switch_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['test2_on_switch'].setState(state, self.theme_value)
        self.ui.gui_widgets['test2_off_switch'].setState(state, self.theme_value)

    # -------------
    # Menu Function
    # -------------
    def on_language_changed(self, index: int) -> None:
        """ Language menu control to change components text language
        
        Parameters
        ----------
        index: int
            Index of language menu control
        
        Returns
        -------
        None
        """
        for key in self.ui.gui_widgets.keys():
            if hasattr(self.ui.gui_widgets[key], 'setLanguage'):
                self.ui.gui_widgets[key].setLanguage(index)
        
        self.language_value = index
        self.config['LANGUAGE'] = index
        with open(self.settings_file, 'w') as file:
            yaml.dump(self.config, file)

    # ----------------
    # Slider Functions
    # ----------------
    def on_test1_slider_sliderMoved(self, value: int) -> None:
        self.ui.gui_widgets['value1_label'].setText(str(value))
    

    def on_test1_slider_sliderReleased(self) -> None:
        print(f'Slider 1 value: {self.ui.gui_widgets["test1_slider"].value()}')
    
    def on_test2_slider_sliderMoved(self, value: int) -> None:
        self.ui.gui_widgets['value2_label'].setText(str(value))
    

    def on_test2_slider_sliderReleased(self) -> None:
        print(f'Slider 2 value: {self.ui.gui_widgets["test2_slider"].value()}')
    
    # --------------------
    # Text Field Functions
    # --------------------
    def on_text8_field_return_pressed(self) -> None:
        print(f'Text 8 Value: {self.ui.gui_widgets["test8_textfield"].text_field.text()}')


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
