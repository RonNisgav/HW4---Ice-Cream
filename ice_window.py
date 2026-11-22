from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np
from about_window import AboutWindow

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

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setParent(self)
        self.canvas.setGeometry(20,115,760,560)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setGeometry(20,70,760,40)

        self.about_window = AboutWindow()
        self.about_button = QPushButton('About', self)
        self.about_button.setGeometry(240,20,100,35)
        self.about_button.clicked.connect(self.show_about)

        self.draw_graph()

    def load_method(self):
        result = QFileDialog.getOpenFileName(self, 'Select data file', '', 'CSV files (*.csv)')
        filename = result[0]
        if not filename: return

        self.selected_file = filename
        self.temperatures = []
        self.profits = []

        with open(self.selected_file) as f:
            lines = f.readlines()

        for line in lines[1:]:
            parts = line.strip().split(',')
            self.temperatures.append(float(parts[0]))
            self.profits.append(float(parts[1]))

        self.draw_graph()


    def draw_graph(self):
        self.axes.clear()
        self.axes.scatter(self.temperatures, self.profits, s=1)

        if len(self.temperatures) > 1:
            slope, intercept = np.polyfit(self.temperatures, self.profits, 1)
            x_line = np.array([min(self.temperatures), max(self.temperatures)])
            y_line = slope * x_line + intercept
            self.axes.plot(x_line, y_line, color='red', label=f'y = {slope:.2f}x + {intercept:.2f}')
            self.axes.legend()

        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)

        self.axes.set_title('Ice Cream Profits vs Temperature')
        self.axes.set_xlabel('Temperature')
        self.axes.set_ylabel('Profit')

        self.canvas.draw()

    def show_about(self):
        self.about_window.show()

if __name__ == '__main__':
    app = QApplication()
    with open('q2.qss') as f:
        app.setStyleSheet(f.read())
    window = IceWindow()
    window.show()
    app.exec()
