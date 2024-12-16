# chat.py
from PySide6.QtWidgets import QMainWindow, QScrollArea, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import ChatWindow, Ui_chat_up


class ChatPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置主布局
        self.main_layout = QVBoxLayout(self)

        # 上半部分 (chat_up)  # noqa: ERA001
        self.chat_up_ui = Ui_chat_up()
        self.chat_up_widget = QMainWindow()
        self.chat_up_ui.setupUi(self.chat_up_widget)
        self.main_layout.addWidget(self.chat_up_widget)
        self.chat_up_widget.setFixedHeight(70)

        # 下半部分 (chat_down)  # noqa: ERA001
        self.chat_down_widget = ChatWindow()
        self.chat_down_scroll_area = QScrollArea()
        self.chat_down_scroll_area.setWidget(self.chat_down_widget)
        self.chat_down_scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.chat_down_scroll_area)
