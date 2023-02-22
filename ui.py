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
            'enabled': False,
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
            'enabled': False,
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
            'enabled': False,
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
            'clicked': parent.on_test1_switch_clicked } )
        
        self.gui_widgets['test1_on_switch'] = MD3Switch(self.gui_widgets['filled_card'], {
            'name': 'test1_on_switch',
            'position': (34, 248),
            'side': 'right',
            'state': False,
            'theme': self.theme_value,
            'clicked': parent.on_test1_switch_clicked } )

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
            'width': 120,
            'labels': ('Cuadro', 'Frame'),
            'enabled': False,
            # 'type': 'integers',
            # 'size': '9',
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['test2_textfield'] = MD3TextField(self.gui_widgets['filled_card'], {
            'name': 'test2_textfield',
            'position': (136, 328),
            'width': 120,
            'labels': ('Cuadro', 'Frame'),
            # 'type': 'integers',
            # 'size': 9,
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['test3_textfield'] = MD3TextField(self.gui_widgets['filled_card'], {
            'name': 'test3_textfield',
            'position': (264, 328),
            'width': 120,
            'labels': ('Cuadro', 'Frame'),
            # 'type': 'integers',
            # 'size': 9,
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['test4_textfield'] = MD3TextField(self.gui_widgets['filled_card'], {
            'name': 'test4_textfield',
            'position': (392, 328),
            'width': 120,
            'labels': ('Cuadro', 'Frame'),
            # 'type': 'integers',
            # 'size': 9,
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
            'enabled': False,
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
            'position': (250, 448),
            'size': (300, 200),
            'theme': self.theme_value } )

        # ------
        # Labels
        # ------
        self.gui_widgets['icon1_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'name': 'icon1_label', 
            'position': (8, 508),
            'type': 'icon',
            'icon': 'delete',
            'theme': self.theme_value } )

        self.gui_widgets['subtitle1_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'name': 'subtitle1_label',
            'position': (48, 508),
            'width': 100,
            'type': 'subtitle',
            'align': 'left',
            'labels': ('Eliminar', 'Delete'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['subtitle2_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'name': 'subtitle2_label',
            'position': (48, 528),
            'width': 100,
            'type': 'subtitle',
            'align': 'center',
            'labels': ('Eliminar', 'Delete'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['subtitle3_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'name': 'subtitle3_label',
            'position': (48, 548),
            'width': 100,
            'type': 'subtitle',
            'align': 'right',
            'labels': ('Eliminar', 'Delete'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['color1_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'name': 'color2_label',
            'position': (8, 568),
            'type': 'color',
            'color': '#0000FF',
            'theme': self.theme_value } )
        
        self.gui_widgets['value1_label'] = MD3Label(self.gui_widgets['filled_card'], {
            'name': 'value2_label', 
            'position': (48, 568),
            'width': 100,
            'type': 'value',
            'align': 'center',
            'border_color': '#0000FF',
            'theme': self.theme_value } )

        # ------
        # Slider
        # ------
        self.gui_widgets['test1_slider'] = MD3Slider(self.gui_widgets['filled_card'], {
            'name': 'test1_slider',
            'position': (8, 608),
            'width': 200,
            'range': (0, 1, 100),
            'value': 50,
            'slider_moved': parent.on_test1_slider_sliderMoved,
            'slider_released': parent.on_test1_slider_sliderReleased,
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
            'enabled': False,
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
            'enabled': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_test2_switch_clicked } )
        
        self.gui_widgets['test2_on_switch'] = MD3Switch(self.gui_widgets['outlined_card'], {
            'name': 'test2_on_switch',
            'position': (34, 248),
            'side': 'right',
            'state': True,
            'enabled': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_test2_switch_clicked } )

        # ----
        # Menu
        # ----
        self.gui_widgets['test2_menu'] = MD3Menu(self.gui_widgets['outlined_card'], {
            'name': 'test2_menu',
            'position': (8, 288),
            'width': 72,
            'options': self.test_options,
            'set': self.language_value,
            'enabled': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'index_changed': parent.on_language_changed,
            'text_activated': parent.on_language_changed } )

        # ----------
        # Text Field
        # ----------
        self.gui_widgets['test5_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'name': 'test5_textfield',
            'position': (8, 328),
            'width': 120,
            'labels': ('Cuadro', 'Frame'),
            # 'type': 'integers',
            # 'size': 9,
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['test6_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'name': 'test6_textfield',
            'position': (136, 328),
            'width': 120,
            'labels': ('Cuadro', 'Frame'),
            # 'type': 'integers',
            # 'size': 9,
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['test7_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'name': 'test7_textfield',
            'position': (264, 328),
            'width': 120,
            'labels': ('Cuadro', 'Frame'),
            # 'type': 'integers',
            # 'size': 9,
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['test8_textfield'] = MD3TextField(self.gui_widgets['outlined_card'], {
            'name': 'test8_textfield',
            'position': (392, 328),
            'width': 120,
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
            'length': 44,
            'shape': 'vertical',
            'theme': self.theme_value } )

        # -----------
        # Image Label
        # -----------
        self.gui_widgets['image2_label'] = MD3ImageLabel(self.gui_widgets['outlined_card'], {
            'name': 'image2_label',
            'position': (250, 448),
            'size': (300, 200),
            'theme': self.theme_value } )

        # ------
        # Labels
        # ------
        self.gui_widgets['icon2_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'name': 'icon2_label', 
            'position': (8, 508),
            'type': 'icon',
            'icon': 'delete',
            'theme': self.theme_value } )

        self.gui_widgets['subtitle4_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'name': 'subtitle4_label',
            'position': (48, 508),
            'width': 100,
            'type': 'subtitle',
            'align': 'left',
            'labels': ('Eliminar', 'Delete'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['subtitle5_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'name': 'subtitle5_label',
            'position': (48, 528),
            'width': 100,
            'type': 'subtitle',
            'align': 'center',
            'labels': ('Eliminar', 'Delete'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['subtitle6_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'name': 'subtitle6_label',
            'position': (48, 548),
            'width': 100,
            'type': 'subtitle',
            'align': 'right',
            'labels': ('Eliminar', 'Delete'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['color2_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'name': 'color2_label',
            'position': (8, 568),
            'type': 'color',
            'color': '#FF0000',
            'theme': self.theme_value } )
        
        self.gui_widgets['value2_label'] = MD3Label(self.gui_widgets['outlined_card'], {
            'name': 'value2_label', 
            'position': (48, 568),
            'width': 100,
            'type': 'value',
            'border_color': '#FF0000',
            'theme': self.theme_value } )

        # ------
        # Slider
        # ------
        self.gui_widgets['test2_slider'] = MD3Slider(self.gui_widgets['outlined_card'], {
            'name': 'test2_slider',
            'position': (8, 608),
            'width': 200,
            'range': (0, 1, 100),
            'value': 1,
            'enabled': False,
            'slider_moved': parent.on_test2_slider_sliderMoved,
            'slider_released': parent.on_test2_slider_sliderReleased,
            'theme': self.theme_value } )
                