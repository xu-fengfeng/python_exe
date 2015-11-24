# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.uic import loadUi

class LatinPigGame(object):
    def __init__(self):
        self.vowellist = "aeiuo"
    def LatinPigChange(self,input):
        if not isinstance(input, str):
            print ("str is not a string")
        for i in input:
            if i not in self.vowellist:
                print ("%s is in vowel"%i)
                index = input.index(i)
                print (index)
                
                inputlist = list(input)
                inputlist.remove(i)
                
                print (inputlist)
                return "".join(inputlist) +"-ay"     #index
            
        return None

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
        inputstr = self.InputLine.text()
        if inputstr == "":
            print ("inputline is empty.")
        else:
            print ("inputline = %s"%inputstr)
            lpg = LatinPigGame()
            outputstr = lpg.LatinPigChange(inputstr)
            '''
            index = lpg.LatinPigChange(inputstr)
            print ("index = %d"%index)
            if index == None:
                outputstr = ""
            else:
                inputlist = list(inputstr)
                outputlist = inputlist.pop(index)
                outputstr = "".join(outputlist) 
            '''

            self.OutputLine.setText(outputstr)
    def Exit(self):
        QtWidgets.QApplication.quit()
        
    
        
if __name__ == '__main__':
    print ("start...")
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    
    sys.exit(app.exec_())
