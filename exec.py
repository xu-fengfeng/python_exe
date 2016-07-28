import os, sys, re

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setTitle("Name")

        layout = QGridLayout()
        self.setLayout(layout)
        
        frame = QFrame()
        frame.setWindowTitle("Frame")
        frame.setLineWidth(5)
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Raised)
        #frame.setFixedSize(150, 150)
        layout.addWidget(frame)
        
        layout2 = QGridLayout()
        frame.setLayout(layout2)
        
        button = QPushButton("action")
        layout2.addWidget(button, 1, 1, 1, 1)
        
        #Slider
        #slider = QSlider(Qt.Vertical)
        self.slider = QSlider(Qt.Horizontal)
        layout.addWidget(self.slider)
        
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setTracking(True)
        self.slider.setValue(30)
        self.slider.setMaximum(80)
        self.slider.valueChanged.connect(self.sliderValueChage)
        
        self.scrollbar = QScrollBar(Qt.Horizontal)
        layout.addWidget(self.scrollbar)
        
        self.scrollarea = QScrollArea()
        layout.addWidget(self.scrollarea)
        
        button1 = QPushButton("ScrollArea")
        labelx = QLabel("ggg")
        labelx.setGeometry(0,0,200,200)

        image = QImage("./ubuntu.jpg")
        labelx.setPixmap(QPixmap.fromImage(image))
        
        self.scrollarea.setAlignment(Qt.AlignCenter)
        self.scrollarea.setWidget(labelx)
        #self.scrollarea.addScrollBarWidget(button1, Qt.AlignBottom)
        #self.scrollarea.AdjustToContents()
        self.scrollarea.setMinimumSize(80,80)
        self.scrollarea.setMaximumSize(180,180)
        
        self.dial = QDial()
        layout.addWidget(self.dial, 3,1)
        self.dial.setMaximum(100)
        self.dial.setMinimum(0)
        #self.dial.setWrapping(False)
        self.dial.setWrapping(True)
        self.dial.setNotchesVisible(True)
        self.dial.setNotchTarget(50)
        
        spinbox = QSpinBox()
        layout.addWidget(spinbox)
        spinbox.setMaximum(80)
        spinbox.setMinimum(30)
        spinbox.setSingleStep(2)
        spinbox.setPrefix("prefix-")
        spinbox.setSuffix("-suffix")
        
        doublespinbox = QDoubleSpinBox()
        layout.addWidget(doublespinbox)
        
        toolbar = QToolBar()
        layout.addWidget(toolbar)
        
        buttonx = QToolButton()
        buttonx.setText("ToolButton x")
        buttonx.setDown(True)
        
        buttony = QToolButton()
        buttony.setText("ToolButton y")
        buttony.setCheckable(True)
        buttony.setAutoExclusive(True)
        
        menu = QMenu()
        
        buttonz = QToolButton()
        buttonz.setText("ToolButton z")
        buttonz.setCheckable(True)
        buttonz.setAutoExclusive(True)
        buttonz.setMenu(menu)
        buttonz.setPopupMode(QToolButton.InstantPopup)
                        
        toolbar.addWidget(buttonx)
        toolbar.addWidget(buttony)
        toolbar.addWidget(buttonz)
        toolbar.addSeparator()
        
        buttona = QToolButton()
        buttona.setText("ToolButton a")
        buttona.setCheckable(False)
        toolbar.addWidget(buttona)
        
        #toolbar.setOrientation(Qt.Vertical)
        toolbar.setOrientation(Qt.Horizontal)
        
        toolbar.setMovable(True)
        toolbar.setFloatable(True)
        
        toolbox = QToolBox()
        layout.addWidget(toolbox)
        
        buttonb = QToolButton()
        toolbox.addItem(buttonb, "buttonb")
        
        labely = QLabel("txxt")
        toolbox.addItem(labely, "tyyyt")   
        
        spinbox5 = QSpinBox()
        layout.addWidget(spinbox5)
        
        spinbox5.setValue(77)
        
        menubar = QMenuBar()
        menubar.setVisible(True)
        menubar.setBackgroundRole(False)
        action = menubar.addAction("quit")
        action1 = menubar.addAction("about")
        menu = menubar.addMenu("File")
        action2 = menu.addAction("Open")
        layout.addWidget(menubar, 0 ,0 )
        
    def toolbar_action(self):
        print ("toolbar action is triggerd.!")    
        
    def sliderValueChage(self):
        value = self.slider.value()
        print ("value=%d"%value)


