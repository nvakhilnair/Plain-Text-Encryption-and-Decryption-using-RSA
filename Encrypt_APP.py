from PyQt5 import QtCore, QtGui, QtWidgets
from encrpytion import encrpytion


class Ui_Encryption(object):
    def setupUi(self, Encryption):
        Encryption.setObjectName("Encryption")
        Encryption.resize(546, 417)
        self.textEdit_input = QtWidgets.QPlainTextEdit(Encryption)
        self.textEdit_input.setGeometry(QtCore.QRect(140, 20, 371, 121))
        self.textEdit_input.setObjectName("textEdit_input")
        self.label_input = QtWidgets.QLabel(Encryption)
        self.label_input.setGeometry(QtCore.QRect(30, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.textEdit_output = QtWidgets.QPlainTextEdit(Encryption)
        self.textEdit_output.setGeometry(QtCore.QRect(140, 270, 371, 131))
        self.textEdit_output.setObjectName("textEdit_output")
        self.label_output = QtWidgets.QLabel(Encryption)
        self.label_output.setGeometry(QtCore.QRect(0, 320, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.pushButton_cipher = QtWidgets.QPushButton(Encryption)
        self.pushButton_cipher.setGeometry(QtCore.QRect(290, 220, 88, 27))
        self.pushButton_cipher.setObjectName("pushButton_cipher")
        self.pushButton_cipher.clicked.connect(self.Cipher)

        self.retranslateUi(Encryption)
        QtCore.QMetaObject.connectSlotsByName(Encryption)


    def Cipher(self):
        self.textEdit_output.clear()
        data = list(self.textEdit_input.toPlainText())
        data_ciphered = []
        for i in data:
            data_ciphered.append(encrpytion(ord(i),12095,12317))
        self.textEdit_output.insertPlainText(str(data_ciphered))


    def retranslateUi(self, Encryption):
        _translate = QtCore.QCoreApplication.translate
        Encryption.setWindowTitle(_translate("Encryption", "Encryption"))
        self.label_input.setText(_translate("Encryption", "Input Text"))
        self.label_output.setText(_translate("Encryption", "Ciphered Text"))
        self.pushButton_cipher.setText(_translate("Encryption", "Cipher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Encryption = QtWidgets.QDialog()
    ui = Ui_Encryption()
    ui.setupUi(Encryption)
    Encryption.show()
    sys.exit(app.exec_())
