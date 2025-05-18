from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QRadioButton, QTabWidget, QGroupBox, QComboBox, QTableWidget, QTableWidgetItem, QTextEdit, QLineEdit, QStatusBar, QFileDialog, QMessageBox
from PyQt5.QtGui import QBrush, QColor, QFont, QPalette
from PyQt5.QtCore import Qt, QSize, QLocale, QRect, QMetaObject
import sys
import os
import shutil
import zipfile
import json
import re

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class Ui_MiconLauncherWindow(object):
    def setupUi(self, MiconLauncherWindow):
        # Main Window
        if MiconLauncherWindow.objectName():
            MiconLauncherWindow.setObjectName("MiconLauncherWindow")
        MiconLauncherWindow.resize(673, 550)
        MiconLauncherWindow.setMinimumSize(QSize(673, 550))
        MiconLauncherWindow.setMaximumSize(QSize(673, 550))
        MiconLauncherWindow.setWindowTitle("MiconLauncher")
        MiconLauncherWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MiconLauncherWindow.setAnimated(True)
        MiconLauncherWindow.setTabShape(QTabWidget.Rounded)
        MiconLauncherWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MiconLauncherWindow)

        #Central widget
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)

        #Tabs
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Tabs.setGeometry(QRect(0, 0, 681, 551))
        self.CreateTab = QWidget()
        self.CreateTab.setObjectName(u"CreateTab")

        #Minecraft Options Comment
        self.MinecraftOptionsComment = QGroupBox(self.CreateTab)
        self.MinecraftOptionsComment.setObjectName(u"MinecraftOptionsComment")
        self.MinecraftOptionsComment.setGeometry(QRect(10, 160, 661, 291))

        #Minecraft version selection
        self.MinecraftVersionAuswahl_1 = QComboBox(self.MinecraftOptionsComment)
        self.MinecraftVersionAuswahl_1.addItem(u"Minecraft Version")
        self.MinecraftVersionAuswahl_1.addItem(u"1.0")
        self.MinecraftVersionAuswahl_1.addItem(u"1.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.2.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.2.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.2.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.2.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.2.5")
        self.MinecraftVersionAuswahl_1.addItem(u"1.3.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.3.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.4.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.4.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.4.5")
        self.MinecraftVersionAuswahl_1.addItem(u"1.4.6")
        self.MinecraftVersionAuswahl_1.addItem(u"1.4.7")
        self.MinecraftVersionAuswahl_1.addItem(u"1.5.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.5.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.6.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.6.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.6.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.5")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.6")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.7")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.8")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.9")
        self.MinecraftVersionAuswahl_1.addItem(u"1.7.10")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.5")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.6")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.7")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.8")
        self.MinecraftVersionAuswahl_1.addItem(u"1.8.9")
        self.MinecraftVersionAuswahl_1.addItem(u"1.9")
        self.MinecraftVersionAuswahl_1.addItem(u"1.9.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.9.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.9.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.9.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.10")
        self.MinecraftVersionAuswahl_1.addItem(u"1.10.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.10.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.11")
        self.MinecraftVersionAuswahl_1.addItem(u"1.11.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.11.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.12")
        self.MinecraftVersionAuswahl_1.addItem(u"1.12.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.12.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.13")
        self.MinecraftVersionAuswahl_1.addItem(u"1.13.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.13.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.14")
        self.MinecraftVersionAuswahl_1.addItem(u"1.14.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.14.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.14.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.14.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.15")
        self.MinecraftVersionAuswahl_1.addItem(u"1.15.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.15.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.16")
        self.MinecraftVersionAuswahl_1.addItem(u"1.16.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.16.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.16.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.16.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.16.5")
        self.MinecraftVersionAuswahl_1.addItem(u"1.17")
        self.MinecraftVersionAuswahl_1.addItem(u"1.17.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.18")
        self.MinecraftVersionAuswahl_1.addItem(u"1.18.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.18.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.19")
        self.MinecraftVersionAuswahl_1.addItem(u"1.19.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.19.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.19.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.19.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.20")
        self.MinecraftVersionAuswahl_1.addItem(u"1.20.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.20.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.20.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.20.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.20.5")
        self.MinecraftVersionAuswahl_1.addItem(u"1.20.6")
        self.MinecraftVersionAuswahl_1.addItem(u"1.21")
        self.MinecraftVersionAuswahl_1.addItem(u"1.21.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.21.2")
        self.MinecraftVersionAuswahl_1.addItem(u"1.21.3")
        self.MinecraftVersionAuswahl_1.addItem(u"1.21.4")
        self.MinecraftVersionAuswahl_1.addItem(u"1.21.5")
        self.MinecraftVersionAuswahl_1.setObjectName(u"MinecraftVersionAuswahl_1")
        self.MinecraftVersionAuswahl_1.setGeometry(QRect(280, 40, 191, 22))
        self.MinecraftVersionAuswahlLabel_1 = QLabel(self.MinecraftOptionsComment)
        self.MinecraftVersionAuswahlLabel_1.setObjectName(u"MinecraftVersionAuswahlLabel_1")
        self.MinecraftVersionAuswahlLabel_1.setGeometry(QRect(10, 43, 261, 16))

        # Create radio buttons
        self.VanillaSelect = QRadioButton("Vanilla", self.MinecraftOptionsComment)
        self.ForgeSelect = QRadioButton("Forge", self.MinecraftOptionsComment)
        self.FabricSelect = QRadioButton("Fabric", self.MinecraftOptionsComment)

        self.VanillaSelect.setGeometry(QRect(10, 80, 82, 17))
        self.ForgeSelect.setGeometry(QRect(100, 80, 82, 17))
        self.FabricSelect.setGeometry(QRect(190, 80, 82, 17))

        
        self.RemoveButton = QPushButton("Remove Selected", self.MinecraftOptionsComment)
        self.RemoveButton.setGeometry(QRect(460, 80, 120, 25))  # Adjust as needed
        self.RemoveButton.clicked.connect(MiconLauncherWindow.remove_selected_rows)
        



        #Mods Table for addition of mods
        self.ModsTable = DragDropTable(self.MinecraftOptionsComment)
        if (self.ModsTable.columnCount() < 5):
            self.ModsTable.setColumnCount(5)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.ModsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ModsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ModsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.ModsTable.setHorizontalHeaderItem(3, QTableWidgetItem("File Type"))
        self.ModsTable.setHorizontalHeaderItem(4, QTableWidgetItem("Minecraft Version"))
        self.ModsTable.setObjectName(u"ModsTable")
        self.ModsTable.setGeometry(QRect(10, 110, 541, 161))

        # Disable initially if Vanilla is default
        self.ModsTable.setEnabled(False)
        
        # Function to update table state
        def updateModsTableState():
            if self.VanillaSelect.isChecked():
                self.ModsTable.setEnabled(False)
            else:
                self.ModsTable.setEnabled(True)
        
        # Connect signals
        self.VanillaSelect.toggled.connect(updateModsTableState)
        self.ForgeSelect.toggled.connect(updateModsTableState)
        self.FabricSelect.toggled.connect(updateModsTableState)

        

        #A Comment to mark the General Settings area
        self.GeneralSettingComment = QGroupBox(self.CreateTab)
        self.GeneralSettingComment.setObjectName(u"GeneralSettingComment")
        self.GeneralSettingComment.setGeometry(QRect(10, 20, 661, 131))

        #A Text box and Label to choose a name for the folder the server is located in
        self.FolderNameEdit_1 = QTextEdit(self.GeneralSettingComment)
        self.FolderNameEdit_1.setObjectName(u"FolderNameEdit_1")
        self.FolderNameEdit_1.setGeometry(QRect(280, 60, 191, 23))
        self.FolderNameLabel_1 = QLabel(self.GeneralSettingComment)
        self.FolderNameLabel_1.setObjectName(u"FolderNameLabel_1")
        self.FolderNameLabel_1.setGeometry(QRect(20, 63, 251, 16))

        #A Text box and Label to choose a name for the server
        self.ServerNameEdit_1 = QTextEdit(self.GeneralSettingComment)
        self.ServerNameEdit_1.setObjectName(u"ServerNameEdit_1")
        self.ServerNameEdit_1.setEnabled(True)
        self.ServerNameEdit_1.setGeometry(QRect(280, 20, 191, 23))
        self.ServerNameLabel_1 = QLabel(self.GeneralSettingComment)
        self.ServerNameLabel_1.setObjectName(u"ServerNameLabel_1")
        self.ServerNameLabel_1.setGeometry(QRect(20, 23, 221, 16))

        #A Text, Label and browse button to easily choose a location for the folder containing the server
        self.FolderPathLabel_1 = QLabel(self.GeneralSettingComment)
        self.FolderPathLabel_1.setObjectName(u"FolderPathLabel_1")
        self.FolderPathLabel_1.setGeometry(QRect(20, 100, 251, 16))
        self.FolderPathText_1 = QLineEdit(self.GeneralSettingComment)
        self.FolderPathText_1.setObjectName(u"FolderPathText_1")
        self.FolderPathText_1.setGeometry(QRect(280, 99, 191, 21))
        self.BrowseButton_1 = QPushButton(self.GeneralSettingComment)
        self.BrowseButton_1.setObjectName(u"BrowseButton_1")
        self.BrowseButton_1.setGeometry(QRect(480, 98, 75, 23))
        

        #A label and a drop down box to choose the used language
        self.LanguageSelectionLabel = QLabel(self.CreateTab)
        self.LanguageSelectionLabel.setObjectName(u"LanguageSelectionLabel")
        self.LanguageSelectionLabel.setGeometry(QRect(470, 2, 91, 16))
        self.LanguageSelectionLabel.setMinimumSize(QSize(91, 16))
        self.LanguageSelectionLabel.setMaximumSize(QSize(91, 16))
        self.LanguageSelectionBox = QComboBox(self.CreateTab)
        self.LanguageSelectionBox.addItem(u"English")
        self.LanguageSelectionBox.addItem(u"Deutsch")
        self.LanguageSelectionBox.setObjectName(u"LanguageSelectionBox")
        self.LanguageSelectionBox.setGeometry(QRect(570, 0, 101, 21))
        self.LanguageSelectionBox.setMinimumSize(QSize(101, 21))
        self.LanguageSelectionBox.setMaximumSize(QSize(101, 21))
        self.LanguageSelectionBox.setEditable(False)

        #A button to switch between the server creation and management tabs
        self.CreateButton = QPushButton(self.CreateTab)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setGeometry(QRect(210, 460, 191, 41))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(16)
        self.CreateButton.setFont(font1)
        self.Tabs.addTab(self.CreateTab, "")
        self.ManageTab = QWidget()
        self.ManageTab.setObjectName(u"ManageTab")
        self.StartButton = QPushButton(self.ManageTab)

        #A button with green text to start the server
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(10, 70, 321, 71))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 170, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(240, 240, 240, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        self.StartButton.setPalette(palette)
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setWeight(75)
        self.StartButton.setFont(font2)
        self.StartButton.setMouseTracking(False)
        self.StartButton.setAutoFillBackground(False)
        self.StartButton.setFlat(False)

        #A stop button with red text to stop the server
        self.StopButton = QPushButton(self.ManageTab)
        self.StopButton.setObjectName(u"StopButton")
        self.StopButton.setGeometry(QRect(340, 70, 321, 71))
        palette1 = QPalette()
        brush5 = QBrush(QColor(170, 0, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.StopButton.setPalette(palette1)
        self.StopButton.setFont(font2)

        #Two labels and a  browse button to easily select the folder containing the server you created
        self.FolderSelection_1 = QLabel(self.ManageTab)
        self.FolderSelection_1.setObjectName(u"FolderSelection_1")
        self.FolderSelection_1.setGeometry(QRect(10, 10, 321, 16))
        self.FolderSelection_2 = QLabel(self.ManageTab)
        self.FolderSelection_2.setObjectName(u"FolderSelection_2")
        self.FolderSelection_2.setGeometry(QRect(10, 30, 311, 16))
        self.FolderPathLine = QLineEdit(self.ManageTab)
        self.FolderPathLine.setObjectName(u"FolderPathLine")
        self.FolderPathLine.setGeometry(QRect(340, 10, 221, 20))
        self.BrowseButton_2 = QPushButton(self.ManageTab)
        self.BrowseButton_2.setObjectName(u"BrowseButton_2")
        self.BrowseButton_2.setGeometry(QRect(570, 8, 75, 23))

        #A Table to add more mods to your server
        self.AddModsTable = QTableWidget(self.ManageTab)
        if (self.AddModsTable.columnCount() < 3):
            self.AddModsTable.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.AddModsTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.AddModsTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.AddModsTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.AddModsTable.setObjectName(u"AddModsTable")
        self.AddModsTable.setEnabled(False)
        self.AddModsTable.setGeometry(QRect(10, 340, 641, 161))
        self.AddModsLabel = QLabel(self.ManageTab)
        self.AddModsLabel.setObjectName(u"AddModsLabel")
        self.AddModsLabel.setGeometry(QRect(10, 320, 121, 16))
        self.Tabs.addTab(self.ManageTab, "")
        MiconLauncherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MiconLauncherWindow)
        self.statusbar.setObjectName(u"statusbar")
        MiconLauncherWindow.setStatusBar(self.statusbar)



### ----- Some stuff i dont understand to translate the text or something ----- ###
        self.retranslateUi(MiconLauncherWindow)

        self.Tabs.setCurrentIndex(0)
        self.StartButton.setDefault(False)


        QMetaObject.connectSlotsByName(MiconLauncherWindow)
    # setupUi

    def retranslateUi(self, MiconLauncherWindow):
        MiconLauncherWindow.setWindowTitle(QApplication.translate("MiconLauncherWindow", u"MiconLauncher", None))
        self.MinecraftOptionsComment.setTitle(QApplication.translate("MiconLauncherWindow", u"Minecraft options", None))
        self.VanillaSelect.setText(QApplication.translate("MiconLauncherWindow", u"Vanilla", None))

        self.MinecraftVersionAuswahlLabel_1.setText(QApplication.translate("MiconLauncherWindow", u"Choose the Minecraft Version you want to use", None))
        self.ForgeSelect.setText(QApplication.translate("MiconLauncherWindow", u"Forge", None))
        self.FabricSelect.setText(QApplication.translate("MiconLauncherWindow", u"Fabric", None))
        ___qtablewidgetitem = self.ModsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QApplication.translate("MiconLauncherWindow", u"File name", None));
        ___qtablewidgetitem1 = self.ModsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QApplication.translate("MiconLauncherWindow", u"File size", None));
        ___qtablewidgetitem2 = self.ModsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QApplication.translate("MiconLauncherWindow", u"File path", None));
        self.GeneralSettingComment.setTitle(QApplication.translate("MiconLauncherWindow", u"General Settings", None))
        self.FolderNameEdit_1.setHtml(QApplication.translate("MiconLauncherWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Folder name</p></body></html>", None))
        self.FolderNameLabel_1.setText(QApplication.translate("MiconLauncherWindow", u"Name the folder in which the server is located", None))
        self.ServerNameEdit_1.setHtml(QApplication.translate("MiconLauncherWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Server name</p></body></html>", None))
        self.ServerNameLabel_1.setText(QApplication.translate("MiconLauncherWindow", u"Name the server you want to create", None))
        self.FolderPathLabel_1.setText(QApplication.translate("MiconLauncherWindow", u"Choose the path where the server folder will be put", None))
        self.BrowseButton_1.setText(QApplication.translate("MiconLauncherWindow", u"Browse", None))
        self.LanguageSelectionLabel.setText(QApplication.translate("MiconLauncherWindow", u"Select a language:", None))

        self.CreateButton.setText(QApplication.translate("MiconLauncherWindow", u"Start creating", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.CreateTab), QApplication.translate("MiconLauncherWindow", u"Create", None))
        self.StartButton.setText(QApplication.translate("MiconLauncherWindow", u"Start", None))
        self.StopButton.setText(QApplication.translate("MiconLauncherWindow", u"Stop", None))
        self.FolderSelection_1.setText(QApplication.translate("MiconLauncherWindow", u"Select the Folder containing the server files (Self-made or edited", None))
        self.FolderSelection_2.setText(QApplication.translate("MiconLauncherWindow", u"servers may not work, select folder made by this tool)", None))
        self.BrowseButton_2.setText(QApplication.translate("MiconLauncherWindow", u"Browse", None))
        ___qtablewidgetitem3 = self.AddModsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QApplication.translate("MiconLauncherWindow", u"File name", None));
        ___qtablewidgetitem4 = self.AddModsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QApplication.translate("MiconLauncherWindow", u"File size", None));
        ___qtablewidgetitem5 = self.AddModsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QApplication.translate("MiconLauncherWindow", u"File path", None));
        self.AddModsLabel.setText(QApplication.translate("MiconLauncherWindow", u"Add more mods here:", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.ManageTab), QApplication.translate("MiconLauncherWindow", u"Manage", None))
    # retranslateUi


class DragDropTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()
        
    def get_minecraft_version_from_jar(self, file_path):
        mod_loader = "Unknown"
        version = "Unknown"

        try:
            with zipfile.ZipFile(file_path, 'r') as jar:
                namelist = jar.namelist()

                # --- Fabric mod detection ---
                if 'fabric.mod.json' in namelist:
                    mod_loader = "Fabric"
                    with jar.open('fabric.mod.json') as f:
                        import json
                        data = json.load(f)
                        if 'depends' in data and 'minecraft' in data['depends']:
                            version = data['depends']['minecraft']
                        elif 'minecraft' in data.get('depends', {}):
                            version = data['depends']['minecraft']

                # --- Forge mod detection ---
                elif 'META-INF/mods.toml' in namelist:
                    mod_loader = "Forge"
                    with jar.open('META-INF/mods.toml') as f:
                        content = f.read().decode(errors='ignore')

                        # Look for the block that depends on Minecraft
                        match = re.search(r'\[\[dependencies\..*?\]\](.*?)\n\s*\n', content, re.DOTALL)
                        while match:
                            block = match.group(1)
                            if 'modId="minecraft"' in block:
                                version_match = re.search(r'versionRange\s*=\s*"\[?([^\],]+)', block)
                                if version_match:
                                    version = version_match.group(1)
                                break
                            # Try next block
                            content = content[match.end():]
                            match = re.search(r'\[\[dependencies\..*?\]\](.*?)\n\s*\n', content, re.DOTALL)

                # --- Fallback: Try to guess from filename ---
                if version == "Unknown":
                    filename = os.path.basename(file_path)
                    version_guess = re.search(r'(1\.\d+(?:\.\d+)?)', filename)
                    if version_guess:
                        version = version_guess.group(1)

                if mod_loader != "Unknown" and version != "Unknown":
                    return f"{mod_loader} {version}"

                # --- Ask user if both methods failed ---
                if self:
                    reply = QMessageBox.question(self, "Mod Version Unknown",
                                                f"Could not detect Minecraft version or mod loader for:\n{os.path.basename(file_path)}\n\nAdd anyway?",
                                                QMessageBox.Yes | QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        return "Unknown"
                    else:
                        return None

                return "Unknown"

        except Exception as e:
            print(f"Error reading jar file: {e}")
            return None
    

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()

                if os.path.isfile(file_path):
                    file_name = os.path.basename(file_path)
                    file_size = os.path.getsize(file_path)

                    row = self.rowCount()
                    self.insertRow(row)
                    
                    file_type = os.path.splitext(file_path)[1]
                    minecraft_modloader = self.get_minecraft_version_from_jar(file_path)

                    self.setItem(row, 0, QTableWidgetItem(file_name))
                    self.setItem(row, 1, QTableWidgetItem(str(file_size) + " bytes"))
                    self.setItem(row, 2, QTableWidgetItem(file_path))
                    self.setItem(row, 3, QTableWidgetItem(file_type))
                    self.setItem(row, 4, QTableWidgetItem(minecraft_modloader))

                    # Copy the file to a 'mods' folder
                    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
                    target_folder = os.path.join(desktop, "MiconLauncher_Mods")
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.copy(file_path, os.path.join(target_folder, file_name))
    
    

    

    

# Main function
class MiconLauncher(QtWidgets.QMainWindow):
    def remove_selected_rows(self):
            selected_rows = set()
            for idx in self.ui.ModsTable.selectedIndexes():
                selected_rows.add(idx.row())
            for row in sorted(selected_rows, reverse=True):
                self.ui.ModsTable.removeRow(row)
                
    def copy_files_from_table(self, Widget_table, folder_name, target_folder):
        base_folder_name = folder_name.strip()
        complete_folder_path = os.path.join(target_folder, base_folder_name)
        counter = 1

        # Add a suffix if the folder already exists
        while os.path.exists(complete_folder_path):
            complete_folder_path = os.path.join(target_folder, f"{base_folder_name}_{counter}")
            counter += 1

        # Now create the uniquely named folder
        os.makedirs(complete_folder_path)
    
        for row in range(Widget_table.rowCount()):
            item = Widget_table.item(row, 2)  # column 2 = file_path
            if item:
                file_path = item.text()
                if os.path.isfile(file_path):  # Ensure it's a valid file
                    try:
                        shutil.copy(file_path, complete_folder_path)
                        QMessageBox.information(self, "Done", "Files have been copied successfully.")
                    except Exception as e:
                        print(f"Failed to copy {file_path}: {e}")

    def startCreating(self):
        selected_version = self.ui.MinecraftVersionAuswahl_1.currentText()
        for row in range(self.ui.ModsTable.rowCount()):
            file_path = self.ui.ModsTable.item(row, 2).text()
            self.tble = DragDropTable()
            detected_version = self.tble.get_minecraft_version_from_jar(file_path)
        
            if detected_version != selected_version and detected_version != "Unknown":
                QMessageBox.warning(self, "Version Mismatch",
                    f"File '{file_path}' may be for version {detected_version}, not {selected_version}.")
                return  # Stop or ask to continue
            
        folder_copy_name = self.ui.FolderNameEdit_1.toPlainText()
        folder_copy_path = self.ui.FolderPathText_1.text()
        if not folder_copy_path:
            QMessageBox.warning(self, "No folder", "Please select a target folder.")
            return

        os.makedirs(folder_copy_path, exist_ok=True)

        if os.path.isdir(folder_copy_path):
            self.copy_files_from_table(self.ui.ModsTable, folder_copy_name, folder_copy_path)
        else:
            print("Invalid target folder.")

        

    def browseFolder(self):
            folder = QFileDialog.getExistingDirectory(self, "Select Folder")
            if folder:
                self.ui.FolderPathText_1.setText(folder)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MiconLauncherWindow()
        self.ui.setupUi(self)

        self.ui.BrowseButton_1.clicked.connect(self.browseFolder)
        self.ui.CreateButton.clicked.connect(self.startCreating)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MiconLauncher()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()