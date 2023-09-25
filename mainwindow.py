# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


def scale(image, target_width):
    aspect_ratio = image.width() / image.height()
    target_height = int(target_width / aspect_ratio)
    pixmap = image.scaled(
        target_width, target_height,
        aspectMode=QtCore.Qt.KeepAspectRatio,
        mode=QtCore.Qt.SmoothTransformation
    )
    return pixmap


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pic = QPixmap('C:/Users/Jonas/Desktop/Beispielbilder/JPG/DSC02807.JPG')
        logo = QPixmap('C:/Users/Jonas/Pictures/Rheinmetall_Logo')

        self.ui.label_left_image.setPixmap(scale(pic, 640))
        self.ui.label_right_image.setPixmap(scale(pic, 640))
        self.ui.label_logo.setPixmap(scale(logo, 145))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