class MainWindow1(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow1, self).__init__(parent)
        
        self.mainwidgets = QWidget(self)
        self.setCentralWidget(self.mainwidgets)
                
        layout = QGridLayout()
        self.mainwidgets.setLayout(layout)
        toolbar = QToolBar()

        self.addToolBar(toolbar)
        
        buttonx = QToolButton()
        buttonx.setText("ToolButton x")
        buttony = QToolButton()
        buttony.setText("ToolButton y")
        buttony.setCheckable(True)
        buttony.setAutoExclusive(True)
        buttonz = QToolButton()
        buttonz.setText("ToolButton z")
        buttonz.setCheckable(True)
        buttonz.setAutoExclusive(True)                
        toolbar.addWidget(buttonx)
        toolbar.addWidget(buttony)
        toolbar.addWidget(buttonz)
        toolbar.addSeparator()
        
        buttona = QToolButton()
        buttona.setText("ToolButton a")
        buttona.setCheckable(False)
        toolbar.addWidget(buttona)
        
        #toolbar.setOrientation(Qt.Vertical)
        toolbar.setOrientation(Qt.Horizontal)
        
        toolbar.setMovable(True)
        toolbar.setFloatable(True) 


class MainWindow2(QWidget):
    def __init__(self, parent=None):
        super(MainWindow2, self).__init__(parent)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        menubar = QMenuBar()
        filemenu = menubar.addMenu("File")
        layout.addWidget(menubar)
        
        open = filemenu.addAction("Open")
        
        filemenu.addSeparator()
        
        save = filemenu.addAction("Save")
        
        filemenu.addSection("Section")
        exit = filemenu.addAction("Quit")
        
        filemenu.setTearOffEnabled(True)
        
        runmenu = menubar.addMenu("Run")
        runasmenu = runmenu.addMenu("Run As")
        
        #runmenu.setTitle("RUNMENU")
        
        tabwidget = QTabWidget()
        layout.addWidget(tabwidget, 1, 0)
        label1 = QLabel("label1")
        label2 = QLabel("label2")
        tabwidget.addTab(label1, "Tab1")
        tabwidget.addTab(label2, "Tab2")
        tabwidget.setTabEnabled(1, False)
        tabwidget.setMovable(True)
        tabwidget.setTabsClosable(True)
        tabwidget.setTabPosition(QTabWidget.West)
        
        
        self.tabbar = QTabBar()
        layout.addWidget(self.tabbar, 2,0)
        index = self.tabbar.addTab("Tabbar1")
        print("index=",index)
        index = self.tabbar.addTab("Tabbar2")
        print("index=",index)
        index = self.tabbar.insertTab(1, "TabbarX")
        print("index=",index)
        index = self.tabbar.insertTab(5, "TabbarY")
        print("index=",index)
        self.tabbar.setMovable(True)
        self.tabbar.setTabEnabled(2, False)
        self.tabbar.setTabsClosable(True)
        self.tabbar.tabCloseRequested[int].connect(self.removetab)
        
        self.stackedwidget = QStackedWidget()
        layout.addWidget(self.stackedwidget,3, 0)
        
        for x in range(1, 4):
            label = QLabel("Label%x"%x)
            self.stackedwidget.addWidget(label)
            
            button = QPushButton("Stack %i" % (x))
            button.page = x
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button, x+3, 0)

        self.combobox = QComboBox()
        self.combobox.addItem("abc")
        self.combobox.addItems(["def", "ghi", "jkl"])
        self.combobox.insertItem(3, "xyz")
        self.combobox.insertItems(1,["ccc", "ddd", "eee"])
        
        self.combobox.currentIndexChanged.connect(self.onComboboxItemChange)
        
        self.combobox.setEditable(True)
        
        lineedit = QLineEdit()
        
        self.combobox.setLineEdit(lineedit)
        
        self.combobox.setInsertPolicy(QComboBox.InsertAtBottom)
   
        name = QCompleter(["aaa","abc", "bbb", "ccc", "ddd", "eee"])
        self.combobox.setCompleter(name)
        #self.combobox.setModel()
        
        layout.addWidget(self.combobox, 8, 0, 1 ,1)
    
        lineedit1 = QLineEdit()
        layout.addWidget(lineedit1, 9,0,1,1)
        completer = QCompleter(["aaa","abc", "bbb", "ccc", "ddd", "eee"])
        completer.setCompletionMode(QCompleter.PopupCompletion)
        
        lineedit1.setCompleter(completer)
        #lineedit1.completer.setModel()
        
        calendar = QCalendarWidget()
        layout.addWidget(calendar, 10, 0, 1, 1)
        #calendar.showToday()
        #calendar.showNextYear()
        calendar.setDateEditEnabled(False)
        calendar.isGridVisible()
        calendar.setGridVisible(True)
        calendar.setNavigationBarVisible(False)
        calendar.showMinimized()
        
        
        dateedit = QDateEdit()
        layout.addWidget(dateedit, 17, 0, 1, 1)
        
        timeedit=QTimeEdit()
        layout.addWidget(timeedit, 18, 0, 1, 1)
        
        time = QTime()
        time.setHMS(12, 29, 0)
        timeedit.setTime(time)
        
        datetimeedit = QDateTimeEdit()
        layout.addWidget(datetimeedit, 19,0, 1, 1)
        
        calendarwidget = QCalendarWidget()
        datetimeedit.setCalendarWidget(calendarwidget)
        datetimeedit.setCalendarPopup(True)

        buttonf = QPushButton("file Dialog")
        buttonf.clicked.connect(self.onOpenFileDialog)
        layout.addWidget(buttonf)
  
        self.fontdialog = QFontDialog(self)
        
        buttonx = QPushButton("font Dialog")
        buttonx.clicked.connect(self.onOpenFontDialog)
        layout.addWidget(buttonx)
        
        self.fontcombobox = QFontComboBox()
        self.fontcombobox.setFontFilters(QFontComboBox.MonospacedFonts)
        layout.addWidget(self.fontcombobox)
    
    def onOpenFileDialog(self):
        filedialog = QFileDialog(self)
        filedialog.setViewMode(QFileDialog.List)
        filedialog.setAcceptMode(QFileDialog.AcceptOpen)
        #filedialog.setAcceptMode(QFileDialog.AcceptSave)
        filedialog.setLabelText(QFileDialog.FileName, "xcx")
        filedialog.setDefaultSuffix("jpg")
        #filedialog.show()
        filename, x = filedialog.getOpenFileName(self)
        print("file %s is opened %r"%(filename, x)) 
        
        
    def onOpenFontDialog(self):
        self.fontdialog.show()
        font = self.fontdialog.currentFont()
        print("current font =%s"%font.family())
        self.fontdialog.fontSelected.connect(self.onPrintCurrentFont)
    def onPrintCurrentFont(self):
        font = self.fontdialog.selectedFont()
        print("font = %s"%font.family())
        self.fontdialog.setCurrentFont(font)
        options = self.fontdialog.options()
        print ("option = %r"%options)
        self.setFont(font)
        self.fontcombobox.setCurrentFont(font)
        
    def onComboboxItemChange(self):
        print(self.combobox.currentText())        

    def on_button_clicked(self):
        button = self.sender()
        self.stackedwidget.setCurrentIndex(button.page - 1)    
    def removetab(self, index):    
        print ("removetab[%d] is triggerd."%index)
        self.tabbar.removeTab(index)

