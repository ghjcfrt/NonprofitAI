# chat_down.py
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QKeySequence, QShortcut
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QScrollArea, QTextEdit, QVBoxLayout, QWidget

from NonprofitAI.feat.AIChat import AIChat  # 导入AI聊天生成函数


class MessageWidget(QWidget):
    def __init__(self, sender, text, *, is_ai=False):
        super().__init__()

        self.sender_label = QLabel(sender)
        self.sender_label.setFixedHeight(20)
        self.sender_label.setAlignment(Qt.AlignCenter)

        self.text_label = QLabel(text)
        self.text_label.setWordWrap(True)

        self.init_ui(is_ai)

    def init_ui(self, is_ai):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.sender_label)
        self.layout.addWidget(self.text_label)
        self.layout.setContentsMargins(10, 5, 10, 5)

        if is_ai:
            self_layout = QHBoxLayout(self)
            container = QWidget()
            container.setLayout(self.layout)
            self_layout.addWidget(container)
            self_layout.addSpacing(200)
            self.setStyleSheet("""
                QWidget {
                    background-color: #e0f7fa;
                    border-radius: 20px;
                    color: black;
                }
                QLabel {
                    color: black;
                }
            """)
            self.setLayout(self_layout)
        else:
            container = QWidget()
            container.setLayout(self.layout)
            outer_layout = QHBoxLayout(self)
            outer_layout.addSpacing(200)
            outer_layout.addWidget(container, Qt.AlignRight)
            self.setStyleSheet("""
                QWidget {
                    background-color: #fff9c4;
                    border-radius: 20px;
                    color: black;
                }
                QLabel {
                    color: black;
                }
            """)
            self.setLayout(outer_layout)


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat Window")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("QWidget { background-color: white; }")

        self.main_layout = QVBoxLayout()

        self.message_container = QWidget()
        self.message_layout = QVBoxLayout(self.message_container)
        self.message_layout.setSpacing(10)
        self.message_layout.setContentsMargins(0, 0, 0, 0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.message_container)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet("""
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
        self.main_layout.addWidget(self.scroll_area)

        self.input_layout = QHBoxLayout()
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("输入消息...")
        self.input_text.setFixedHeight(30)
        self.input_text.setStyleSheet("QTextEdit { color: black; background-color: white; border: 1px solid #ccc; }")
        self.input_layout.addWidget(self.input_text, 1)

        self.send_button = QPushButton("发送")
        self.send_button.setStyleSheet(
            "QPushButton { background-color: #007BFF; color: white; border: none; border-radius: 4px; padding: 5px 10px; }"
        )
        self.send_button.clicked.connect(self.send_message)
        self.input_layout.addWidget(self.send_button)

        self.main_layout.addLayout(self.input_layout)
        self.setLayout(self.main_layout)

        self.add_message("AI", "你好！今天我能为您提供什么帮助？", is_ai=True)
        self.add_message("You", "你好，我需要一些帮助...", is_ai=False)

        # 绑定回车键到发送按钮
        self.shortcut = QShortcut(QKeySequence(Qt.Key_Return), self)
        self.shortcut.activated.connect(self.send_message)

    def add_message(self, sender, text, *, is_ai=False):
        message_widget = MessageWidget(sender, text, is_ai=is_ai)
        self.message_layout.addWidget(message_widget)
        self.message_container.adjustSize()

    def send_message(self):
        message = self.input_text.toPlainText()
        if message:
            self.add_message("You", message, is_ai=False)
            # 创建AIChat实例并传递用户输入
            ai_chat = AIChat()  # 创建AIChat实例
            ai_response = ai_chat.generate_response(message)  # 传递用户输入作为参数
            self.add_message("AI", ai_response, is_ai=True)
            # 清空输入框内容
            self.input_text.clear()  # 清空发送框

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return:  # 检查是否按下回车键
            self.send_message()  # 发送消息
            event.accept()  # 阻止文本框换行
        else:
            super().keyPressEvent(event)  # 处理其他按键
