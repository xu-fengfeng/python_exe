# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.uic import loadUi

class LatinPigGame(object):
    def __init__(self):
        vowellist = "aeiuo"
    def LatinPigChange(self,input):
        if not isinstance(input, str):
            print ("str is not a string")
        return input

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        loadUi('mainwindow.ui', self)
        
        self.ConfirmButton.clicked.connect(self.valueChange)
        self.ExitButton.clicked.connect(self.Exit)
        self.LatinPigButton.clicked.connect(self.latinPigGame)

    def valueChange(self):
        str = self.InputLine.text()
        
        if str == "":
            print ("inputline is empyt.")
        else:
            print ("inputline = %s"%str)
            newstr = self.reverseStr(str)

            self.OutputLine.setText(newstr)

    def reverseStr(self,str):
        newlist = list(str)
        newlist.reverse()
        #print (newlist)
        newstr = "".join(newlist)
        return newstr
    def latinPigGame(self):
        str = self.InputLine.text()
        if str == "":
            print ("inputline is empty.")
        else:
            print ("inputline = %s"%str)
            lpg = LatinPigGame()
            newstr = lpg.LatinPigChange(str)

            self.OutputLine.setText(newstr)
    def Exit(self):
        QtWidgets.QApplication.quit()
        
    
        
if __name__ == '__main__':
    print ("start...")
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    
    sys.exit(app.exec_())