class MainWindow3(QWidget):
    def __init__(self, parent=None):
        super(MainWindow3, self).__init__(parent)
        
        layout = QFormLayout()
        self.setLayout(layout)
        
        button1 = QPushButton("B1")
        layout.addRow("label1", button1)
        
        button2 = QPushButton("B2")
        layout.addRow("label2", button2)
        
        button3 = QPushButton("B3")
        layout.insertRow(1,"label3", button3)
        
        layout.setVerticalSpacing(50)
        layout.setHorizontalSpacing(10)
        
        layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        #layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        #layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        
#class Dialog(QWidget): 
class Dialog(QDialog):       
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)
        
        label = QLabel("This is a dialog")
        layout.addWidget(label, 0, 0)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttonBox)
        
        self.setSizeGripEnabled(True)
        
 
class MainWindow4(QWidget):
    def __init__(self, parent=None):
        super(MainWindow4, self).__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)
        button = QPushButton("Color")
        button.clicked.connect(self.onColorDialog)
        layout.addWidget(button, 0, 0, 1, 1)
    
        self.label = QLabel("Color")
        layout.addWidget(self.label, 0, 1, 1, 2)
        
        self.listwidget = QListWidget()
        layout.addWidget(self.listwidget, 1, 0)
        self.listwidget.addItems(["a", "b", "c", "d"])
        self.listwidget.insertItem(2, "2")
        
        item = self.listwidget.item(3)
        print("item3.text=%s"%item.text())
        self.listwidget.editItem(item)
        self.listwidget.setCurrentRow(1)
    
        
        listwidgetitem = QListWidgetItem()
        listwidgetitem.setText("abcde")
        content = listwidgetitem.text()
        print("content = %s"%content)
        
        
        listwidgetitem1 = listwidgetitem.clone()
        listwidgetitem1.setText("ABCDE")
        
        self.listwidget.addItem(listwidgetitem)
        self.listwidget.addItem(listwidgetitem1)
    
        listwidgetitem.setHidden(False)
    
        self.listwidget.clicked.connect(self.listwidgetclicked)
        self.listwidget.itemClicked.connect(self.listwidgetitemclicked)
        
        button1 = QPushButton("&Sort")
        layout.addWidget(button1, 2, 0)
        button1.clicked.connect(self.onListWidgetSort)
    
        tablewidget = QTableWidget()
        layout.addWidget(tablewidget, 1, 1)
        
        tablewidget.setRowCount(5)
        tablewidget.setColumnCount(3)
        tablewidget.setShowGrid(True)
        
        tablewidget.setHorizontalHeaderLabels(["x", "xx", "xxx"])
        tablewidget.setVerticalHeaderLabels(["y", "yy", "yyy"])
        #tablewidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        #tablewidget.setSelectionMode(QAbstractItemView.MultiSelection)
        #tablewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        tablewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #tablewidget.setEditTriggers(QAbstractItemView.SelectedClicked)
        tablewidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        
        x = tablewidget.horizontalHeader()
        print ("type x = %r"%type(x))
    
        columnview = QColumnView()
        layout.addWidget(columnview, 2, 0, 10, 1)
        columnview.setResizeGripsVisible(True)
        columnview.setColumnWidths([30,30,30,30])
        
        model = QDirModel()
        columnview.setModel(model)
    
        scrollarea = QScrollArea()
        layout.addWidget(scrollarea, 2, 1)
        
        labelx = QLabel()
        
        #image = QImage("Wikipedia-logo-v2.png")
        #self.imageLabel.setPixmap(QPixmap.fromImage(image))
        labelx.setPixmap(QPixmap.fromImage(QImage("IMG_0030.JPG")))
        scrollarea.setWidget(labelx)
        
        scrollarea.setAlignment(Qt.AlignBottom|Qt.AlignRight)
        scrollarea.setWidgetResizable(True)
    
    def listwidgetitemclicked(self):
        item = self.listwidget.currentItem()
        print("ITEM %s is clicked"%item.text())
            
    def listwidgetclicked(self):
        item = self.listwidget.currentItem()
        print("item %s is clicked"%item.text())
        
    def onListWidgetSort(self):
        self.listwidget.sortItems(Qt.DescendingOrder)
        
    def onColorDialog(self):
        self.colordialog = QColorDialog(self)
        self.colordialog.currentColorChanged.connect(self.onColorChanged)
        self.colordialog.colorSelected.connect(self.onColorSelected)
        self.colordialog.open()
    def onColorChanged(self):
        color = self.colordialog.selectedColor()
        print("color %s is changed"%color.name())
    def onColorSelected(self):
        color = self.colordialog.currentColor()
        self.label.setText("color %s is selected"%color.name())
        print("color %s is selected"%color.name())

