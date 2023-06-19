# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'Calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QSignalMapper, )
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_PyCalc(object):
    def setupUi(self, PyCalc):
        if not PyCalc.objectName():
            PyCalc.setObjectName(u"PyCalc")
        PyCalc.setEnabled(True)
        PyCalc.resize(235, 235)
        PyCalc.setMinimumSize(QSize(235, 235))
        PyCalc.setMaximumSize(QSize(235, 235))
        self.centralwidget = QWidget(PyCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 241, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(40, 40))
        self.pushButton_7.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(40, 40))
        self.pushButton_8.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(40, 40))
        self.pushButton_13.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_13, 0, 3, 1, 1)

        self.pushButton_14 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(40, 40))
        self.pushButton_14.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_14, 1, 3, 1, 1)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(40, 40))
        self.pushButton_6.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(40, 40))
        self.pushButton_9.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(40, 40))
        self.pushButton_17.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_17, 0, 4, 1, 1)

        self.pushButton_19 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(40, 40))
        self.pushButton_19.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_19, 2, 4, 1, 1)

        self.pushButton_16 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(40, 40))
        self.pushButton_16.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_16, 3, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setMaximumSize(QSize(40, 40))
        self.pushButton_5.setBaseSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(40, 40))
        self.pushButton_18.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_18, 1, 4, 1, 1)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(40, 40))
        self.pushButton_11.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(40, 40))
        self.pushButton_10.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_10, 1, 2, 1, 1)

        self.pushButton_20 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(40, 40))
        self.pushButton_20.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_20, 3, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(40, 40))
        self.pushButton_12.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        self.pushButton_4.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(40, 40))
        self.pushButton_15.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_15, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        PyCalc.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(PyCalc)
        self.statusbar.setObjectName(u"statusbar")
        PyCalc.setStatusBar(self.statusbar)

        self.retranslateUi(PyCalc)

        QMetaObject.connectSlotsByName(PyCalc)
    # setupUi

    def retranslateUi(self, PyCalc):
        PyCalc.setWindowTitle(QCoreApplication.translate("PyCalc", u"Calculator", None))
        self.lineEdit.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("PyCalc", u"2", None))
        self.pushButton_8.setText(QCoreApplication.translate("PyCalc", u"00", None))
        self.pushButton_13.setText(QCoreApplication.translate("PyCalc", u"/", None))
        self.pushButton_14.setText(QCoreApplication.translate("PyCalc", u"*", None))
        self.pushButton_6.setText(QCoreApplication.translate("PyCalc", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("PyCalc", u"9", None))
        self.pushButton_17.setText(QCoreApplication.translate("PyCalc", u"C", None))
        self.pushButton_19.setText(QCoreApplication.translate("PyCalc", u")", None))
        self.pushButton_16.setText(QCoreApplication.translate("PyCalc", u"+", None))
        self.pushButton_3.setText(QCoreApplication.translate("PyCalc", u"1", None))
        self.pushButton_5.setText(QCoreApplication.translate("PyCalc", u"8", None))
        self.pushButton_18.setText(QCoreApplication.translate("PyCalc", u"(", None))
        self.pushButton_11.setText(QCoreApplication.translate("PyCalc", u"3", None))
        self.pushButton_10.setText(QCoreApplication.translate("PyCalc", u"6", None))
        self.pushButton_20.setText(QCoreApplication.translate("PyCalc", u"=", None))
        self.pushButton_2.setText(QCoreApplication.translate("PyCalc", u"4", None))
        self.pushButton.setText(QCoreApplication.translate("PyCalc", u"7", None))
        self.pushButton_12.setText(QCoreApplication.translate("PyCalc", u".", None))
        self.pushButton_4.setText(QCoreApplication.translate("PyCalc", u"0", None))
        self.pushButton_15.setText(QCoreApplication.translate("PyCalc", u"-", None))
    # retranslateUi


if __name__ == '__main__':
    app = QApplication([])
    calc = QMainWindow()
    ui = Ui_PyCalc()
    ui.setupUi(calc)
    calc.show()
    sys.exit(app.exec())