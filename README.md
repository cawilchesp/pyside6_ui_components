# UI Components

This repository contains a collection of UI components developed using PySide 6 library. PySide 6 is a set of Python bindings for the Qt toolkit, which allows Python developers to create graphical applications with a native look and feel on a variety of platforms.

The UI components in this repository are designed to be used in desktop applications, and include components such as buttons, text fields, sliders, and more. These components are customizable and can be used to create modern and intuitive user interfaces.

## Credits

PySide 6 is the official Python module from the Qt for Python project, which provides access to the complete Qt 6.0+ framework and is available under LGPLv3/GPLv2 and commercial licenses. To learn more about Qt for Python project, visit the official website at [Qt for Python project](https://wiki.qt.io/Qt_for_Python).

## Installation

To use the components in this repository, you must have PySide 6 installed. You can install PySide 6 using pip:

```
pip install pyside6
```

## Usage

This repository has 3 components:

- `main.py`: Contains the UI implementation and components functions.
- `main_ui.py`: Contains the creation of components.
- `icon_color.py`: Contains a function to adapt icons color to the selected theme.
- `settings.yaml`: Contains language and themes app settings.
- `components` folder: Contains the components.
- `dialogs` folder: Contains dialog window class.
- `icons` folder: Contains some icons obtained from [Pictogrammers.com](https://pictogrammers.com/library/mdi/)
- `themes` folder: Contains the theme colors in `qss` format.

To use the components in your PySide 6 application, simply import the component class as presented in `main_ui.py` and use it in your code. For example, to use a button, you would import the `UI_Button` class from the `ui_button` module:

```python
from components.md3_button import MD3Button

button1 = MD3Button (
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
```

The implementation in this library was developed so the theme can be changed easily and the functions are separated from the UI component creation.

## Contributing

Contributions to this repository are welcome! If you would like to contribute a new component, or improve an existing one, please create a pull request with your changes.

## License

The components in this repository are released under the GNU General Public License v3.0. See the LICENSE file for more information.