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
from functools import partial

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
import json
from xls2xlsx import XLS2XLSX
import openpyxl
from openpyxl.styles import PatternFill, Color

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
class NumericItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
        return ((self.data(QtCore.Qt.UserRole)) <
                (other.data(QtCore.Qt.UserRole)))
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        file = open('variables.json')
        self.data = json.load(file)
        print(self.data["file"])
        self.tempaddr = self.data["file"]  # "G:\\FIles\\Products\\Product Test.xlsx"
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.flag_generate_factorys = True

        global widgets
        widgets = self.ui
        for col in range(5):
            item = widgets.tableWidget.item(0, col)
            item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
        self.keys = []
        self.values = []
        self.a_number_column = 0
        self.havetb_column = 2
        self.stock_column = 3
        self.dictionary = dict()
        self.dictionary_all_values = dict()
        self.dict_values_factory = []
        self.firstTable = False
        self.secondTable = False
        self.current_page = "home"
        self.set_factorys  = set()

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        self.Must_have()
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        description = "Westa GmbH Product control"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        self.end_non_empty = -1
        self.dictionary_factorys = {}
        self.keys_for_dict = []
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        widgets.toggleLeftBox.clicked.connect(lambda: self.openCloseLeftBox(self.current_page))
        widgets.extraCloseColumnBtn.clicked.connect(lambda: self.openCloseLeftBox(self.current_page))
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
        widgets.pushButton.clicked.connect(self.buttonClick)
        widgets.btn_export.clicked.connect(self.buttonClick)
        widgets.button_select.clicked.connect(self.buttonClick)
        widgets.button1.clicked.connect(self.buttonClick)
        widgets.button2.clicked.connect(self.buttonClick)
        widgets.button3.clicked.connect(self.buttonClick)
        widgets.button4.clicked.connect(self.buttonClick)
        widgets.button5.clicked.connect(self.buttonClick)
        widgets.button6.clicked.connect(self.buttonClick)
        widgets.button7.clicked.connect(self.buttonClick)
        widgets.button8.clicked.connect(self.buttonClick)
        widgets.button9.clicked.connect(self.buttonClick)
        widgets.button10.clicked.connect(self.buttonClick)
        widgets.btn_global.clicked.connect(self.buttonClick)
        widgets.button_reset.clicked.connect(self.buttonClick)
        self.buttonarray = [widgets.button1, widgets.button2, widgets.button3, widgets.button4,
                         widgets.button5, widgets.button6, widgets.button7, widgets.button8, widgets.button9, widgets.button10]
        self.sorting_design(widgets.button8)
        self.already_created = False

        self.another_dict = {}
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
        self.array_keys = [4]
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
        self.option = "global"
        # self.TableSorting(widgets.tableWidget, 'DESC', 3, "global")


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    def sorting_design(self, button):
            btnName = button.objectName()
            num = 0
            if "Asc" in btnName:
                num = int(btnName[-1]) * 2 - 1
            elif "Desc" in btnName:
                num = int(btnName[-1]) * 2 - 2
            self.buttonarray[num].setStyleSheet("""
                    """)
            button.setStyleSheet("background-color: #ff79c6;")

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.current_page = "home"
            self.Must_have()

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            if self.dictionary == {} or self.firstTable==False:
                self.LoadExcel(widgets.tableWidget)
                self.firstTable = True
            self.current_page = "widgets"
            self.Must_have()

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            # if self.dictionary.keys() == {}:
            if self.secondTable == False:
                self.LoadExcel(widgets.tableWidgetSecond)
                self.secondTable=True
            self.current_page = "new"
            self.Must_have()

        if btnName == "btn_save":
            print("Save BTN clicked!")
        if btnName == "pushButton1":
            self.OpenExcelFile()
        if btnName == "btn_export":
            self.Export_Rows()
        if btnName == "btn_select":
            selection_range = widgets.tableWidget.selectAll()
        if btnName in ["AscButton1","AscButton2","AscButton3","AscButton4", "AscButton5"] :
            self.sorting_design(btn)
            column = int(btnName[-1])
            if column not in self.array_keys:
                self.TableSorting(widgets.tableWidget, 'Asc', column)
            else:
                self.TableSorting(widgets.tableWidget, 'Asc', column)
                self.reset_button_style(btn)

        if btnName in ["DescButton1", "DescButton2", "DescButton3", "DescButton4", "DescButton5"]:
            self.sorting_design(btn)
            column = int(btnName[-1])
            if column*-1 not in self.array_keys:
                self.TableSorting(widgets.tableWidget, 'Desc', column)
            else:
                self.TableSorting(widgets.tableWidget, 'Desc', column)
                self.reset_button_style(btn)
        if btnName == "btn_reset":
            self.array_keys = [-4]
            self.TableSorting(widgets.tableWidget, 'Desc', 4)
            self.reset_button_style()

        if btnName == "btn_global":
            self.reset_selected_factory()
            self.array_keys=[]
            style = btn.styleSheet()
            btn.setStyleSheet(style + "\n" + "background-color: rgb(29, 34, 38)")
            self.option = "global"
            self.LoadExcel(widgets.tableWidget)
            # self.TableSorting(widgets.tableWidget, 'DESC', 3)


        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    def reset_button_style(self, button = None):
        if button == None:
            for btn in self.buttonarray:
                btn.setStyleSheet("""""")
        else:
            button.setStyleSheet("""""")
    def Must_have(self):
        extraTopMenuLayout = self.ui.extraTopMenu.layout()
        for i in range(extraTopMenuLayout.count()):
            widget = extraTopMenuLayout.itemAt(i).widget()
            # print(widget.objectName() in self.set_factorys)
            if widget.objectName() == 'btn_share':
                widget.setVisible(self.current_page == 'home' )
            elif widget.objectName() == 'btn_more':
                widget.setVisible(self.current_page == 'home' )
            elif widget.objectName() == 'btn_adjustments':
                widget.setVisible(self.current_page == 'home' )
            elif widget.objectName() in list(self.set_factorys) or widget.objectName() == "btn_global":
                widget.setVisible( self.current_page == 'widgets')

        extrapMenuLayout = self.ui.topMenus.layout()
        for i in range(extrapMenuLayout.count()):
            widget = extrapMenuLayout.itemAt(i).widget()
            if widget.objectName() == 'btn_export':
                widget.setVisible(self.current_page == 'widgets')

    def openCloseLeftBox(self, page):
            UIFunctions.toggleLeftBox(self, True, page)
            print(page)

    def search_table(self, search_text):
        if search_text in self.dictionary or search_text.lower() in self.dictionary:
                # show only the row that matches the user input key
                items = widgets.tableWidget.findItems(search_text, QtCore.Qt.MatchExactly)
                row = items[0].row()
                print(row)
                widgets.tableWidget.setCurrentItem(widgets.tableWidget.item(row, 0))
        else:
            widgets.tableWidget.setCurrentItem(widgets.tableWidget.item(0, 0))

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
            self.flag_generate_factorys = True
            self.secondTable=False
            self.LoadExcel(widgets.tableWidget, "global")
            self.data["file"] = self.tempaddr
        with open("variables.json", "w") as outfile:
            outfile.write(json.dumps(self.data, indent=4))
    def LoadExcel(self, widget):

        for row in range(widget.rowCount()):

            for column in range(widget.columnCount()):
                item = widget.item(row, column)
                if item is not None and row!=0:
                    item.setText("")
                    widget.setRowHidden(row, False)
        key2_0 = set()
        # keys_all = []
        if len(self.tempaddr) > 0:
                arr_of_sheets = (openpyxl.load_workbook(self.tempaddr, read_only=True)).sheetnames
                Table = openpyxl.load_workbook(self.tempaddr)
                Sheet = Table[arr_of_sheets[0]]
                a = 0
                for i in Sheet.iter_rows():
                    if (a != 0):
                        key2_0.add(int(i[5].value))
                        self.set_factorys.add(str(i[5].value))
                    a += 1
                for i in key2_0:
                    self.another_dict[i] = []
                a=0

                for i in Sheet.iter_rows():
                    if(a!=0):

                        item2 = QTableWidgetItem()
                        item2.setData(QtCore.Qt.DisplayRole, (int(i[self.havetb_column].value)))

                        self.keys.append(str(i[self.a_number_column].value))
                        self.values.append(str(i[0].value)+" " +str(i[1].value) + " " + str(i[5].value))

                        item4 = QTableWidgetItem()
                        item4.setData(QtCore.Qt.DisplayRole, int(i[self.havetb_column].value)-int(i[self.stock_column].value))

                        diff_num = int(i[self.havetb_column].value)-int(i[self.stock_column].value)
                        item5 = QTableWidgetItem()
                        if diff_num>=0:
                            item5.setData(QtCore.Qt.DisplayRole, int(int(round((diff_num)/10 + 0.5))*10))
                        else :
                            item5.setData(QtCore.Qt.DisplayRole, int(int(round((diff_num) / 10 - 0.5)) * 10))


                        all_values = [str(i[0].value), int(i[2].value), int(i[3].value),diff_num,
                                                                  int(item5.text()), int(i[5].value)]
                        self.keys_for_dict.append(str(i[0].value))
                        self.dict_values_factory.append(all_values)
                        self.another_dict[int(i[5].value)].append(all_values)

                    a+=1

                self.dictionary = dict(zip(self.keys,self.values))
                self.dictionary_all_values = dict(zip(self.keys_for_dict, self.dict_values_factory))
                # self.set_factorys = set(key2_0)
                if self.flag_generate_factorys == True:
                    key2_0 = sorted(key2_0)
                    for i in range(0,len(key2_0)):
                            name = key2_0.pop(0)
                            button = QPushButton(f"{name}")
                            button.setObjectName(f"{name}")
                            button.setMinimumSize(QSize(0, 45))
                            button.setCursor(QCursor(Qt.PointingHandCursor))
                            button.setLayoutDirection(Qt.LeftToRight)
                            button.setStyleSheet(
                                u"background-image: url(images/icons/cil-share-boxed.png);")
                            button.clicked.connect(partial( self.ForButtons,button, widget))
                            widgets.verticalLayout_11.addWidget(button)
                    self.flag_generate_factorys = False

        self.TableSorting(widgets.tableWidget, 'Des', 4)
        # widget.sortItems(3, QtCore.Qt.AscendingOrder, 2, 5)

    def ForButtons(self, button,widget):
        self.array_keys = []
        self.option = button.objectName()
        self.LoadExcel(widget)
        self.Must_have()
        self.reset_selected_factory()
        widgets.btn_global.setStyleSheet((widgets.btn_global.styleSheet()).replace("background-color: rgb(29, 34, 38)", "") )
        self.sorting_design(widgets.button8)
        style = button.styleSheet()
        button.setStyleSheet(style+ "\n"+"background-color: rgb(29, 34, 38)")
    def reset_selected_factory(self):
        for i in self.set_factorys:
            my_button = self.findChild(QtWidgets.QPushButton, i)
            my_button.setStyleSheet(u"background-image: url(images/icons/cil-share-boxed.png);")
    def TableSorting(self, widget, method, sort_column):
        widget.setRowCount(1)
        widget.setRowCount(len(self.dictionary_all_values)+1)
        row_data_list = []

        # self.sorting_design(self.findChild(QtWidgets.QPushButton, method+"Button"+str(sort_column)))


        print(self.array_keys)
        if method == 'Asc':
            sort_column = sort_column
        else:
            sort_column= sort_column*-1

        if sort_column in self.array_keys:
            self.array_keys.remove(sort_column)

        elif sort_column * (-1) in self.array_keys:
            self.array_keys[self.array_keys.index(sort_column * (-1))] = sort_column
        elif sort_column not in self.array_keys:
            self.array_keys.append(sort_column)

        if self.option == "global":
            for row in range(1, len(self.dictionary_all_values)):
                row_data = []
                for col in range(widget.columnCount()):
                        item = list(self.dictionary_all_values.values())[row]
                        # print(item)
                        if item != None and col != 0:
                            row_data.append(int(item[col]))
                        if item != None and col == 0:
                            row_data.append((item[col]))
                if row_data != []:
                    row_data_list.append(row_data)
        else:
            for row in range(1, len(self.another_dict[int(self.option)])):
                row_data = []
                for col in range(widget.columnCount()):
                    # if widget.isRowHidden(row)==False:
                        item = self.another_dict[int(self.option)][row]
                        if item != None and col != 0 :
                            row_data.append(item[col])
                        if item != None and col == 0:
                            row_data.append(item[col])
                if row_data != []:
                    row_data_list.append(row_data)


        row_data_list.sort(key=lambda x: tuple(x[col - 1] if col > 0  else -x[(col*-1) - 1] if col != -1 else int(''.join(filter(str.isdigit, str(x[col*-1 - 1])))) for col in self.array_keys), reverse=True if col==-1  else False)

        for row, row_data in enumerate(row_data_list, 1):
            for col, cell_data in enumerate(row_data):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, cell_data)
                item.setForeground(self.colortype_func(row_data[1], row_data[2]))
                widget.setItem(row, col, item)

        for row in range(widget.rowCount()):
            if row != 0:
                empty = True
                for column in range(widget.columnCount()):
                    item = widget.item(row, column)
                    if item is not None and not item.text().strip() == '':
                        empty = False
                        self.end_non_empty = row
                        break

                widget.setRowHidden(row, empty)

    def colortype_func(self, havetb, stock):
        diff = havetb - stock
        match diff:
            case diff if diff >= 100:
                color = QColor(255, 0, 0)
            case diff if 50 <= diff < 100:
                color = QColor(255, 127, 0)
            case diff if 0 < diff < 50:
                color = QColor(255, 255, 0)
            case diff if (-1 * havetb) <= diff <= 0:
                color = QColor(0, 255, 0)
            case _:
                color = QColor(255, 255, 255)
        return color
    def Export_Rows(self):
        selectionModel = widgets.tableWidget.selectionModel()
        selectedRanges = selectionModel.selectedRows()

        # Create a new workbook
        wb = openpyxl.Workbook()

        # Add a new worksheet
        ws = wb.active
        h = ["Number", "Have to be", "Now we have", "Diff", "Diff up to 10"]
        # ws.append(h)

        # Create a progress dialog
        progressDialog = QProgressDialog("Exporting rows...", "Cancel", 0, len(selectedRanges), self)
        progressDialog.setWindowModality(Qt.WindowModal)
        progressDialog.setValue(0)
        progressDialog.setWindowTitle("Export")
        progressDialog.setCancelButton(None)
        # Export the selected rows to Excel
        realrow = 1
        for i in range (5):
            ws.cell(row=realrow, column=i + 1).fill =PatternFill(patternType='solid', fgColor=Color("538DD5"))
            ws.cell(row=realrow, column=i+1).value = h[i]
        realrow+=1
        for i, r in enumerate(selectedRanges):
            # Update the progress dialog
            progressDialog.setValue(i)
            if progressDialog.wasCanceled():
                break

            # Get the items in the row
            rowItems = [widgets.tableWidget.item(r.row(), c) for c in
                        range(widgets.tableWidget.columnCount())]

            rowValues = []
            c=0
            for item in rowItems:
                if item is None:
                    break
                cellValue = item.text()
                cellForeground = item.foreground()
                # if cellValue =='Number':
                #     break

                # Get the color components
                red = hex(cellForeground.color().red())[2:].upper().zfill(2)
                blue = hex(cellForeground.color().blue())[2:].upper().zfill(2)
                green = hex(cellForeground.color().green())[2:].upper().zfill(2)

                color = red + green + blue
                if color == "000000":
                    color = "538DD5"
                # print(color)
                fill = PatternFill(patternType='solid', fgColor=Color(color))

                ws.cell(row=realrow, column=c + 1).fill = fill
                ws.cell(row=realrow, column=c + 1).value = cellValue
                rowValues.append(cellValue)
                c+=1
            if r.row() == 1:
                continue
            # ws.append(rowValues)
            realrow += 1

        # Close the progress dialog
        progressDialog.setValue(len(selectedRanges))

        # Save the workbook
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Excel file", "", "Excel Files (*.xlsx)", options=options)
        if fileName:
            wb.save(fileName)
    def CellClicked(self, row, column):
        item = widgets.tableWidget.item(row, 0)
        if item is not None and row != 0:
            widgets.plainTextEdit.setPlainText(str(self.dictionary[item.text()]))

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
