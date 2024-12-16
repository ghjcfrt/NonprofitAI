from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QMainWindow, QMessageBox, QVBoxLayout, QWidget

from NonprofitAI.feat import Game
from NonprofitAI.gui.up_and_down import Ui_game_down, Ui_game_up


class GamePage(QWidget):
    game_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置主布局
        self.layout = QVBoxLayout(self)

        # 初始化 Game 类
        self.game = Game()

        # 上半部分
        self.game_up_ui = Ui_game_up()
        self.game_up_widget = QMainWindow()
        self.game_up_ui.setupUi(self.game_up_widget)
        self.layout.addWidget(self.game_up_widget)
        self.game_up_widget.setFixedHeight(70)

        # 下半部分
        self.game_down_ui = Ui_game_down()
        self.game_down_widget = QFrame()
        self.game_down_ui.setupUi(self.game_down_widget)
        self.layout.addWidget(self.game_down_widget)

        # 加载随机项目
        self.load_random_project()

        # 绑定确认按钮的点击事件
        self.game_down_ui.check_btn.clicked.connect(self.check_answer)

    def load_random_project(self):
        """加载随机项目并更新 UI"""
        # 获取随机项目图片
        image_path, project_key = self.game.get_random_project()

        # 设置图片
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            # 获取按钮的大小
            button_size = self.game_down_ui.image.size()

            # 缩放图片到按钮大小，保持纵横比
            scaled_pixmap = pixmap.scaled(
                button_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
            )
            # 设置图片为按钮的背景
            self.game_down_ui.image.setStyleSheet("")
            self.game_down_ui.image.setIcon(scaled_pixmap)
            self.game_down_ui.image.setIconSize(button_size)
        else:
            self.game_down_ui.image.setStyleSheet("background-color: rgb(200, 200, 200);")
            self.game_down_ui.image.setText("无图片")

        # 绑定点击事件，点击按钮后跳转到详情页
        self.game_down_ui.image.clicked.connect(lambda _, pk=project_key: self.game_selected.emit(pk))

        # 清空用户输入
        self.game_down_ui.lineEdit.clear()

    def check_answer(self):
        """检查用户答案是否正确"""
        user_input = self.game_down_ui.lineEdit.text()
        is_correct = self.game.verify_answer(user_input)

        # 弹窗提示
        msg_box = QMessageBox()
        msg_box.setWindowTitle("答案验证")
        if is_correct:
            msg_box.setText("恭喜你，回答正确！")
            msg_box.setIcon(QMessageBox.Icon.Information)
        else:
            msg_box.setText("很遗憾，答案错误，请再试一次。")
            msg_box.setIcon(QMessageBox.Icon.Warning)

        msg_box.exec()

        # 如果答案正确，刷新随机项目
        if is_correct:
            self.load_random_project()
