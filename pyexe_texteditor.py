# -*- coding: utf-8 -*-
import sys, os
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.uic import loadUi
from _overlapped import NULL

class py_filemenu():
    def __init__(self, mainwindow):
        self.menubar = mainwindow.menuBar()
        self.filemenu = self.menubar.addMenu("&File")
        
        self.newAction = QtWidgets.QAction("&New", mainwindow, shortcut=NULL, statusTip="Create a new file", triggered=self.newFile)
        self.filemenu.addAction(self.newAction)  
        
        self.openAction = QtWidgets.QAction("&Open", mainwindow, shortcut=NULL,
                statusTip="open a file", triggered=self.openFile)
        self.filemenu.addAction(self.openAction)
        
        self.closeAction = QtWidgets.QAction("&Close", mainwindow, shortcut=NULL,
                statusTip="Close.",triggered = self.closeWindow)      
        self.filemenu.addAction(self.closeAction)
             
    def newFile(self):
        pass
    def openFile(self):
        pass
    def closeWindow(self):
        pass    

class py_editmenu():
    def __init__(self, mainwindow):
        self.menubar = mainwindow.menuBar() 
        
        self.editmenu = self.menubar.addMenu("&Edit")               
        
        self.copyAction = QtWidgets.QAction("&Copy", mainwindow, shortcut=NULL,
                statusTip="copy.", triggered = self.copyContent)
        self.editmenu.addAction(self.copyAction)
    def copyContent(self):
        pass          

class py_aboutmenu():
    def __init__(self,mainwindow):
        self.menubar = mainwindow.menuBar()
        self.helpmenu = self.menubar.addMenu("&Help")   
        self.aboutAction = QtWidgets.QAction("&About", mainwindow, shortcut=NULL,
                statusTip="about.", triggered = self.aboutFunction)
             
        self.helpmenu.addAction(self.aboutAction)
    def aboutFunction(self):
        pass        


class py_texteditor(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(py_texteditor, self).__init__(parent)
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        self.setWindowTitle("py_texteditor")
        self.setWindowIcon(QtGui.QIcon("qt-logo.png"))
        self.setGeometry(400,250,500,300)
        
        self.menubar = self.menuBar()
        
        py_filemenu(self)
        py_editmenu(self)
        py_aboutmenu(self)
        

if __name__ == "__main__":
    print ("---pyeditor--")
    
    app = QtWidgets.QApplication(sys.argv)
    py_editor = py_texteditor()
    py_editor.show()
    sys.exit(app.exec_())
    
    #from PyQt5 import QtWidget
    #app = QtWidgets.QApplication(sys.argv) 
    #first_window = QtWidgets.QWidget()
    #first_window = QtWidgets.QMainWindow()
    #first_window = QtWidgets.QDialog()
    
    #first_window.show()
    sys.exit(app.exec_())  
