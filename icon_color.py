from PySide6.QtGui import QPixmap, QPainter, QIcon, QColor

colors = {
    'blue': [200/360, 1.0, 0.50],
    'yellow': [48/360, 1.0, 0.67],
    'black': [0.0, 0.0, 0.13],
    'white': [0.0, 0.0, 0.98]
}


def icon_color(theme_color: str, icon_name: str) -> QIcon:
    h, s, l = colors[theme_color]
    icon_color = QColor.fromHslF(h, s, l)

    icon_pixmap = QPixmap(f"icons/{icon_name}.png")
    painter = QPainter(icon_pixmap)
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(icon_pixmap.rect(), icon_color)
    painter.end()

    return QIcon(icon_pixmap)