class MainWindow5(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow5, self).__init__(parent)
        
        widget = QWidget()
        self.setCentralWidget(widget)
        
        layout = QGridLayout()
        widget.setLayout(layout)
        
        self.plaintextedit = QPlainTextEdit()
        layout.addWidget(self.plaintextedit, 0, 0, 2, 10)
        
        self.plaintextedit.setReadOnly(False)
        #plaintextedit.appendPlainText("append something")
        
        self.plaintextedit.setPlaceholderText("input something...")
        button1 = QPushButton("Insert")
        button2 = QPushButton("Append")
        button3 = QPushButton("Show")
        layout.addWidget(button1, 2, 0)
        layout.addWidget(button2, 2, 1)
        layout.addWidget(button3, 2, 2)
        
        button1.clicked.connect(self.str_insert)
        button2.clicked.connect(self.str_append)

        button3.clicked.connect(self.get_all_content)
        
        self.plaintextedit.setDocumentTitle("xxx")
        title = self.plaintextedit.documentTitle()
        print("plaintextedt.title =%s"%title)
        
        
        
    def get_all_content(self):
        content = self.plaintextedit.toPlainText()
        print ("content = %s"%content)
    def str_append(self):
        self.plaintextedit.appendPlainText("append word.")
    def str_insert(self):
        self.plaintextedit.insertPlainText("insert word.")


