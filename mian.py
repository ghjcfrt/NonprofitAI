# main.py

import json
import random
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from NonprofitAI.gui import (
    BBSPage,
    ChatPage,
    CulturalPage,
    DetailPage,
    FeedbackPage,
    FundPage,
    GamePage,
    ImagePage,
    MapPage,
    MorePage,
    ProjectPage,
    RecommendPage,
    SubmitPage,
)
from NonprofitAI.gui import Ui_MainWindow as MainUI


class MainApp(QMainWindow):
    def __init__(self):  # noqa: PLR0915
        super().__init__()

        # 解决项目界面进入详情页时图片与文字会重叠的bug
        self.debug = False

        # 设置窗口标题
        self.setWindowTitle("非遗AI助手")

        # 设置窗口最大大小
        self.setMaximumSize(16777215, 600)

        # 加载项目数据
        # 创建 Path 对象（项目字典）
        path = Path("./NonprofitAI/json/project_dictionary.json")

        # 使用 Path.open() 打开文件
        with path.open(encoding="utf-8") as file:
            self.project_data = json.load(file)

        # 创建 QStackedWidget 管理不同界面
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("background-color: white;")

        # 记录进入 DetailPage 的来源界面
        self.detail_source_page = None

        # 主界面设置
        self.main_ui = MainUI()
        self.main_window = QMainWindow()
        self.main_ui.setupUi(self.main_window)
        self.central_widget.addWidget(self.main_window)

        # 设置 project 界面
        self.project_page = ProjectPage(self.project_data)
        self.project_page.project_selected.connect(self.show_detail_from_project)  # 绑定项目选择信号
        self.project_page.project_up_ui.back.clicked.connect(self.show_main)
        self.project_page.project_up_ui.home_page.clicked.connect(self.show_main)
        self.central_widget.addWidget(self.project_page)

        # 获取所有项目的图片路径
        project_images = [project["图片"] for project in self.project_data.values()]

        # 随机选择三张图片
        random_images = random.sample(project_images, 3)

        # 设置界面图片
        self.main_ui.hot_image.setPixmap(QPixmap(random_images[0]))
        self.main_ui.recommend_image.setPixmap(QPixmap(random_images[1]))
        self.main_ui.art_image.setPixmap(QPixmap(random_images[2]))

        # 调整图片大小以适应标签
        self.main_ui.hot_image.setScaledContents(True)
        self.main_ui.recommend_image.setScaledContents(True)
        self.main_ui.art_image.setScaledContents(True)

        # 设置 chat 界面
        self.chat_page = ChatPage()
        self.chat_page.chat_up_ui.back.clicked.connect(self.show_main)
        self.chat_page.chat_up_ui.home_page.clicked.connect(self.show_main)
        self.central_widget.addWidget(self.chat_page)

        # 设置 image 界面
        self.image_page = ImagePage()
        self.central_widget.addWidget(self.image_page)
        self.image_page.image_up_ui.back.clicked.connect(self.show_main)
        self.image_page.image_up_ui.home_page.clicked.connect(self.show_main)

        # 设置 detail 界面
        self.detail_page = DetailPage()
        self.detail_page.detail_up_ui.back.clicked.connect(self.return_to_source_page)
        self.detail_page.detail_up_ui.home_page.clicked.connect(self.show_main)
        self.central_widget.addWidget(self.detail_page)

        # 设置 recommend 界面
        self.recommend_page = RecommendPage(self.project_data)  # 传递项目数据
        self.recommend_page.recommend_selected.connect(self.show_detail_from_recommend)  # 跳转详情页
        self.central_widget.addWidget(self.recommend_page)
        self.recommend_page.recommend_up_ui.back.clicked.connect(self.show_main)
        self.recommend_page.recommend_up_ui.home_page.clicked.connect(self.show_main)

        # 设置 more 界面
        self.more_page = MorePage()
        self.central_widget.addWidget(self.more_page)
        self.more_page.more_up_ui.back.clicked.connect(self.show_main)
        self.more_page.more_up_ui.home_page.clicked.connect(self.show_main)
        self.more_page.more_down_ui.first.clicked.connect(self.show_submit)
        self.more_page.more_down_ui.second.clicked.connect(self.show_feedback)
        self.more_page.more_down_ui.third.clicked.connect(self.show_fund)

        # 设置 cultural 界面
        self.cultural_page = CulturalPage()
        self.cultural_page.cultural_down_ui.game_btn.clicked.connect(self.show_game)
        self.cultural_page.cultural_down_ui.offline_btn.clicked.connect(self.show_map)
        self.central_widget.addWidget(self.cultural_page)
        self.cultural_page.cultural_up_ui.back.clicked.connect(self.show_main)
        self.cultural_page.cultural_up_ui.home_page.clicked.connect(self.show_main)

        # 设置 game 界面
        self.game_page = GamePage()
        self.game_page.game_selected.connect(self.show_detail_from_game)
        self.central_widget.addWidget(self.game_page)
        self.game_page.game_up_ui.back.clicked.connect(self.show_cultural)
        self.game_page.game_up_ui.home_page.clicked.connect(self.show_main)

        # 设置 bbs 界面
        self.bbs_page = BBSPage()
        self.central_widget.addWidget(self.bbs_page)
        self.bbs_page.bbs_up_ui.back.clicked.connect(self.show_main)
        self.bbs_page.bbs_up_ui.home_page.clicked.connect(self.show_main)

        # 设置 map 界面
        self.map_page = MapPage()
        self.central_widget.addWidget(self.map_page)
        self.map_page.map_up_ui.back.clicked.connect(self.show_cultural)
        self.map_page.map_up_ui.home_page.clicked.connect(self.show_main)

        # 设置 submit 界面
        self.submit_page = SubmitPage()
        self.central_widget.addWidget(self.submit_page)
        self.submit_page.submit_up_ui.back.clicked.connect(self.show_more)
        self.submit_page.submit_up_ui.home_page.clicked.connect(self.show_main)

        # 设置 feedback 界面
        self.feedback_page = FeedbackPage()
        self.central_widget.addWidget(self.feedback_page)
        self.feedback_page.feedback_up_ui.back.clicked.connect(self.show_more)
        self.feedback_page.feedback_up_ui.home_page.clicked.connect(self.show_main)

        # 设置 fund 界面
        self.fund_page = FundPage()
        self.central_widget.addWidget(self.fund_page)
        self.fund_page.fund_up_ui.back.clicked.connect(self.show_more)
        self.fund_page.fund_up_ui.home_page.clicked.connect(self.show_main)

        # 主界面点击按钮以显示 recommend 界面
        self.main_ui.recommend_more.clicked.connect(self.show_recommend)

        # 绑定主界面点击事件
        self.main_ui.Project_Button_icon.clicked.connect(self.show_project)
        self.main_ui.Trivia_Button_icon.clicked.connect(self.show_chat)
        self.main_ui.Image_Button_icon.clicked.connect(self.show_image)
        self.main_ui.More_Button_icon.clicked.connect(self.show_more)
        self.main_ui.Cultural_Button_icon.clicked.connect(self.show_cultural)
        self.main_ui.Bbs_Button_icon.clicked.connect(self.show_bbs)

    @Slot()
    def show_detail_from_project(self, project_key):
        """从 ProjectPage 显示详情界面"""
        self.detail_source_page = "project"  # 设置来源为 project 界面
        project_info = self.project_data.get(project_key)
        if self.debug:  # 解决初次进入详情页时图片与文字重叠的bug
            self.show_detail(project_key)
        else:
            self.show_detail(project_key)
            self.show_detail(project_key)
            self.debug = True
        self.detail_page.recommendation_system.record_click(project_info["名称"])  # 记录点击

    @Slot()
    def show_detail_from_recommend(self, project_key):
        """从 RecommendPage 显示详情界面"""
        self.detail_source_page = "recommend"  # 设置来源为 recommend 界面
        project_info = self.project_data.get(project_key)
        self.show_detail(project_key)
        self.detail_page.recommendation_system.record_click(project_info["名称"])  # 记录点击

    @Slot()
    def show_detail_from_game(self, project_key):
        """从 GamePage 显示详情界面"""
        self.detail_source_page = "game"
        if self.debug:  # 解决初次进入详情页时图片与文字重叠的bug
            self.show_detail(project_key)
        else:
            self.show_detail(project_key)
            self.show_detail(project_key)
            self.debug = True

    @Slot()
    def return_to_source_page(self):
        """根据来源界面返回"""
        if self.detail_source_page == "project":
            self.show_project()
        elif self.detail_source_page == "recommend":
            self.show_recommend()
        elif self.detail_source_page == "game":
            self.show_game()

    @Slot()
    def show_fund(self):
        """显示基金界面"""
        self.central_widget.setCurrentWidget(self.fund_page)
        self.fund_page.fund_up_ui.back.setEnabled(True)
        self.fund_page.fund_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_feedback(self):
        """显示反馈界面"""
        self.central_widget.setCurrentWidget(self.feedback_page)
        self.feedback_page.feedback_up_ui.back.setEnabled(True)
        self.feedback_page.feedback_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_submit(self):
        """显示提交界面"""
        self.central_widget.setCurrentWidget(self.submit_page)
        self.submit_page.submit_up_ui.back.setEnabled(True)
        self.submit_page.submit_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_map(self):
        """显示地图界面"""
        self.central_widget.setCurrentWidget(self.map_page)
        self.map_page.map_up_ui.back.setEnabled(True)
        self.map_page.map_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_bbs(self):
        """显示论坛界面"""
        self.central_widget.setCurrentWidget(self.bbs_page)
        self.bbs_page.bbs_up_ui.back.setEnabled(True)
        self.bbs_page.bbs_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_game(self):
        """显示游戏界面"""
        self.central_widget.setCurrentWidget(self.game_page)
        self.game_page.game_up_ui.back.setEnabled(True)
        self.game_page.game_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_cultural(self):
        """显示文化体验界面"""
        self.central_widget.setCurrentWidget(self.cultural_page)
        self.cultural_page.cultural_up_ui.back.setEnabled(True)
        self.cultural_page.cultural_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_more(self):
        """显示更多界面"""
        self.central_widget.setCurrentWidget(self.more_page)
        self.more_page.more_up_ui.back.setEnabled(True)
        self.more_page.more_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_recommend(self):
        """显示推荐界面并刷新推荐"""
        self.recommend_page.add_recommendation_buttons()  # 清空推荐并刷新按钮
        self.central_widget.setCurrentWidget(self.recommend_page)
        self.central_widget.setCurrentWidget(self.recommend_page)
        self.recommend_page.recommend_up_ui.back.setEnabled(True)
        self.recommend_page.recommend_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_detail(self, project_key):
        """显示详情界面并加载项目内容"""
        project_info = self.project_data.get(project_key)
        if project_info:
            self.detail_page.update_content(project_info)
            self.central_widget.setCurrentWidget(self.detail_page)
        # self.detail_page.recommendation_system.record_click(project_info["名称"])  # noqa: ERA001

    @Slot()
    def show_image(self):
        """显示识图界面"""
        self.central_widget.setCurrentWidget(self.image_page)
        self.image_page.image_up_ui.back.setEnabled(True)
        self.image_page.image_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_chat(self):
        """显示聊天界面"""
        self.central_widget.setCurrentWidget(self.chat_page)
        self.chat_page.chat_up_ui.back.setEnabled(True)
        self.chat_page.chat_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_project(self):
        """显示项目界面"""
        self.central_widget.setCurrentWidget(self.project_page)
        self.project_page.project_up_ui.back.setEnabled(True)
        self.project_page.project_up_ui.home_page.setEnabled(True)

    @Slot()
    def show_main(self):
        """显示主界面"""
        self.central_widget.setCurrentWidget(self.main_window)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # 设置全局样式，确保所有消息框的文本为黑色
    app.setStyleSheet("""
        QMessageBox QLabel {
            color: black;
        }
        QMessageBox QPushButton {
            color: black;
        }
    """)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
