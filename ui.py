# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 520, 781, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.left_btn.setObjectName("left_btn")
        self.horizontalLayout.addWidget(self.left_btn)
        self.right_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.right_btn.setObjectName("right_btn")
        self.horizontalLayout.addWidget(self.right_btn)
        self.mirror_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.mirror_btn.setObjectName("mirror_btn")
        self.horizontalLayout.addWidget(self.mirror_btn)
        self.sharp_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.sharp_btn.setObjectName("sharp_btn")
        self.horizontalLayout.addWidget(self.sharp_btn)
        self.bw_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.bw_btn.setObjectName("bw_btn")
        self.horizontalLayout.addWidget(self.bw_btn)
        self.choose_dir_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.choose_dir_btn.setGeometry(QtCore.QRect(10, 0, 151, 23))
        self.choose_dir_btn.setObjectName("choose_dir_btn")
        self.files_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.files_list.setGeometry(QtCore.QRect(10, 30, 149, 479))
        self.files_list.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.files_list.setObjectName("files_list")
        self.image_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_lb.setGeometry(QtCore.QRect(180, 12, 611, 491))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.image_lb.setFont(font)
        self.image_lb.setStyleSheet("")
        self.image_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image_lb.setObjectName("image_lb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.left_btn.setText(_translate("MainWindow", "To Left"))
        self.right_btn.setText(_translate("MainWindow", "To Right"))
        self.mirror_btn.setText(_translate("MainWindow", "Mirror"))
        self.sharp_btn.setText(_translate("MainWindow", "Sharpen"))
        self.bw_btn.setText(_translate("MainWindow", "Black/White"))
        self.choose_dir_btn.setText(_translate("MainWindow", "Folder"))
        self.image_lb.setText(_translate("MainWindow", "Picture"))
