# -*- coding: utf-8 -*-
import sys, os
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.uic import loadUi
from _overlapped import NULL

class py_texteditor(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(py_texteditor, self).__init__(parent)
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        self.setWindowTitle("py_texteditor")
        self.setWindowIcon(QtGui.QIcon("qt-logo.png"))
        self.setGeometry(400,250,500,300)
        
        self.createActions()
        self.addmenubar()
                
    def createActions(self):
        self.newAction = QtWidgets.QAction("&New", self, shortcut=NULL,
                statusTip="Create a new file", triggered=self.newFile)
        self.openAction = QtWidgets.QAction("&Open", self, shortcut=NULL,
                statusTip="open a file", triggered=self.openFile)
        self.closeAction = QtWidgets.QAction("&Close", self, shortcut=NULL,
                statusTip="Close.",triggered = self.closeWindow)      
        self.copyAction = QtWidgets.QAction("&Copy", self, shortcut=NULL,
                statusTip="copy.", triggered = self.copyContent)
        self.aboutAction = QtWidgets.QAction("&About", self, shortcut=NULL,
                statusTip="copy.", triggered = self.aboutFunction)
    def addmenubar(self):
        self.menubar = self.menuBar()
        self.filemenu = self.menubar.addMenu("&File")
        self.editmenu = self.menubar.addMenu("&Edit")
        self.aboutmenu = self.menubar.addMenu("&About")        
        
        self.filemenu.addAction(self.newAction)
        self.filemenu.addAction(self.openAction)
        self.filemenu.addAction(self.closeAction)
        
        self.editmenu.addAction(self.copyAction)
        
        self.aboutmenu.addAction(self.aboutAction)
              
    def newFile(self):
        pass
    def openFile(self):
        pass
    def closeWindow(self):
        pass    
    def copyContent(self):
        pass  
    def aboutFunction(self):
        pass
        

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
