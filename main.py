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
        self.num_a = 0
        self.num_e = 0
        self.num_u = 0
        self.num_i = 0
        self.num_o = 0
    def vowelCheck(self,input):
        if not isinstance(input, str):
           print ("input is not a string")        
        for i in range(len(input)):
            if input[i] == 'a':
                self.num_a+=1
            if input[i] == 'e':
                self.num_e+=1            
            if input[i] == 'u':
                self.num_u+=1
            if input[i] == 'i':
                self.num_i+=1               
            if input[i] == 'o':
                self.num_o+=1
        return (self.num_a, self.num_e, self.num_u, self.num_i, self.num_o)  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        loadUi('mainwindow.ui', self)
        
        self.ConfirmButton.clicked.connect(self.valueChange)
        self.ExitButton.clicked.connect(self.Exit)
        self.LatinPigButton.clicked.connect(self.latinPigGame)

        self.vowelcheck_Button.clicked.connect(self.vowelCheck)
        self.palindrome_Button.clicked.connect(self.palindromeCheck)
        
        self.wordstatisc_Button.clicked.connect(self.wordstatisc)

    def vowelCheck(self):          #元音统计
        print ("in vowelCheck mode")
        input = self.InputLine.text()
        if input == "":
            print ("inputline is empyt.")
        vcg = vowelCheckGame()
        (a,e,u,i,o) = vcg.vowelCheck(input)
        output = "num_a = %d,\nnum_e = %d,\nnum_u = %d,\nnum_i = %dd,\nnum_o = %d"%(a,e,u,i,o)
        QtWidgets.QMessageBox.information(self, "vowelCheckGame Result", output)

    def palindromeCheck(self):    #拉丁猪游戏
        print ("in palindromeCheck mode")
        input = self.InputLine.text()
        if str == "":
            print ("inputline is empyt.")
                    
        pcg = PalindromeCheckGame()
        retstr = pcg.PalindromeCheck(input)
        QtWidgets.QMessageBox.information(self, "PalindromeCheckGame Result",retstr)
        
    def valueChange(self):          #回转字符
        str = self.InputLine.text()
        
        if str == "":
            print ("inputline is empyt.")
        else:
            print ("inputline = %s"%str)
            newstr = self.reverseStr(str)

            self.OutputLine.setText(newstr)
    def wordstatisc(self):
        str = self.wordstatisc_txtbox.toPlainText();
        print (str)
        str_list = str.split(' ')
        print (len(str_list))
        output_mssage = "total %d words!"%len(str_list)
        QtWidgets.QMessageBox.information(self, "result", output_mssage)
    
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
