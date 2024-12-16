# image_down.py
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QPixmap, QShortcut
from PySide6.QtWidgets import QFileDialog, QHBoxLayout, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget

from NonprofitAI.feat import AIImage


class MessageWidget(QWidget):
    def __init__(self, sender, text=None, image=None, *, is_ai=False):
        super().__init__()

        self.sender_label = QLabel(sender)
        self.sender_label.setFixedHeight(20)
        self.sender_label.setAlignment(Qt.AlignCenter)

        self.text_label = QLabel(text or "")
        self.text_label.setWordWrap(True)

        self.image_label = QLabel()
        if image:
            pixmap = QPixmap(image)
            self.image_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))

        self.init_ui(is_ai)

    def init_ui(self, is_ai):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.sender_label)

        if self.image_label.pixmap():
            self.layout.addWidget(self.image_label)
        elif self.text_label.text():
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


class imageWindow(QWidget):
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

        # 添加选择图片按钮
        self.select_image_button = QPushButton("选择图片")
        self.select_image_button.setStyleSheet("color: black;")
        self.select_image_button.clicked.connect(self.select_image)
        self.input_layout.addWidget(self.select_image_button)

        # 添加显示路径的 QLabel
        self.image_path_label = QLabel("未选择图片")
        self.image_path_label.setStyleSheet("color: black; font-size: 12px;")
        self.input_layout.addWidget(self.image_path_label)

        self.send_button = QPushButton("发送")
        self.send_button.setStyleSheet(
            "QPushButton { background-color: #007BFF; color: white; border: none; border-radius: 4px; padding: 5px 10px; }"
        )
        self.send_button.clicked.connect(self.send_message)
        self.input_layout.addWidget(self.send_button)

        self.main_layout.addLayout(self.input_layout)
        self.setLayout(self.main_layout)

        self.selected_image_path = None  # 用于存储选择的图片路径
        self.add_message("AI", "你好！今天我能为您提供什么帮助？", is_ai=True)

        # 绑定回车键到发送按钮
        self.shortcut = QShortcut(QKeySequence(Qt.Key_Return), self)
        self.shortcut.activated.connect(self.send_message)

    def add_message(self, sender, text=None, image=None, *, is_ai=False):
        message_widget = MessageWidget(sender, text, image, is_ai=is_ai)
        self.message_layout.addWidget(message_widget)
        self.message_container.adjustSize()

    def select_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.selected_image_path = Path(selected_files[0])  # 选择的图片路径
                self.image_path_label.setText(f"当前选择的图片路径: {self.selected_image_path}")

    def send_message(self):
        if self.selected_image_path:
            self.add_message("You", image=self.selected_image_path, is_ai=False)
            ai_image = AIImage()

            # 获取 AI 对图片的识别描述
            access_token = ai_image.access_token
            if not access_token:
                print("无法获取 access_token，AI 无法识别图片")
                return

            task_id = ai_image.get_task_id(self.selected_image_path)
            if task_id is None:
                print("获取任务 ID 失败")
                return

            description = ai_image.get_task_result(task_id, self.selected_image_path)
            if description:
                self.add_message("AI", description, is_ai=True)
            else:
                print("AI 识别失败")

            # 发送后清空图片路径
            self.selected_image_path = None
            self.image_path_label.setText("未选择图片")
