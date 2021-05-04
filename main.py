from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import sys


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1074, 616)
        Dialog.setStyleSheet("background (rgb:0,0,0) ")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1081, 621))
        self.frame.setStyleSheet("QFrame\n"
                                 "{\n"
                                 "background:white;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 1051, 80))
        self.frame_2.setStyleSheet("QFrame\n"
                                   "{\n"
                                   "background:#D3D3D3;\n"
                                   "border-radius:15;\n"
                                   "border:1px solid black;\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
                                   "{\n"
                                   "border:0px;\n"
                                   "}")

        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 150, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(250, 150, 171, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 220, 171, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 220, 171, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 290, 381, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 120, 81, 21))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(250, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(250, 190, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 260, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 510, 411, 61))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(538, 120, 519, 330))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)

        self.pushButton.clicked.connect(self.connect_db)
        self.pushButton.clicked.connect(self.upload_data)
        self.pushButton.clicked.connect(self.clean)


        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Record Maintainer System"))
        self.label.setText(_translate("Dialog", " Full Name"))
        self.label_3.setText(_translate("Dialog", "Age"))
        self.label_4.setText(_translate("Dialog", "Phone Number"))
        self.label_5.setText(_translate("Dialog", "City"))
        self.label_6.setText(_translate("Dialog", "Email Address"))
        self.pushButton.setText(_translate("Dialog", "Submit"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Full Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Age"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Phone Number"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "City"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Email Address"))

    def clean(self):
        self.lineEdit_4.clear()
        self.lineEdit_8.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_2.clear()

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def connect_db(self):
        connection = sqlite3.connect('data_base.db')
        conn = connection.cursor()
        _name = str(self.lineEdit_2.text())
        _age = str(self.lineEdit_8.text())
        _phone = str(self.lineEdit_3.text())
        _city = str(self.lineEdit_5.text())
        _email = str(self.lineEdit_4.text())

        exist_name = conn.execute('SELECT names FROM data_base WHERE names=?', (_name,))
        data_name = exist_name.fetchall()
        exit_phone = conn.execute('SELECT phone FROM data_base WHERE phone=?', (_phone,))
        data_phone = exit_phone.fetchall()
        print(data_name)
        print(data_phone)
        if len(data_name) == 0 and len(data_phone) == 0 and  [] not in data_phone:
            conn.execute('INSERT INTO data_base(names,ages,phone,cities,email) VALUES(?,?,?,?,?)',
                         (_name, _age, _phone, _city, _email))
            connection.commit()
            self.show_popup("Submitted to data base!")
        else:
            self.show_popup("This person already exist")

    def upload_data(self):
        conn = sqlite3.connect('data_base.db')
        c = conn.cursor()
        query = 'SELECT * FROM data_base'
        show_data = c.execute(query)
        self.tableWidget.setRowCount(0)
        for row_idx, row_data in enumerate(show_data):
            self.tableWidget.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.upload_data()
    Dialog.show()
    sys.exit(app.exec_())
