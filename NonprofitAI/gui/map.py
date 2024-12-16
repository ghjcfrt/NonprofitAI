# map.py
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import Ui_map_down, Ui_map_up


class MapPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置主布局
        self.layout = QVBoxLayout(self)

        # 上半部分（导航栏部分）
        self.map_up_ui = Ui_map_up()
        self.map_up_widget = QMainWindow()
        self.map_up_ui.setupUi(self.map_up_widget)
        self.layout.addWidget(self.map_up_widget)
        self.map_up_widget.setFixedHeight(70)

        # 下半部分（嵌入的浏览器部分）
        self.map_down = Ui_map_down()
        self.layout.addWidget(self.map_down)
