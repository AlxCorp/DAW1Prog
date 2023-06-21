import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel,
                               QListWidget, )
from ej09_primos import n_numeros_primos

WINDOW_SIZE = 400


class AdivinaNumeroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numeros Primos")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.general_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.general_layout)
        self.setCentralWidget(central_widget)

        self._create_statement()
        self._create_input_()
        self._create_button()
        self._create_display()

    def _create_statement(self):
        self._statement = QLabel("Ingrese la cantidad de números primos a mostrar")
        self._statement.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self._statement)

    def _create_input_(self):
        self.input_ = QLineEdit()
        self.input_.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self.input_)

    def _create_button(self):
        self.button = QPushButton("Mostrar!")
        self.button.clicked.connect(self._show_primes)
        self.general_layout.addWidget(self.button)

    def _create_display(self):
        self.display = QListWidget()
        self.display.setStyleSheet("color: green")
        self.general_layout.addWidget(self.display)

    def _show_primes(self):
        if self.input_.text() != "":
            self.display.clear()
            returned = n_numeros_primos(int(self.input_.text()))
            self.display.addItems(returned)
            self.input_.setText("")


def main():
    adivina_numero_app = QApplication([])
    adivina_numero_window = AdivinaNumeroWindow()
    adivina_numero_window.show()
    sys.exit(adivina_numero_app.exec())


if __name__ == "__main__":
    main()
