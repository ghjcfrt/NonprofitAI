# image.py
from PySide6.QtWidgets import QMainWindow, QScrollArea, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import Ui_image_up, imageWindow


class ImagePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置主布局
        self.main_layout = QVBoxLayout(self)

        # 上半部分 (image_up)  # noqa: ERA001
        self.image_up_ui = Ui_image_up()
        self.image_up_widget = QMainWindow()
        self.image_up_ui.setupUi(self.image_up_widget)
        self.main_layout.addWidget(self.image_up_widget)
        self.image_up_widget.setFixedHeight(70)

        # 下半部分 (image_down)  # noqa: ERA001
        self.image_down_widget = imageWindow()
        self.image_down_scroll_area = QScrollArea()
        self.image_down_scroll_area.setWidget(self.image_down_widget)
        self.image_down_scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.image_down_scroll_area)
