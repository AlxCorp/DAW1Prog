import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Calculadora")
window.setGeometry(100, 100, 280, 80)
hello_message = QLabel("<h1>Hola Mundo!</h1>", parent=window)
hello_message.move(60, 15)

window.show()
sys.exit(app.exec())
