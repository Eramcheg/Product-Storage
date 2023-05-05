# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from xls2xlsx import XLS2XLSX
import openpyxl
from PySide6 import QtWidgets, QtCore
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.tempaddr = "G:\\FIles\\Products\\Product Test.xlsx"
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.keys = []
        self.values = []
        self.dictionary = dict()
        self.firstTable = False
        self.secondTable = False
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        description = "Westa GmbH Product control"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        widgets.toggleLeftBox.clicked.connect(lambda: self.openCloseLeftBox("home"))
        widgets.extraCloseColumnBtn.clicked.connect(lambda: self.openCloseLeftBox("home"))
        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.tableWidget.cellClicked.connect(self.CellClicked)
        widgets.lineEdit.textChanged.connect(self.search_table)
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.pushButton.clicked.connect(self.buttonClick)
        # EXTRA LEFT BOX


        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.openCloseLeftBox("home")

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            if self.dictionary == {}:
                self.LoadExcel(widgets.tableWidget)
            self.openCloseLeftBox("widgets")

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            # if self.dictionary.keys() == {}:
            if self.secondTable == False:
                self.LoadExcel(widgets.tableWidgetSecond)
                self.secondTable=True
            self.openCloseLeftBox("new")

        if btnName == "btn_save":
            print("Save BTN clicked!")
        if btnName == "pushButton1":
            self.OpenExcelFile()

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def openCloseLeftBox(self, page):
            UIFunctions.toggleLeftBox(self, True, page)

    def search_table(self, search_text):
        if search_text in self.dictionary or search_text.lower() in self.dictionary:
            # self.tableWidget.setRowCount(len(self.dictionary[search_text]))
                # show only the row that matches the user input key
                items = widgets.tableWidget.findItems(search_text, QtCore.Qt.MatchExactly)
                row = items[0].row()
                print(row)
                widgets.tableWidget.setCurrentItem(widgets.tableWidget.item(row, 0))
        else:
            widgets.tableWidget.setCurrentItem(widgets.tableWidget.item(0, 0))
        # for row in range(1, widgets.tableWidget.rowCount()):
        #     # Get the text in the first column of the row
        #     if widgets.tableWidget.item(row, 0) is not None:
        #         name = widgets.tableWidget.item(row, 0).text()
        #         # name = widgets.tableWidget.item(row, 0).text()
        #         # If the search_text is in the name, show the row; otherwise, hide the row
        #         if search_text.lower() in name.lower():
        #             widgets.tableWidget.setRowHidden(row, False)
        #         else:
        #             widgets.tableWidget.setRowHidden(row, True)

    def OpenExcelFile(self):
        # tempdir = filedialog.askopenfilename(initialdir="/", title="Select An Excel File", filetypes=(
        #     ("excel files", "*.xlsx"), ("old excel files", "*.xls"), ("All files", "*.*")))
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Excel Files (*.xlsx *.xls)")
        if dialog.exec() == QDialog.Accepted:
            self.tempaddr = dialog.selectedFiles()[0]
            if self.tempaddr[-3:] == "xls":
                x2x = XLS2XLSX(self.tempaddr)
                x2x.to_xlsx(self.tempaddr + 'x')
                self.tempaddr += 'x'
            self.secondTable=False
            self.LoadExcel(widgets.tableWidget)
    def LoadExcel(self, widget):
            if len(self.tempaddr) > 0:
                arr_of_sheets = (openpyxl.load_workbook(self.tempaddr, read_only=True)).sheetnames
                Table = openpyxl.load_workbook(self.tempaddr)
                Sheet = Table[arr_of_sheets[0]]
                a = 0
                for i in Sheet.iter_rows():
                    # print(i[0].value)
                    if(a!=0):
                        color = QColor(0,0,0)
                        percentage = int(i[2].value)/int(i[1].value) * 100
                        if percentage < 50 :
                            color= QColor(255, 0, 0)
                        elif 50<=percentage<= 80 :
                            color = QColor(255, 127, 0)
                        elif 80<percentage<= 100:
                            color = QColor(0,  255, 0)
                        for j in range(3):

                            item = QTableWidgetItem(str(i[j].value))
                            item.setForeground(color)
                            widget.setItem(a, j, item)
                        # if self.dictionary.keys() == []:
                        self.keys.append(str(i[0].value))
                        self.values.append(i[2].value)
                        item4 = QTableWidgetItem(str(int(i[1].value)-int(i[2].value)))
                        item4.setForeground(color)
                        widget.setItem(a, 3, item4)

                        item5 = QTableWidgetItem(str(int(round((int(i[1].value)-int(i[2].value))/10 + 0.5))*10))
                        item5.setForeground(color)
                        widget.setItem(a, 4, item5)


                    a+=1
                #if self.dictionary.keys() == []:
                self.dictionary = dict(zip(self.keys,self.values))
                print(self.dictionary)

            # print(filepath)

    def CellClicked(self, row, column):
        item = widgets.tableWidget.item(row, column)
        if item is not None:
            widgets.plainTextEdit.setPlainText(item.text())

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
