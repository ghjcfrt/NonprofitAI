# recommend.py
from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame, QMainWindow, QScrollArea, QVBoxLayout, QWidget

from NonprofitAI.feat import PersonalizedRecommend
from NonprofitAI.gui.up_and_down import Ui_recommend_down, Ui_recommend_up


class RecommendPage(QWidget):
    recommend_selected = Signal(str)

    def __init__(self, project_data, parent=None):
        super().__init__(parent)

        self.project_data = project_data  # 保存项目数据

        # 设置布局
        self.layout = QVBoxLayout(self)

        # 上半部分
        self.recommend_up_ui = Ui_recommend_up()
        self.recommend_up_widget = QMainWindow()
        self.recommend_up_ui.setupUi(self.recommend_up_widget)
        self.layout.addWidget(self.recommend_up_widget)
        self.recommend_up_widget.setFixedHeight(70)

        # 下半部分
        self.recommend_down_ui = Ui_recommend_down()
        self.recommend_down_widget = QFrame()
        self.recommend_down_ui.setupUi(self.recommend_down_widget)

        # 实例化个性化推荐类
        self.recommendation_system = PersonalizedRecommend()

        # 读取点击历史和项目字典数据
        self.click_history = self.recommendation_system.load_from_json(
            self.recommendation_system.click_history_filename
        )
        self.project_data = self.recommendation_system.load_from_json(self.recommendation_system.project_dict_filename)

        # 添加推荐项目按钮
        self.add_recommendation_buttons()

        # 设置滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.recommend_down_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(self.scrollbar_style())
        self.layout.addWidget(scroll_area)

    def add_recommendation_buttons(self):
        """根据点击历史和项目数据设置推荐按钮"""
        # 获取推荐项目的名称和图片路径
        recommendations_with_images = self.recommendation_system.recommend_based_on_history_or_category()

        # 获取按钮列表
        self.btns = [
            self.recommend_down_ui._1_1,  # noqa: SLF001
            self.recommend_down_ui._1_2,  # noqa: SLF001
            self.recommend_down_ui._2_1,  # noqa: SLF001
            self.recommend_down_ui._2_2,  # noqa: SLF001
        ]

        # 为每个按钮设置推荐的项目
        for i, btn in enumerate(self.btns):
            if i < len(recommendations_with_images):
                item_info = recommendations_with_images[i]
                project_key = item_info["项目序号"]
                project_image = item_info.get("图片", "")

                # 设置按钮图标
                if project_image:
                    btn.setIcon(QIcon(project_image))
                    btn.setIconSize(QSize(270, 270))

                # 绑定点击事件，点击按钮后跳转到详情页
                btn.clicked.connect(lambda _, pk=project_key: self.recommend_selected.emit(pk))

    @staticmethod
    def scrollbar_style():
        return """
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
        """
