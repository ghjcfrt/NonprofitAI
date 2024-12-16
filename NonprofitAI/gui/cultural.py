# culture.py
from PySide6.QtWidgets import QFrame, QMainWindow, QScrollArea, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import Ui_cultural_down, Ui_cultural_up


class CulturalPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置布局
        self.layout = QVBoxLayout(self)

        # 上半部分
        self.cultural_up_ui = Ui_cultural_up()
        self.cultural_up_widget = QMainWindow()
        self.cultural_up_ui.setupUi(self.cultural_up_widget)
        self.layout.addWidget(self.cultural_up_widget)
        self.cultural_up_widget.setFixedHeight(70)

        # 下半部分
        self.cultural_down_ui = Ui_cultural_down()
        self.cultural_down_widget = QFrame()
        self.cultural_down_ui.setupUi(self.cultural_down_widget)
        self.cultural_down_widget.setMinimumHeight(100)  # 设置最小高度

        # 设置滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.cultural_down_widget)
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
