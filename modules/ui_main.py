# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingnxZcz.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import *
from PySide6.QtCharts import QChart, QChartView, QPieSeries

from . resources_rc import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from pychartdir import *
# import plotly.graph_objs as go
# import plotly.offline as pyo
import pyqtgraph as pg
import pyqtgraph.opengl as gl
# class Splitter(QSplitter):
#     def __init__(self, *args, **kwargs):
#         super(Splitter, self).__init__(*args, **kwargs)
#         self.min_orange = QColor(51, 33, 0).getRgbF()[:3]
#         self.max_orange = QColor(255, 165, 0).getRgbF()[:3]
#         self.min_red = QColor(51, 0, 0).getRgbF()[:3]
#         self.max_red = QColor(255, 165, 0).getRgbF()[:3]
#         self.min_yellow = QColor(51, 51, 0).getRgbF()[:3]
#         self.max_yellow = QColor(255, 255, 0).getRgbF()[:3]
#         self.min_green = QColor(0, 51, 0).getRgbF()[:3]
#         self.max_green = QColor(0, 255, 0).getRgbF()[:3]
#         self.min_white = QColor(51, 51, 51).getRgbF()[:3]
#         self.max_white = QColor(255, 255, 255).getRgbF()[:3]
#         self.labelHello = QLabel(self)
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.labelHello)
#     def mousePressEvent(self, event):
#         print('fewfewf')
#         # Get the global mouse position
#         globalPos = QCursor.pos()
#
#         # Create a QPixmap, and render the screen content into it
#         screen = QApplication.primaryScreen()
#         if screen is not None:
#             pixmap = screen.grabWindow(0, globalPos.x(), globalPos.y(), 1, 1)
#         else:
#             return
#
#         # Get the color of the pixel under the mouse cursor
#         color = QColor(pixmap.toImage().pixelColor(0, 0)).getRgbF()[:3]
#
#         if color[0] == color[1] == color[2]:  # white
#             if self.is_white(color):
#                 self.labelHello.setText('White')
#
#         elif color[0] == color[1] != 0 and color[2] == 0:  # yellow
#             if self.is_yellow(color):
#                 self.labelHello.setText('Yellow')
#         elif color[1] == color[2] == 0 and color[0] != 0:  # red
#             if self.is_red(color):
#                 self.labelHello.setText('Red')
#
#         elif color[1] != 0 and color[0] == color[2] == 0:  # green
#             if self.is_green(color):
#                 self.labelHello.setText('Green')
#
#         elif color[1] != color[0] and color[1] != 0 and round(color[0] / color[1], 2) == 1.55:
#             if self.is_orange(color):
#                 self.labelHello.setText('Orange')
#         else:
#             self.labelHello.setText('')
#
#         # Check if the color is within the range of orange
#         # if self.is_orange(color):
#         #     self.label.setText('Orange')
#         # else:
#         #     self.label.setText('')
#         # print("SOM")
#         super().mouseMoveEvent(event)
#
#     def is_orange(self, color):
#         return all(self.min_orange[i] <= color[i] <= self.max_orange[i] for i in range(3))
#
#     def is_yellow(self, color):
#         return all(self.min_yellow[i] <= color[i] <= self.max_yellow[i] for i in range(3))
#
#     def is_red(self, color):
#         return all(self.min_red[i] <= color[i] <= self.max_red[i] for i in range(3))
#
#     def is_green(self, color):
#         return all(self.min_green[i] <= color[i] <= self.max_green[i] for i in range(3))
#
#     def is_white(self, color):
#         return all(self.min_white[i] <= color[i] <= self.max_white[i] for i in range(3))
class MyGLViewWidget(gl.GLViewWidget):
    def wheelEvent(self, ev):
        ev.ignore()
    def mouseMoveEvent(self, ev):
        return  # Ignore all mouse moves
class CustomTableWidget(QTableWidget):
    def __init__(self, *args, **kwargs):
        super(CustomTableWidget, self).__init__(*args, **kwargs)

    def sortItems(self, column, order=Qt.AscendingOrder):
        # Create a list of all rows except the first one
        rows_data = []
        for row in range(1, self.rowCount()):
            row_data = []
            for col in range(self.columnCount()):
                if self.item(row, col) is not None:
                    row_data.append(self.item(row, col).text())
            rows_data.append(row_data)

        # Sort the rows data based on the specified column
        rows_data.sort(key=lambda x: x[column], reverse=order == Qt.DescendingOrder)

        # Re-populate the table with the sorted rows
        for row, row_data in enumerate(rows_data, start=1):
            for col, item_text in enumerate(row_data):

                self.setItem(row, col, QTableWidgetItem(item_text))


