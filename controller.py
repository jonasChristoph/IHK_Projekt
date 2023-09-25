from model import Database
import mainwindow


class Data:
    def __int__(self):
        pass

    def show_img(self):
        return Database.read_single_image("1")

if __name__ == "__main__":
    Data.show_img()
