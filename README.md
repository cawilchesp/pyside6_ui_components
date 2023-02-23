# MD3 Components

This repository contains a collection of Material Design 3 components built using PyQt6 library. PyQt6 is a set of Python bindings for the Qt toolkit, which allows Python programmers to create graphical applications with a native look and feel on a variety of platforms.

The Material Design 3 components in this repository are designed to be used in desktop applications, and include widgets such as buttons, text fields, sliders, and more. These components are customizable and can be used to create modern and intuitive user interfaces.

## Credits

The Material Design 3 system was developed by Google and is licensed under the Apache License 2.0. To learn more about Material Design 3, visit the official website at [material.io](https://material.io).

PyQt6 is developed by Riverbank Computing Limited and is licensed under the GPL and commercial licenses. To learn more about PyQt6, visit the official website at [riverbankcomputing.com](https://www.riverbankcomputing.com/software/pyqt/).

## Installation

To use the components in this repository, you must have PyQt6 installed. You can install PyQt6 using pip:

```
pip install pyqt6
```

## Usage

This repository has 3 components:

- `main.py`: Contains the UI implementation and components functions.
- `ui.py`: Contains the creation of components.
- `components` folder: Contains the components and the theme colors in `style_color.py`

To use the components in your PyQt6 application, simply import the component class as presented in `ui.py` and use it in your code. For example, to use a material design button, you would import the `MD3Button` class from the `md3_button` module:

```python
from components.md3_button import MD3Button

button1 = MD3Button(parent, {
        'name': 'button1',
        'position': (8,88),
        'width': 100,
        'type': 'filled',
        'icon': 'delete',
        'labels': ('Borrar','Delete'),
        'theme': theme_value,
        'language': language_value,
        'clicked': parent.on_boton1_button_clicked } )
```

The implementation in this library was developed so the theme can be changed easily and the functions are separated from the UI component creation.

## Contributing

Contributions to this repository are welcome! If you would like to contribute a new component, or improve an existing one, please create a pull request with your changes.

## License

The components in this repository are released under the GNU General Public License v3.0. See the LICENSE file for more information.