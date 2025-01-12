from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

from ui import Ui_MainWindow
import os

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)

workdir = ""
extensions = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]

def filter(files: list[str]):
    filtered_files = []

    for file in files:
        for ext in  extensions:
            if file.endswith(ext):
                filtered_files.append(file)

    return filtered_files
        

def choose_workdir():
    global workdir

    workdir = QFileDialog.getExistingDirectory()
    files_list = os.listdir(workdir)

    files_list = filter(files_list)
    ui.files_list.addItems(files_list)




ui.choose_dir_btn.clicked.connect(choose_workdir)




win.show()
app.exec()