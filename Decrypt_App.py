from PyQt5 import QtCore, QtGui, QtWidgets
from decrpytion import decrpytion


class Ui_Decryption(object):
    def setupUi(self, Decryption):
        Decryption.setObjectName("Decryption")
        Decryption.resize(546, 417)
        self.textEdit_input = QtWidgets.QPlainTextEdit(Decryption)
        self.textEdit_input.setGeometry(QtCore.QRect(140, 20, 371, 181))
        self.textEdit_input.setObjectName("textEdit_input")
        self.label_input = QtWidgets.QLabel(Decryption)
        self.label_input.setGeometry(QtCore.QRect(0, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.textEdit_output = QtWidgets.QPlainTextEdit(Decryption)
        self.textEdit_output.setGeometry(QtCore.QRect(160, 260, 361, 131))
        self.textEdit_output.setObjectName("textEdit_output")
        self.label_output = QtWidgets.QLabel(Decryption)
        self.label_output.setGeometry(QtCore.QRect(0, 320, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.pushButton_Decipher = QtWidgets.QPushButton(Decryption)
        self.pushButton_Decipher.setGeometry(QtCore.QRect(280, 220, 88, 27))
        self.pushButton_Decipher.setObjectName("pushButton_Decipher")
        self.pushButton_Decipher.clicked.connect(self.Decipher)

        self.retranslateUi(Decryption)
        QtCore.QMetaObject.connectSlotsByName(Decryption)

    def Decipher(self):
        self.textEdit_output.clear()
        data = self.textEdit_input.toPlainText()
        data = data[1:(len(data)-1)]
        data = data.split(',')
        data = [int(i) for i in data]
        data_ciphered = data
        data_deciphered = []
        for i in data_ciphered:
            data_deciphered.append(chr(decrpytion(i,24191,12317)))
        sep = ''
        data_deciphered = sep.join(data_deciphered)
        self.textEdit_output.insertPlainText(str(data_deciphered))


    def retranslateUi(self, Decryption):
        _translate = QtCore.QCoreApplication.translate
        Decryption.setWindowTitle(_translate("Decryption", "Decryption"))
        self.label_input.setText(_translate("Decryption", "Ciphered Text"))
        self.label_output.setText(_translate("Decryption", "Deciphered Text"))
        self.pushButton_Decipher.setText(_translate("Decryption", "Decipher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Decryption = QtWidgets.QDialog()
    ui = Ui_Decryption()
    ui.setupUi(Decryption)
    Decryption.show()
    sys.exit(app.exec_())
