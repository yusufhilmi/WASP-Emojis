from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os, sys
import cv2
from PIL.ImageQt import ImageQt


class GuiCakep(QtGui.QWidget):

    global label1, label2

    def __init__(self):
        super(GuiCakep, self).__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle('Single Browse')

        self.label1 = QtGui.QLabel(self)
        self.label1.setFrameShape(QtGui.QFrame.Box)
        self.label1.setGeometry(QtCore.QRect(20, 10, 451, 451))
        pixmap = QPixmap('1stimage.jpg')
        self.label1.setPixmap(pixmap)
        self.label2 =QtGui.QLabel(self)
        self.label2.setFrameShape(QtGui.QFrame.Box)
        self.label2.setGeometry(QtCore.QRect(481, 10, 451, 451))
        btn = QtGui.QPushButton('Browse', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.browse)
        btn.move(775, 500)
        self.show()

    def browse(self):
        filePath = QtGui.QFileDialog.getOpenFileName(self, 'a file','*.jpg')
        fileHandle = open(filePath, 'r')
        pixmap = QPixmap('filePath')
        self.label1.setPixmap(pixmap)
        print("Whoa awesome")



def main():
    app = QtGui.QApplication(sys.argv)
    w = GuiCakep()
    app.exec_()


if __name__ == '__main__':
    main()