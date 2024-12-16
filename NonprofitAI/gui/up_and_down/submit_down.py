# submit_down.py
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout


class Ui_submit_down:
    def setupUi(self, submit_down):  # noqa: PLR0915
        if not submit_down.objectName():
            submit_down.setObjectName("submit_down")
        submit_down.resize(683, 505)
        submit_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout_9 = QHBoxLayout(submit_down)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name_all = QHBoxLayout()
        self.name_all.setObjectName("name_all")
        self.name = QLabel(submit_down)
        self.name.setObjectName("name")
        self.name.setMinimumSize(QSize(70, 31))
        self.name.setMaximumSize(QSize(70, 31))
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(20)
        font.setBold(True)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgba(255, 255, 255, 0);")

        self.name_all.addWidget(self.name)

        self.name_input = QTextEdit(submit_down)
        self.name_input.setObjectName("name_input")
        font1 = QFont()
        font1.setFamilies(["\u5b8b\u4f53"])
        font1.setPointSize(10)
        self.name_input.setFont(font1)
        self.name_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')

        self.name_all.addWidget(self.name_input)

        self.verticalLayout_3.addLayout(self.name_all)

        self.category_all = QHBoxLayout()
        self.category_all.setObjectName("category_all")
        self.category = QLabel(submit_down)
        self.category.setObjectName("category")
        self.category.setMinimumSize(QSize(70, 31))
        self.category.setMaximumSize(QSize(70, 31))
        self.category.setFont(font)
        self.category.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgba(255, 255, 255, 0);")

        self.category_all.addWidget(self.category)

        self.category_input = QTextEdit(submit_down)
        self.category_input.setObjectName("category_input")
        self.category_input.setFont(font1)
        self.category_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')

        self.category_all.addWidget(self.category_input)

        self.verticalLayout_3.addLayout(self.category_all)

        self.area_all = QHBoxLayout()
        self.area_all.setObjectName("area_all")
        self.area = QLabel(submit_down)
        self.area.setObjectName("area")
        self.area.setMinimumSize(QSize(70, 31))
        self.area.setMaximumSize(QSize(70, 31))
        self.area.setFont(font)
        self.area.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgba(255, 255, 255, 0);")

        self.area_all.addWidget(self.area)

        self.area_input = QTextEdit(submit_down)
        self.area_input.setObjectName("area_input")
        self.area_input.setFont(font1)
        self.area_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')

        self.area_all.addWidget(self.area_input)

        self.verticalLayout_3.addLayout(self.area_all)

        self.introduction_all = QHBoxLayout()
        self.introduction_all.setObjectName("introduction_all")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.introduction = QLabel(submit_down)
        self.introduction.setObjectName("introduction")
        self.introduction.setMinimumSize(QSize(70, 31))
        self.introduction.setMaximumSize(QSize(70, 31))
        self.introduction.setFont(font)
        self.introduction.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.introduction)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.introduction_all.addLayout(self.verticalLayout)

        self.introduction_input = QTextEdit(submit_down)
        self.introduction_input.setObjectName("introduction_input")
        self.introduction_input.setMinimumSize(QSize(0, 135))
        self.introduction_input.setFont(font1)
        self.introduction_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 14pt "\u5b8b\u4f53";')
        self.introduction_input.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )

        self.introduction_all.addWidget(self.introduction_input)

        self.verticalLayout_3.addLayout(self.introduction_all)

        self.history_all = QHBoxLayout()
        self.history_all.setObjectName("history_all")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.history = QLabel(submit_down)
        self.history.setObjectName("history")
        self.history.setMinimumSize(QSize(70, 31))
        self.history.setMaximumSize(QSize(70, 31))
        self.history.setFont(font)
        self.history.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_2.addWidget(self.history)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.history_all.addLayout(self.verticalLayout_2)

        self.history_input = QTextEdit(submit_down)
        self.history_input.setObjectName("history_input")
        self.history_input.setMinimumSize(QSize(0, 135))
        self.history_input.setFont(font1)
        self.history_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 14pt "\u5b8b\u4f53";')
        self.history_input.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )

        self.history_all.addWidget(self.history_input)

        self.verticalLayout_3.addLayout(self.history_all)

        self.image_all = QHBoxLayout()
        self.image_all.setObjectName("image_all")
        self.image = QLabel(submit_down)
        self.image.setObjectName("image")
        self.image.setMinimumSize(QSize(70, 31))
        self.image.setMaximumSize(QSize(70, 31))
        self.image.setFont(font)
        self.image.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgba(255, 255, 255, 0);")

        self.image_all.addWidget(self.image)

        self.image_input = QLabel(submit_down)
        self.image_input.setObjectName("image_input")
        self.image_input.setMinimumSize(QSize(0, 0))
        self.image_input.setMaximumSize(QSize(16777215, 29))
        self.image_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 14pt "\u5b8b\u4f53";')

        self.image_all.addWidget(self.image_input)

        self.pushButton_2 = QPushButton(submit_down)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(70, 30))
        font2 = QFont()
        font2.setFamilies(["\u5b8b\u4f53"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(172, 172, 172);")

        self.image_all.addWidget(self.pushButton_2)

        self.verticalLayout_3.addLayout(self.image_all)

        self.verify_all = QHBoxLayout()
        self.verify_all.setObjectName("verify_all")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verify_all.addItem(self.horizontalSpacer_3)

        self.verify = QPushButton(submit_down)
        self.verify.setObjectName("verify")
        font3 = QFont()
        font3.setFamilies(["\u5b8b\u4f53"])
        font3.setPointSize(21)
        font3.setBold(True)
        self.verify.setFont(font3)
        self.verify.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(181, 181, 181);")

        self.verify_all.addWidget(self.verify)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verify_all.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3.addLayout(self.verify_all)

        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.retranslateUi(submit_down)

        QMetaObject.connectSlotsByName(submit_down)

    # setupUi

    def retranslateUi(self, submit_down):
        submit_down.setWindowTitle(QCoreApplication.translate("submit_down", "Frame", None))
        self.name.setText(QCoreApplication.translate("submit_down", "\u540d\u79f0\uff1a", None))
        self.category.setText(QCoreApplication.translate("submit_down", "\u7c7b\u522b\uff1a", None))
        self.area.setText(QCoreApplication.translate("submit_down", "\u5730\u533a\uff1a", None))
        self.introduction.setText(QCoreApplication.translate("submit_down", "\u7b80\u4ecb\uff1a", None))
        self.history.setText(QCoreApplication.translate("submit_down", "\u5386\u53f2\uff1a", None))
        self.image.setText(QCoreApplication.translate("submit_down", "\u56fe\u7247\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("submit_down", "\u4e0a\u4f20", None))
        self.verify.setText(QCoreApplication.translate("submit_down", "\u786e\u8ba4", None))

    # retranslateUi
