import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, )
from ej01_adivina_un_numero_v2 import AdivinaNumero

WINDOW_SIZE = 500


class AdivinaNumeroWindow(QMainWindow):
    def __init__(self):
        self._adivina_numero = AdivinaNumero()

        super().__init__()
        self.setWindowTitle("Adivina un Número")
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
        self._statement = QLabel("Ingrese un número entre 1 y 100")
        self._statement.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self._statement)

    def _create_input_(self):
        self.input_ = QLineEdit()
        self.input_.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self.input_)

    def _create_button(self):
        self.button = QPushButton("Try!")
        self.button.clicked.connect(self._try_to_solve)
        self.general_layout.addWidget(self.button)

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("color: red")
        self.display.setText(f"Te quedan {self._adivina_numero.remaining_hints} intentos")
        self.general_layout.addWidget(self.display)

    def _try_to_solve(self):
        if self.input_.text() != "":
            returned = self._adivina_numero.input_number(int(self.input_.text()))
            self.display.setText(returned)
            self.input_.setText("")


def main():
    adivina_numero_app = QApplication([])
    adivina_numero_window = AdivinaNumeroWindow()
    adivina_numero_window.show()
    sys.exit(adivina_numero_app.exec())


if __name__ == "__main__":
    main()
