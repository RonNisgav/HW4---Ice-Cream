from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog


class IceWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ice Cream Profits')
        self.setGeometry(200,200,800,700)

        self.temperatures = []
        self.profits = []
        self.selected_file = ''

        self.load_button = QPushButton('Load File', self)
        self.load_button.setGeometry(20,20,200,35)
        self.load_button.clicked.connect(self.load_method)

    def load_method(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    window = IceWindow()
    window.show()
    app.exec()