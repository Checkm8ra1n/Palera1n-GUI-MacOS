import sys
import subprocess
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(551, 309)
        self.actionWebsite = QAction(MainWindow)
        self.actionWebsite.setObjectName(u"actionWebsite")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(110, -40, 351, 111))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Title.setFont(font)
        self.GitHub = QPushButton(self.centralwidget)
        self.GitHub.setObjectName(u"GitHub")
        self.GitHub.setGeometry(QRect(460, 10, 71, 21))
        icon = QIcon()
        icon.addFile(u"../Downloads/GitHub_Invertocat_Logo.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GitHub.setIcon(icon)
        self.Run = QPushButton(self.centralwidget)
        self.Run.setObjectName(u"Run")
        self.Run.setGeometry(QRect(230, 120, 75, 23))
        self.VerboseD = QCheckBox(self.centralwidget)
        self.VerboseD.setObjectName(u"VerboseD")
        self.VerboseD.setGeometry(QRect(10, 80, 111, 17))
        self.VerboseT = QCheckBox(self.centralwidget)
        self.VerboseT.setObjectName(u"VerboseT")
        self.VerboseT.setGeometry(QRect(10, 100, 121, 17))
        self.Revert = QCheckBox(self.centralwidget)
        self.Revert.setObjectName(u"Revert")
        self.Revert.setGeometry(QRect(10, 120, 101, 17))
        self.Recovery = QPushButton(self.centralwidget)
        self.Recovery.setObjectName(u"Recovery")
        self.Recovery.setGeometry(QRect(40, 150, 151, 23))
        self.DFU = QPushButton(self.centralwidget)
        self.DFU.setObjectName(u"DFU")
        self.DFU.setGeometry(QRect(380, 150, 121, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 551, 22))
        self.menuHelo = QMenu(self.menubar)
        self.menuHelo.setObjectName(u"menuHelo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelo.menuAction())
        self.menuHelo.addAction(self.actionWebsite)
        self.menuHelo.addAction(self.action)
        self.menuHelo.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.Run.clicked.connect(self.execute_jailbreak)
        self.Recovery.clicked.connect(self.execute_recovery)
        self.DFU.clicked.connect(self.execute_dfu)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionWebsite.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Palera1n GUI - by Checkm8ra1n", None))
        self.GitHub.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.Run.setText(QCoreApplication.translate("MainWindow", u"Jailbreak", None))
        self.VerboseD.setText(QCoreApplication.translate("MainWindow", u"Verbose on Device", None))
        self.VerboseT.setText(QCoreApplication.translate("MainWindow", u"Verbose on Terminal", None))
        self.Revert.setText(QCoreApplication.translate("MainWindow", u"Force Revert", None))
        self.Recovery.setText(QCoreApplication.translate("MainWindow", u"Exit from Recovery mode", None))
        self.DFU.setText(QCoreApplication.translate("MainWindow", u"Exit from DFU mode", None))
        self.menuHelo.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

    def execute_jailbreak(self):
        command = "palera1n"
        if self.VerboseD.isChecked():
            command += " -V"
        if self.VerboseT.isChecked():
            command += " -v"
        if self.Revert.isChecked():
            command += " --force-revert"
        subprocess.run(command, shell=True)

    def execute_recovery(self):
        command = "palera1n -n"
        subprocess.run(command, shell=True)
    def execute_dfu(self):
        command = "palera1n -D"
        subprocess.run(command, shell=True)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
