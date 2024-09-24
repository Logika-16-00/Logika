# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 311, 521))
        self.textEdit.setStyleSheet("border-radius: 5px;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 211, 41))
        self.label.setObjectName("label")
        self.list_1 = QtWidgets.QListWidget(self.centralwidget)
        self.list_1.setGeometry(QtCore.QRect(330, 50, 411, 81))
        self.list_1.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(251, 255, 237);")
        self.list_1.setObjectName("list_1")
        self.btn_make = QtWidgets.QPushButton(self.centralwidget)
        self.btn_make.setGeometry(QtCore.QRect(330, 140, 191, 61))
        self.btn_make.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.btn_make.setObjectName("btn_make")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(540, 140, 201, 61))
        self.btn_delete.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(330, 210, 411, 51))
        self.btn_save.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 254, 240);")
        self.btn_save.setObjectName("btn_save")
        self.btn_detach = QtWidgets.QPushButton(self.centralwidget)
        self.btn_detach.setGeometry(QtCore.QRect(550, 450, 191, 61))
        self.btn_detach.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.btn_detach.setObjectName("btn_detach")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(330, 520, 411, 51))
        self.btn_search.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 253, 242);")
        self.btn_search.setObjectName("btn_search")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(330, 450, 201, 61))
        self.btn_add.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.btn_add.setObjectName("btn_add")
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setGeometry(QtCore.QRect(330, 320, 411, 81))
        self.list2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 238);")
        self.list2.setObjectName("list2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 270, 211, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 419, 401, 21))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Введи сюди текст</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Список заміток"))
        self.btn_make.setText(_translate("MainWindow", "Створити замітку"))
        self.btn_delete.setText(_translate("MainWindow", "Видалити замітку"))
        self.btn_save.setText(_translate("MainWindow", "Зберегти замітку"))
        self.btn_detach.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.btn_search.setText(_translate("MainWindow", "Шукати замітки по замітку"))
        self.btn_add.setText(_translate("MainWindow", "Додати до замітки"))
        self.label_2.setText(_translate("MainWindow", "Список заміток"))
        self.lineEdit.setText(_translate("MainWindow", "Введіть тег"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