class MainWindow6(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow6, self).__init__(parent)
        
        widget = QWidget()
        self.setCentralWidget(widget)
        
        layout = QGridLayout()
        widget.setLayout(layout)
        
        self.textedit = QTextEdit()
        self.textedit.setReadOnly(False)
        self.textedit.setPlaceholderText("input something...")
        self.textedit.setMaximumHeight(100)
                
        layout.addWidget(self.textedit, 0, 0, 2, 3)

        button = QPushButton("paste")
        layout.addWidget(button, 0, 3, 1, 1)
        
        #button = QPushButton("paste2")
        #layout.addWidget(button, 1, 3, 1, 1)
                
        button1 = QPushButton("Insert")
        button2 = QPushButton("Append")
        button3 = QPushButton("Show")
        layout.addWidget(button1, 2, 0)
        layout.addWidget(button2, 2, 1)
        layout.addWidget(button3, 2, 2)
        
        button1.clicked.connect(self.str_insert)
        button2.clicked.connect(self.str_append)

        button3.clicked.connect(self.get_all_content)
        
        self.textedit.setDocumentTitle("xxx")
        title = self.textedit.documentTitle()
        print("textedit.title =%s"%title)
        
        button4 = QPushButton("Overwrite")
        layout.addWidget(button4, 3, 0)
        button4.clicked.connect(self.overrite_content)
        
        button5 = QPushButton("Overwrite")
        layout.addWidget(button5, 3, 1)
        button4.clicked.connect(self.linewrapmode)
                 
        button6 = QPushButton("Message")
        layout.addWidget(button6, 3, 2)
        button6.clicked.connect(self.showMessage)
        
    def showMessage(self):
        message = QMessageBox(self)
        message.setText("MessageBox Show.")
        
        message.setInformativeText("ggggggxg")
        
        message.setStandardButtons(QMessageBox.Save |QMessageBox.Open)
        
        button = QPushButton("nxc")
        message.addButton(button, QMessageBox.ActionRole)
        
        image = QImage("./ubuntu.jpg")
        message.setIconPixmap(QPixmap.fromImage(image))
        
        message.show()               
    def linewrapmode(self):
        self.textedit.setLineWrapMode(False)
               
    def overrite_content(self):
        self.textedit.setOverwriteMode(True)
        self.textedit.insertPlainText("overwrite string")

    def get_all_content(self):
        content = self.textedit.toPlainText()
        print ("content = %s"%content)
    def str_append(self):
        self.textedit.append("append word.")
    def str_insert(self):
        self.textedit.insertPlainText("insert word.")



