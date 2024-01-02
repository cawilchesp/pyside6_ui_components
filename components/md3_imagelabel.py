from PySide6.QtWidgets import QLabel, QFrame, QWidget


class MD3ImageLabel(QLabel):
    """
    PySide6 Image Label component
    """
    def __init__(
        self,
        parent: QWidget,
        position: tuple[int, int] = (8,8),
        size: tuple[int, int] = (96,96),
        scaled_image: bool = True,
    ):
        """
        Parameters
        ----------
            position (tuple[int, int]): Image label top left corner position (x, y)
            size (tuple[int, int]): Image label size (width, height)
            scaled_image (bool): Fit image to label
                Options: True: Fit, False: Unfit
        """
        super().__init__(parent)

        self.parent = parent
        self.move(position[0], position[1])
        self.resize(size[0], size[1])

        self.setScaledContents(scaled_image)
        self.setFrameStyle(QFrame.Shape.Box)