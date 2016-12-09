import sys

from PyQt4.QtGui import *


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()  # other alternatives QHBoxLayout,QGridLayout,QFormLayout
        label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        button.clicked.connect(self.close)


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.setWindowTitle("Hello World!")
dialog.show()
sys.exit(app.exec_())