class Ui_MainWindow(object):
    def on_button_clicked(self):
        print("HEllo")


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(images/images/diamond.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
# "	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
# "	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
# "	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(images/icons/cil-catalog.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(images/icons/cil-dollar.png);")

        self.verticalLayout_8.addWidget(self.btn_new)




        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        # self.scrbarea = QScrollArea(self.extraContent)
        # self.scrbarea.setObjectName(u"scrollArea")
        # self.scrbarea.setStyleSheet(u" QScrollBar:vertical {\n"
        #                               "    background: rgb(52, 59, 72);\n"
        #                               " }\n"
        #                               " QScrollBar:horizontal {\n"
        #                               "    background: rgb(52, 59, 72);\n"
        #                               " }")
        # self.scrbarea.setFrameShape(QFrame.NoFrame)
        # self.scrbarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scrbarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # self.scrbarea.setWidgetResizable(True)
        # self.scrollAreaWidgetContents = QWidget()
        # self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        # self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        # self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
        #                                             "	border: none;\n"
        #                                             "    background: rgb(52, 59, 72);\n"
        #                                             "    width: 14px;\n"
        #                                             "    margin: 21px 0 21px 0;\n"
        #                                             "	border-radius: 0px;\n"
        #                                             " }")
        # self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        # self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")
        # self.verticalScrollBar = QScrollBar(self.extraTopMenu)
        # self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        # self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
        # " QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        # self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.verticalLayout_11.addWidget(self.btn_share)


        # self.verticalLayout_11.addWidget(self.verticalScrollBar)


        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)

        self.btn_global = QPushButton(self.extraTopMenu)
        self.btn_global.setObjectName(u"btn_global")
        sizePolicy.setHeightForWidth(self.btn_global.sizePolicy().hasHeightForWidth())
        self.btn_global.setSizePolicy(sizePolicy)
        self.btn_global.setMinimumSize(QSize(0, 45))
        self.btn_global.setFont(font)
        self.btn_global.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_global.setLayoutDirection(Qt.LeftToRight)
        self.btn_global.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_global)




        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        # self.home.setStyleSheet(u"background-image: url(images/images/logo_oliverweber.png);\n")
