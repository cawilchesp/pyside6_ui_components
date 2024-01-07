from PySide6.QtWidgets import QWidget

from components.ui_window import UI_Window
from components.ui_card import UI_Card
from components.ui_label import UI_Label, UI_IconLabel, UI_ColorLabel
from components.ui_button import UI_Button, UI_ToggleButton, UI_ThemeButton, UI_DropDownButton
from components.ui_checkbox import UI_CheckBox
from components.ui_combobox import UI_ComboBox
from components.md3_chip import MD3Chip
from components.md3_datepicker import MD3DatePicker
from components.md3_divider import MD3Divider
from components.md3_imagelabel import MD3ImageLabel
from components.md3_segmentedbutton import MD3SegmentedButton
from components.md3_slider import MD3Slider
from components.md3_switch import MD3Switch
from components.md3_textfield import MD3TextField

import yaml


class Main_UI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # --------
        # Settings
        # --------
        self.settings_file = 'settings.yaml'
        with open(self.settings_file, 'r') as file:
            self.config = yaml.safe_load(file)

        self.language_value = self.config['LANGUAGE']
        self.theme_style = self.config['THEME_STYLE']
        self.theme_color = self.config['THEME_COLOR']

        # ---------
        # Variables
        # ---------
        self.test_options = {
            0: ('Opción 1', 'Option 1'),
            1: ('Opción 2', 'Option 2')
        }

        self.gui_widgets = {}

        # *****************************************************************
        #                           Main Window
        # *****************************************************************
        (width, height) = (1300, 700)
        self.gui_widgets['main_window'] = UI_Window(
            parent=parent,
            size=(width, height),
            minimum_size=(width,height),
            titles=('Componentes de UI', 'UI Components'),
            language=self.language_value
        )

        # *****************************************************************
        #                           Card Filled
        # *****************************************************************
        self.gui_widgets['filled_card'] = UI_Card(
            parent=parent,
            position=(16, 16), 
            size=(628, height - 32),
            type='filled',
            titles=('Tarjeta Llena', 'Filled Card'),
            language=self.language_value
        )

        # -------
        # Buttons
        # -------
        self.gui_widgets['buttons_1_label'] = UI_Label(
            parent=self.gui_widgets['filled_card'],
            position=(16, 60),
            width=100,
            align='left',
            labels=('Botones', 'Buttons'),
            language=self.language_value
        )

        self.gui_widgets['standard_1_button'] = UI_Button(
            parent=self.gui_widgets['filled_card'],
            position=(16, 100),
            width=100,
            type='standard',
            icon_name='bicycle',
            labels=('Estándar', 'Standard'),
            theme_color=self.theme_color,
            theme_style=self.theme_style,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['accent_1_button'] = UI_Button(
            parent=self.gui_widgets['filled_card'],
            position=(124, 100),
            width=100,
            type='accent',
            icon_name='bicycle',
            labels=('Acentuado', 'Accent'),
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['outline_1_button'] = UI_Button(
            parent=self.gui_widgets['filled_card'],
            position=(16, 140),
            width=100,
            type='outlined',
            icon_name='bicycle',
            labels=('Delineado', 'Outlined'),
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['hyperlink_1_button'] = UI_Button(
            parent=self.gui_widgets['filled_card'],
            position=(124, 140),
            width=100,
            type='hyperlink',
            icon_name='bicycle',
            labels=('Hipervínculo', 'Hyperlink'),
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['standard_2_button'] = UI_Button(
            parent=self.gui_widgets['filled_card'],
            position=(16, 180),
            type='standard',
            icon_name='bicycle',
            theme_color=self.theme_color,
            theme_style=self.theme_style,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['accent_2_button'] = UI_Button(
            parent=self.gui_widgets['filled_card'],
            position=(56, 180),
            type='accent',
            icon_name='bicycle',
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['outline_2_button'] = UI_Button(
            parent=self.gui_widgets['filled_card'],
            position=(96, 180),
            type='outlined',
            icon_name='bicycle',
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['hyperlink_2_button'] = UI_Button(
            parent=self.gui_widgets['filled_card'],
            position=(136, 180),
            type='hyperlink',
            icon_name='bicycle',
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['theme_1_button'] = UI_ThemeButton(
            parent=self.gui_widgets['filled_card'],
            position=(16, 220),
            state=self.theme_style,
            clicked_signal=parent.theme_button_clicked
        )
        
        self.gui_widgets['toggle_1_button'] = UI_ToggleButton(
            parent=self.gui_widgets['filled_card'],
            position=(56, 220),
            width=150,
            icon_name='bicycle',
            labels=('Botón Toggle', 'Toggle Button'),
            theme_style=self.theme_style,
            language=self.language_value,
            clicked_signal=parent.toggle_1_button_clicked
        )

        self.gui_widgets['toggle_2_button'] = UI_ToggleButton(
            parent=self.gui_widgets['filled_card'],
            position=(214, 220),
            icon_name='bicycle',
            theme_style=self.theme_style,
            language=self.language_value,
            clicked_signal=parent.toggle_2_button_clicked
        )

        self.gui_widgets['dropdown_1_button'] = UI_DropDownButton(
            parent=self.gui_widgets['filled_card'],
            position=(16, 260),
            width=170,
            icon_name='bicycle',
            labels=('Botón Drop Down', 'Drop Down Button'),
            actions_list=[
                ['Bus', parent.action_1, 'bus'],
                ['Car', parent.action_2, 'car'],
                ['Man', parent.action_3, None],
                ['Woman', parent.action_4, None],
                ['School', parent.action_5, None]
            ],
            theme_style=self.theme_style,
            language=self.language_value,
            clicked_signal=parent.dropdown_1_button_clicked
        )

        # -----------
        # Check Boxes
        # -----------
        self.gui_widgets['checkboxes_1_label'] = UI_Label(
            parent=self.gui_widgets['filled_card'],
            position=(360, 60),
            width=100,
            align='left',
            labels=('Cajas de Selección', 'Check Boxes'),
            language=self.language_value
        )

        self.gui_widgets['option_1_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['filled_card'],
            state_changed_signal=parent.option_1_changed,
            position=(360,100),
            width=150,
            icon_name='bus',
            labels=('Opción Bus', 'Option Bus'),
            tristate=False,
            state=0,
            theme_style=self.theme_style,
            language=self.language_value
        )

        self.gui_widgets['option_2_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['filled_card'],
            state_changed_signal=parent.option_2_changed,
            position=(360,140),
            width=150,
            icon_name='car',
            tristate=True,
            state=1,
            theme_style=self.theme_style,
            language=self.language_value
        )

        self.gui_widgets['option_3_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['filled_card'],
            state_changed_signal=parent.option_3_changed,
            position=(360,180),
            width=150,
            labels=('Opción Camión', 'Option Truck'),
            tristate=True,
            state=2,
            theme_style=self.theme_style,
            language=self.language_value
        )

        # -----------
        # Combo Boxes
        # -----------
        self.gui_widgets['combobox_1_label'] = UI_Label(
            parent=self.gui_widgets['filled_card'],
            position=(360, 220),
            width=100,
            align='left',
            labels=('Cajas Combo', 'Combo Boxes'),
            language=self.language_value
        )

        self.gui_widgets['menu_1_combobox'] = UI_ComboBox(
            parent=self.gui_widgets['filled_card'],
            position=(360, 260),
            width=150,
            options=self.test_options,
            # set=self.language_value,
            language=self.language_value,
            # index_changed_signal=parent.on_language_changed
        )










        
        # # -----------------
        # # Segmented Buttons
        # # -----------------
        # self.gui_widgets['left_segmented1_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(8, 88),
        #     width=100,
        #     labels=('Izquierda', 'Left'),
        #     check_icon=True,
        #     location='left',
        #     state=False,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_left_segmented1_button_clicked
        # )
        
        # self.gui_widgets['center1_segmented1_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(108, 88),
        #     width=100,
        #     labels=('Centro 1', 'Center 1'),
        #     location='center',
        #     state=False,
        #     icon_name='delete',
        #     check_icon=True,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_center1_segmented1_button_clicked
        # )

        # self.gui_widgets['center2_segmented1_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(208, 88),
        #     width=100,
        #     labels=('Centro 2', 'Center 2'),
        #     icon_name='delete',
        #     check_icon=True,
        #     location='center',
        #     state=True,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_center2_segmented1_button_clicked
        # ) 

        # self.gui_widgets['right_segmented1_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(308, 88),
        #     width=100,
        #     labels=('Derecha', 'Right'),
        #     check_icon=True,
        #     location='right',
        #     state=True,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_right_segmented1_button_clicked
        # )
        
        # # ------
        # # Switch
        # # ------
        # self.gui_widgets['test1_switch'] = MD3Switch(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(504, 88),
        #     state=False,
        #     theme_color=self.theme_color,
        #     clicked_signal=parent.on_test1_switch_clicked
        # )

        # # -----
        # # Chips
        # # -----
        # self.gui_widgets['chip1_button'] = MD3Chip(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(8, 128),
        #     width=100,
        #     labels=('Borrar', 'Delete'),
        #     icon_name='delete',
        #     state=False,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_chip1_clicked
        # )
        
        # self.gui_widgets['chip2_button'] = MD3Chip(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(116, 128),
        #     width=100,
        #     labels=('Correo', 'Mail'),
        #     icon_name='mail',
        #     state=True,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_chip2_clicked
        # )
        
        # self.gui_widgets['chip3_button'] = MD3Chip(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(224, 128),
        #     width=100,
        #     labels=('Mejorar', 'Improve'),
        #     state=False,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_chip3_clicked
        # )
        
        

        # # ----------
        # # Text Field
        # # ----------
        # self.gui_widgets['test1_textfield'] = MD3TextField(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(8, 168),
        #     width=120,
        #     type='filled',
        #     labels=('Cuadro', 'Frame'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )

        # self.gui_widgets['test2_textfield'] = MD3TextField(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(136, 168),
        #     width=120,
        #     length=9,
        #     type='filled',
        #     labels=('Cuadro', 'Frame'),
        #     input='integer',
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['test3_textfield'] = MD3TextField(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(264, 168),
        #     width=120,
        #     length=9,
        #     type='filled',
        #     labels=('Cuadro', 'Frame'),
        #     input='password',
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['test4_textfield'] = MD3TextField(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(392, 168),
        #     width=120,
        #     length=9,
        #     type='filled',
        #     labels=('Cuadro', 'Frame'),
        #     input='text',
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )

        # # -----------
        # # Date Picker
        # # -----------
        # self.gui_widgets['test1_date'] = MD3DatePicker(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(8, 228),
        #     width=120,
        #     type='filled',
        #     labels=('Fecha', 'Date'),
        #     language=self.language_value
        # )

        # # ------
        # # Labels
        # # ------
        # self.gui_widgets['icon1_label'] = MD3Label(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(136, 228),
        #     type='icon',
        #     icon_name='delete',
        #     theme_color=self.theme_color
        # )

        # self.gui_widgets['subtitle1_label'] = MD3Label(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(176, 228),
        #     width=100,
        #     type='subtitle',
        #     align='left',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['subtitle2_label'] = MD3Label(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(176, 248),
        #     width=100,
        #     type='subtitle',
        #     align='center',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )

        # self.gui_widgets['subtitle3_label'] = MD3Label(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(176, 268),
        #     width=100,
        #     type='subtitle',
        #     align='right',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['color1_label'] = MD3Label(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(284, 228),
        #     type='color',
        #     color='#ff8888',
        #     theme_color=self.theme_color
        # )
        
        # self.gui_widgets['value1_label'] = MD3Label(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(324, 228),
        #     width=100,
        #     type='value',
        #     align='center',
        #     border_color='#ff8888',
        #     theme_color=self.theme_color
        # )

        # # ------
        # # Slider
        # # ------
        # self.gui_widgets['test1_slider'] = MD3Slider(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(432, 228),
        #     length=100,
        #     orientation='vertical',
        #     range=(0, 1, 100),
        #     value=50,
        #     slider_moved_signal=parent.on_test1_slider_sliderMoved,
        #     slider_released_signal=parent.on_test1_slider_sliderReleased
        # )

        # # --------
        # # Dividers
        # # --------
        # self.gui_widgets['horizontal1_divider'] = MD3Divider(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(8, 288),
        #     length=100,
        #     orientation='horizontal'
        # )
        
        # self.gui_widgets['vertical1_divider'] = MD3Divider(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(116, 288),
        #     length=32,
        #     orientation='vertical'
        # )
        
        # # -----------
        # # Image Label
        # # -----------
        # self.gui_widgets['image1_label'] = MD3ImageLabel(
        #     parent=self.gui_widgets['filled_card'],
        #     position=(124, 288),
        #     size=(300, 32),
        #     scaled_image=True
        # )







        # *****************************************************************
        #                           Card Outlined
        # *****************************************************************
        self.gui_widgets['outlined_card'] = UI_Card(
            parent=parent,
            position=(656, 16), 
            size=(628, height - 32),
            type='outlined',
            titles=('Tarjeta con Borde', 'Outlined Card'),
            language=self.language_value
        )

        # ------------
        # Icon Buttons
        # ------------
        self.gui_widgets['buttons_2_label'] = UI_Label(
            parent=self.gui_widgets['outlined_card'],
            position=(16, 60),
            width=100,
            align='left',
            labels=('Botones', 'Buttons'),
            language=self.language_value
        )

        self.gui_widgets['standard_3_button'] = UI_Button(
            parent=self.gui_widgets['outlined_card'],
            position=(16, 100),
            width=100,
            type='standard',
            icon_name='bicycle',
            labels=('Estándar', 'Standard'),
            theme_color=self.theme_color,
            theme_style=self.theme_style,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['accent_3_button'] = UI_Button(
            parent=self.gui_widgets['outlined_card'],
            position=(124, 100),
            width=100,
            type='accent',
            icon_name='bicycle',
            labels=('Acentuado', 'Accent'),
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['outline_3_button'] = UI_Button(
            parent=self.gui_widgets['outlined_card'],
            position=(16, 140),
            width=100,
            type='outlined',
            icon_name='bicycle',
            labels=('Delineado', 'Outlined'),
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['hyperlink_3_button'] = UI_Button(
            parent=self.gui_widgets['outlined_card'],
            position=(124, 140),
            width=100,
            type='hyperlink',
            icon_name='bicycle',
            labels=('Hipervínculo', 'Hyperlink'),
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['standard_4_button'] = UI_Button(
            parent=self.gui_widgets['outlined_card'],
            position=(16, 180),
            type='standard',
            icon_name='bicycle',
            theme_color=self.theme_color,
            theme_style=self.theme_style,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['accent_4_button'] = UI_Button(
            parent=self.gui_widgets['outlined_card'],
            position=(56, 180),
            type='accent',
            icon_name='bicycle',
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['outline_4_button'] = UI_Button(
            parent=self.gui_widgets['outlined_card'],
            position=(96, 180),
            type='outlined',
            icon_name='bicycle',
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['hyperlink_4_button'] = UI_Button(
            parent=self.gui_widgets['outlined_card'],
            position=(136, 180),
            type='hyperlink',
            icon_name='bicycle',
            theme_color=self.theme_color,
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['theme_2_button'] = UI_ThemeButton(
            parent=self.gui_widgets['outlined_card'],
            position=(16, 220),
            state=self.theme_style,
            clicked_signal=parent.theme_button_clicked
        )
        
        self.gui_widgets['toggle_3_button'] = UI_ToggleButton(
            parent=self.gui_widgets['outlined_card'],
            position=(56, 220),
            width=150,
            icon_name='bicycle',
            labels=('Botón Toggle', 'Toggle Button'),
            theme_style=self.theme_style,
            language=self.language_value,
            clicked_signal=parent.toggle_3_button_clicked
        )

        self.gui_widgets['toggle_4_button'] = UI_ToggleButton(
            parent=self.gui_widgets['outlined_card'],
            position=(214, 220),
            icon_name='bicycle',
            theme_style=self.theme_style,
            language=self.language_value,
            clicked_signal=parent.toggle_4_button_clicked
        )

        self.gui_widgets['dropdown_2_button'] = UI_DropDownButton(
            parent=self.gui_widgets['outlined_card'],
            position=(16, 260),
            width=170,
            icon_name='bicycle',
            labels=('Botón Drop Down', 'Drop Down Button'),
            actions_list=[
                ['Bus', parent.action_1, 'bus'],
                ['Car', parent.action_2, 'car'],
                ['Man', parent.action_3, None],
                ['Woman', parent.action_4, None],
                ['School', parent.action_5, None]
            ],
            theme_style=self.theme_style,
            language=self.language_value,
            clicked_signal=parent.dropdown_1_button_clicked
        )

        # -----------
        # Check Boxes
        # -----------
        self.gui_widgets['checkboxes_2_label'] = UI_Label(
            parent=self.gui_widgets['outlined_card'],
            position=(296, 60),
            width=100,
            align='left',
            labels=('Cajas de Selección', 'Check Boxes'),
            language=self.language_value
        )

        self.gui_widgets['option_4_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['outlined_card'],
            state_changed_signal=parent.option_1_changed,
            position=(296,100),
            width=150,
            icon_name='bus',
            labels=('Opción Bus', 'Option Bus'),
            tristate=False,
            state=0,
            theme_style=self.theme_style,
            language=self.language_value
        )

        self.gui_widgets['option_5_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['outlined_card'],
            state_changed_signal=parent.option_2_changed,
            position=(296,140),
            width=150,
            icon_name='car',
            tristate=True,
            state=1,
            theme_style=self.theme_style,
            language=self.language_value
        )

        self.gui_widgets['option_6_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['outlined_card'],
            state_changed_signal=parent.option_3_changed,
            position=(296,180),
            width=150,
            labels=('Opción Camión', 'Option Truck'),
            tristate=True,
            state=2,
            theme_style=self.theme_style,
            language=self.language_value
        )














        # # -----------------
        # # Segmented Buttons
        # # -----------------
        # self.gui_widgets['left_segmented2_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(8, 88),
        #     width=100,
        #     labels=('Izquierda', 'Left'),
        #     check_icon=True,
        #     location='left',
        #     state=False,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_left_segmented2_button_clicked
        # )
        
        # self.gui_widgets['center1_segmented2_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(108, 88),
        #     width=100,
        #     labels=('Centro 1', 'Center 1'),
        #     location='center',
        #     state=False,
        #     icon_name='delete',
        #     check_icon=True,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_center1_segmented2_button_clicked
        # )

        # self.gui_widgets['center2_segmented2_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(208, 88),
        #     width=100,
        #     labels=('Centro 2', 'Center 2'),
        #     icon_name='delete',
        #     check_icon=True,
        #     location='center',
        #     state=True,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_center2_segmented2_button_clicked
        # )

        # self.gui_widgets['right_segmented2_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(308, 88),
        #     width=100,
        #     labels=('Derecha', 'Right'),
        #     check_icon=True,
        #     location='right',
        #     state=True,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_right_segmented2_button_clicked
        # )
        
        # # ------
        # # Switch
        # # ------
        # self.gui_widgets['test2_switch'] = MD3Switch(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(504, 88),
        #     state=False,
        #     theme_color=self.theme_color,
        #     clicked_signal=parent.on_test2_switch_clicked
        # )

        # # -----
        # # Chips
        # # -----
        # self.gui_widgets['chip4_button'] = MD3Chip(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(8, 128),
        #     width=100,
        #     labels=('Borrar', 'Delete'),
        #     icon_name='delete',
        #     state=False,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_chip4_clicked
        # )
        
        # self.gui_widgets['chip5_button'] = MD3Chip(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(116, 128),
        #     width=100,
        #     labels=('Correo', 'Mail'),
        #     icon_name='mail',
        #     state=True,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_chip5_clicked
        # )
        
        # self.gui_widgets['chip6_button'] = MD3Chip(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(224, 128),
        #     width=100,
        #     labels=('Mejorar', 'Improve'),
        #     state=False,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_chip6_clicked
        # )
        
        # # ----
        # # Menu
        # # ----
        # self.gui_widgets['test2_menu'] = MD3Menu(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(332, 128),
        #     width=72,
        #     type='outlined',
        #     options=self.test_options,
        #     set=self.language_value,
        #     language=self.language_value,
        #     index_changed_signal=parent.on_language_changed
        # )

        # # ----------
        # # Text Field
        # # ----------
        # self.gui_widgets['test5_textfield'] = MD3TextField(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(8, 168),
        #     width=120,
        #     type='outlined',
        #     labels=('Cuadro', 'Frame'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )

        # self.gui_widgets['test6_textfield'] = MD3TextField(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(136, 168),
        #     width=120,
        #     length=9,
        #     type='outlined',
        #     labels=('Cuadro', 'Frame'),
        #     input='integer',
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['test7_textfield'] = MD3TextField(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(264, 168),
        #     width=120,
        #     length=9,
        #     type='outlined',
        #     labels=('Cuadro', 'Frame'),
        #     input='double',
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['test8_textfield'] = MD3TextField(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(392, 168),
        #     width=120,
        #     length=9,
        #     type='outlined',
        #     labels=('Cuadro', 'Frame'),
        #     input='text',
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )

        # # -----------
        # # Date Picker
        # # -----------
        # self.gui_widgets['test2_date'] = MD3DatePicker(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(8, 228),
        #     width=120,
        #     type='outlined',
        #     labels=('Fecha', 'Date'),
        #     language=self.language_value
        # )

        # # ------
        # # Labels
        # # ------
        # self.gui_widgets['icon2_label'] = MD3Label(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(136, 228),
        #     type='icon',
        #     icon_name='delete',
        #     theme_color=self.theme_color
        # )

        # self.gui_widgets['subtitle4_label'] = MD3Label(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(176, 228),
        #     width=100,
        #     type='subtitle',
        #     align='left',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['subtitle5_label'] = MD3Label(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(176, 248),
        #     width=100,
        #     type='subtitle',
        #     align='center',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )

        # self.gui_widgets['subtitle6_label'] = MD3Label(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(176, 268),
        #     width=100,
        #     type='subtitle',
        #     align='right',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['color2_label'] = MD3Label(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(284, 228),
        #     type='color',
        #     color='#0000FF',
        #     theme_color=self.theme_color
        # )
        
        # self.gui_widgets['value2_label'] = MD3Label(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(324, 228),
        #     width=100,
        #     type='value',
        #     align='center',
        #     border_color='#0000FF',
        #     theme_color=self.theme_color
        # )

        # # ------
        # # Slider
        # # ------
        # self.gui_widgets['test2_slider'] = MD3Slider(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(432, 228),
        #     length=100,
        #     range=(0, 1, 100),
        #     value=50,
        #     slider_moved_signal=parent.on_test2_slider_sliderMoved,
        #     slider_released_signal=parent.on_test2_slider_sliderReleased
        # )

        # # --------
        # # Dividers
        # # --------
        # self.gui_widgets['horizontal2_divider'] = MD3Divider(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(8, 288),
        #     length=100,
        #     orientation='horizontal'
        # )
        
        # self.gui_widgets['vertical2_divider'] = MD3Divider(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(116, 288),
        #     length=32,
        #     orientation='vertical'
        # )
        
        # # -----------
        # # Image Label
        # # -----------
        # self.gui_widgets['image2_label'] = MD3ImageLabel(
        #     parent=self.gui_widgets['outlined_card'],
        #     position=(124, 288),
        #     size=(300, 32),
        #     scaled_image=True
        # )
        