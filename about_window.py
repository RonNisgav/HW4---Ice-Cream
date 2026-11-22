from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('About me')
        self.setFixedSize(520, 450)

        self.setStyleSheet('background-color: cyan; font-size: 17px;')

        self.title = QLabel('About Me', self)
        self.title.setGeometry(20, 15, 480, 40)
        self.title.setStyleSheet('font-size: 26px; color: blue')

        self.name_label = QLabel('Ron Nisgav', self)
        self.name_label.setGeometry(20, 290, 480, 30)

        self.email_label = QLabel('rnisgav@gmail.com', self)
        self.email_label.setGeometry(20, 335, 480, 30)

        self.linkedin_label = QLabel('<a href="https://www.linkedin.com/">My LinkedIn</a>'' (i dont have a linkedin yet)',self)
        self.linkedin_label.setGeometry(20, 380, 480, 30)
        self.linkedin_label.setOpenExternalLinks(True)


if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()