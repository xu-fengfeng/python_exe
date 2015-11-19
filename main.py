# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        loadUi('mainwindow.ui', self)
        
        self.ConfirmButton.clicked.connect(self.valueChange)
        self.ExitButton.clicked.connect(self.Exit)
        
        '''
        InputLabel = QtWidgets.QLabel("Input:")
        self.InputLine = QtWidgets.QLineEdit()

        OutputLabel = QtWidgets.QLabel("Output:")
        self.OutputLine =QtWidgets.QLineEdit()

        self.ConfirmButton = QtWidgets.QPushButton("&Reverse")
        self.ConfirmButton.clicked.connect(self.valueChange)
        self.ConfirmButton.show()
        
        self.ExitButton = QtWidgets.QPushButton("&Exit")
        self.ExitButton.clicked.connect(self.Exit)
        
        #buttonLayout1 = QtWidgets.QVBoxLayout()
        buttonLayout1 = QtWidgets.QHBoxLayout()
        buttonLayout1.addWidget(self.ConfirmButton, QtCore.Qt.AlignTop)
        buttonLayout1.addWidget(self.ExitButton, QtCore.Qt.AlignTop)
        #buttonLayout1.addStretch()        
        
        #mainLayout是主界面，addWidget把item添加到主界面
        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(InputLabel, 0, 0)
        mainLayout.addWidget(self.InputLine, 0, 1)
        mainLayout.addWidget(OutputLabel, 1, 0, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.OutputLine, 1, 1)
        
        mainLayout.addLayout(buttonLayout1, 2, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Ex1:Reverse string")
        '''        
    def valueChange(self):
        str = self.InputLine.text()
        
        if str == "":
            print ("inputline is empyt")
        else:
            print ("inputline = %s"%str)
            newstr = self.reverseStr(str)

            #print ("newstr = %s"%newstr)
            self.OutputLine.setText(newstr)

    def reverseStr(self,str):
        newlist = list(str)
        newlist.reverse()
        #print (newlist)
        newstr = "".join(newlist)
        return newstr
    
    def Exit(self):
        QtWidgets.QApplication.quit()
    
        
if __name__ == '__main__':
    print ("start...")
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    
    sys.exit(app.exec_())
