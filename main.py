from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from main_ui import Main_UI

from components.ui_button import UI_Button, UI_ToggleButton, UI_DropDownButton

import sys
import yaml


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings_file = 'settings.yaml'
        with open(self.settings_file, 'r') as file:
            self.config = yaml.safe_load(file)

        self.language_value = self.config['LANGUAGE']
        self.theme_style = self.config['THEME_STYLE']
        self.theme_color = self.config['THEME_COLOR']

        # ----------------
        # Generación de UI
        # ----------------
        self.ui = Main_UI(self)
        theme_file = f"themes/{self.theme_color}_light_theme.qss" if self.theme_style else f"themes/{self.theme_color}_dark_theme.qss"
        with open(theme_file, "r") as theme_qss:
            self.setStyleSheet(theme_qss.read())


    # ---------------------
    # Icon Button Functions
    # ---------------------
    def standard_button_clicked(self) -> None:
        print('Standard button clicked')

    def toggle_1_button_clicked(self, state: bool) -> None:
        print(f'toggle 1 button state: {state}')
        self.ui.gui_widgets['toggle_1_button'].set_icon(state, self.theme_style)
        self.ui.gui_widgets['toggle_1_button'].state = state

    def toggle_2_button_clicked(self, state: bool) -> None:
        print(f'toggle 2 button state: {state}')
        self.ui.gui_widgets['toggle_2_button'].set_icon(state, self.theme_style)
        self.ui.gui_widgets['toggle_2_button'].state = state

    def toggle_3_button_clicked(self, state: bool) -> None:
        print(f'toggle 3 button state: {state}')
        self.ui.gui_widgets['toggle_3_button'].set_icon(state, self.theme_style)
        self.ui.gui_widgets['toggle_3_button'].state = state

    def toggle_4_button_clicked(self, state: bool) -> None:
        print(f'toggle 4 button state: {state}')
        self.ui.gui_widgets['toggle_4_button'].set_icon(state, self.theme_style)
        self.ui.gui_widgets['toggle_4_button'].state = state

    def dropdown_1_button_clicked(self, index: int) -> None:
        print(f'Indice: {index}')

    def action_1(self):
        print('test')


    # # --------------------------
    # # Segmented Button Functions
    # # --------------------------
    # def on_left_segmented1_button_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['left_segmented1_button'].set_state(state, self.theme_color)
        
    # def on_center1_segmented1_button_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['center1_segmented1_button'].set_state(state, self.theme_color)

    # def on_center2_segmented1_button_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['center2_segmented1_button'].set_state(state, self.theme_color)

    # def on_right_segmented1_button_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['right_segmented1_button'].set_state(state, self.theme_color)

    # def on_left_segmented2_button_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['left_segmented2_button'].set_state(state, self.theme_color)

    # def on_center1_segmented2_button_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['center1_segmented2_button'].set_state(state, self.theme_color)

    # def on_center2_segmented2_button_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['center2_segmented2_button'].set_state(state, self.theme_color)

    # def on_right_segmented2_button_clicked(self, state:bool) -> None:
    #     self.ui.gui_widgets['right_segmented2_button'].set_state(state, self.theme_color)


    # ---------------------
    # Theme Button Function
    # ---------------------
    def theme_button_clicked(self) -> None:
        """
        Theme toggle control
        """
        state = not self.theme_style
        theme = 'light' if state else 'dark'
        theme_qss_file = f"themes/{self.theme_color}_{theme}_theme.qss"
        with open(theme_qss_file, "r") as theme_qss:
            self.setStyleSheet(theme_qss.read())

        for key in self.ui.gui_widgets.keys():
            if isinstance(self.ui.gui_widgets[key], UI_Button) and self.ui.gui_widgets[key].type == 'standard':
                self.ui.gui_widgets[key].set_icon(state, self.theme_color) if self.ui.gui_widgets[key].icon_name is not None else None
            if isinstance(self.ui.gui_widgets[key], UI_ToggleButton):
                self.ui.gui_widgets[key].set_icon(self.ui.gui_widgets[key].state, state) if self.ui.gui_widgets[key].icon_name is not None else None
            if isinstance(self.ui.gui_widgets[key], UI_DropDownButton):
                self.ui.gui_widgets[key].set_icon(state) if self.ui.gui_widgets[key].icon_name is not None else None


        self.ui.gui_widgets['theme_1_button'].set_state(state)
        self.ui.gui_widgets['theme_2_button'].set_state(state)

        # Save settings
        self.theme_style = state
        self.config['THEME_STYLE'] = state
        with open(self.settings_file, 'w') as file:
            yaml.dump(self.config, file)


    # # ---------------
    # # Chips Functions
    # # ---------------
    # def on_chip1_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['chip1_button'].set_state(state, self.theme_color)

    # def on_chip2_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['chip2_button'].set_state(state, self.theme_color)

    # def on_chip3_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['chip3_button'].set_state(state, self.theme_color)

    # def on_chip4_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['chip4_button'].set_state(state, self.theme_color)

    # def on_chip5_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['chip5_button'].set_state(state, self.theme_color)

    # def on_chip6_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['chip6_button'].set_state(state, self.theme_color)


    # # ----------------
    # # Switch Functions
    # # ----------------
    # def on_test1_switch_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['test1_switch'].set_state(state, self.theme_color)
        
    # def on_test2_switch_clicked(self, state: bool) -> None:
    #     self.ui.gui_widgets['test2_switch'].set_state(state, self.theme_color)

    # # -------------
    # # Menu Function
    # # -------------
    # def on_language_changed(self, index: int) -> None:
    #     """ Language menu control to change components text language
        
    #     Parameters
    #     ----------
    #     index: int
    #         Index of language menu control
        
    #     Returns
    #     -------
    #     None
    #     """
    #     for key in self.ui.gui_widgets.keys():
    #         if hasattr(self.ui.gui_widgets[key], 'set_language'):
    #             self.ui.gui_widgets[key].set_language(index)
        
    #     self.language_value = index
    #     self.config['LANGUAGE'] = index
    #     with open(self.settings_file, 'w') as file:
    #         yaml.dump(self.config, file)

    # # ----------------
    # # Slider Functions
    # # ----------------
    # def on_test1_slider_sliderMoved(self, value: int) -> None:
    #     self.ui.gui_widgets['value1_label'].setText(str(value))
    

    # def on_test1_slider_sliderReleased(self) -> None:
    #     print(f'Slider 1 value: {self.ui.gui_widgets["test1_slider"].value()}')
    
    
    # def on_test2_slider_sliderMoved(self, value: int) -> None:
    #     self.ui.gui_widgets['value2_label'].setText(str(value))
    

    # def on_test2_slider_sliderReleased(self) -> None:
    #     print(f'Slider 2 value: {self.ui.gui_widgets["test2_slider"].value()}')
    
    # # --------------------
    # # Text Field Functions
    # # --------------------
    # def on_text8_field_return_pressed(self) -> None:
    #     print(f'Text 8 Value: {self.ui.gui_widgets["test8_textfield"].text_field.text()}')


if __name__=="__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
