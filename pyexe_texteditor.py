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
        
        #self.createActions()
        #self.addmenubar()
        
        #self.setMinimumSize(240,160)
        #self.resize(480,320)

    def createActions(self):
        self.newAct = QtWidgets.QAction("&New", self, shortcut=NULL,
                statusTip="Create a new file", triggered=self.newFile)
        self.closeAct = QtWidgets.QAction("&Close", self, shortcut=NULL,
                statusTip="Close.",triggered = self.closeWindow)
        
        
        self.copyAct = QtWidgets.QAction("&Copy", self, shortcut=NULL,
                statusTip="copy.", triggered = self.copyContent)
            
    def addmenubar(self):
        self.filemenu = self.menuBar().addMenu("&File")
        self.filemenu.addAction(self.newAct)
        self.filemenu.addAction(self.closeAct)
        
        self.Editmenu = self.menuBar().addMenu("&Edit")
        self.Editmenu.addAction(self.copyAct)
        
        self.Aboutmenu = self.menuBar().addMenu("&About")
              
    def newFile(self):
        pass
    def closeWindow(self):
        pass    
    
    def copyContent(self):
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
