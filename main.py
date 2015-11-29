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

class PalindromeCheckGame():
    def __init__(self):
        pass
    def PalindromeCheck(self, input):
        if not isinstance(input, str):
            print ("input is not a string")
        lens = len(input)
        print ("str len = %d"%lens)
        if lens%2 == 0:
            newstr1 = input[0:(int(lens/2))]
            newstr2 = input[int(lens/2):]
        else:
            newstr1 = input[0:(int(lens/2))]
            newstr2 = input[int(lens/2+1):]            

        if newstr1 == newstr2:
            resultstr = "Yes,it's a Palindrome string"
        else:
            resultstr = "No, it's not aPalindrome string"    
        return resultstr

class vowelCheckGame():
    def __init__(self):
        pass
    def vowelCheck(self,input):
        if not isinstance(input, str):
           print ("input is not a string")        
        


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        loadUi('mainwindow.ui', self)
        
        self.ConfirmButton.clicked.connect(self.valueChange)
        self.ExitButton.clicked.connect(self.Exit)
        self.LatinPigButton.clicked.connect(self.latinPigGame)

        self.vowelcheck_Button.clicked.connect(self.vowelCheck)
        self.palindrome_Button.clicked.connect(self.palindromeCheck)

    def vowelCheck(self):
        print ("in vowelCheck mode")
        input = self.InputLine.text()
        if input == "":
            print ("inputline is empyt.")
        QtWidgets.QMessageBox.information(self, "vowelCheckGame Result", "Null")

    def palindromeCheck(self):
        print ("in palindromeCheck mode")
        input = self.InputLine.text()
        if str == "":
            print ("inputline is empyt.")
                    
        pcg = PalindromeCheckGame()
        retstr = pcg.PalindromeCheck(input)
        QtWidgets.QMessageBox.information(self, "PalindromeCheckGame Result",retstr)
        
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
