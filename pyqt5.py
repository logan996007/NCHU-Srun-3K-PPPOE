import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
################################################
# 创建主窗口
################################################
import time
import os
from datetime import datetime
# 连接ADSL


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('主界面')
        self.showMaximized()


################################################
# 对话框
################################################
class logindialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('移动有线校园网小工具')
        self.resize(400, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        # 设置界面控件
        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("连接")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("断开")
        self.verticalLayout.addWidget(self.pushButton_quit)
        self.tip = QTextEdit('power by dtkk')
        self.verticalLayout.addWidget(self.tip)

        # 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_quit.clicked.connect(self.left)

    def on_pushButton_enter_clicked(self):
        # 账号判断
        str = '宽带连接'
        true = getName(self.lineEdit_account.text())
        cmd_string = f'rasdial {str} {true} {self.lineEdit_password.text()}'
        str = ''
        tipp = os.popen(cmd_string).readlines()
        for s in tipp:
            if(len(s) > 0):
                str += '\n'+s
        time.sleep(5)
        self.setWindowTitle('连接成功 dtkk祝你上网愉快')
        print(str)
        self.tip.setPlainText(str+'\n使用360免费wifi软件可以与室友共享上网')

    def left(self):
        str = '宽带连接'
        cmd_string = f'rasdial {str} /disconnect'
        str = ''
        tipp = os.popen(cmd_string).readlines()
        for s in tipp:
            if(len(s) > 0):
                str += '\n'+s
        time.sleep(5)
        self.setWindowTitle('成功断开连接')
        self.tip.setPlainText(s)

    def getName(username):
        username_crypto = ""
        for i in range(len(username)):
            username_crypto += chr(ord(username[i])+4)

        return "{SRUN2}" + username_crypto+'@stu.nchu.edu.cn'


################################################
# 程序入门
################################################

def getName(username):
    username_crypto = ""
    for i in range(len(username)):
        username_crypto += chr(ord(username[i])+4)

    return "{SRUN2}" + username_crypto+'@stu.nchu.edu.cn'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = logindialog()
    if dialog.exec_() == QDialog.Accepted:
        the_window = MainWindow()
        the_window.show()
        sys.exit(app.exec_())
