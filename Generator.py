from PyQt5 import QtCore, QtGui, QtWidgets
from primeGen import primeGen
from Decrpyt_KeyGen import Decrpyt_KeyGen
from encrypt_KeyGen import encrypt_KeyGen
import os
import sys

global e,d,N

class Ui_keyGeneration(object):
    def setupUi(self, keyGeneration):
        keyGeneration.setObjectName("keyGeneration")
        keyGeneration.resize(400, 300)
        self.label_title = QtWidgets.QLabel(keyGeneration)
        self.label_title.setGeometry(QtCore.QRect(20, 20, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_generate = QtWidgets.QPushButton(keyGeneration)
        self.pushButton_generate.setGeometry(QtCore.QRect(140, 70, 88, 27))
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.pushButton_generate.clicked.connect(self.Generate)
        self.label_Enkey = QtWidgets.QLabel(keyGeneration)
        self.label_Enkey.setGeometry(QtCore.QRect(40, 140, 101, 16))
        self.label_Enkey.setObjectName("label_Enkey")
        self.label_DeKey = QtWidgets.QLabel(keyGeneration)
        self.label_DeKey.setGeometry(QtCore.QRect(40, 200, 101, 16))
        self.label_DeKey.setObjectName("label_DeKey")
        self.lineEdit_EnKey = QtWidgets.QLineEdit(keyGeneration)
        self.lineEdit_EnKey.setGeometry(QtCore.QRect(160, 140, 111, 21))
        self.lineEdit_EnKey.setAutoFillBackground(True)
        self.lineEdit_EnKey.setReadOnly(True)
        self.lineEdit_EnKey.setObjectName("lineEdit_EnKey")
        self.lineEdit_DeKey = QtWidgets.QLineEdit(keyGeneration)
        self.lineEdit_DeKey.setGeometry(QtCore.QRect(160, 200, 113, 21))
        self.lineEdit_DeKey.setAutoFillBackground(True)
        self.lineEdit_DeKey.setReadOnly(True)
        self.lineEdit_DeKey.setObjectName("lineEdit_DeKey")
        self.pushButton_Exit = QtWidgets.QPushButton(keyGeneration)
        self.pushButton_Exit.setGeometry(QtCore.QRect(290, 250, 88, 27))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Exit.clicked.connect(self.Exit)
        self.label_Modulus = QtWidgets.QLabel(keyGeneration)
        self.label_Modulus.setGeometry(QtCore.QRect(40, 170, 101, 16))
        self.label_Modulus.setObjectName("label_Modulus")
        self.lineEdit_Modulus = QtWidgets.QLineEdit(keyGeneration)
        self.lineEdit_Modulus.setGeometry(QtCore.QRect(160, 170, 113, 21))
        self.lineEdit_Modulus.setAutoFillBackground(True)
        self.lineEdit_Modulus.setReadOnly(True)
        self.lineEdit_Modulus.setObjectName("lineEdit_Modulus")
        self.pushButton_build = QtWidgets.QPushButton(keyGeneration)
        self.pushButton_build.setGeometry(QtCore.QRect(190, 250, 88, 27))
        self.pushButton_build.setObjectName("pushButton_build")
        self.pushButton_build.clicked.connect(self.build)

        self.retranslateUi(keyGeneration)
        QtCore.QMetaObject.connectSlotsByName(keyGeneration)


    def Generate(self):
        global e,d,N
        p,q = primeGen()
        N = p*q
        Qn = (p-1)*(q-1)
        e = encrypt_KeyGen(Qn,N)
        d = Decrpyt_KeyGen(e,Qn)
        self.lineEdit_EnKey.setText(str(e))
        self.lineEdit_DeKey.setText(str(d))
        self.lineEdit_Modulus.setText(str(N))

    def build(self):
        global e,d,N
        fin = open("Decryption.txt", "rt")
        fout = open("out1.txt", "wt")
        for line in fin:
            fout.write(line.replace('D_KEY',str(d)))
        fin.close()
        fout.close()

        fin = open("out1.txt", "rt")
        fout = open("D_App.py", "wt")
        for line in fin:
            fout.write(line.replace('N_MOD',str(N)))
        fin.close()
        os.remove("out1.txt")
        fout.close()

        fin = open("Encryption.txt", "rt")
        fout = open("out2.txt", "wt")
        for line in fin:
            fout.write(line.replace('E_KEY', str(e)))
        fin.close()
        fout.close()

        fin = open("out2.txt", "rt")
        fout = open("E_APP.py", "wt")
        for line in fin:
            fout.write(line.replace('N_MOD',str(N)))
        fin.close()
        os.remove("out2.txt")
        fout.close()

    def Exit(self):
        sys.exit(0)


    def retranslateUi(self, keyGeneration):
        _translate = QtCore.QCoreApplication.translate
        keyGeneration.setWindowTitle(_translate("keyGeneration", "Key Generator"))
        self.label_title.setText(_translate("keyGeneration", "Encryption and Decrption Key Generation"))
        self.pushButton_generate.setText(_translate("keyGeneration", "Generate"))
        self.label_Enkey.setText(_translate("keyGeneration", "Encryption Key "))
        self.label_DeKey.setText(_translate("keyGeneration", "Decryption Key "))
        self.pushButton_Exit.setText(_translate("keyGeneration", "Exit"))
        self.label_Modulus.setText(_translate("keyGeneration", "Modulus N"))
        self.pushButton_build.setText(_translate("keyGeneration", "Bulid App"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    keyGeneration = QtWidgets.QDialog()
    ui = Ui_keyGeneration()
    ui.setupUi(keyGeneration)
    keyGeneration.show()
    sys.exit(app.exec_())
