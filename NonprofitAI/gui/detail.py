# detail.py

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QScrollArea, QVBoxLayout, QWidget

from NonprofitAI.feat import PersonalizedRecommend
from NonprofitAI.gui.up_and_down import Ui_detail_down, Ui_detail_up


class DetailPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置布局
        self.layout = QVBoxLayout(self)

        # 上半部分
        self.detail_up_ui = Ui_detail_up()
        self.detail_up_widget = QMainWindow()
        self.detail_up_ui.setupUi(self.detail_up_widget)
        self.layout.addWidget(self.detail_up_widget)
        self.detail_up_widget.setFixedHeight(70)

        # 下半部分 (detail_down) 包含滚动区域
        self.detail_down_ui = Ui_detail_down()
        self.detail_down_widget = QWidget()
        self.detail_down_ui.setupUi(self.detail_down_widget)
        self.detail_down_widget.setStyleSheet("background-color: rgb(255, 255, 255);")

        # 实例化推荐系统
        self.recommendation_system = PersonalizedRecommend()

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.detail_down_widget)
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
        self.layout.addWidget(scroll_area)

    @Slot()
    def update_content(self, project_info):
        """更新详情页面内容"""
        # 设置图片
        image_path = project_info["图片"]
        pixmap = QPixmap(image_path)
        self.detail_down_ui.imglabel.setPixmap(
            pixmap.scaled(
                self.detail_down_ui.imglabel.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        self.detail_down_ui.imglabel.setScaledContents(True)

        # 设置文本内容
        self.detail_down_ui.name_word.setText(project_info["名称"])
        self.detail_down_ui.category_word.setText(project_info["类别"])
        self.detail_down_ui.area_word.setText(project_info["地区"])
        self.detail_down_ui.introduction_word.setText(project_info["简介"])
        self.detail_down_ui.history_word.setText(project_info["历史"])

        # 确保文本控件换行和居中
        for widget in [
            self.detail_down_ui.name_word,
            self.detail_down_ui.category_word,
            self.detail_down_ui.area_word,
            self.detail_down_ui.introduction_word,
            self.detail_down_ui.history_word,
        ]:
            widget.setWordWrap(True)
            widget.setAlignment(Qt.AlignCenter)
