from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from tool import  Ui_MainWindow
# from main2 import  Ui_Dialog
# from _matplot import MyDynamicMplCanvas
import sys
import os
class MainDlg(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_py.clicked.connect(self.open_py_file)
        self.pushButton_ui.clicked.connect(self.open_ui_file)
        self.pushButton_get.clicked.connect(self.get)
    def open_ui_file(self):
        self.file_path_ui, filetype= QFileDialog.getOpenFileName(
            self,
            '选取要转换的ui文件'
        )
        self.lineEdit_ui.setText(self.file_path_ui)


    def open_py_file(self):
        self.file_path_py, filetype= QFileDialog.getOpenFileName(
            self,
            '选取生成py文件路径'
        )
        self.lineEdit_py.setText(self.file_path_py)
    def get(self):
        try:
            os.system('pyuic5 -o %s %s' % (self.file_path_py, self.file_path_ui))
            self.label_inf.setText('成功！\r\nui文件:%s\r\npy文件:%s'%(self.file_path_ui,self.file_path_py))
        except :
            self.label_inf.setText('失败！\r\nui文件:%s\r\npy文件:%s' % (self.file_path_ui, self.file_path_py))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainDlg()
    dlg.show()
    sys.exit(app.exec_())