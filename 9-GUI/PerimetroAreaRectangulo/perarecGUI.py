import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, )
from rectangulo import Rectangle

WINDOW_SIZE = 500


class PerimetroAreaRectangulo(QMainWindow):
    def __init__(self):
        self._rectangle = Rectangle()

        super().__init__()
        self.setWindowTitle("Area y Perimetro Rectangulo")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.general_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.general_layout)
        self.setCentralWidget(central_widget)

        self._create_statement()
        self._create_input_base()
        self._create_input_altura()
        self._create_button()
        self._create_display()

    def _create_statement(self):
        self._statement = QLabel("Ingrese la BASE y ALTURA del rectangulo")
        self._statement.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self._statement)

    def _create_input_base(self):
        self.input_ = QLineEdit()
        self.input_.setPlaceholderText("Base")
        self.input_.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self.input_)

    def _create_input_altura(self):
        self.input2_ = QLineEdit()
        self.input2_.setPlaceholderText("Altura")
        self.input2_.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self.input2_)

    def _create_button(self):
        self.button = QPushButton("Try!")
        self.button.clicked.connect(self._calculate)
        self.general_layout.addWidget(self.button)
        self.button.setFocus()

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("color: aqua")
        self.general_layout.addWidget(self.display)

    def _calculate(self):
        if self.input_.text() and self.input2_.text():
            self._rectangle.base = float(self.input_.text())
            self._rectangle.altura = float(self.input2_.text())
            self.display.setText(f"El AREA es {self._rectangle.area} y el PERIMETRO {self._rectangle.perimetro}")
            self.input_.setText("")
            self.input2_.setText("")



def main():
    perimetro_area_rectangulo_app = QApplication([])
    perimetro_area_rectangulo_window = PerimetroAreaRectangulo()
    perimetro_area_rectangulo_window.show()
    sys.exit(perimetro_area_rectangulo_app.exec())



if __name__ == "__main__":
    main()
