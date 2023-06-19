import sys
from CalculatorGUI import *
from functools import partial

ERROR_MSG = "ERROR"


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PyCalc()
        self.ui.setupUi(self)

        self._operation = ""
        self._result = 0

        self.ui.pushButton.clicked.connect(partial(self._evaluate_content, self.ui.pushButton.text()))
        self.ui.pushButton_2.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_4.text()))
        self.ui.pushButton_5.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_6.text()))
        self.ui.pushButton_7.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_7.text()))
        self.ui.pushButton_8.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_8.text()))
        self.ui.pushButton_9.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_9.text()))
        self.ui.pushButton_10.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_10.text()))
        self.ui.pushButton_11.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_11.text()))
        self.ui.pushButton_12.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_12.text()))
        self.ui.pushButton_13.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_13.text()))
        self.ui.pushButton_14.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_14.text()))
        self.ui.pushButton_15.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_15.text()))
        self.ui.pushButton_16.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_16.text()))
        self.ui.pushButton_17.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_17.text()))
        self.ui.pushButton_18.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_18.text()))
        self.ui.pushButton_19.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_19.text()))
        self.ui.pushButton_20.clicked.connect(partial(self._evaluate_content, self.ui.pushButton_20.text()))

    def _evaluate_content(self, button):
        print(button)
        if button == "C":
            self._clear_display()
        elif button != "=":
            self._operation += str(button)
            self._update_display()
        else:
            self._show_result()

    def _update_display(self):
        if self._result == 0:
            self.ui.lineEdit.setText(self._operation)
            self.ui.lineEdit.setFocus()
        else:
            self.ui.lineEdit.setText(str(self._result))
            self.ui.lineEdit.setFocus()
            self._operation = str(self._result)
            self._result = 0

    def _show_result(self):
        self._result = eval(self._operation)
        self._update_display()

    def _clear_display(self):
        self._operation = ""
        self._result = 0
        self._update_display()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Calculadora()
    my_app.show()
    sys.exit(app.exec())
