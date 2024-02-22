from PySide6.QtWidgets import QApplication, QMainWindow

from main_ui import Main_UI

from components.ui_button import UI_Button, UI_ThemeButton, UI_ToggleButton, UI_DropDownButton
from components.ui_checkbox import UI_CheckBox
from components.ui_radiobutton import UI_RadioButton
from components.ui_switch import UI_Switch
from components.ui_text import UI_PasswordBox
from components.ui_datetimepicker import UI_CalendarView
from themes.colors import dark_colors, light_colors, theme_colors, icons

import sys
import yaml
from typing import Union

from icecream import ic

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

        # -----------
        # Apply Theme
        # -----------
        with open('themes/style.qss', 'r') as qss_file:
            style_qss = qss_file.read()
        
        style_colors = light_colors if self.theme_style else dark_colors
        for color_name, color_value in style_colors.items():
            style_qss = style_qss.replace(color_name, f"hsl({color_value[0]}, {color_value[1]}%, {color_value[2]}%)")
        
        for color_name, color_value in theme_colors[self.theme_color].items():
            style_qss = style_qss.replace(color_name, f"hsl({color_value[0]}, {color_value[1]}%, {color_value[2]}%)")

        for icon_name, icon_value in icons[self.theme_style].items():
            style_qss = style_qss.replace(icon_name, icon_value)

        self.setStyleSheet(style_qss)


    # ---------------------
    # Theme Button Function
    # ---------------------
    def theme_button_clicked(self) -> None:
        """ Theme toggle control """
        state = not self.theme_style
        style_colors = light_colors if state else dark_colors

        with open('themes/style.qss', 'r') as qss_file:
            style_qss = qss_file.read()
        
        for color_name, color_value in style_colors.items():
            style_qss = style_qss.replace(color_name, f"hsl({color_value[0]}, {color_value[1]}%, {color_value[2]}%)")
        
        for color_name, color_value in theme_colors[self.theme_color].items():
            style_qss = style_qss.replace(color_name, f"hsl({color_value[0]}, {color_value[1]}%, {color_value[2]}%)")

        for icon_name, icon_value in icons[state].items():
            style_qss = style_qss.replace(icon_name, icon_value)

        self.setStyleSheet(style_qss)
        
        for key in self.ui.gui_widgets.keys():
            if isinstance(self.ui.gui_widgets[key], Union[UI_Button, UI_ThemeButton, UI_ToggleButton, UI_CheckBox, UI_RadioButton, UI_PasswordBox]):
                self.ui.gui_widgets[key].set_icon(state)
            if isinstance(self.ui.gui_widgets[key], UI_DropDownButton):
                self.ui.gui_widgets[key].set_icon(state)
                for action in self.ui.gui_widgets[key].menu().actions():
                    self.ui.gui_widgets[key].menu().removeAction(action)
                self.ui.gui_widgets[key].set_actions_menu(state, self.language_value)
            if isinstance(self.ui.gui_widgets[key], UI_CalendarView):
                self.ui.gui_widgets[key].set_header(state)
            if isinstance(self.ui.gui_widgets[key], UI_Switch):
                self.ui.gui_widgets[key].set_state(state, self.ui.gui_widgets[key].state)
            

        # Save settings
        self.theme_style = state
        self.config['THEME_STYLE'] = state
        with open(self.settings_file, 'w') as file:
            yaml.dump(self.config, file)

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
            if hasattr(self.ui.gui_widgets[key], 'set_language'):
                self.ui.gui_widgets[key].set_language(index)
            if isinstance(self.ui.gui_widgets[key], UI_DropDownButton):
                for action in self.ui.gui_widgets[key].menu().actions():
                    self.ui.gui_widgets[key].menu().removeAction(action)
                self.ui.gui_widgets[key].set_actions_menu(self.theme_style, index)
        
        self.language_value = index
        self.config['LANGUAGE'] = index
        with open(self.settings_file, 'w') as file:
            yaml.dump(self.config, file)

    # ----------------
    # Button Functions
    # ----------------
    def standard_button_clicked(self) -> None:
        print('Standard button clicked')

    def toggle_1_button_clicked(self, state: bool) -> None:
        print(f'toggle 1 button state: {state}')
        self.ui.gui_widgets['toggle_1_button'].state = state
        self.ui.gui_widgets['toggle_1_button'].set_icon(self.theme_style)

    def toggle_2_button_clicked(self, state: bool) -> None:
        print(f'toggle 2 button state: {state}')
        self.ui.gui_widgets['toggle_2_button'].state = state
        self.ui.gui_widgets['toggle_2_button'].set_icon(self.theme_style)

    def dropdown_1_button_clicked(self) -> None:
        print(f'Botón Drop Down')

    def action_1(self):
        print('Drop Down action 1')

    def action_2(self):
        print('Drop Down action 2')

    def action_3(self):
        print('Drop Down action 3')

    def action_4(self):
        print('Drop Down action 4')

    def action_5(self):
        print('Drop Down action 5')

    # ------------------
    # Checkbox Functions
    # ------------------
    def option_1_changed(self, state) -> None:
        state_dict = {
            0: 'off',
            1: 'indeterminate',
            2: 'on'
        }
        print(state_dict[state])

    def option_2_changed(self, state) -> None:
        state_dict = {
            0: 'off',
            1: 'indeterminate',
            2: 'on'
        }
        print(state_dict[state])

    def option_3_changed(self, state) -> None:
        state_dict = {
            0: 'off',
            1: 'indeterminate',
            2: 'on'
        }
        print(state_dict[state])

    # ------------------
    # Combobox Functions
    # ------------------
    def menu_1_index_changed(self, index: int) -> None:
        print(index)
        
    def menu_1_text_changed(self, text: str) -> None:
        print(text)

    def menu_1_activated(self, index: int) -> None:
        print(index)


    # ----------------
    # Slider Functions
    # ----------------
    def bar_1_slider_sliderMoved(self, value: int) -> None:
        print(f"Slider 1: {value}")
    

    def bar_1_slider_sliderReleased(self, value: int) -> None:
        print(f"Slider 1: {value}")
    
    
    def bar_2_slider_sliderMoved(self, value: int) -> None:
        print(f"Slider 2: {value}")
    

    def bar_2_slider_sliderReleased(self, value: int) -> None:
        print(f"Slider 2: {value}")
    
    # ----------------
    # Switch Functions
    # ----------------
    def on_test1_switch_clicked(self, state: bool) -> None:
        self.ui.gui_widgets['test1_switch'].state = state
        self.ui.gui_widgets['test1_switch'].set_state(self.theme_style, state)


if __name__=="__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())