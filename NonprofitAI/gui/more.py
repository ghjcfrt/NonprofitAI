# more.py
from PySide6.QtWidgets import QFrame, QMainWindow, QScrollArea, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import Ui_more_down, Ui_more_up


class MorePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置布局
        self.layout = QVBoxLayout(self)

        # 上半部分
        self.more_up_ui = Ui_more_up()
        self.more_up_widget = QMainWindow()
        self.more_up_ui.setupUi(self.more_up_widget)
        self.layout.addWidget(self.more_up_widget)
        self.more_up_widget.setFixedHeight(70)

        # 下半部分
        self.more_down_ui = Ui_more_down()
        self.more_down_widget = QFrame()
        self.more_down_ui.setupUi(self.more_down_widget)

        # 设置滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.more_down_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: #f1f1f1;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #888;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #555;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)

        # 将滚动区域添加到布局
        self.layout.addWidget(scroll_area)
