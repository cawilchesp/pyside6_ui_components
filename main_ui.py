from PySide6.QtWidgets import QWidget

from components.md3_button import MD3Button
from components.md3_card import MD3Card
from components.md3_chip import MD3Chip
from components.md3_datepicker import MD3DatePicker
from components.md3_divider import MD3Divider
from components.md3_imagelabel import MD3ImageLabel
from components.md3_label import MD3Label
from components.md3_menu import MD3Menu
from components.md3_segmentedbutton import MD3SegmentedButton
from components.md3_themebutton import MD3ThemeButton
from components.md3_slider import MD3Slider
from components.md3_switch import MD3Switch
from components.md3_textfield import MD3TextField
from components.md3_window import MD3Window

import yaml


class UI(QWidget):
    def __init__(self, parent):
        super(UI, self).__init__(parent)

        # --------
        # Settings
        # --------
        self.settings_file = 'settings.yaml'
        with open(self.settings_file, 'r') as file:
            self.config = yaml.safe_load(file)

        self.language_value = int(self.config['LANGUAGE'])
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
        (width, height) = (1300, 350)
        self.gui_widgets['main_window'] = MD3Window(
            parent=parent,
            size=(width, height),
            minimum_size=(width,height),
            titles=('Componentes de UI', 'UI Components'),
            language=self.language_value
        )

        # *****************************************************************
        #                           Card Filled
        # *****************************************************************
        self.gui_widgets['filled_card'] = MD3Card(parent, {
            'position': (8, 8), 
            'size': ((width / 2) - 16, height - 16),
            'type': 'filled',
            'titles': ('Tarjeta Llena', 'Filled Card'),
            'language': self.language_value } )

        # ------------
        # Icon Buttons
        # ------------
        self.gui_widgets['icon1_button'] = MD3Button (
            parent=self.gui_widgets['filled_card'],
            position=(8,48),
            type='filled',
            icon_name='delete',
            theme_color=self.theme_color,
            clicked_signal=parent.on_icon1_button_clicked
        )

        self.gui_widgets['icon2_button'] = MD3Button(
            parent=self.gui_widgets['filled_card'],
            position=(48,48),
            type='tonal',
            icon_name='delete',
            theme_color=self.theme_color,
            clicked_signal=parent.on_icon2_button_clicked
        )
        
        self.gui_widgets['icon3_button'] = MD3Button(
            parent=self.gui_widgets['filled_card'],
            position=(88,48),
            type='outlined',
            icon_name='delete',
            theme_color=self.theme_color,
            clicked_signal=parent.on_icon3_button_clicked
        )
        
        self.gui_widgets['icon4_button'] = MD3Button(
            parent=self.gui_widgets['filled_card'],
            position=(128,48),
            type='standard',
            icon_name='delete',
            theme_color=self.theme_color,
            clicked_signal=parent.on_icon4_button_clicked
        )
        
        # -------
        # Buttons
        # -------
        self.gui_widgets['boton1_button'] = MD3Button (
            parent=self.gui_widgets['filled_card'],
            position=(168,48),
            width=100,
            type='filled',
            icon_name='delete',
            labels=('Borrar','Delete'),
            theme_color=self.theme_color,
            language=self.language_value,
            clicked_signal=parent.on_boton1_button_clicked
        )

        self.gui_widgets['boton2_button'] = MD3Button(
            parent=self.gui_widgets['filled_card'],
            position=(276,48),
            width=100,
            type='tonal',
            labels=('Borrar','Delete'),
            theme_color=self.theme_color,
            language=self.language_value,
            clicked_signal=parent.on_boton2_button_clicked
        )
        
        self.gui_widgets['boton3_button'] = MD3Button(
            parent=self.gui_widgets['filled_card'],
            position=(394,48),
            width=100,
            type='outlined',
            icon_name='delete',
            enabled=True,
            labels=('Borrar','Delete'),
            theme_color=self.theme_color,
            language=self.language_value,
            clicked_signal=parent.on_boton3_button_clicked
        )
        
        self.gui_widgets['boton4_button'] = MD3Button(
            parent=self.gui_widgets['filled_card'],
            position=(502,48),
            width=100,
            type='standard',
            labels=('Borrar','Delete'),
            theme_color=self.theme_color,
            language=self.language_value,
            clicked_signal=parent.on_boton4_button_clicked
        )
        
        # -----------------
        # Segmented Buttons
        # -----------------
        self.gui_widgets['left_segmented1_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'position': (8, 88),
            'width': 100,
            'labels': ('Izquierda', 'Left'),
            'check_icon': True,
            'location': 'left',
            'state': False,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_left_segmented1_button_clicked } )
        
        self.gui_widgets['center1_segmented1_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'position': (108, 88),
            'width': 100,
            'labels': ('Centro 1', 'Center 1'),
            'location': 'center',
            'state': False,
            'icon': 'delete',
            'check_icon': True,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_center1_segmented1_button_clicked } ) 

        self.gui_widgets['center2_segmented1_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'position': (208, 88),
            'width': 100,
            'labels': ('Centro 2', 'Center 2'),
            'icon': 'delete',
            'check_icon': True,
            'location': 'center',
            'state': True,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_center2_segmented1_button_clicked } ) 

        self.gui_widgets['right_segmented1_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'position': (308, 88),
            'width': 100,
            'labels': ('Derecha', 'Right'),
            'check_icon': True,
            'location': 'right',
            'state': True,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_right_segmented1_button_clicked } )
        
        # -----------------------
        # Theme Segmented Buttons
        # -----------------------
        self.gui_widgets['theme1_button'] = MD3ThemeButton(self.gui_widgets['filled_card'], {
            'position': (416, 88),
            'type': 'outlined',
            'state': self.theme_style,
            'theme_color': self.theme_color,
            'clicked': parent.on_theme_clicked } )
        
        # ------
        # Switch
        # ------
        self.gui_widgets['test1_switch'] = MD3Switch(self.gui_widgets['filled_card'], {
            'position': (504, 88),
            'state': False,
            'enabled': True,
            'theme_color': self.theme_color,
            'clicked': parent.on_test1_switch_clicked } )

        # -----
        # Chips
        # -----
        self.gui_widgets['chip1_button'] = MD3Chip(self.gui_widgets['filled_card'], {
            'position': (8, 128),
            'width': 100,
            'labels': ('Borrar', 'Delete'),
            'icon': 'delete',
            'state': False,
            'enabled': False,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_chip1_clicked } )
        
        self.gui_widgets['chip2_button'] = MD3Chip(self.gui_widgets['filled_card'], {
            'position': (116, 128),
            'width': 100,
            'labels': ('Correo', 'Mail'),
            'icon': 'mail',
            'state': True,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_chip2_clicked } )
        
        self.gui_widgets['chip3_button'] = MD3Chip(self.gui_widgets['filled_card'], {
            'position': (224, 128),
            'width': 100,
            'labels': ('Mejorar', 'Improve'),
            'state': False,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_chip3_clicked } )
        
        # ----
        # Menu
        # ----
        self.gui_widgets['test1_menu'] = MD3Menu(self.gui_widgets['filled_card'], {
            'position': (332, 128),
            'width': 100,
            'type': 'filled',
            'options': self.test_options,
            'set': self.language_value,
            'language': self.language_value,
            'index_changed': parent.on_language_changed } )

        # ----------
        # Text Field
        # ----------
        self.gui_widgets['test1_textfield'] = MD3TextField(self.gui_widgets['filled_card'], {
            'position': (8, 168),
            'width': 120,
            'type': 'filled',
            'labels': ('Cuadro', 'Frame'),
            'enabled': True,
            'theme_color': self.theme_color,
            'language': self.language_value } )

        self.gui_widgets['test2_textfield'] = MD3TextField(self.gui_widgets['filled_card'], {
            'position': (136, 168),
            'width': 120,
            'length': 9,
            'type': 'filled',
            'labels': ('Cuadro', 'Frame'),
            'input': 'integer',
            'theme_color': self.theme_color,
            'language': self.language_value } )
        
        self.gui_widgets['test3_textfield'] = MD3TextField(self.gui_widgets['filled_card'], {
            'position': (264, 168),
            'width': 120,
            'length': 9,
            'type': 'filled',
            'labels': ('Cuadro', 'Frame'),
            'input': 'password',
            'theme_color': self.theme_color,
            'language': self.language_value } )
        
        self.gui_widgets['test4_textfield'] = MD3TextField(self.gui_widgets['filled_card'], {
            'position': (392, 168),
            'width': 120,
            'length': 9,
            'type': 'filled',
            'labels': ('Cuadro', 'Frame'),
            'input': 'text',
            'theme_color': self.theme_color,
            'language': self.language_value } )

        # -----------
        # Date Picker
        # -----------
        self.gui_widgets['test1_date'] = MD3DatePicker(self.gui_widgets['filled_card'], {
            'position': (8, 228),
            'width': 120,
            'type': 'filled',
            'labels': ('Fecha', 'Date'),
            'enabled': True,
            'language': self.language_value } )

        # ------
        # Labels
        # ------
        self.gui_widgets['icon1_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'position': (136, 228),
            'type': 'icon',
            'icon': 'delete',
            'theme_color': self.theme_color } )

        self.gui_widgets['subtitle1_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'position': (176, 228),
            'width': 100,
            'type': 'subtitle',
            'align': 'left',
            'labels': ('Eliminar', 'Delete'),
            'theme_color': self.theme_color,
            'language': self.language_value } )
        
        self.gui_widgets['subtitle2_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'position': (176, 248),
            'width': 100,
            'type': 'subtitle',
            'align': 'center',
            'labels': ('Eliminar', 'Delete'),
            'theme_color': self.theme_color,
            'language': self.language_value } )

        self.gui_widgets['subtitle3_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'position': (176, 268),
            'width': 100,
            'type': 'subtitle',
            'align': 'right',
            'labels': ('Eliminar', 'Delete'),
            'theme_color': self.theme_color,
            'language': self.language_value } )
        
        self.gui_widgets['color1_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'position': (284, 228),
            'type': 'color',
            'color': '#ff8888',
            'theme_color': self.theme_color } )
        
        self.gui_widgets['value1_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'position': (324, 228),
            'width': 100,
            'type': 'value',
            'align': 'center',
            'border_color': '#ff8888',
            'theme_color': self.theme_color } )

        # ------
        # Slider
        # ------
        self.gui_widgets['test1_slider'] = MD3Slider(self.gui_widgets['filled_card'], {
            'position': (432, 228),
            'width': 100,
            'range': (0, 1, 100),
            'value': 50,
            'enabled': False,
            'slider_moved': parent.on_test1_slider_sliderMoved,
            'slider_released': parent.on_test1_slider_sliderReleased } )

        # --------
        # Dividers
        # --------
        self.gui_widgets['horizontal1_divider'] = MD3Divider(self.gui_widgets['filled_card'], {
            'position': (8, 288),
            'length': 100,
            'shape': 'horizontal' } )
        
        self.gui_widgets['vertical1_divider'] = MD3Divider(self.gui_widgets['filled_card'], {
            'position': (116, 288),
            'length': 32,
            'shape': 'vertical' } )
        
        # -----------
        # Image Label
        # -----------
        self.gui_widgets['image1_label'] = MD3ImageLabel(self.gui_widgets['filled_card'], {
            'position': (124, 288),
            'size': (300, 32),
            'scaled_image': True } )

        # *****************************************************************
        #                           Card Outlined
        # *****************************************************************
        self.gui_widgets['outlined_card'] = MD3Card(parent, {
            'position': ((width / 2) + 8, 8), 
            'size': ((width / 2) - 16, height - 16),
            'type': 'outlined',
            'titles': ('Tarjeta con Borde', 'Outlined Card'),
            'language': self.language_value } )

        # # ------------
        # # Icon Buttons
        # # ------------
        # self.gui_widgets['icon5_button'] = MD3Button(self.gui_widgets['outlined_card'], {
        #     'position': (8,48),
        #     'type': 'filled',
        #     'icon': 'delete',
        #     'theme_color': self.theme_color,
        #     'clicked': parent.on_icon5_button_clicked } )

        # self.gui_widgets['icon6_button'] = MD3Button(self.gui_widgets['outlined_card'], {
        #     'position': (48,48),
        #     'type': 'tonal',
        #     'icon': 'delete',
        #     'enabled': True,
        #     'theme_color': self.theme_color,
        #     'clicked': parent.on_icon6_button_clicked } )
        
        # self.gui_widgets['icon7_button'] = MD3Button(self.gui_widgets['outlined_card'], {
        #     'position': (88,48),
        #     'type': 'outlined',
        #     'icon': 'delete',
        #     'theme_color': self.theme_color,
        #     'clicked': parent.on_icon7_button_clicked } )
        
        # self.gui_widgets['icon8_button'] = MD3Button(self.gui_widgets['outlined_card'], {
        #     'position': (128,48),
        #     'type': 'standard',
        #     'icon': 'delete',
        #     'theme_color': self.theme_color,
        #     'clicked': parent.on_icon8_button_clicked } )
        
        # # -------
        # # Buttons
        # # -------
        # self.gui_widgets['boton5_button'] = MD3Button(self.gui_widgets['outlined_card'], {
        #     'position': (168,48),
        #     'width': 100,
        #     'type': 'filled',
        #     'labels': ('Borrar','Delete'),
        #     'theme_color': self.theme_color,
        #     'language': self.language_value,
        #     'clicked': parent.on_boton5_button_clicked } )

        # self.gui_widgets['boton6_button'] = MD3Button(self.gui_widgets['outlined_card'], {
        #     'position': (276,48),
        #     'width': 100,
        #     'type': 'tonal',
        #     'icon': 'delete',
        #     'labels': ('Borrar','Delete'),
        #     'theme_color': self.theme_color,
        #     'language': self.language_value,
        #     'clicked': parent.on_boton6_button_clicked } )
        
        # self.gui_widgets['boton7_button'] = MD3Button(self.gui_widgets['outlined_card'], {
        #     'position': (394,48),
        #     'width': 100,
        #     'type': 'outlined',
        #     'enabled': True,
        #     'labels': ('Borrar','Delete'),
        #     'theme_color': self.theme_color,
        #     'language': self.language_value,
        #     'clicked': parent.on_boton7_button_clicked } )
        
        # self.gui_widgets['boton8_button'] = MD3Button(self.gui_widgets['outlined_card'], {
        #     'position': (502,48),
        #     'width': 100,
        #     'type': 'standard',
        #     'icon': 'delete',
        #     'labels': ('Borrar','Delete'),
        #     'theme_color': self.theme_color,
        #     'language': self.language_value,
        #     'clicked': parent.on_boton8_button_clicked } )

        # -----------------
        # Segmented Buttons
        # -----------------
        self.gui_widgets['left_segmented2_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'position': (8, 88),
            'width': 100,
            'labels': ('Izquierda', 'Left'),
            'check_icon': True,
            'location': 'left',
            'state': False,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_left_segmented2_button_clicked } )
        
        self.gui_widgets['center1_segmented2_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'position': (108, 88),
            'width': 100,
            'labels': ('Centro 1', 'Center 1'),
            'location': 'center',
            'state': False,
            'icon': 'delete',
            'check_icon': True,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_center1_segmented2_button_clicked } ) 

        self.gui_widgets['center2_segmented2_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'position': (208, 88),
            'width': 100,
            'labels': ('Centro 2', 'Center 2'),
            'icon': 'delete',
            'check_icon': True,
            'location': 'center',
            'state': True,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_center2_segmented2_button_clicked } ) 

        self.gui_widgets['right_segmented2_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'position': (308, 88),
            'width': 100,
            'labels': ('Derecha', 'Right'),
            'check_icon': True,
            'location': 'right',
            'state': True,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_right_segmented2_button_clicked } )
        
        # -----------------------
        # Theme Segmented Buttons
        # -----------------------
        self.gui_widgets['theme2_button'] = MD3ThemeButton(self.gui_widgets['outlined_card'], {
            'position': (416, 88),
            'type': 'outlined',
            'state': self.theme_style,
            'theme_color': self.theme_color,
            'clicked': parent.on_theme_clicked } )
        
        # ------
        # Switch
        # ------
        self.gui_widgets['test2_switch'] = MD3Switch(self.gui_widgets['outlined_card'], {
            'position': (504, 88),
            'state': False,
            'enabled': True,
            'theme_color': self.theme_color,
            'clicked': parent.on_test2_switch_clicked } )

        # -----
        # Chips
        # -----
        self.gui_widgets['chip4_button'] = MD3Chip(self.gui_widgets['outlined_card'], {
            'position': (8, 128),
            'width': 100,
            'labels': ('Borrar', 'Delete'),
            'icon': 'delete',
            'state': False,
            'enabled': False,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_chip4_clicked } )
        
        self.gui_widgets['chip5_button'] = MD3Chip(self.gui_widgets['outlined_card'], {
            'position': (116, 128),
            'width': 100,
            'labels': ('Correo', 'Mail'),
            'icon': 'mail',
            'state': True,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_chip5_clicked } )
        
        self.gui_widgets['chip6_button'] = MD3Chip(self.gui_widgets['outlined_card'], {
            'position': (224, 128),
            'width': 100,
            'labels': ('Mejorar', 'Improve'),
            'state': False,
            'theme_color': self.theme_color,
            'language': self.language_value,
            'clicked': parent.on_chip6_clicked } )
        
        # ----
        # Menu
        # ----
        self.gui_widgets['test2_menu'] = MD3Menu(self.gui_widgets['outlined_card'], {
            'position': (332, 128),
            'width': 72,
            'type': 'outlined',
            'options': self.test_options,
            'set': self.language_value,
            'language': self.language_value,
            'index_changed': parent.on_language_changed } )

        # ----------
        # Text Field
        # ----------
        self.gui_widgets['test5_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'position': (8, 168),
            'width': 120,
            'type': 'outlined',
            'labels': ('Cuadro', 'Frame'),
            'theme_color': self.theme_color,
            'language': self.language_value } )

        self.gui_widgets['test6_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'position': (136, 168),
            'width': 120,
            'length': 9,
            'type': 'outlined',
            'labels': ('Cuadro', 'Frame'),
            'input': 'integer',
            'theme_color': self.theme_color,
            'language': self.language_value } )
        
        self.gui_widgets['test7_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'position': (264, 168),
            'width': 120,
            'length': 9,
            'type': 'outlined',
            'labels': ('Cuadro', 'Frame'),
            'input': 'double',
            'theme_color': self.theme_color,
            'language': self.language_value } )
        
        self.gui_widgets['test8_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'position': (392, 168),
            'width': 120,
            'length': 9,
            'type': 'outlined',
            'labels': ('Cuadro', 'Frame'),
            'input': 'text',
            'theme_color': self.theme_color,
            'language': self.language_value } )

        # -----------
        # Date Picker
        # -----------
        self.gui_widgets['test2_date'] = MD3DatePicker(self.gui_widgets['outlined_card'], {
            'position': (8, 228),
            'width': 120,
            'type': 'outlined',
            'labels': ('Fecha', 'Date'),
            'language': self.language_value } )

        # ------
        # Labels
        # ------
        self.gui_widgets['icon2_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'position': (136, 228),
            'type': 'icon',
            'icon': 'delete',
            'theme_color': self.theme_color } )

        self.gui_widgets['subtitle4_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'position': (176, 228),
            'width': 100,
            'type': 'subtitle',
            'align': 'left',
            'labels': ('Eliminar', 'Delete'),
            'theme_color': self.theme_color,
            'language': self.language_value } )
        
        self.gui_widgets['subtitle5_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'position': (176, 248),
            'width': 100,
            'type': 'subtitle',
            'align': 'center',
            'labels': ('Eliminar', 'Delete'),
            'theme_color': self.theme_color,
            'language': self.language_value } )

        self.gui_widgets['subtitle6_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'position': (176, 268),
            'width': 100,
            'type': 'subtitle',
            'align': 'right',
            'labels': ('Eliminar', 'Delete'),
            'theme_color': self.theme_color,
            'language': self.language_value } )
        
        self.gui_widgets['color2_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'position': (284, 228),
            'type': 'color',
            'color': '#0000FF',
            'theme_color': self.theme_color } )
        
        self.gui_widgets['value2_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'position': (324, 228),
            'width': 100,
            'type': 'value',
            'align': 'center',
            'border_color': '#0000FF',
            'theme_color': self.theme_color } )

        # ------
        # Slider
        # ------
        self.gui_widgets['test2_slider'] = MD3Slider(self.gui_widgets['outlined_card'], {
            'position': (432, 228),
            'width': 100,
            'range': (0, 1, 100),
            'value': 50,
            'slider_moved': parent.on_test2_slider_sliderMoved,
            'slider_released': parent.on_test2_slider_sliderReleased } )

        # --------
        # Dividers
        # --------
        self.gui_widgets['horizontal2_divider'] = MD3Divider(self.gui_widgets['outlined_card'], {
            'position': (8, 288),
            'length': 100,
            'shape': 'horizontal' } )
        
        self.gui_widgets['vertical2_divider'] = MD3Divider(self.gui_widgets['outlined_card'], {
            'position': (116, 288),
            'length': 32,
            'shape': 'vertical' } )
        
        # -----------
        # Image Label
        # -----------
        self.gui_widgets['image2_label'] = MD3ImageLabel(self.gui_widgets['outlined_card'], {
            'position': (124, 288),
            'size': (300, 32),
            'scaled_image': True } )
        