# "background-position: center;\n"
# "background-repeat: no-repeat;")

        self.verticalLayout111 = QVBoxLayout(self.home)
        self.verticalLayout111.setSpacing(10)
        self.verticalLayout111.setObjectName(u"verticalLayout111")
        self.verticalLayout111.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout111.setAlignment(Qt.AlignCenter)
        self.logo = QLabel()
        self.logo.setFixedSize(500,154)
        self.logo.setScaledContents(True)
        self.logo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.logo.setStyleSheet(u"background-image: url(images/images/logo_oliverweber.png);\n")
        self.verticalLayout111.addWidget(self.logo)
        self.widg = QWidget()
        self.lay = QVBoxLayout(self.widg)
        # self.inner_layout = QVBoxLayout(self.widg)
        # self.auth_list = QListWidget(self.widg)
        # self.auth_list.setStyleSheet("background-color: #252930; border: none;")
        # self.auth_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_auth = QLabel("Authorization\n")
        self.label_auth.setStyleSheet("font-family: Arial; font-size: 26px;")
        self.label_auth.setGeometry(50, 50, 200, 30)
        self.label_auth.setAlignment(Qt.AlignCenter)


        self.buttonTABLES = QPushButton('TABLES')
        self.buttonPIE = QPushButton('FACTORIES')
        self.buttonTABLES.setObjectName(u"tablesButton")
        self.buttonTABLES.setMinimumSize(QSize(150, 100))
        self.buttonTABLES.setFont(font)
        self.buttonTABLES.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonTABLES.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        icon4_ = QIcon()
        icon4_.addFile(u"images/icons/cil-catalog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTABLES.setIcon(icon4_)
        self.buttonPIE.setObjectName(u"PIEbutton")
        self.buttonPIE.setMinimumSize(QSize(150, 100))
        self.buttonPIE.setFont(font)
        self.buttonPIE.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonPIE.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        icon_ = QIcon()
        icon_.addFile(u"images/icons/cil-dollar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonPIE.setIcon(icon_)



        self.username_input = QLineEdit()
        self.username_input.setGeometry(100, 100, 100, 30)
        self.username_input.setObjectName(u"usernameEdit")
        self.username_input.setMinimumSize(QSize(0, 30))
        self.username_input.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.username_input.setFixedWidth(300)
        self.username_input.setAlignment(Qt.AlignCenter)
        self.password_input = QLineEdit()
        self.password_input.setObjectName(u"passwordEdit")
        self.password_input.setMinimumSize(QSize(0, 30))
        self.password_input.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedWidth(300)
        self.password_input.setAlignment(Qt.AlignCenter)

        self.login_button = QPushButton('Login')
        self.login_button.setObjectName(u"loginButton")

        self.login_button.setMinimumSize(QSize(150, 30))
        self.login_button.setFont(font)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.labelLogin = QLabel('Username: ')
        self.labelLogin.setStyleSheet("font-family: Arial; font-size: 18px;")
        self.labelLogin.setGeometry(50, 50, 200, 30)
        self.labelLogin.setAlignment(Qt.AlignCenter)
        self.labelPassword = QLabel('Password: ')
        self.labelPassword.setStyleSheet("font-family: Arial; font-size: 18px;")
        self.labelPassword.setGeometry(50, 50, 200, 30)
        self.labelPassword.setAlignment(Qt.AlignCenter)
        self.lay.addWidget(self.label_auth)
        self.lay.addWidget(self.buttonTABLES)
        self.lay.addWidget(self.buttonPIE)
        self.lay.addWidget(self.labelLogin)
        self.lay.addWidget(self.username_input)
        self.lay.addWidget(self.labelPassword)
        self.lay.addWidget(self.password_input)
        self.lay.addWidget(self.login_button)
        self.lay.setAlignment(Qt.AlignCenter)
        self.widg.setStyleSheet("background-color: #252930; border-radius:50%;")
        self.widg.setFixedSize(500, 500)

        self.verticalLayout111.addWidget(self.widg)

        # self.navigation_home_buttons = QWidget()
        # self.layout_navigation = QHBoxLayout(self.navigation_home_buttons)


        # self.layout_navigation.addWidget(self.buttonTABLES)
        # self.layout_navigation.addWidget(self.buttonPIE)
        # self.navigation_home_buttons.setLayout(self.layout_navigation)
        # self.verticalLayout111.addWidget(self.navigation_home_buttons)









        # self.verticalLayout111.addWidget(self.gl_view_widget)
        self.home.setLayout(self.verticalLayout111)
        self.stackedWidget.addWidget(self.home)
        # self.stackedWidget.addWidget(self._chart_view)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton1")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        # self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        # self.labelVersion_3.setObjectName(u"labelVersion_3")
        # self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        # self.labelVersion_3.setLineWidth(1)
        # self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        #
        # self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        # self.checkBox = QCheckBox(self.row_2)
        # self.checkBox.setObjectName(u"checkBox")
        # self.checkBox.setAutoFillBackground(False)
        # self.checkBox.setStyleSheet(u"")
        #
        # self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        # self.radioButton = QRadioButton(self.row_2)
        # self.radioButton.setObjectName(u"radioButton")
        # self.radioButton.setStyleSheet(u"")


        # self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        # self.verticalSlider = QSlider(self.row_2)
        # self.verticalSlider.setObjectName(u"verticalSlider")
        # self.verticalSlider.setStyleSheet(u"")
        # self.verticalSlider.setOrientation(Qt.Vertical)
        #
        # self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

#         self.verticalScrollBar = QScrollBar(self.row_2)
#         self.verticalScrollBar.setObjectName(u"verticalScrollBar")
#         self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
# " QScrollBar:horizontal { background: rgb(52, 59, 72); }")
#         self.verticalScrollBar.setOrientation(Qt.Vertical)
#
#         self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)
        self.labelImage = QLabel()
        self.labelImage.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align the label to the top

        self.horizontalLayout_11.addWidget(self.labelImage)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        # self.comboBox = QComboBox(self.row_2)
        # self.comboBox.addItem("")
        # self.comboBox.addItem("")
        # self.comboBox.addItem("")
        # self.comboBox.setObjectName(u"comboBox")
        # self.comboBox.setFont(font)
        # self.comboBox.setAutoFillBackground(False)
        # self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        # self.comboBox.setIconSize(QSize(16, 16))
        # self.comboBox.setFrame(True)
        #
        # self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

#         self.horizontalScrollBar = QScrollBar(self.row_2)
#         self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
#         sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
#         self.horizontalScrollBar.setSizePolicy(sizePolicy)
#         self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
# " QScrollBar:horizontal { background: rgb(52, 59, 72); }")
#         self.horizontalScrollBar.setOrientation(Qt.Horizontal)
#
#         self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        # self.commandLinkButton = QCommandLinkButton(self.row_2)
        # self.commandLinkButton.setObjectName(u"commandLinkButton")
        # self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        # self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.commandLinkButton.setIcon(icon5)

        # self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        # self.horizontalSlider = QSlider(self.row_2)
        # self.horizontalSlider.setObjectName(u"horizontalSlider")
        # self.horizontalSlider.setStyleSheet(u"")
        # self.horizontalSlider.setOrientation(Qt.Horizontal)

        # self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)
        self.container1 = QWidget()
        layout = QHBoxLayout(self.container1)
        layout.setAlignment(Qt.AlignRight )
        # self.label01 = QLabel()
        self.label1 = QLabel("")
        self.button1 = QPushButton()
        self.button2 = QPushButton()


        self.button1.setObjectName(u"AscButton1")
        self.button1.setFixedSize(QSize(30, 30))
        self.button1.setFont(font)
        self.button1.setCursor(QCursor(Qt.PointingHandCursor))
        self.button2.setObjectName(u"DescButton1")
        self.button2.setFixedSize(QSize(30, 30))
        self.button2.setFont(font)
        self.button2.setCursor(QCursor(Qt.PointingHandCursor))
        # self.button1.setStyleSheet((u"background-image: url(images/icons/cil-desc.png);"))
        # self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        icon4_1 = QIcon()
        icon4_1.addFile(u"images/icons/cil-asc.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4_2 = QIcon()
        icon4_2.addFile(u"images/icons/cil-desc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button1.setIcon(icon4_1)
        self.button2.setIcon(icon4_2)
        self.button1.setIconSize(QSize(18, 18))
        self.button2.setIconSize(QSize(18, 18))
        self.button1.setFlat(True)
        self.button2.setFlat(True)
        # layout.addWidget(self.label01)
        layout.addWidget(self.label1)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.setContentsMargins(0, 0, 0, 0)
        self.container1.setLayout(layout)

        self.container2 = QWidget()
        layout = QHBoxLayout(self.container2)
        layout.setAlignment(Qt.AlignRight)
        self.label2 = QLabel()
        self.button3 = QPushButton()
        self.button4 = QPushButton()
        self.button3.setObjectName(u"AscButton2")
        self.button3.setFixedSize(QSize(30, 30))
        self.button3.setFont(font)
        self.button3.setCursor(QCursor(Qt.PointingHandCursor))
        self.button4.setObjectName(u"DescButton2")
        self.button4.setFixedSize(QSize(30, 30))
        self.button4.setFont(font)
        self.button4.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        self.button3.setIcon(icon4_1)
        self.button4.setIcon(icon4_2)
        self.button3.setIconSize(QSize(18, 18))
        self.button4.setIconSize(QSize(18, 18))
        layout.addWidget(self.label2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.setContentsMargins(0, 0, 0, 0)
        self.container2.setLayout(layout)

        self.container3 = QWidget()
        layout = QHBoxLayout(self.container3)
        layout.setAlignment(Qt.AlignRight)
        self.label3 = QLabel()
        self.button5 = QPushButton()
        self.button6 = QPushButton()
        self.button5.setObjectName(u"AscButton3")
        self.button5.setFixedSize(QSize(30, 30))
        self.button5.setFont(font)
        self.button5.setCursor(QCursor(Qt.PointingHandCursor))
        self.button6.setObjectName(u"DescButton3")
        self.button6.setFixedSize(QSize(30, 30))
        self.button6.setFont(font)
        self.button6.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        self.button5.setIcon(icon4_1)
        self.button6.setIcon(icon4_2)
        self.button5.setIconSize(QSize(18, 18))
        self.button6.setIconSize(QSize(18, 18))
        layout.addWidget(self.label3)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.setContentsMargins(0, 0, 0, 0)
        self.container3.setLayout(layout)

        self.container4 = QWidget()
        layout = QHBoxLayout(self.container4)
        layout.setAlignment(Qt.AlignRight)
        self.label4 = QLabel()
        self.button7 = QPushButton()
        self.button8 = QPushButton()
        self.button7.setObjectName(u"AscButton4")
        self.button7.setFixedSize(QSize(30, 30))
        self.button7.setFont(font)
        self.button7.setCursor(QCursor(Qt.PointingHandCursor))
        self.button8.setObjectName(u"DescButton4")
        self.button8.setFixedSize(QSize(30, 30))
        self.button8.setFont(font)
        self.button8.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        self.button7.setIcon(icon4_1)
        self.button8.setIcon(icon4_2)
        self.button7.setIconSize(QSize(18, 18))
        self.button8.setIconSize(QSize(18, 18))
        layout.addWidget(self.label4)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)
        layout.setContentsMargins(0, 0, 0, 0)
        self.container4.setLayout(layout)

        self.container5 = QWidget()
        layout = QHBoxLayout(self.container5)
        layout.setAlignment(Qt.AlignRight)
        self.label5 = QLabel()
        self.button9 = QPushButton()
        self.button10 = QPushButton()
        self.button9.setObjectName(u"AscButton5")
        self.button9.setFixedSize(QSize(30, 30))
        self.button9.setFont(font)
        self.button9.setCursor(QCursor(Qt.PointingHandCursor))
        self.button10.setObjectName(u"DescButton5")
        self.button10.setFixedSize(QSize(30, 30))
        self.button10.setFont(font)
        self.button10.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        self.button9.setIcon(icon4_1)
        self.button10.setIcon(icon4_2)
        self.button9.setIconSize(QSize(18, 18))
        self.button10.setIconSize(QSize(18, 18))
        layout.addWidget(self.label5)
        layout.addWidget(self.button9)
        layout.addWidget(self.button10)
        layout.setContentsMargins(0, 0, 0, 0)

        self.container5.setLayout(layout)
        self.container6 = QWidget()
        layout = QHBoxLayout(self.container6)
        layout.setAlignment(Qt.AlignRight)
        self.label6 = QLabel()
        self.button11 = QPushButton()
        self.button12 = QPushButton()
        self.button11.setObjectName(u"AscButton6")
        self.button11.setFixedSize(QSize(30, 30))
        self.button11.setFont(font)
        self.button11.setCursor(QCursor(Qt.PointingHandCursor))
        self.button12.setObjectName(u"DescButton6")
        self.button12.setFixedSize(QSize(30, 30))
        self.button12.setFont(font)
        self.button12.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        # self.pushButton.clicked.connect(self.on_button_clicked())
        self.button11.setIcon(icon4_1)
        self.button12.setIcon(icon4_2)
        self.button11.setIconSize(QSize(18, 18))
        self.button12.setIconSize(QSize(18, 18))
        layout.addWidget(self.label6)
        layout.addWidget(self.button11)
        layout.addWidget(self.button12)
        layout.setContentsMargins(0, 0, 0, 0)
        self.container6.setLayout(layout)

        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)



        font4 = QFont()
        font4.setFamily(u"Segoe UI")

        # self.tableWidgetSecond = CustomTableWidget(self.row_3)
        # if (self.tableWidgetSecond.columnCount() < 5):
        #     self.tableWidgetSecond.setColumnCount(5)
        # # self.tableWidgetSecond.setHorizontalHeaderLabels(CustomHeaderView(self.tableWidgetSecond))
        # __qsecondtablewidgetitem = QTableWidgetItem()
        # self.tableWidgetSecond.setHorizontalHeaderItem(0, __qsecondtablewidgetitem)
        # __qsecondtablewidgetitem1 = QTableWidgetItem()
        # self.tableWidgetSecond.setHorizontalHeaderItem(1, __qsecondtablewidgetitem1)
        # __qsecondtablewidgetitem2 = QTableWidgetItem()
        # self.tableWidgetSecond.setHorizontalHeaderItem(2, __qsecondtablewidgetitem2)
        # __qsecondtablewidgetitem3 = QTableWidgetItem()
        # self.tableWidgetSecond.setHorizontalHeaderItem(3, __qsecondtablewidgetitem3)
        # if (self.tableWidgetSecond.rowCount() < 19000):
        #     self.tableWidgetSecond.setRowCount(19000)
        #
        # __qsecondtablewidgetitem4 = QTableWidgetItem()
        #
        # __qsecondtablewidgetitem4.setFont(font4);
        # self.tableWidgetSecond.setVerticalHeaderItem(0, __qsecondtablewidgetitem4)
        # __qsecondtablewidgetitem5 = QTableWidgetItem()
        # __qsecondtablewidgetitem5.setBackground(QColor(255, 255, 0))
        # self.tableWidgetSecond.setVerticalHeaderItem(1, __qsecondtablewidgetitem5)
        # __qsecondtablewidgetitem6 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(2, __qsecondtablewidgetitem6)
        # __qsecondtablewidgetitem7 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(3, __qsecondtablewidgetitem7)
        # __qsecondtablewidgetitem8 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(4, __qsecondtablewidgetitem8)
        # __qsecondtablewidgetitem9 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(5, __qsecondtablewidgetitem9)
        # __qsecondtablewidgetitem10 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(6, __qsecondtablewidgetitem10)
        # __qsecondtablewidgetitem11 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(7, __qsecondtablewidgetitem11)
        # __qsecondtablewidgetitem12 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(8, __qsecondtablewidgetitem12)
        # __qsecondtablewidgetitem13 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(9, __qsecondtablewidgetitem13)
        # __qsecondtablewidgetitem14 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(10, __qsecondtablewidgetitem14)
        # __qsecondtablewidgetitem15 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(11, __qsecondtablewidgetitem15)
        # __qsecondtablewidgetitem16 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(12, __qsecondtablewidgetitem16)
        # __qsecondtablewidgetitem17 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(13, __qsecondtablewidgetitem17)
        # __qsecondtablewidgetitem18 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(14, __qsecondtablewidgetitem18)
        # __qsecondtablewidgetitem19 = QTableWidgetItem()
        # self.tableWidgetSecond.setVerticalHeaderItem(15, __qsecondtablewidgetitem19)
        # __qsecondtablewidgetitem20 = QTableWidgetItem()
        # self.tableWidgetSecond.setItem(0, 0, __qsecondtablewidgetitem20)
        # __qsecondtablewidgetitem21 = QTableWidgetItem()
        # self.tableWidgetSecond.setItem(0, 1, __qsecondtablewidgetitem21)
        # __qsecondtablewidgetitem22 = QTableWidgetItem()
        # self.tableWidgetSecond.setItem(0, 2, __qsecondtablewidgetitem22)
        # __qsecondtablewidgetitem23 = QTableWidgetItem()
        # self.tableWidgetSecond.setItem(0, 3, __qsecondtablewidgetitem23)
        # __qsecondtablewidgetitem24 = QTableWidgetItem()
        # self.tableWidgetSecond.setItem(0, 4, __qsecondtablewidgetitem24)
        # self.tableWidgetSecond.setObjectName(u"tableWidget")





        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 10000):
            self.tableWidget.setRowCount(10000)

        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem25)
        self.tableWidget.setObjectName(u"tableWidget")


        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)


        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        # sizePolicy3.setHeightForWidth(self.tableWidgetSecond.sizePolicy().hasHeightForWidth())
        # self.tableWidgetSecond.setSizePolicy(sizePolicy4)

        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif

        self.tableWidget.setPalette(palette)

        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.setRowHeight(0, 50)


        # self.tableWidgetSecond.setPalette(palette)
        # self.tableWidgetSecond.setFrameShape(QFrame.NoFrame)
        # self.tableWidgetSecond.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.tableWidgetSecond.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # self.tableWidgetSecond.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # # self.tableWidgetSecond.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.tableWidgetSecond.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableWidgetSecond.setShowGrid(True)
        # self.tableWidgetSecond.setGridStyle(Qt.SolidLine)
        # self.tableWidgetSecond.setSortingEnabled(False)
        # self.tableWidgetSecond.horizontalHeader().setVisible(False)
        # self.tableWidgetSecond.horizontalHeader().setCascadingSectionResizes(True)
        # self.tableWidgetSecond.horizontalHeader().setDefaultSectionSize(200)
        # self.tableWidgetSecond.horizontalHeader().setStretchLastSection(True)
        # self.tableWidgetSecond.verticalHeader().setVisible(False)
        # self.tableWidgetSecond.verticalHeader().setCascadingSectionResizes(False)
        # self.tableWidgetSecond.verticalHeader().setHighlightSections(False)
        # self.tableWidgetSecond.verticalHeader().setStretchLastSection(True)

        self.button_select = QPushButton(self.row_3)
        self.button_select.setObjectName(u"btn_select")
        self.button_select.setMinimumSize(QSize(150, 30))
        self.button_select.setFont(font)
        self.button_select.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_select.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.verticalLayout.addWidget(self.button_select)
        self.button_reset = QPushButton(self.row_3)
        self.button_reset.setObjectName(u"btn_reset")
        self.button_reset.setMinimumSize(QSize(80, 30))
        self.button_reset.setFont(font)
        self.button_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_reset.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.verticalLayout.addWidget(self.button_reset)
        # self.horizontalLayout_12.addWidget(self.button_select)
        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.table_factories = QTableWidget(self.new_page)
        if (self.table_factories.columnCount() < 3):
            self.table_factories.setColumnCount(3)
        # self.tableWidgetSecond.setHorizontalHeaderLabels(CustomHeaderView(self.tableWidgetSecond))
        __qsecondtablewidgetitem = QTableWidgetItem()
        self.table_factories.setHorizontalHeaderItem(0, __qsecondtablewidgetitem)
        __qsecondtablewidgetitem1 = QTableWidgetItem()
        self.table_factories.setHorizontalHeaderItem(1, __qsecondtablewidgetitem1)
        __qsecondtablewidgetitem2 = QTableWidgetItem()
        self.table_factories.setHorizontalHeaderItem(2, __qsecondtablewidgetitem2)
        # __qsecondtablewidgetitem3? = QTableWidgetItem()
        # self.table_factories.setHorizontalHeaderItem(3, __qsecondtablewidgetitem3)
        if (self.table_factories.rowCount() < 19000):
            self.table_factories.setRowCount(19000)

        __qsecondtablewidgetitem4 = QTableWidgetItem()

        __qsecondtablewidgetitem4.setFont(font4)
        self.table_factories.setVerticalHeaderItem(0, __qsecondtablewidgetitem4)
        __qsecondtablewidgetitem5 = QTableWidgetItem()
        sizePolicy3.setHeightForWidth(self.table_factories.sizePolicy().hasHeightForWidth())

        # Set the width of the second column to 150 pixels
        # self.table_factories.setColumnWidth(1, 20)

        # Set the width of the third column to 200 pixels
        # self.table_factories.setColumnWidth(2, 20)
        self.table_factories.setVerticalHeaderItem(1, __qsecondtablewidgetitem5)
        __qsecondtablewidgetitem6 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(2, __qsecondtablewidgetitem6)
        __qsecondtablewidgetitem7 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(3, __qsecondtablewidgetitem7)
        __qsecondtablewidgetitem8 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(4, __qsecondtablewidgetitem8)
        __qsecondtablewidgetitem9 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(5, __qsecondtablewidgetitem9)
        __qsecondtablewidgetitem10 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(6, __qsecondtablewidgetitem10)
        __qsecondtablewidgetitem11 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(7, __qsecondtablewidgetitem11)
        __qsecondtablewidgetitem12 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(8, __qsecondtablewidgetitem12)
        __qsecondtablewidgetitem13 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(9, __qsecondtablewidgetitem13)
        __qsecondtablewidgetitem14 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(10, __qsecondtablewidgetitem14)
        __qsecondtablewidgetitem15 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(11, __qsecondtablewidgetitem15)
        __qsecondtablewidgetitem16 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(12, __qsecondtablewidgetitem16)
        __qsecondtablewidgetitem17 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(13, __qsecondtablewidgetitem17)
        __qsecondtablewidgetitem18 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(14, __qsecondtablewidgetitem18)
        __qsecondtablewidgetitem19 = QTableWidgetItem()
        self.table_factories.setVerticalHeaderItem(15, __qsecondtablewidgetitem19)
        __qsecondtablewidgetitem20 = QTableWidgetItem()
        self.table_factories.setItem(0, 0, __qsecondtablewidgetitem20)
        __qsecondtablewidgetitem21 = QTableWidgetItem()
        self.table_factories.setItem(0, 1, __qsecondtablewidgetitem21)
        __qsecondtablewidgetitem22 = QTableWidgetItem()
        self.table_factories.setItem(0, 2, __qsecondtablewidgetitem22)
        self.table_factories.setObjectName(u"tableWidget")
        # self.table_factories.setSizePolicy(sizePolicy4)

        self.table_factories.setPalette(palette)
        self.table_factories.setFrameShape(QFrame.NoFrame)
        self.table_factories.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.table_factories.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_factories.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_factories.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_factories.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_factories.setShowGrid(True)
        self.table_factories.setGridStyle(Qt.SolidLine)
        self.table_factories.setSortingEnabled(False)
        self.table_factories.horizontalHeader().setVisible(False)
        self.table_factories.horizontalHeader().setCascadingSectionResizes(True)
        self.table_factories.horizontalHeader().setDefaultSectionSize(200)
        self.table_factories.horizontalHeader().setStretchLastSection(True)
        self.table_factories.verticalHeader().setVisible(False)
        self.table_factories.verticalHeader().setCascadingSectionResizes(False)
        self.table_factories.verticalHeader().setHighlightSections(False)
        self.table_factories.verticalHeader().setStretchLastSection(True)

        self.table_factories.setFixedWidth(500)
        # self.table_factories.setColumnWidth(0, 20)
        self.table_factories.setColumnWidth(0, 200)

        # Set the width of the second column to 150 pixels
        self.table_factories.setColumnWidth(1, 120)

        # Set the width of the third column to 200 pixels
        self.table_factories.setColumnWidth(2, 66)
        view = gl.GLViewWidget(self.new_page)
        # view.setAspectLocked(True)
        view.setCameraPosition(distance=100, azimuth=30)
        view.setBackgroundColor(1,1,1,1)
        self.gl_view = MyGLViewWidget()
        self.gl_view.setCameraPosition(distance=5)
        self.gl_view.setBackgroundColor((0, 0, 0, 0))
        # gl_view.show()
        # view.setCameraEnabled(orbit=False)
        # Define pie chart data and colors
        data = [5, 35, 40, 40]
        colors = [
            (1, 0, 0, 55),
            (1, 1, 1, 255),
            (0, 0, 2, 255),
            (0, 1, 1, 255)
        ]
        self.create_3d_pie_chart(data, colors, self.gl_view)
        # self.verticalLayout_20.addWidget(gl_view)
        # self.splitter = QSplitter(Qt.Horizontal)
        self.widget1 = QWidget()
        self.layout_splitter = QHBoxLayout(self.widget1)
        self.layout_splitter.addWidget(self.table_factories)
        self.widget1.setLayout(self.layout_splitter)
        # self.labelHello = QLabel(self.new_page)
        # self.labelHello.setText("Hello World")
        # self.layout_splitter.addWidget(self.labelHello)
        # self.layout_splitter.addWidget(self.gl_view)
        # self.splitter.addWidget(self.widget1)
        self.verticalLayout_20.addWidget(self.widget1)


        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.label)
        self.verticalLayout_20.addWidget(self.label)


        # self.pushButton.clicked.connect(self.on_button_clicked())
        # icon4 = QIcon()
        # icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.pushButton.setIcon(icon4)
        # self.button.clicked.connect(self.select_all_rows)


        # self.pushButton.clicked.connect(self.on_button_clicked())
        # icon4 = QIcon()
        # icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.pushButton.setIcon(icon4)
        # self.button.clicked.connect(self.select_all_rows)

        # self.verticalLayout_20.addWidget(self.button_select)
        # self.verticalLayout_20.addWidget(self.table_factories)
        # self.verticalLayout_20.addWidget(gl_view)
        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")
        self.btn_export = QPushButton(self.topMenus)
        self.btn_export.setObjectName(u"btn_export")
        sizePolicy.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy)
        self.btn_export.setMinimumSize(QSize(0, 45))
        self.btn_export.setFont(font)
        self.btn_export.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export.setLayoutDirection(Qt.LeftToRight)
        self.btn_export.setStyleSheet(u"background-image: url(images/icons/cil-excel.png);")

        self.verticalLayout_14.addWidget(self.btn_export)
        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Product control", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Control logic / Smart view", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Catalog", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"Stocks", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Functions menu", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Functions menu", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.btn_global.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Export to excel", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Westa GmbH Product control", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here product number", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))

        # self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        # self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        # self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        # self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        # self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        # self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        # self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        # self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));

        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()


        self.tableWidget.setCellWidget(0, 0, self.container1)
        self.tableWidget.setCellWidget(0, 1, self.container2)
        self.tableWidget.setCellWidget(0, 2, self.container3)
        self.tableWidget.setCellWidget(0, 3, self.container4)
        self.tableWidget.setCellWidget(0, 4, self.container5)
        self.tableWidget.setCellWidget(0, 5, self.container6)

        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Have to be", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Ordered", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"To order", None));
        ___qtablewidgetitem25 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"To order up to 10", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)




        ___qsecondtablewidgetitem = self.table_factories.horizontalHeaderItem(0)
        ___qsecondtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qsecondtablewidgetitem1 = self.table_factories.horizontalHeaderItem(1)
        ___qsecondtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qsecondtablewidgetitem2 = self.table_factories.horizontalHeaderItem(2)
        ___qsecondtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        # ___qsecondtablewidgetitem3 = self.table_factories.horizontalHeaderItem(3)
        # ___qsecondtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        # ___qsecondtablewidgetitem4 = self.table_factories.verticalHeaderItem(0)
        # ___qsecondtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem5 = self.table_factories.verticalHeaderItem(1)
        ___qsecondtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem6 = self.table_factories.verticalHeaderItem(2)
        ___qsecondtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem7 = self.table_factories.verticalHeaderItem(3)
        ___qsecondtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem8 = self.table_factories.verticalHeaderItem(4)
        ___qsecondtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem9 = self.table_factories.verticalHeaderItem(5)
        ___qsecondtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem10 = self.table_factories.verticalHeaderItem(6)
        ___qsecondtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem11 = self.table_factories.verticalHeaderItem(7)
        ___qsecondtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem12 = self.table_factories.verticalHeaderItem(8)
        ___qsecondtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem13 = self.table_factories.verticalHeaderItem(9)
        ___qsecondtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem14 = self.table_factories.verticalHeaderItem(10)
        ___qsecondtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem15 = self.table_factories.verticalHeaderItem(11)
        ___qsecondtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem16 = self.table_factories.verticalHeaderItem(12)
        ___qsecondtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem17 = self.table_factories.verticalHeaderItem(13)
        ___qsecondtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem18 = self.table_factories.verticalHeaderItem(14)
        ___qsecondtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qsecondtablewidgetitem19 = self.table_factories.verticalHeaderItem(15)
        ___qsecondtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.table_factories.isSortingEnabled()
        self.table_factories.setSortingEnabled(False)
        ___qsecondtablewidgetitem20 = self.table_factories.item(0, 0)
        ___qsecondtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Factory", None));
        ___qsecondtablewidgetitem21 = self.table_factories.item(0, 1)
        ___qsecondtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Total Cost", None));
        ___qsecondtablewidgetitem22 = self.table_factories.item(0, 2)
        ___qsecondtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"", None));
        # ___qsecondtablewidgetitem23 = self.table_factories.item(0, 3)
        # ___qsecondtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Diff", None));
        # ___qsecondtablewidgetitem24 = self.table_factories.item(0, 4)
        # ___qsecondtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Diff up to 10", None));
        self.table_factories.setSortingEnabled(__sortingEnabled)



        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.button_select.setText(QCoreApplication.translate("MainWindow", u"Select all rows", None))
        self.button_reset.setText(QCoreApplication.translate("MainWindow", u"Reset sorting to default", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"Alpha v0.0.1", None))
    # retranslateUi

    def create_3d_pie_chart(self,data, colors,gl_view, edge_color=(0, 0, 0, 255), ):
        num_segments = len(data)
        summ = sum(data)
        print(data)
        print(summ)
        radius = 1
        height = 0.5  # Height of each pie chart segment

        angle_start = 0
        for i in range(num_segments):
            segment_vertices = []

            angle_end = angle_start + 2 * np.pi * data[i] / summ

            # Add bottom center vertex
            segment_vertices.append((0, 0, 0))

            # Add bottom vertices along the arc
            num_arc_points = 50
            arc_angles = np.linspace(angle_start, angle_end, num_arc_points)
            for angle in arc_angles:
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                segment_vertices.append((x, y, 0))

            # Add top center vertex
            segment_vertices.append((0, 0, height))

            # Add top vertices along the arc
            for angle in arc_angles:
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                segment_vertices.append((x, y, height))

            segment_vertices = np.array(segment_vertices, dtype=np.float32)

            # Define faces
            faces = []
            for j in range(1, num_arc_points):
                # Bottom face
                faces.append([0, j, j + 1])
                # Side faces
                faces.append([j, j + num_arc_points + 1, j + num_arc_points])
                faces.append([j + 1, j + num_arc_points + 1, j])
                # Top face
                faces.append([num_arc_points + 1, j + num_arc_points + 2, j + num_arc_points + 1])
            faces = np.array(faces, dtype=np.uint)

            # Create and add mesh item
            mesh_data = gl.MeshData(vertexes=segment_vertices, faces=faces)
            mesh_item = gl.GLMeshItem(
                meshdata=mesh_data,
                color=colors[i],
                edge_color=(240, 100, 0, 255),
                smooth=True,
                shader='shaded'
            )
            gl_view.addItem(mesh_item)

            angle_start = angle_end





