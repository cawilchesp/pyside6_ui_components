from PySide6.QtGui import QPixmap, QPainter, QIcon, QColor

dark_colors = {
    'blue': [229/360, 0.53, 0.53],
    'yellow': [48/360, 1.0, 0.67]
}
light_colors = {
    'blue': [229/360, 0.53, 0.86],
    'yellow': [48/360, 1.0, 0.86]
}


def icon_color(color: QColor, icon_name: str) -> QIcon:
    icon_pixmap = QPixmap(f"icons/{icon_name}.png")
    painter = QPainter(icon_pixmap)
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(icon_pixmap.rect(), color)
    painter.end()

    return QIcon(icon_pixmap)