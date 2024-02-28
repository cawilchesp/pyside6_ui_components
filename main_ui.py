from PySide6.QtWidgets import QWidget, QButtonGroup
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QPoint

from components.ui_window import UI_Window
from components.ui_card import UI_Card
from components.ui_label import UI_Label, UI_IconLabel, UI_ColorLabel, UI_ImageLabel
from components.ui_button import UI_Button, UI_ToggleButton, UI_ThemeButton, UI_DropDownButton
from components.ui_checkbox import UI_CheckBox
from components.ui_combobox import UI_ComboBox
from components.ui_radiobutton import UI_RadioButton
from components.ui_slider import UI_Slider
from components.ui_switch import UI_Switch
from components.ui_text import UI_TextBox, UI_PasswordBox, UI_EmailBox, UI_IpAddressBox
from components.ui_numberbox import UI_NumberBox, UI_FloatBox
from components.ui_datetimepicker import UI_DateEdit, UI_TimeEdit, UI_CalendarView, UI_DatePicker, UI_TimePicker
from components.ui_chart import UI_Chart
from components.ui_divider import UI_Divider

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
            1: ('Opción 2', 'Option 2'),
            2: ('Opción 3', 'Option 3'),
            3: ('Opción 4', 'Option 4'),
            4: ('Opción 5', 'Option 5')
        }

        self.gui_widgets = {}

        # -----------
        # Main Window
        # -----------
        (width, height) = (1300, 700)
        self.gui_widgets['main_window'] = UI_Window(
            parent=parent,
            size=(width, height),
            minimum_size=(width,height),
            titles=('Componentes de UI', 'UI Components'),
            language=self.language_value
        )
        
        # ----
        # Card
        # ----
        self.gui_widgets['card_card'] = UI_Card(
            parent=parent,
            position=(16, 16), 
            size=(width-32, height-32)
        )

        self.gui_widgets['card_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(16, 7),
            width=150,
            align='left',
            font_size=24,
            texts=('Tarjeta', 'Card'),
            language=self.language_value
        )

        # -------
        # Buttons
        # -------
        self.gui_widgets['buttons_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(16, 64),
            width=100,
            align='left',
            font_size=16,
            texts=('Botones', 'Buttons'),
            language=self.language_value
        )

        self.gui_widgets['standard_button'] = UI_Button(
            parent=self.gui_widgets['card_card'],
            position=(12, 104),
            width=120,
            type='standard',
            icon_name='account',
            texts=('Estándar', 'Standard'),
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['standard_2_button'] = UI_Button(
            parent=self.gui_widgets['card_card'],
            position=(132, 104),
            type='standard',
            icon_name='account',
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['accent_button'] = UI_Button(
            parent=self.gui_widgets['card_card'],
            position=(12, 144),
            width=120,
            type='accent',
            texts=('Acentuado', 'Accent'),
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['accent_2_button'] = UI_Button(
            parent=self.gui_widgets['card_card'],
            position=(132, 144),
            type='accent',
            icon_name='account',
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['outline_button'] = UI_Button(
            parent=self.gui_widgets['card_card'],
            position=(12, 184),
            width=120,
            type='outlined',
            icon_name='account',
            texts=('Delineado', 'Outlined'),
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['outline_2_button'] = UI_Button(
            parent=self.gui_widgets['card_card'],
            position=(132, 184),
            type='outlined',
            icon_name='account',
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['hyperlink_button'] = UI_Button(
            parent=self.gui_widgets['card_card'],
            position=(12, 224),
            width=120,
            type='hyperlink',
            icon_name='account',
            texts=('Hipervínculo', 'Hyperlink'),
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['hyperlink_2_button'] = UI_Button(
            parent=self.gui_widgets['card_card'],
            position=(132, 224),
            type='hyperlink',
            icon_name='account',
            clicked_signal=parent.standard_button_clicked
        )

        self.gui_widgets['theme_button'] = UI_ThemeButton(
            parent=self.gui_widgets['card_card'],
            position=(12, 264),
            state=self.theme_style,
            clicked_signal=parent.theme_button_clicked
        )
        
        self.gui_widgets['toggle_1_button'] = UI_ToggleButton(
            parent=self.gui_widgets['card_card'],
            position=(52, 264),
            width=150,
            icon_name='account',
            texts=('Botón Toggle', 'Toggle Button'),
            language=self.language_value,
            clicked_signal=parent.toggle_1_button_clicked
        )

        self.gui_widgets['toggle_2_button'] = UI_ToggleButton(
            parent=self.gui_widgets['card_card'],
            position=(202, 264),
            icon_name='account',
            language=self.language_value,
            clicked_signal=parent.toggle_2_button_clicked
        )

        self.gui_widgets['dropdown_1_button'] = UI_DropDownButton(
            parent=self.gui_widgets['card_card'],
            position=(12, 304),
            width=230,
            icon_name='account',
            texts=('Botón Drop Down', 'Drop Down Button'),
            actions_list=[
                ['Cámara', 'Camera', parent.action_1, 'account'],
                ['Carros', 'Cars', parent.action_2, 'account'],
                ['Hombre', 'Man', parent.action_3, None],
                ['Mujer', 'Woman', parent.action_4, 'account'],
                ['Colegio', 'School', parent.action_5, 'account']
            ],
            language=self.language_value,
            clicked_signal=parent.dropdown_1_button_clicked
        )

        # -----------
        # Check Boxes
        # -----------
        self.gui_widgets['checkboxes_1_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(16, 344),
            width=120,
            align='left',
            font_size=16,
            texts=('Cajas de Selección', 'Check Boxes'),
            language=self.language_value
        )

        self.gui_widgets['option_1_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['card_card'],
            state_changed_signal=parent.option_1_changed,
            position=(12, 384),
            width=150,
            icon_name='account',
            texts=('Opción Bus', 'Option Bus'),
            tristate=False,
            state=0,
            language=self.language_value
        )

        self.gui_widgets['option_2_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['card_card'],
            state_changed_signal=parent.option_2_changed,
            position=(12, 424),
            width=150,
            icon_name='account',
            tristate=True,
            state=1,
            language=self.language_value
        )

        self.gui_widgets['option_3_checkbox'] = UI_CheckBox(
            parent=self.gui_widgets['card_card'],
            state_changed_signal=parent.option_3_changed,
            position=(12, 464),
            width=150,
            texts=('Opción Camión', 'Option Truck'),
            tristate=True,
            state=2,
            language=self.language_value
        )

        # -----------
        # Combo Boxes
        # -----------
        self.gui_widgets['combobox_1_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(12, 504),
            width=140,
            align='left',
            font_size=16,
            texts=('Cajas Combo', 'Combo Boxes'),
            language=self.language_value
        )

        self.gui_widgets['menu_1_combobox'] = UI_ComboBox(
            parent=self.gui_widgets['card_card'],
            position=(16, 544),
            width=150,
            texts=('Seleccione una opción', 'Select an option'),
            options=self.test_options,
            set=4,
            editable=True,
            language=self.language_value,
            index_changed_signal=parent.menu_1_index_changed,
            text_changed_signal=parent.menu_1_text_changed,
            activated_signal=parent.menu_1_activated
        )

        self.gui_widgets['menu_1_combobox'] = UI_ComboBox(
            parent=self.gui_widgets['card_card'],
            position=(16, 584),
            width=150,
            texts=('Seleccione una opción', 'Select an option'),
            options=self.test_options,
            set=4,
            editable=False,
            language=self.language_value,
            index_changed_signal=parent.menu_1_index_changed,
            text_changed_signal=parent.menu_1_text_changed,
            activated_signal=parent.menu_1_activated
        )

        # -------------
        # Radio Buttons
        # -------------
        self.gui_widgets['radiobuttons_1_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(246, 64),
            width=140,
            align='left',
            font_size=16,
            texts=('Botones Radio', 'Radio Buttons'),
            language=self.language_value
        )

        self.gui_widgets['radiobuttons_1_groupbox'] = QButtonGroup()

        self.gui_widgets['option_1_radiobutton'] = UI_RadioButton(
            parent=self.gui_widgets['card_card'],
            state_changed_signal=parent.option_1_changed,
            position=(242, 104),
            width=150,
            icon_name='account',
            texts=('Opción Bus', 'Option Bus'),
            state=0,
            group=self.gui_widgets['radiobuttons_1_groupbox'],
            language=self.language_value
        )

        self.gui_widgets['option_2_radiobutton'] = UI_RadioButton(
            parent=self.gui_widgets['card_card'],
            state_changed_signal=parent.option_2_changed,
            position=(242, 144),
            width=150,
            texts=('Opción Carro', 'Option Car'),
            state=0,
            group=self.gui_widgets['radiobuttons_1_groupbox'],
            language=self.language_value
        )

        self.gui_widgets['option_3_radiobutton'] = UI_RadioButton(
            parent=self.gui_widgets['card_card'],
            state_changed_signal=parent.option_3_changed,
            position=(242, 184),
            width=150,
            icon_name='account',
            texts=('Opción Bicicleta', 'Option Bicycle'),
            state=0,
            language=self.language_value
        )

        # ------
        # Slider
        # ------
        self.gui_widgets['sliders_1_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(246, 224),
            width=100,
            align='left',
            font_size=16,
            texts=('Deslizador', 'Slider'),
            language=self.language_value
        )

        self.gui_widgets['bar_1_slider'] = UI_Slider(
            parent=self.gui_widgets['card_card'],
            position=(242, 264),
            length=200,
            orientation='horizontal',
            range=(0, 1, 100),
            value=50,
            slider_moved_signal=parent.bar_1_slider_sliderMoved,
            slider_released_signal=parent.bar_1_slider_sliderReleased
        )

        self.gui_widgets['bar_2_slider'] = UI_Slider(
            parent=self.gui_widgets['card_card'],
            position=(242, 304),
            length=200,
            orientation='vertical',
            range=(0, 1, 100),
            value=50,
            slider_moved_signal=parent.bar_1_slider_sliderMoved,
            slider_released_signal=parent.bar_1_slider_sliderReleased
        )
        
        # -------------
        # Toggle Switch
        # -------------
        self.gui_widgets['switch_1_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(242, 524),
            width=100,
            align='left',
            font_size=16,
            texts=('Interruptor', 'Switch'),
            language=self.language_value
        )

        self.gui_widgets['test1_switch'] = UI_Switch(
            parent=self.gui_widgets['card_card'],
            position=(242, 564),
            state=False,
            clicked_signal=parent.on_test1_switch_clicked
        )

        # ----------
        # Text Boxes
        # ----------
        self.gui_widgets['textbox_1_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(466, 64),
            width=100,
            align='left',
            font_size=16,
            texts=('Cuadros de Texto', 'Text Boxes'),
            language=self.language_value
        )

        self.gui_widgets['text_1_textbox'] = UI_TextBox(
            parent=self.gui_widgets['card_card'],
            position=(462, 104),
            width=170,
            input='alphanumeric',
            placeholder_texts=('Opción', 'Option'),
            language=self.language_value
        )

        self.gui_widgets['text_2_passwordbox'] = UI_PasswordBox(
            parent=self.gui_widgets['card_card'],
            position=(462, 144),
            width=170,
            language=self.language_value
        )

        self.gui_widgets['text_3_emailbox'] = UI_EmailBox(
            parent=self.gui_widgets['card_card'],
            position=(462, 184),
            width=170,
            language=self.language_value
        )

        self.gui_widgets['text_4_ipaddressbox'] = UI_IpAddressBox(
            parent=self.gui_widgets['card_card'],
            position=(462, 224),
            width=170,
            language=self.language_value
        )

        # ------------
        # Number Boxes
        # ------------
        self.gui_widgets['numberbox_1_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(462, 264),
            width=170,
            align='left',
            font_size=16,
            texts=('Cuadros de Números', 'Number Boxes'),
            language=self.language_value
        )

        self.gui_widgets['integer_1_numberbox'] = UI_NumberBox(
            parent=self.gui_widgets['card_card'],
            position=(462, 304),
            width=170,
            range=(0,1000,100000),
            value=1000
        )

        self.gui_widgets['float_1_numberbox'] = UI_FloatBox(
            parent=self.gui_widgets['card_card'],
            position=(462, 344),
            width=170,
        )

        # -----------------
        # Date Time Pickers
        # -----------------
        self.gui_widgets['datetimepicker_1_label'] = UI_Label(
            parent=self.gui_widgets['card_card'],
            position=(660, 64),
            width=170,
            align='left',
            font_size=16,
            texts=('Selección de Fecha', 'Date Picker'),
            language=self.language_value
        )

        self.gui_widgets['dateedit_1_datepicker'] = UI_DateEdit(
            parent=self.gui_widgets['card_card'],
            position=(656, 104),
            width=150
        )

        self.gui_widgets['timeedit_1_timepicker'] = UI_TimeEdit(
            parent=self.gui_widgets['card_card'],
            position=(656, 144),
            width=150,
            range=((8,0,0),(16,59,59))
        )
        
        self.gui_widgets['datepicker_1_datepicker'] = UI_DatePicker(
            parent=self.gui_widgets['card_card'],
            position=(656, 184),
            language=self.language_value
        )

        self.gui_widgets['timepicker_1_timepicker'] = UI_TimePicker(
            parent=self.gui_widgets['card_card'],
            position=(656, 224),
            language=self.language_value
        )

        self.gui_widgets['calendar_1_calendar'] = UI_CalendarView(
            parent=self.gui_widgets['card_card'],
            position=(656, 272),
            theme_color=self.theme_color,
            theme_style=self.theme_style
        )

        self.gui_widgets['divider_1'] = UI_Divider(
            parent=self.gui_widgets['card_card'],
            position=(980, 64),
            length=50,
            orientation='horizontal'
        )
        
        self.gui_widgets['divider_2'] = UI_Divider(
            parent=self.gui_widgets['card_card'],
            position=(980, 72),
            length=50,
            orientation='vertical'
        )

        self.gui_widgets['line_chart'] = UI_Chart(
            parent=self.gui_widgets['card_card'],
            position=(980, 200),
            size=(250, 250),
            texts=('Gráfica de Línea','Line Chart'),
            language=self.language_value
        )

        data_1 = [(0,1), (1,2), (2,4), (3,5), (4,1), (5,0)]
        line1_series = QLineSeries(self.gui_widgets['line_chart'].chart_plot)
        for point in data_1:
            line1_series.append(QPoint(point[0], point[1]))
        self.gui_widgets['line_chart'].chart_plot.addSeries(line1_series)

        






        # ------
        # Labels
        # ------
        # self.gui_widgets['icon1_label'] = MD3Label(
        #     parent=self.gui_widgets['card_card'],
        #     position=(136, 228),
        #     type='icon',
        #     icon_name='delete',
        #     theme_color=self.theme_color
        # )

        # self.gui_widgets['subtitle1_label'] = MD3Label(
        #     parent=self.gui_widgets['card_card'],
        #     position=(176, 228),
        #     width=100,
        #     type='subtitle',
        #     align='left',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['subtitle2_label'] = MD3Label(
        #     parent=self.gui_widgets['card_card'],
        #     position=(176, 248),
        #     width=100,
        #     type='subtitle',
        #     align='center',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )

        # self.gui_widgets['subtitle3_label'] = MD3Label(
        #     parent=self.gui_widgets['card_card'],
        #     position=(176, 268),
        #     width=100,
        #     type='subtitle',
        #     align='right',
        #     labels=('Eliminar', 'Delete'),
        #     theme_color=self.theme_color,
        #     language=self.language_value
        # )
        
        # self.gui_widgets['color1_label'] = MD3Label(
        #     parent=self.gui_widgets['card_card'],
        #     position=(284, 228),
        #     type='color',
        #     color='#ff8888',
        #     theme_color=self.theme_color
        # )
        
        # self.gui_widgets['value1_label'] = MD3Label(
        #     parent=self.gui_widgets['card_card'],
        #     position=(324, 228),
        #     width=100,
        #     type='value',
        #     align='center',
        #     border_color='#ff8888',
        #     theme_color=self.theme_color
        # )

        # self.gui_widgets['image1_label'] = MD3ImageLabel(
        #     parent=self.gui_widgets['card_card'],
        #     position=(124, 288),
        #     size=(300, 32),
        #     scaled_image=True
        # )



























































































        
        # # -----------------
        # # Segmented Buttons
        # # -----------------
        # self.gui_widgets['left_segmented1_button'] = MD3SegmentedButton(
        #     parent=self.gui_widgets['card_card'],
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
        #     parent=self.gui_widgets['card_card'],
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
        #     parent=self.gui_widgets['card_card'],
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
        #     parent=self.gui_widgets['card_card'],
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

        

        # # -----
        # # Chips
        # # -----
        # self.gui_widgets['chip1_button'] = MD3Chip(
        #     parent=self.gui_widgets['card_card'],
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
        #     parent=self.gui_widgets['card_card'],
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
        #     parent=self.gui_widgets['card_card'],
        #     position=(224, 128),
        #     width=100,
        #     labels=('Mejorar', 'Improve'),
        #     state=False,
        #     theme_color=self.theme_color,
        #     language=self.language_value,
        #     clicked_signal=parent.on_chip3_clicked
        # )
        

        

        

        # # --------
        # # Dividers
        # # --------
        # self.gui_widgets['horizontal1_divider'] = MD3Divider(
        #     parent=self.gui_widgets['card_card'],
        #     position=(8, 288),
        #     length=100,
        #     orientation='horizontal'
        # )
        
        # self.gui_widgets['vertical1_divider'] = MD3Divider(
        #     parent=self.gui_widgets['card_card'],
        #     position=(116, 288),
        #     length=32,
        #     orientation='vertical'
        # )
        