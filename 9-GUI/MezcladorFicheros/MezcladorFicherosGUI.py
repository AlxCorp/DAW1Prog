import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTextEdit, QPushButton, QVBoxLayout, QLabel,
                               QFileDialog, )
from MezcladorFicheros import mezcladora

WINDOW_SIZE = 800


class MezcladorDeFicheros(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mezclador Ficheros")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.general_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.general_layout)
        self.setCentralWidget(central_widget)

        self._create_statement()
        self._create_file_input_1()
        self._create_file_input_2()
        self._create_button()
        self._create_display()

    def _create_statement(self):
        self._statement = QLabel("Ingrese los ficheros a mezclar y el fichero resultante")
        self._statement.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.general_layout.addWidget(self._statement)

    def _create_file_input_1(self):
        self.input_1 = QFileDialog()
        self.general_layout.addWidget(self.input_1)

    def _create_file_input_2(self):
        self.input_2 = QFileDialog()
        self.general_layout.addWidget(self.input_2)

    def _create_button(self):
        self.button = QPushButton("MeZcLaR!")
        self.button.clicked.connect(self._mezclar)
        self.general_layout.addWidget(self.button)

    def _create_display(self):
        self.display = QTextEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("color: green")
        self.general_layout.addWidget(self.display)

    def _mezclar(self):
        try:
            mezclado = mezcladora(self.input_1.selectedFiles()[0], self.input_2.selectedFiles()[0])
            print(self.input_1.selectedFiles()[0])
            print(self.input_2.selectedFiles()[0])
            print(mezclado)
            self.display.setText("".join(mezclado))
        except:
            pass


def main():
    mezclador_ficheros_app = QApplication([])
    mezclador_ficheros_window = MezcladorDeFicheros()
    mezclador_ficheros_window.show()
    sys.exit(mezclador_ficheros_app.exec())


if __name__ == "__main__":
    main()
