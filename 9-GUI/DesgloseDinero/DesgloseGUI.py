import sys
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel,
                               QGridLayout, )
from DesgloseMinimoBilletes import desglose_euros

WINDOW_SIZE_X = 1500
WINDOW_SIZE_Y = 500


class DesgloseEuros(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desglose Euros")
        self.setFixedSize(WINDOW_SIZE_X, WINDOW_SIZE_Y)
        self.general_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.general_layout)
        self.setCentralWidget(central_widget)

        self._create_statement()
        self._create_input()
        self._create_button()

        self.aditional_layout = QGridLayout()
        self.general_layout.addLayout(self.aditional_layout)

        self._create_images()
        self._create_labels()

    def _create_statement(self):
        self._statement = QLabel("Ingrese la cantidad (numero entero, no centimos)")
        self._statement.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self._statement)

    def _create_input(self):
        self.input_ = QLineEdit()
        self.input_.setPlaceholderText("Euros")
        self.input_.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self.input_)

    def _create_button(self):
        self.button = QPushButton("Calcular!")
        self.button.clicked.connect(self._calculate)
        self.general_layout.addWidget(self.button)
        self.button.setFocus()

    def _create_images(self):
        self.pixmap_1 = QPixmap("img/1euro.png")
        self.pixmap_1 = self.pixmap_1.scaled(80, 80)
        self.image_1 = QLabel()
        self.image_1.setPixmap(self.pixmap_1)
        self.image_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_1, 0, 0)

        self.pixmap_2 = QPixmap("img/2euros.png")
        self.pixmap_2 = self.pixmap_2.scaled(80, 80)
        self.image_2 = QLabel()
        self.image_2.setPixmap(self.pixmap_2)
        self.image_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_2, 0, 1)

        self.pixmap_3 = QPixmap("img/5euros.png")
        self.pixmap_3 = self.pixmap_3.scaled(160, 80)
        self.image_3 = QLabel()
        self.image_3.setPixmap(self.pixmap_3)
        self.image_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_3, 0, 2)

        self.pixmap_4 = QPixmap("img/10euros.png")
        self.pixmap_4 = self.pixmap_4.scaled(160, 80)
        self.image_4 = QLabel()
        self.image_4.setPixmap(self.pixmap_4)
        self.image_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_4, 0, 3)

        self.pixmap_5 = QPixmap("img/20euros.png")
        self.pixmap_5 = self.pixmap_5.scaled(160, 80)
        self.image_5 = QLabel()
        self.image_5.setPixmap(self.pixmap_5)
        self.image_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_5, 0, 4)

        self.pixmap_6 = QPixmap("img/50euros.png")
        self.pixmap_6 = self.pixmap_6.scaled(160, 80)
        self.image_6 = QLabel()
        self.image_6.setPixmap(self.pixmap_6)
        self.image_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_6, 0, 5)

        self.pixmap_7 = QPixmap("img/100euros.png")
        self.pixmap_7 = self.pixmap_7.scaled(160, 80)
        self.image_7 = QLabel()
        self.image_7.setPixmap(self.pixmap_7)
        self.image_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_7, 0, 6)

        self.pixmap_8 = QPixmap("img/200euros.png")
        self.pixmap_8 = self.pixmap_8.scaled(160, 80)
        self.image_8 = QLabel()
        self.image_8.setPixmap(self.pixmap_8)
        self.image_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_8, 0, 7)

        self.pixmap_9 = QPixmap("img/500euros.png")
        self.pixmap_9 = self.pixmap_9.scaled(160, 80)
        self.image_9 = QLabel()
        self.image_9.setPixmap(self.pixmap_9)
        self.image_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aditional_layout.addWidget(self.image_9, 0, 8)

    def _create_labels(self):
        font = QFont('Arial', 20)

        self.label_1 = QLabel("0")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_1.setFont(font)
        self.aditional_layout.addWidget(self.label_1, 1, 0)

        self.label_2 = QLabel("0")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setFont(font)
        self.aditional_layout.addWidget(self.label_2, 1, 1)

        self.label_3 = QLabel("0")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setFont(font)
        self.aditional_layout.addWidget(self.label_3, 1, 2)

        self.label_4 = QLabel("0")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setFont(font)
        self.aditional_layout.addWidget(self.label_4, 1, 3)

        self.label_5 = QLabel("0")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setFont(font)
        self.aditional_layout.addWidget(self.label_5, 1, 4)

        self.label_6 = QLabel("0")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setFont(font)
        self.aditional_layout.addWidget(self.label_6, 1, 5)

        self.label_7 = QLabel("0")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setFont(font)
        self.aditional_layout.addWidget(self.label_7, 1, 6)

        self.label_8 = QLabel("0")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setFont(font)
        self.aditional_layout.addWidget(self.label_8, 1, 7)

        self.label_9 = QLabel("0")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9.setFont(font)
        self.aditional_layout.addWidget(self.label_9, 1, 8)

    def _calculate(self):
        if self.input_.text():
            result = desglose_euros(int(self.input_.text()))
            self.label_9.setText(str(result[0]))
            self.label_8.setText(str(result[1]))
            self.label_7.setText(str(result[2]))
            self.label_6.setText(str(result[3]))
            self.label_5.setText(str(result[4]))
            self.label_4.setText(str(result[5]))
            self.label_3.setText(str(result[6]))
            self.label_2.setText(str(result[7]))
            self.label_1.setText(str(result[8]))

def main():
    desglose_euros_app = QApplication([])
    desglose_euros_window = DesgloseEuros()
    desglose_euros_window.show()
    sys.exit(desglose_euros_app.exec())


if __name__ == "__main__":
    main()
