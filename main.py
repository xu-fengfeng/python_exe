import sys
from PyQt5 import QtWidgets,QtCore,QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        InputLabel = QtWidgets.QLabel("Input:")
        self.InputLine = QtWidgets.QLineEdit()

        OutputLabel = QtWidgets.QLabel("Output:")
        self.OutputLine =QtWidgets.QLineEdit()

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(InputLabel, 0, 0)
        mainLayout.addWidget(self.InputLine, 0, 1)
        mainLayout.addWidget(OutputLabel, 1, 0, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.OutputLine, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Ex1:Reverse string")
        
if __name__ == '__main__':
    print ("start...")
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    
    sys.exit(app.exec_())
