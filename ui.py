from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import QSettings, Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

from components.md3_button import MD3Button
from components.md3_card import MD3Card
from components.md3_chip import MD3Chip
from components.md3_datepicker import MD3DatePicker
from components.md3_divider import MD3Divider
from components.md3_iconbutton import MD3IconButton
from components.md3_imagelabel import MD3ImageLabel
from components.md3_label import MD3Label
from components.md3_menu import MD3Menu
from components.md3_segmentedbutton import MD3SegmentedButton
from components.md3_slider import MD3Slider
from components.md3_switch import MD3Switch
from components.md3_textfield import MD3TextField
from components.md3_window import MD3Window

import sys


class UI(QWidget):
    def __init__(self, parent):
        super(UI, self).__init__(parent)

        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.test_options = {
            0: ('Opción 1', 'Option 1'),
            1: ('Opción 2', 'Option 2')
        }

        self.gui_widgets = {}

        # -----------
        # Main Window
        # -----------
        (width, height) = (1300, 700)
        self.gui_widgets['main_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'labels': ('Componentes de Material 3 UI', 'Material 3 UI Components'),
            'theme': self.theme_value, 
            'language': self.language_value } )

        # -----------
        # Card Filled
        # -----------
        self.gui_widgets['filled_card'] = MD3Card(parent, { 
            'name': 'filled_card',
            'position': (8, 8), 
            'size': ((width / 2) - 16, height - 16),
            'type': 'filled',
            'theme': self.theme_value, 
            'labels': ('Tarjeta Llena', 'Filled Card'), 
            'language': self.language_value } )

        # ------------
        # Icon Buttons
        # ------------
        self.gui_widgets['icon1_button'] = MD3IconButton(self.gui_widgets['filled_card'], {
            'name': 'icon1_button',
            'position': (8,48),
            'type': 'filled',
            'icon': 'delete', 
            'theme': self.theme_value,
            'clicked': parent.on_icon1_button_clicked } )

        self.gui_widgets['icon2_button'] = MD3IconButton(self.gui_widgets['filled_card'], {
            'name': 'icon2_button',
            'position': (48,48),
            'type': 'tonal',
            'icon': 'delete', 
            'theme': self.theme_value,
            'clicked': parent.on_icon2_button_clicked } )
        
        self.gui_widgets['icon3_button'] = MD3IconButton(self.gui_widgets['filled_card'], {
            'name': 'icon3_button',
            'position': (88,48),
            'type': 'outlined',
            'icon': 'delete', 
            'theme': self.theme_value,
            'clicked': parent.on_icon3_button_clicked } )
        
        self.gui_widgets['icon4_button'] = MD3IconButton(self.gui_widgets['filled_card'], {
            'name': 'icon4_button',
            'position': (128,48),
            'type': 'standard',
            'icon': 'delete', 
            'theme': self.theme_value,
            'clicked': parent.on_icon4_button_clicked } )
        
        # -------
        # Buttons
        # -------
        self.gui_widgets['boton1_button'] = MD3Button(self.gui_widgets['filled_card'], {
            'name': 'boton1_button',
            'position': (8,88),
            'width': 100,
            'type': 'filled',
            'icon': 'delete',
            'labels': ('Borrar','Delete'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_boton1_button_clicked } )

        self.gui_widgets['boton2_button'] = MD3Button(self.gui_widgets['filled_card'], {
            'name': 'boton2_button',
            'position': (116,88),
            'width': 100,
            'type': 'tonal',
            'icon': 'delete',
            'labels': ('Borrar','Delete'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_boton2_button_clicked } )
        
        self.gui_widgets['boton3_button'] = MD3Button(self.gui_widgets['filled_card'], {
            'name': 'boton3_button',
            'position': (224,88),
            'width': 100,
            'type': 'outlined',
            'icon': 'delete',
            'labels': ('Borrar','Delete'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_boton3_button_clicked } )
        
        self.gui_widgets['boton4_button'] = MD3Button(self.gui_widgets['filled_card'], {
            'name': 'boton4_button',
            'position': (332,88),
            'width': 100,
            'type': 'text',
            'icon': 'delete',
            'labels': ('Borrar','Delete'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_boton4_button_clicked } )

        # -----------------
        # Segmented Buttons
        # -----------------
        self.gui_widgets['left_segmented1_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'name': 'left_segmented1_button',
            'position': (8, 128),
            'width': 100,
            'labels': ('Izquierda', 'Left'),
            'check_icon': True,
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_left_segmented1_button_clicked } )
        
        self.gui_widgets['center1_segmented1_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'name': 'center1_segmented1_button',
            'position': (108, 128),
            'width': 100,
            'labels': ('Centro 1', 'Center 1'),
            'location': 'center',
            'state': False,
            'icon': 'delete',
            'check_icon': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_center1_segmented1_button_clicked } ) 

        self.gui_widgets['center2_segmented1_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'name': 'center2_segmented1_button',
            'position': (208, 128),
            'width': 100,
            'labels': ('Centro 2', 'Center 2'),
            'icon': 'delete',
            'check_icon': True,
            'location': 'center',
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_center2_segmented1_button_clicked } ) 

        self.gui_widgets['right_segmented1_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'name': 'right_segmented1_button',
            'position': (308, 128),
            'width': 100,
            'labels': ('Derecha', 'Right'),
            'check_icon': True,
            'location': 'right',
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_right_segmented1_button_clicked } )
        
        # -----------------------
        # Theme Segmented Buttons
        # -----------------------
        self.gui_widgets['light_theme_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'name': 'light_theme_button',
            'position': (8, 168),
            'width': 40,
            'icon': 'light_mode',
            'check_icon': False,
            'location': 'left',
            'state': self.theme_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_light_theme_clicked } )

        self.gui_widgets['dark_theme_button'] = MD3SegmentedButton(self.gui_widgets['filled_card'], {
            'name': 'dark_theme_button',
            'position': (48, 168),
            'width': 40,
            'icon': 'dark_mode',
            'check_icon': False,
            'location': 'right',
            'state': not self.theme_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_dark_theme_clicked } )

        # -----
        # Chips
        # -----
        self.gui_widgets['chip1_button'] = MD3Chip(self.gui_widgets['filled_card'], {
            'name': 'chip1_button',
            'position': (8, 208),
            'width': 100,
            'labels': ('Borrar', 'Delete'),
            'icon': 'delete',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_chip1_clicked } )
        
        
        self.gui_widgets['chip2_button'] = MD3Chip(self.gui_widgets['filled_card'], {
            'name': 'chip2_button',
            'position': (116, 208),
            'width': 100,
            'labels': ('Correo', 'Mail'),
            'icon': 'mail',
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_chip2_clicked } )
        
        self.gui_widgets['chip3_button'] = MD3Chip(self.gui_widgets['filled_card'], {
            'name': 'chip3_button',
            'position': (224, 208),
            'width': 100,
            'labels': ('Mejorar', 'Improve'),
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_chip3_clicked } )
        
        # ------
        # Switch
        # ------
        self.gui_widgets['test1_off_switch'] = MD3Switch(self.gui_widgets['filled_card'], {
            'name': 'test1_off_switch',
            'position': (8, 248),
            'side': 'left',
            'state': False,
            'theme': self.theme_value,
            'clicked': parent.on_test1_off_clicked } )
        
        self.gui_widgets['test1_on_switch'] = MD3Switch(self.gui_widgets['filled_card'], {
            'name': 'test1_on_switch',
            'position': (34, 248),
            'side': 'right',
            'state': False,
            'theme': self.theme_value,
            'clicked': parent.on_test1_on_clicked } )

        # ----
        # Menu
        # ----
        self.gui_widgets['test1_menu'] = MD3Menu(self.gui_widgets['filled_card'], {
            'name': 'test1_menu',
            'position': (8, 288),
            'width': 72,
            'options': self.test_options,
            'set': self.language_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'index_changed': parent.on_language_changed } )

        # ----------
        # Text Field
        # ----------
        self.gui_widgets['test1_textfield'] = MD3TextField(self.gui_widgets['filled_card'], {
            'name': 'test1_textfield',
            'position': (8, 328),
            'width': 200,
            'labels': ('Cuadro', 'Frame'),
            # 'type': 'integers',
            # 'size': '9',
            'theme': self.theme_value,
            'language': self.language_value } )

        # -----------
        # Date Picker
        # -----------
        self.gui_widgets['test1_date'] = MD3DatePicker(self.gui_widgets['filled_card'], {
            'name': 'test1_date',
            'position': (8, 388),
            'width': 200,
            'labels': ('Fecha', 'Date'),
            'theme': self.theme_value,
            'language': self.language_value } )

        # --------
        # Dividers
        # --------
        self.gui_widgets['horizontal1_divider'] = MD3Divider(self.gui_widgets['filled_card'], {
            'name': 'horizontal1_divider',
            'position': (8, 448),
            'length': 200,
            'shape': 'horizontal',
            'theme': self.theme_value } )
        
        self.gui_widgets['vertical1_divider'] = MD3Divider(self.gui_widgets['filled_card'], {
            'name': 'vertical1_divider',
            'position': (104, 456),
            'length': 52,
            'shape': 'vertical',
            'theme': self.theme_value } )
        
        # -----------
        # Image Label
        # -----------
        self.gui_widgets['image1_label'] = MD3ImageLabel(self.gui_widgets['filled_card'], {
            'name': 'image1_label',
            'position': (250, 248),
            'size': (300, 200),
            'theme': self.theme_value } )
































        # -------------
        # Card Outlined
        # -------------
        self.gui_widgets['outlined_card'] = MD3Card(parent, { 
            'name': 'outlined_card',
            'position': ((width / 2) + 8, 8), 
            'size': ((width / 2) - 16, height - 16),
            'type': 'outlined',
            'theme': self.theme_value, 
            'labels': ('Tarjeta con Borde', 'Outlined Card'), 
            'language': self.language_value } )

        # ------------
        # Icon Buttons
        # ------------
        self.gui_widgets['icon5_button'] = MD3IconButton(self.gui_widgets['outlined_card'], {
            'name': 'icon5_button',
            'position': (8,48),
            'type': 'filled',
            'icon': 'delete', 
            'theme': self.theme_value,
            'clicked': parent.on_icon5_button_clicked } )

        self.gui_widgets['icon6_button'] = MD3IconButton(self.gui_widgets['outlined_card'], {
            'name': 'icon6_button',
            'position': (48,48),
            'type': 'tonal',
            'icon': 'delete', 
            'theme': self.theme_value,
            'clicked': parent.on_icon6_button_clicked } )
        
        self.gui_widgets['icon7_button'] = MD3IconButton(self.gui_widgets['outlined_card'], {
            'name': 'icon7_button',
            'position': (88,48),
            'type': 'outlined',
            'icon': 'delete', 
            'theme': self.theme_value,
            'clicked': parent.on_icon7_button_clicked } )
        
        self.gui_widgets['icon8_button'] = MD3IconButton(self.gui_widgets['outlined_card'], {
            'name': 'icon8_button',
            'position': (128,48),
            'type': 'standard',
            'icon': 'delete', 
            'theme': self.theme_value,
            'clicked': parent.on_icon8_button_clicked } )
        
        # -------
        # Buttons
        # -------
        self.gui_widgets['boton5_button'] = MD3Button(self.gui_widgets['outlined_card'], {
            'name': 'boton5_button',
            'position': (8,88),
            'width': 100,
            'type': 'filled',
            'icon': 'delete',
            'labels': ('Borrar','Delete'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_boton5_button_clicked } )

        self.gui_widgets['boton6_button'] = MD3Button(self.gui_widgets['outlined_card'], {
            'name': 'boton6_button',
            'position': (116,88),
            'width': 100,
            'type': 'tonal',
            'icon': 'delete',
            'labels': ('Borrar','Delete'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_boton6_button_clicked } )
        
        self.gui_widgets['boton7_button'] = MD3Button(self.gui_widgets['outlined_card'], {
            'name': 'boton7_button',
            'position': (224,88),
            'width': 100,
            'type': 'outlined',
            'icon': 'delete',
            'labels': ('Borrar','Delete'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_boton7_button_clicked } )
        
        self.gui_widgets['boton8_button'] = MD3Button(self.gui_widgets['outlined_card'], {
            'name': 'boton8_button',
            'position': (332,88),
            'width': 100,
            'type': 'text',
            'icon': 'delete',
            'labels': ('Borrar','Delete'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_boton8_button_clicked } )

        # -----------------
        # Segmented Buttons
        # -----------------
        self.gui_widgets['left_segmented2_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'name': 'left_segmented2_button',
            'position': (8, 128),
            'width': 100,
            'labels': ('Izquierda', 'Left'),
            'check_icon': True,
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_left_segmented2_button_clicked } )
        
        self.gui_widgets['center1_segmented2_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'name': 'center1_segmented2_button',
            'position': (108, 128),
            'width': 100,
            'labels': ('Centro 1', 'Center 1'),
            'location': 'center',
            'state': False,
            'icon': 'delete',
            'check_icon': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_center1_segmented2_button_clicked } ) 

        self.gui_widgets['center2_segmented2_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'name': 'center2_segmented2_button',
            'position': (208, 128),
            'width': 100,
            'labels': ('Centro 2', 'Center 2'),
            'icon': 'delete',
            'check_icon': True,
            'location': 'center',
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_center2_segmented2_button_clicked } ) 

        self.gui_widgets['right_segmented2_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'name': 'right_segmented2_button',
            'position': (308, 128),
            'width': 100,
            'labels': ('Derecha', 'Right'),
            'check_icon': True,
            'location': 'right',
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_right_segmented2_button_clicked } )

        # -----------------------
        # Theme Segmented Buttons
        # -----------------------
        self.gui_widgets['light2_theme_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'name': 'light2_theme_button',
            'position': (8, 168),
            'width': 40,
            'icon': 'light_mode',
            'check_icon': False,
            'location': 'left',
            'state': self.theme_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_light_theme_clicked } )

        self.gui_widgets['dark2_theme_button'] = MD3SegmentedButton(self.gui_widgets['outlined_card'], {
            'name': 'dark2_theme_button',
            'position': (48, 168),
            'width': 40,
            'icon': 'dark_mode',
            'check_icon': False,
            'location': 'right',
            'state': not self.theme_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_dark_theme_clicked } )

        # -----
        # Chips
        # -----
        self.gui_widgets['chip4_button'] = MD3Chip(self.gui_widgets['outlined_card'], {
            'name': 'chip4_button',
            'position': (8, 208),
            'width': 100,
            'labels': ('Borrar', 'Delete'),
            'icon': 'delete',
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_chip4_clicked } )
        
        self.gui_widgets['chip5_button'] = MD3Chip(self.gui_widgets['outlined_card'], {
            'name': 'chip5_button',
            'position': (116, 208),
            'width': 100,
            'labels': ('Correo', 'Mail'),
            'icon': 'mail',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_chip5_clicked } )

        self.gui_widgets['chip6_button'] = MD3Chip(self.gui_widgets['outlined_card'], {
            'name': 'chip6_button',
            'position': (224, 208),
            'width': 100,
            'labels': ('Mejorar', 'Improve'),
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_chip6_clicked } )

        # ------
        # Switch
        # ------
        self.gui_widgets['test2_off_switch'] = MD3Switch(self.gui_widgets['outlined_card'], {
            'name': 'test2_off_switch',
            'position': (8, 248),
            'side': 'left',
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_test2_off_clicked } )
        
        self.gui_widgets['test2_on_switch'] = MD3Switch(self.gui_widgets['outlined_card'], {
            'name': 'test2_on_switch',
            'position': (34, 248),
            'side': 'right',
            'state': True,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_test2_on_clicked } )

        # ----
        # Menu
        # ----
        self.gui_widgets['test2_menu'] = MD3Menu(self.gui_widgets['outlined_card'], {
            'name': 'test2_menu',
            'position': (8, 288),
            'width': 72,
            'options': self.test_options,
            'set': self.language_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'index_changed': parent.on_language_changed } )

        # ----------
        # Text Field
        # ----------
        self.gui_widgets['test2_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'name': 'test2_textfield',
            'position': (8, 328),
            'width': 200,
            'labels': ('Cuadro', 'Frame'),
            # 'type': 'integers',
            # 'size': 9,
            'theme': self.theme_value,
            'language': self.language_value } )

        # -----------
        # Date Picker
        # -----------
        self.gui_widgets['test2_date'] = MD3DatePicker(self.gui_widgets['outlined_card'], {
            'name': 'test2_date',
            'position': (8, 388),
            'width': 200,
            'labels': ('Fecha', 'Date'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        # --------
        # Dividers
        # --------
        self.gui_widgets['horizontal2_divider'] = MD3Divider(self.gui_widgets['outlined_card'], {
            'name': 'horizontal2_divider',
            'position': (8, 448),
            'length': 200,
            'shape': 'horizontal',
            'theme': self.theme_value } )
        
        self.gui_widgets['vertical2_divider'] = MD3Divider(self.gui_widgets['outlined_card'], {
            'name': 'vertical2_divider',
            'position': (104, 456),
            'length': 52,
            'shape': 'vertical',
            'theme': self.theme_value } )

        # -----------
        # Image Label
        # -----------
        self.gui_widgets['image2_label'] = MD3ImageLabel(self.gui_widgets['outlined_card'], {
            'name': 'image2_label',
            'position': (250, 248),
            'size': (300, 200),
            'theme': self.theme_value } )



















        # self.gui_widgets['source_icon'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'id_icon', 
        #     'position': (8, 48),
        #     'type': 'icon',
        #     'icon': 'cam',
        #     'theme': self.theme_value } )

        # self.gui_widgets['source_value'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'source_value',
        #     'position': (48, 56),
        #     'width': 124,
        #     'type': 'subtitle',
        #     'labels': ('Origen', 'Source'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        
        # self.gui_widgets['filename_value'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'filename_value', 
        #     'position': (48, 88), 
        #     'width': 124,
        #     'type': 'subtitle',
        #     'labels': ('Nombre del archivo', 'File Name'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )

        # self.gui_widgets['width_icon'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'width_icon', 
        #     'position': (8, 112),
        #     'type': 'icon',
        #     'icon': 'width',
        #     'theme': self.theme_value } )

        # self.gui_widgets['width_value'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'width_value',
        #     'position': (48, 120),
        #     'width': 124,
        #     'type': 'subtitle',
        #     'labels': ('Ancho', 'Width'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        
        # self.gui_widgets['height_icon'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'height_icon',
        #     'position': (8, 144),
        #     'type': 'icon',
        #     'icon': 'height',
        #     'theme': self.theme_value } )

        # self.gui_widgets['height_value'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'height_value', 
        #     'position': (48, 152), 
        #     'width': 124,
        #     'type': 'subtitle',
        #     'labels': ('Alto', 'Height'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )

        # self.gui_widgets['count_icon'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'count_icon',
        #     'position': (8, 176),
        #     'type': 'icon',
        #     'icon': 'number',
        #     'theme': self.theme_value } )

        # self.gui_widgets['count_value'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'count_value', 
        #     'position': (48, 184),
        #     'width': 124,
        #     'type': 'subtitle',
        #     'labels': ('Número de Cuadros', 'Frame Count'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )

        # self.gui_widgets['fps_icon'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'fps_icon', 
        #     'position': (8, 208),
        #     'type': 'icon',
        #     'icon': 'fps',
        #     'theme': self.theme_value } )

        # self.gui_widgets['fps_value'] = MD3Label(self.gui_widgets['info_card'], {
        #     'name': 'fps_value', 
        #     'position': (48, 216), 
        #     'width': 124,
        #     'type': 'subtitle',
        #     'labels': ('CPS', 'FPS'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )



        # self.gui_widgets['classes_menu'] = MD3Menu(self.gui_widgets['classes_card'], {
        #     'name': 'classes_menu',
        #     'position': (8, 48),
        #     'size': (164, 32),
        #     'language': self.language_value,
        #     'theme': self.theme_value } )
        # # self.gui_widgets['classes_menu'].textActivated.connect(parent.on_classes_menu_textActivated)


        # self.gui_widgets['video_slider'] = MD3Slider(self.gui_widgets['video_toolbar_card'], {
        #     'name': 'video_slider',
        #     'position': (288, 20),
        #     'theme': self.theme_value } )
        # # self.gui_widgets['video_slider'].setEnabled(False)
        # self.gui_widgets['video_slider'].setValue(1)
        # # self.gui_widgets['video_slider'].sliderMoved.connect(parent.on_video_slider_sliderMoved)
        # # self.gui_widgets['video_slider'].sliderReleased.connect(parent.on_video_slider_sliderReleased)

        
        
        # self.gui_widgets['video_label'] = MD3ImageLabel(self.gui_widgets['video_output_card'], {
        #     'name': 'video_label',
        #     'theme': self.theme_value } )
        

    
        # self.gui_widgets['model_configuration_label'] = MD3Label(self.gui_widgets['yolor_deepsort_card'], {
        #     'name': 'model_configuration_label', 
        #     'position': (8, 48), 
        #     'width': self.gui_widgets['yolor_deepsort_card'].width() - 16,
        #     'type': 'subtitle',
        #     'labels': ('Configuración del Modelo', 'Model Configuration'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
       

        # self.gui_widgets['model_weights_label'] = MD3Label(self.gui_widgets['yolor_deepsort_card'], {
        #     'name': 'model_weights_label', 
        #     'position': (8, 108), 
        #     'width': self.gui_widgets['yolor_deepsort_card'].width() - 16,
        #     'type': 'subtitle',
        #     'labels': ('Pesos del Modelo', 'Model Weights'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
       

        # self.gui_widgets['size_label'] = MD3Label(self.gui_widgets['yolor_deepsort_card'], {
        #     'name': 'size_label', 
        #     'position': (8, 168), 
        #     'width': self.gui_widgets['yolor_deepsort_card'].width() - 16,
        #     'type': 'subtitle',
        #     'labels': ('Tamaño de Inferencia', 'Inference Size'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )

        # self.gui_widgets['gpu_label'] = MD3Label(self.gui_widgets['yolor_deepsort_card'], {
        #     'name': 'gpu_label', 
        #     'position': (8, 228), 
        #     'width': self.gui_widgets['yolor_deepsort_card'].width() - 16,
        #     'type': 'subtitle',
        #     'labels': ('Uso de GPU', 'GPU Usage'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )


        # self.gui_widgets['names_label'] = MD3Label(self.gui_widgets['yolor_deepsort_card'], {
        #     'name': 'names_label', 
        #     'position': (8, 288), 
        #     'width': self.gui_widgets['yolor_deepsort_card'].width() - 16,
        #     'type': 'subtitle',
        #     'labels': ('Archivo .names', 'File .names'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )


        # self.gui_widgets['save_image_label'] = MD3Label(self.gui_widgets['yolor_deepsort_card'], {
        #     'name': 'save_image_label', 
        #     'position': (8, 348),
        #     'width': self.gui_widgets['yolor_deepsort_card'].width() - 16,
        #     'type': 'subtitle',
        #     'labels': ('Guardar Imagen', 'Save Image'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )

        