from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout


class Ui_detail_down:
    def setupUi(self, detail_down):  # noqa: PLR0915
        if not detail_down.objectName():
            detail_down.setObjectName("detail_down")
        detail_down.resize(875, 976)
        detail_down.setMaximumSize(QSize(16777215, 16777213))
        detail_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(detail_down)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.imglabel = QLabel(detail_down)
        self.imglabel.setObjectName("imglabel")
        self.imglabel.setMinimumSize(QSize(270, 270))
        self.imglabel.setStyleSheet("border-image: url(:/demo.png);")

        self.horizontalLayout.addWidget(self.imglabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.name_all = QVBoxLayout()
        self.name_all.setObjectName("name_all")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.name = QLabel(detail_down)
        self.name.setObjectName("name")
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(25)
        font.setBold(True)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgba(255, 255, 255, 0);")
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.name)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.name_all.addLayout(self.horizontalLayout_2)

        self.name_word = QLabel(detail_down)
        self.name_word.setObjectName("name_word")
        font1 = QFont()
        font1.setFamilies(["\u5b8b\u4f53"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.name_word.setFont(font1)
        self.name_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')
        self.name_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.name_all.addWidget(self.name_word)

        self.verticalLayout_2.addLayout(self.name_all)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.category_all = QVBoxLayout()
        self.category_all.setObjectName("category_all")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.category = QLabel(detail_down)
        self.category.setObjectName("category")
        self.category.setFont(font)
        self.category.setStyleSheet("color: rgb(0, 0, 0);")
        self.category.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.category)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.category_all.addLayout(self.horizontalLayout_3)

        self.category_word = QLabel(detail_down)
        self.category_word.setObjectName("category_word")
        self.category_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')
        self.category_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.category_all.addWidget(self.category_word)

        self.verticalLayout_2.addLayout(self.category_all)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.area_all = QVBoxLayout()
        self.area_all.setObjectName("area_all")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.area = QLabel(detail_down)
        self.area.setObjectName("area")
        self.area.setFont(font)
        self.area.setStyleSheet("color: rgb(0, 0, 0);")
        self.area.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.area)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.area_all.addLayout(self.horizontalLayout_4)

        self.area_word = QLabel(detail_down)
        self.area_word.setObjectName("area_word")
        self.area_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')
        self.area_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.area_all.addWidget(self.area_word)

        self.verticalLayout_2.addLayout(self.area_all)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.introduction_all = QVBoxLayout()
        self.introduction_all.setObjectName("introduction_all")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.introduction = QLabel(detail_down)
        self.introduction.setObjectName("introduction")
        self.introduction.setFont(font)
        self.introduction.setStyleSheet("color: rgb(0, 0, 0);")
        self.introduction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.introduction)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.introduction_all.addLayout(self.horizontalLayout_5)

        self.introduction_word = QLabel(detail_down)
        self.introduction_word.setObjectName("introduction_word")
        self.introduction_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')

        self.introduction_all.addWidget(self.introduction_word)

        self.verticalLayout_2.addLayout(self.introduction_all)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.history_all = QVBoxLayout()
        self.history_all.setObjectName("history_all")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.history = QLabel(detail_down)
        self.history.setObjectName("history")
        self.history.setFont(font)
        self.history.setStyleSheet("color: rgb(0, 0, 0);")
        self.history.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.history)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.history_all.addLayout(self.horizontalLayout_6)

        self.history_word = QLabel(detail_down)
        self.history_word.setObjectName("history_word")
        self.history_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')

        self.history_all.addWidget(self.history_word)

        self.verticalLayout_2.addLayout(self.history_all)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(detail_down)

        QMetaObject.connectSlotsByName(detail_down)

    # setupUi

    def retranslateUi(self, detail_down):
        detail_down.setWindowTitle(QCoreApplication.translate("detail_down", "Frame", None))
        self.imglabel.setText(QCoreApplication.translate("detail_down", "TextLabel", None))
        self.name.setText(QCoreApplication.translate("detail_down", "\u540d\u79f0", None))
        self.name_word.setText(QCoreApplication.translate("detail_down", "TextLabel", None))
        self.category.setText(QCoreApplication.translate("detail_down", "\u7c7b\u522b", None))
        self.category_word.setText(QCoreApplication.translate("detail_down", "TextLabel", None))
        self.area.setText(QCoreApplication.translate("detail_down", "\u5730\u533a", None))
        self.area_word.setText(QCoreApplication.translate("detail_down", "TextLabel", None))
        self.introduction.setText(QCoreApplication.translate("detail_down", "\u7b80\u4ecb", None))
        self.introduction_word.setText(QCoreApplication.translate("detail_down", "TextLabel", None))
        self.history.setText(QCoreApplication.translate("detail_down", "\u5386\u53f2", None))
        self.history_word.setText(QCoreApplication.translate("detail_down", "TextLabel", None))

    # retranslateUi
