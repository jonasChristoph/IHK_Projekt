import model
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
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

class MyController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.database = model.Database(model.ConnectionPool(max_connections=10, database='C:/Users/Jonas/Downloads/SQLiteSpy_v1.9.17/win64/Image_database.db3'))
        # Load the UI from the .ui file and set it up
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pic = QPixmap('C:/Users/Jonas/Desktop/Beispielbilder/JPG/DSC02807.JPG')
        self.logo = QPixmap('C:/Users/Jonas/Pictures/Rheinmetall_Logo')

        self.ui.label_left_image.setPixmap(scale(self.pic, 640))
        self.ui.label_right_image.setPixmap(scale(self.pic, 640))
        self.ui.label_logo.setPixmap(scale(self.logo, 145))
        # Connect the button_start to a slot (function)
        self.ui.button_start.clicked.connect(self.on_button_start_clicked)
        self.ui.actionImport.triggered.connect(self.on_actionImport_clicked)
        self.ui.actionImport_Folder.triggered.connect(self.on_actionImport_folder_clicked)


    def on_button_start_clicked(self):
        print("Button Start clicked!")
        self.ui.label_right_image.setPixmap(scale(self.logo, 640))

    def on_actionImport_clicked(self):
        print("Button Start clicked!")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Optional: Set additional options as needed

        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Text Files (*.txt);;All Files (*)")  # Set a file filter

        # Use the getOpenFileName or getSaveFileName method to open the dialog
        file_name, _ = file_dialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)

        if file_name:
            print(f"Selected file: {file_name}")
            model.Database.update_images(self.database, str(file_name), "5")

    def on_actionImport_folder_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Optional: Set additional options as needed

        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Text Files (*.txt);;All Files (*)")  # Set a file filter

        # Use the getOpenFileNames method to open the dialog for selecting multiple files
        file_names, _ = file_dialog.getOpenFileNames(self, "Open Multiple Files", "", "All Files (*)", options=options)

        if file_names:
            print("Selected files:")
            for file_name in file_names:
                print(file_name)
                model.Database.update_images(self.database, str(file_name), "6")


if __name__ == "__main__":
    app = QApplication([])
    controller = MyController()
    controller.show()
    sys.exit(app.exec())
