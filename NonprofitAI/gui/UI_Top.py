from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLayout, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

# 虽未取用，但仍需导入此文件，否则无法正常显示按钮图标
import NonprofitAI.gui.button_rc  # noqa: F401


class Ui_MainWindow:
    def setupUi(self, MainWindow):  # noqa: PLR0915
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 514)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.page_name = QLabel(self.centralwidget)
        self.page_name.setObjectName("page_name")
        self.page_name.setMinimumSize(QSize(0, 31))
        self.page_name.setMaximumSize(QSize(16777215, 31))
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.page_name.setFont(font)
        self.page_name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page_name.setStyleSheet(
            'color:rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";\nbackground-color: rgb(168,218,181);\n'
        )
        self.page_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.page_name)

        self.button_all = QVBoxLayout()
        self.button_all.setObjectName("button_all")
        self.first_button = QHBoxLayout()
        self.first_button.setObjectName("first_button")
        self.Project_Button_all = QVBoxLayout()
        self.Project_Button_all.setObjectName("Project_Button_all")
        self.Project_Button = QHBoxLayout()
        self.Project_Button.setObjectName("Project_Button")
        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Project_Button.addItem(self.horizontalSpacer_2)

        self.Project_Button_icon = QPushButton(self.centralwidget)
        self.Project_Button_icon.setObjectName("Project_Button_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Project_Button_icon.sizePolicy().hasHeightForWidth())
        self.Project_Button_icon.setSizePolicy(sizePolicy)
        self.Project_Button_icon.setMinimumSize(QSize(100, 100))
        self.Project_Button_icon.setMaximumSize(QSize(100, 100))
        self.Project_Button_icon.setStyleSheet("border-radius: 50px; \nborder-image: url(:/project.png);\n")

        self.Project_Button.addWidget(self.Project_Button_icon)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Project_Button.addItem(self.horizontalSpacer)

        self.Project_Button_all.addLayout(self.Project_Button)

        self.Project = QLabel(self.centralwidget)
        self.Project.setObjectName("Project")
        self.Project.setMinimumSize(QSize(200, 16))
        self.Project.setMaximumSize(QSize(16777215, 16))
        font1 = QFont()
        font1.setFamilies(["\u5b8b\u4f53"])
        font1.setPointSize(12)
        self.Project.setFont(font1)
        self.Project.setStyleSheet("color: rgb(0, 0, 0);")
        self.Project.setTextFormat(Qt.TextFormat.AutoText)
        self.Project.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Project_Button_all.addWidget(self.Project)

        self.first_button.addLayout(self.Project_Button_all)

        self.Trivia_Button_all = QVBoxLayout()
        self.Trivia_Button_all.setObjectName("Trivia_Button_all")
        self.Trivia_Button = QHBoxLayout()
        self.Trivia_Button.setObjectName("Trivia_Button")
        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Trivia_Button.addItem(self.horizontalSpacer_3)

        self.Trivia_Button_icon = QPushButton(self.centralwidget)
        self.Trivia_Button_icon.setObjectName("Trivia_Button_icon")
        sizePolicy.setHeightForWidth(self.Trivia_Button_icon.sizePolicy().hasHeightForWidth())
        self.Trivia_Button_icon.setSizePolicy(sizePolicy)
        self.Trivia_Button_icon.setMinimumSize(QSize(100, 100))
        self.Trivia_Button_icon.setMaximumSize(QSize(100, 100))
        self.Trivia_Button_icon.setStyleSheet("border-radius: 50px; \nborder-image: url(:/trivia.png);\n")

        self.Trivia_Button.addWidget(self.Trivia_Button_icon)

        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Trivia_Button.addItem(self.horizontalSpacer_4)

        self.Trivia_Button_all.addLayout(self.Trivia_Button)

        self.Trivia = QLabel(self.centralwidget)
        self.Trivia.setObjectName("Trivia")
        self.Trivia.setMinimumSize(QSize(200, 16))
        self.Trivia.setMaximumSize(QSize(16777215, 16))
        self.Trivia.setFont(font1)
        self.Trivia.setStyleSheet("color: rgb(0, 0, 0);")
        self.Trivia.setTextFormat(Qt.TextFormat.AutoText)
        self.Trivia.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Trivia_Button_all.addWidget(self.Trivia)

        self.first_button.addLayout(self.Trivia_Button_all)

        self.Image_Button_all = QVBoxLayout()
        self.Image_Button_all.setObjectName("Image_Button_all")
        self.Image_Button = QHBoxLayout()
        self.Image_Button.setObjectName("Image_Button")
        self.horizontalSpacer_5 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Image_Button.addItem(self.horizontalSpacer_5)

        self.Image_Button_icon = QPushButton(self.centralwidget)
        self.Image_Button_icon.setObjectName("Image_Button_icon")
        self.Image_Button_icon.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Image_Button_icon.sizePolicy().hasHeightForWidth())
        self.Image_Button_icon.setSizePolicy(sizePolicy)
        self.Image_Button_icon.setMinimumSize(QSize(100, 100))
        self.Image_Button_icon.setMaximumSize(QSize(100, 100))
        self.Image_Button_icon.setStyleSheet("border-radius: 50px; \nborder-image: url(:/image_recognition.png);\n")

        self.Image_Button.addWidget(self.Image_Button_icon)

        self.horizontalSpacer_6 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Image_Button.addItem(self.horizontalSpacer_6)

        self.Image_Button_all.addLayout(self.Image_Button)

        self.image_recognition = QLabel(self.centralwidget)
        self.image_recognition.setObjectName("image_recognition")
        self.image_recognition.setMinimumSize(QSize(200, 16))
        self.image_recognition.setMaximumSize(QSize(16777215, 16))
        self.image_recognition.setFont(font1)
        self.image_recognition.setStyleSheet("color: rgb(0, 0, 0);")
        self.image_recognition.setTextFormat(Qt.TextFormat.AutoText)
        self.image_recognition.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Image_Button_all.addWidget(self.image_recognition)

        self.first_button.addLayout(self.Image_Button_all)

        self.button_all.addLayout(self.first_button)

        self.second_button = QHBoxLayout()
        self.second_button.setObjectName("second_button")
        self.Cultural_Button_all = QVBoxLayout()
        self.Cultural_Button_all.setObjectName("Cultural_Button_all")
        self.Cultural_Button = QHBoxLayout()
        self.Cultural_Button.setObjectName("Cultural_Button")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Cultural_Button.addItem(self.horizontalSpacer_12)

        self.Cultural_Button_icon = QPushButton(self.centralwidget)
        self.Cultural_Button_icon.setObjectName("Cultural_Button_icon")
        sizePolicy.setHeightForWidth(self.Cultural_Button_icon.sizePolicy().hasHeightForWidth())
        self.Cultural_Button_icon.setSizePolicy(sizePolicy)
        self.Cultural_Button_icon.setMinimumSize(QSize(100, 100))
        self.Cultural_Button_icon.setMaximumSize(QSize(100, 100))
        self.Cultural_Button_icon.setStyleSheet("border-radius: 50px; \n\nborder-image: url(:/cultural.png);")

        self.Cultural_Button.addWidget(self.Cultural_Button_icon)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Cultural_Button.addItem(self.horizontalSpacer_11)

        self.Cultural_Button_all.addLayout(self.Cultural_Button)

        self.Cultural = QLabel(self.centralwidget)
        self.Cultural.setObjectName("Cultural")
        self.Cultural.setMinimumSize(QSize(200, 16))
        self.Cultural.setMaximumSize(QSize(16777215, 16))
        self.Cultural.setFont(font1)
        self.Cultural.setStyleSheet("color: rgb(0, 0, 0);")
        self.Cultural.setTextFormat(Qt.TextFormat.AutoText)
        self.Cultural.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Cultural_Button_all.addWidget(self.Cultural)

        self.second_button.addLayout(self.Cultural_Button_all)

        self.Bbs_Button_all = QVBoxLayout()
        self.Bbs_Button_all.setObjectName("Bbs_Button_all")
        self.Bbs_Button = QHBoxLayout()
        self.Bbs_Button.setObjectName("Bbs_Button")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Bbs_Button.addItem(self.horizontalSpacer_10)

        self.Bbs_Button_icon = QPushButton(self.centralwidget)
        self.Bbs_Button_icon.setObjectName("Bbs_Button_icon")
        sizePolicy.setHeightForWidth(self.Bbs_Button_icon.sizePolicy().hasHeightForWidth())
        self.Bbs_Button_icon.setSizePolicy(sizePolicy)
        self.Bbs_Button_icon.setMinimumSize(QSize(100, 100))
        self.Bbs_Button_icon.setMaximumSize(QSize(100, 100))
        self.Bbs_Button_icon.setStyleSheet("border-radius: 50px; \nborder-image: url(:/bbs.png);")

        self.Bbs_Button.addWidget(self.Bbs_Button_icon)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Bbs_Button.addItem(self.horizontalSpacer_9)

        self.Bbs_Button_all.addLayout(self.Bbs_Button)

        self.bbs = QLabel(self.centralwidget)
        self.bbs.setObjectName("bbs")
        self.bbs.setMinimumSize(QSize(200, 16))
        self.bbs.setMaximumSize(QSize(16777215, 16))
        self.bbs.setFont(font1)
        self.bbs.setStyleSheet("color: rgb(0, 0, 0);")
        self.bbs.setTextFormat(Qt.TextFormat.AutoText)
        self.bbs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Bbs_Button_all.addWidget(self.bbs)

        self.second_button.addLayout(self.Bbs_Button_all)

        self.More_Button_all = QVBoxLayout()
        self.More_Button_all.setObjectName("More_Button_all")
        self.More_Button = QHBoxLayout()
        self.More_Button.setObjectName("More_Button")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.More_Button.addItem(self.horizontalSpacer_8)

        self.More_Button_icon = QPushButton(self.centralwidget)
        self.More_Button_icon.setObjectName("More_Button_icon")
        sizePolicy.setHeightForWidth(self.More_Button_icon.sizePolicy().hasHeightForWidth())
        self.More_Button_icon.setSizePolicy(sizePolicy)
        self.More_Button_icon.setMinimumSize(QSize(100, 100))
        self.More_Button_icon.setMaximumSize(QSize(100, 100))
        self.More_Button_icon.setStyleSheet("border-radius: 50px; \nborder-image: url(:/more.png);")

        self.More_Button.addWidget(self.More_Button_icon)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.More_Button.addItem(self.horizontalSpacer_7)

        self.More_Button_all.addLayout(self.More_Button)

        self.More = QLabel(self.centralwidget)
        self.More.setObjectName("More")
        self.More.setMinimumSize(QSize(200, 16))
        self.More.setMaximumSize(QSize(16777215, 16))
        self.More.setFont(font1)
        self.More.setStyleSheet("color: rgb(0, 0, 0);")
        self.More.setTextFormat(Qt.TextFormat.AutoText)
        self.More.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.More_Button_all.addWidget(self.More)

        self.second_button.addLayout(self.More_Button_all)

        self.button_all.addLayout(self.second_button)

        self.verticalLayout.addLayout(self.button_all)

        self.showcase = QHBoxLayout()
        self.showcase.setObjectName("showcase")
        self.project_hot_all = QVBoxLayout()
        self.project_hot_all.setObjectName("project_hot_all")
        self.project_hot_first = QHBoxLayout()
        self.project_hot_first.setObjectName("project_hot_first")
        self.project_hot_first.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.project_hot_first.setSizeConstraint(QHBoxLayout.SetFixedSize)
        self.project_hot = QLabel(self.centralwidget)
        self.project_hot.setObjectName("project_hot")
        self.project_hot.setMinimumSize(QSize(0, 35))
        self.project_hot.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamilies(["\u5b8b\u4f53"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.project_hot.setFont(font2)
        self.project_hot.setStyleSheet('color: rgb(0, 0, 0);\nfont: 14pt "\u5b8b\u4f53";\n')

        self.project_hot_first.addWidget(self.project_hot)

        self.project_hot_more = QPushButton(self.centralwidget)
        self.project_hot_more.setObjectName("project_hot_more")
        self.project_hot_more.setMinimumSize(QSize(80, 35))
        self.project_hot_more.setMaximumSize(QSize(80, 35))
        self.project_hot_more.setStyleSheet('color: rgb(0, 0, 0);\nfont: 9pt "\u5b8b\u4f53";')

        self.project_hot_first.addWidget(self.project_hot_more)

        self.project_hot_all.addLayout(self.project_hot_first)

        self.hot_image = QLabel(self.centralwidget)
        self.hot_image.setObjectName("hot_image")
        self.hot_image.setMinimumSize(QSize(278, 140))
        self.hot_image.setMaximumSize(QSize(278, 278))

        self.project_hot_all.addWidget(self.hot_image)

        self.showcase.addLayout(self.project_hot_all)

        self.recommend_all = QVBoxLayout()
        self.recommend_all.setObjectName("recommend_all")
        self.recommend_first = QHBoxLayout()
        self.recommend_first.setSpacing(6)
        self.recommend_first.setObjectName("recommend_first")
        self.recommend_first.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.recommend_first.setSizeConstraint(QHBoxLayout.SetFixedSize)
        self.recommend = QLabel(self.centralwidget)
        self.recommend.setObjectName("recommend")
        self.recommend.setMinimumSize(QSize(0, 35))
        self.recommend.setMaximumSize(QSize(16777215, 35))
        self.recommend.setFont(font2)
        self.recommend.setStyleSheet('color: rgb(0, 0, 0);\nfont: 14pt "\u5b8b\u4f53";\n')

        self.recommend_first.addWidget(self.recommend)

        self.recommend_more = QPushButton(self.centralwidget)
        self.recommend_more.setObjectName("recommend_more")
        self.recommend_more.setMinimumSize(QSize(80, 35))
        self.recommend_more.setMaximumSize(QSize(80, 35))
        self.recommend_more.setStyleSheet('color: rgb(0, 0, 0);\nfont: 9pt "\u5b8b\u4f53";')

        self.recommend_first.addWidget(self.recommend_more)

        self.recommend_all.addLayout(self.recommend_first)

        self.recommend_image = QLabel(self.centralwidget)
        self.recommend_image.setObjectName("recommend_image")
        self.recommend_image.setMinimumSize(QSize(278, 140))
        self.recommend_image.setMaximumSize(QSize(278, 278))

        self.recommend_all.addWidget(self.recommend_image)

        self.showcase.addLayout(self.recommend_all)

        self.art_hot_all = QVBoxLayout()
        self.art_hot_all.setObjectName("art_hot_all")
        self.art_hot_first = QHBoxLayout()
        self.art_hot_first.setObjectName("art_hot_first")
        self.art_hot_first.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.art_hot_first.setSizeConstraint(QHBoxLayout.SetFixedSize)
        self.art_hot = QLabel(self.centralwidget)
        self.art_hot.setObjectName("art_hot")
        self.art_hot.setMinimumSize(QSize(0, 35))
        self.art_hot.setMaximumSize(QSize(16777215, 35))
        self.art_hot.setFont(font2)
        self.art_hot.setStyleSheet('color: rgb(0, 0, 0);\nfont: 14pt "\u5b8b\u4f53";\n')

        self.art_hot_first.addWidget(self.art_hot)

        self.art_hot_more = QPushButton(self.centralwidget)
        self.art_hot_more.setObjectName("art_hot_more")
        self.art_hot_more.setMinimumSize(QSize(80, 35))
        self.art_hot_more.setMaximumSize(QSize(80, 35))
        self.art_hot_more.setStyleSheet('color: rgb(0, 0, 0);\nfont: 9pt "\u5b8b\u4f53";')

        self.art_hot_first.addWidget(self.art_hot_more)

        self.art_hot_all.addLayout(self.art_hot_first)

        self.art_image = QLabel(self.centralwidget)
        self.art_image.setObjectName("art_image")
        self.art_image.setMinimumSize(QSize(278, 140))
        self.art_image.setMaximumSize(QSize(278, 278))

        self.art_hot_all.addWidget(self.art_image)

        self.showcase.addLayout(self.art_hot_all)

        self.verticalLayout.addLayout(self.showcase)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.page_name.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:700;">\u9996\u9875</span></p></body></html>',
                None,
            )
        )
        self.Project_Button_icon.setText("")
        self.Project.setText(QCoreApplication.translate("MainWindow", "\u975e\u9057\u9879\u76ee", None))
        self.Trivia_Button_icon.setText("")
        self.Trivia.setText(QCoreApplication.translate("MainWindow", "\u7591\u95ee\u54a8\u8be2", None))
        self.Image_Button_icon.setText("")
        self.image_recognition.setText(QCoreApplication.translate("MainWindow", "\u56fe\u50cf\u8bc6\u522b", None))
        self.Cultural_Button_icon.setText("")
        self.Cultural.setText(QCoreApplication.translate("MainWindow", "\u6587\u5316\u4f53\u9a8c", None))
        self.Bbs_Button_icon.setText("")
        self.bbs.setText(QCoreApplication.translate("MainWindow", "\u8bba\u575b", None))
        self.More_Button_icon.setText("")
        self.More.setText(QCoreApplication.translate("MainWindow", "\u66f4\u591a", None))
        self.project_hot.setText(QCoreApplication.translate("MainWindow", "\u70ed\u95e8\u975e\u9057\u9879\u76ee", None))
        self.project_hot_more.setText(QCoreApplication.translate("MainWindow", "\u67e5\u770b\u66f4\u591a>", None))
        self.hot_image.setText(QCoreApplication.translate("MainWindow", "TextLabel", None))
        self.recommend.setText(QCoreApplication.translate("MainWindow", "\u4e2a\u6027\u5316\u63a8\u8350", None))
        self.recommend_more.setText(QCoreApplication.translate("MainWindow", "\u67e5\u770b\u66f4\u591a>", None))
        self.recommend_image.setText(QCoreApplication.translate("MainWindow", "TextLabel", None))
        self.art_hot.setText(QCoreApplication.translate("MainWindow", "\u70ed\u95e8\u4f5c\u54c1", None))
        self.art_hot_more.setText(QCoreApplication.translate("MainWindow", "\u67e5\u770b\u66f4\u591a>", None))
        self.art_image.setText(QCoreApplication.translate("MainWindow", "TextLabel", None))

    # retranslateUi
