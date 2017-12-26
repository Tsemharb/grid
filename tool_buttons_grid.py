from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QGridLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

import sys


class Window(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        self.vert_layout = QVBoxLayout(self)
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)

        self.status_label = QLabel('no btn')

        c = 0
        for x in range(5):
            for y in range(5):
                button = (QToolButton(self))
                button.setText(str(c))
                button.setObjectName(str([x, y]))
                button.released.connect(self.button_released)
                self.grid_layout.addWidget(button, x, y)
                c = c + 1

#        [[self.grid_layout.addWidget(QToolButton(self), x, y) for x in range(5)] for y in range(5)]

        self.vert_layout.addItem(self.grid_layout)
        self.vert_layout.addWidget(self.status_label)

    def button_released(self):
        sending_button = self.sender()
        print (sending_button.objectName())
        self.status_label.setText('{} Clicked!'.format(str(sending_button.objectName())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())