class MainWindow7(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow7, self).__init__(parent)
        
        widget = QWidget()
        self.setCentralWidget(widget)
        
        layout = QGridLayout()
        widget.setLayout(layout)
        
        icon = QIcon("ubuntu.jpg")
        if icon.isNull():
            print ("icon is null")
        else:
            print ("icon is not null")
        #icon.addFile("qt-logo.png")
        #image = QImage("./ubuntu.jpg")
        #icon.addPixmap(QPixmap.fromImage(image))
        
        button = QPushButton(icon, "start")
        
        layout.addWidget(button)
        
        button.clicked.connect(self.wizardstart)
        
        self.wizard = QWizard()
        
        self.setWindowTitle("py_texteditor")
        self.setWindowIcon(icon)
        
        #layout.addWidget(icon, 1, 0)
    
    
        for i in range(0,5):
            wizardpage = QWizardPage()
            wizardpage.setTitle("Page-%d"%i)
            self.wizard.addPage(wizardpage)
    
        page = self.wizard.page(2)
        page.setCommitPage(True)
        
        
        page = self.wizard.page(3)
        page.setFinalPage(True)     
        
        time = QTime(23, 23, 0, 0)        
        time1 = QTime(23, 22, 0, 0)
        x = time.secsTo(time1)
        print("x=%d"%x)        
        y = time.msecsTo(time1)
        print ("y=%d"%y)

        timeedit = QTimeEdit(time)
        layout.addWidget(timeedit, 1, 1)

        date = QDate(2016,7,24)
        
        self.dateedit = QDateEdit(date)
        layout.addWidget(self.dateedit, 1, 0)        
        
        buttonx = QPushButton("sync")
        layout.addWidget(buttonx, 2, 1)
        buttonx.clicked.connect(self.dateSync)   

        self.dateedit2 = QDateEdit()
        layout.addWidget(self.dateedit2, 2, 0)
        
        dir = QDir()
        path = QDir.currentPath()
        print("path = ", path)
        
        path = QDir.absolutePath(dir)
        print("path = ", path)
        
        path = QDir.canonicalPath(dir)
        print("path = ", path)
        
        dirname = QDir.dirName(dir)
        print("name = %s"%dirname)
        
        dir.cdUp()
        path = QDir.canonicalPath(dir)
        print("path = ", path)
        
        dirname = QDir.dirName(dir)
        print("name = %s"%dirname) 
        
        s = QDir.entryList(dir)
        print("info = %s"%s)
        
    def dateSync(self):
        date = self.dateedit.date()
        datestr = date.toString("yyyy.MM.dd")
        print(datestr)
        
        date2 = QDate.fromString(datestr, "yyyy.MM.dd")
        
        day = date2.day()
        print("day = %d"%day)
        
        self.dateedit2.setDate(date2)
        
    def wizardstart(self):
        self.wizard.open()


#pixmap = QPixmap("./geometry.GIF")

#splashscreen = QSplashScreen(pixmap)
#splashscreen.show()

#style = QStyle()
        
app =QApplication(sys.argv)
app.setStyle(QStyleFactory.create("Fusion"))

mainwindow = MainWindow6()
#mainwindow = Dialog()

#splashscreen.finish(mainwindow)

mainwindow.show()

sys.exit(app.exec_()) 
