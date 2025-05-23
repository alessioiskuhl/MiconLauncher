from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QLocale)
from PySide2.QtWidgets import *

EnableAddModv = 0

class Ui_MiconLauncherWindow(object):
    def setupUi(self, MiconLauncherWindow):
        # Main Window
        if MiconLauncherWindow.objectName():
            MiconLauncherWindow.setObjectName(u"MiconLauncherWindow")
        MiconLauncherWindow.resize(673, 550)
        MiconLauncherWindow.setMinimumSize(QSize(673, 502))
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

        #Radio Button for selection of Vanilla Minecraft
        self.VanillaSelect = QRadioButton(self.MinecraftOptionsComment)
        self.VanillaSelect.setObjectName(u"VanillaSelect")
        self.VanillaSelect.setGeometry(QRect(10, 80, 82, 17))
        if self.VanillaSelect.isChecked():
            EnableAddModv = 0

        #Minecraft version selection
        self.MinecraftVersionAuswahl_1 = QComboBox(self.MinecraftOptionsComment)
        self.MinecraftVersionAuswahl_1.addItem(u"Minecraft Version")
        self.MinecraftVersionAuswahl_1.addItem(u"1.21")
        self.MinecraftVersionAuswahl_1.addItem(u"1.20.1")
        self.MinecraftVersionAuswahl_1.addItem(u"1.19.4")
        self.MinecraftVersionAuswahl_1.setObjectName(u"MinecraftVersionAuswahl_1")
        self.MinecraftVersionAuswahl_1.setGeometry(QRect(280, 40, 191, 22))
        self.MinecraftVersionAuswahlLabel_1 = QLabel(self.MinecraftOptionsComment)
        self.MinecraftVersionAuswahlLabel_1.setObjectName(u"MinecraftVersionAuswahlLabel_1")
        self.MinecraftVersionAuswahlLabel_1.setGeometry(QRect(10, 43, 261, 16))

        #Radio Button for selection of Forge Minecraft
        self.ForgeSelect = QRadioButton(self.MinecraftOptionsComment)
        self.ForgeSelect.setObjectName(u"ForgeSelect")
        self.ForgeSelect.setGeometry(QRect(100, 80, 82, 17))
        if self.ForgeSelect.isChecked():
            EnableAddModv = 1

        #Radio Button for selection of Fabric Minecraft
        self.FabricSelect = QRadioButton(self.MinecraftOptionsComment)
        self.FabricSelect.setObjectName(u"FabricSelect")
        self.FabricSelect.setGeometry(QRect(190, 80, 82, 17))
        if self.FabricSelect.isChecked():
            EnableAddModv = 1

        #Mods Table for addition of mods
        self.ModsTable = QTableWidget(self.MinecraftOptionsComment)
        if (self.ModsTable.columnCount() < 3):
            self.ModsTable.setColumnCount(3)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.ModsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ModsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ModsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.ModsTable.setObjectName(u"ModsTable")
        if EnableAddModv == 0:
            self.ModsTable.setEnabled(False)
        else:
            self.ModsTable.setEnabled(True)
        self.ModsTable.setGeometry(QRect(10, 110, 541, 161))

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
        MiconLauncherWindow.setWindowTitle(QCoreApplication.translate("MiconLauncherWindow", u"MiconLauncher", None))
        self.MinecraftOptionsComment.setTitle(QCoreApplication.translate("MiconLauncherWindow", u"Minecraft options", None))
        self.VanillaSelect.setText(QCoreApplication.translate("MiconLauncherWindow", u"Vanilla", None))

        self.MinecraftVersionAuswahlLabel_1.setText(QCoreApplication.translate("MiconLauncherWindow", u"Choose the Minecraft Version you want to use", None))
        self.ForgeSelect.setText(QCoreApplication.translate("MiconLauncherWindow", u"Forge", None))
        self.FabricSelect.setText(QCoreApplication.translate("MiconLauncherWindow", u"Fabric", None))
        ___qtablewidgetitem = self.ModsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MiconLauncherWindow", u"File name", None));
        ___qtablewidgetitem1 = self.ModsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MiconLauncherWindow", u"File size", None));
        ___qtablewidgetitem2 = self.ModsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MiconLauncherWindow", u"File path", None));
        self.GeneralSettingComment.setTitle(QCoreApplication.translate("MiconLauncherWindow", u"General Settings", None))
        self.FolderNameEdit_1.setHtml(QCoreApplication.translate("MiconLauncherWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Folder name</p></body></html>", None))
        self.FolderNameLabel_1.setText(QCoreApplication.translate("MiconLauncherWindow", u"Name the folder in which the server is located", None))
        self.ServerNameEdit_1.setHtml(QCoreApplication.translate("MiconLauncherWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Server name</p></body></html>", None))
        self.ServerNameLabel_1.setText(QCoreApplication.translate("MiconLauncherWindow", u"Name the server you want to create", None))
        self.FolderPathLabel_1.setText(QCoreApplication.translate("MiconLauncherWindow", u"Choose the path where the server folder will be put", None))
        self.BrowseButton_1.setText(QCoreApplication.translate("MiconLauncherWindow", u"Browse", None))
        self.LanguageSelectionLabel.setText(QCoreApplication.translate("MiconLauncherWindow", u"Select a language:", None))

        self.CreateButton.setText(QCoreApplication.translate("MiconLauncherWindow", u"Start creating", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.CreateTab), QCoreApplication.translate("MiconLauncherWindow", u"Create", None))
        self.StartButton.setText(QCoreApplication.translate("MiconLauncherWindow", u"Start", None))
        self.StopButton.setText(QCoreApplication.translate("MiconLauncherWindow", u"Stop", None))
        self.FolderSelection_1.setText(QCoreApplication.translate("MiconLauncherWindow", u"Select the Folder containing the server files (Self-made or edited", None))
        self.FolderSelection_2.setText(QCoreApplication.translate("MiconLauncherWindow", u"servers may not work, select folder made by this tool)", None))
        self.BrowseButton_2.setText(QCoreApplication.translate("MiconLauncherWindow", u"Browse", None))
        ___qtablewidgetitem3 = self.AddModsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MiconLauncherWindow", u"File name", None));
        ___qtablewidgetitem4 = self.AddModsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MiconLauncherWindow", u"File size", None));
        ___qtablewidgetitem5 = self.AddModsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MiconLauncherWindow", u"File path", None));
        self.AddModsLabel.setText(QCoreApplication.translate("MiconLauncherWindow", u"Add more mods here:", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.ManageTab), QCoreApplication.translate("MiconLauncherWindow", u"Manage", None))
    # retranslateUi
