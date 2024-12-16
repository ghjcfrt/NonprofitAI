# bbs.py
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import Ui_bbs_down, Ui_bbs_up


class BBSPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置主布局
        self.layout = QVBoxLayout(self)

        # 上半部分（导航栏部分）
        self.bbs_up_ui = Ui_bbs_up()
        self.bbs_up_widget = QMainWindow()
        self.bbs_up_ui.setupUi(self.bbs_up_widget)
        self.layout.addWidget(self.bbs_up_widget)
        self.bbs_up_widget.setFixedHeight(70)

        # 下半部分（嵌入的浏览器部分）
        self.bbs_down = Ui_bbs_down()
        self.layout.addWidget(self.bbs_down)
