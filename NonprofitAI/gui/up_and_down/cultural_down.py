from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout


class Ui_cultural_down:
    def setupUi(self, cultural_down):
        if not cultural_down.objectName():
            cultural_down.setObjectName("cultural_down")
        cultural_down.resize(863, 524)
        cultural_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(cultural_down)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.offine = QVBoxLayout()
        self.offine.setObjectName("offine")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.offine.addItem(self.verticalSpacer)

        self.offline_btn = QPushButton(cultural_down)
        self.offline_btn.setObjectName("offline_btn")
        self.offline_btn.setMinimumSize(QSize(200, 190))
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.offline_btn.setFont(font)
        self.offline_btn.setStyleSheet("background-color: rgb(197, 197, 197);\ncolor: rgb(0, 0, 0);")

        self.offine.addWidget(self.offline_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.offine.addItem(self.verticalSpacer_3)

        self.horizontalLayout.addLayout(self.offine)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.game = QVBoxLayout()
        self.game.setObjectName("game")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.game.addItem(self.verticalSpacer_2)

        self.game_btn = QPushButton(cultural_down)
        self.game_btn.setObjectName("game_btn")
        self.game_btn.setMinimumSize(QSize(200, 190))
        self.game_btn.setFont(font)
        self.game_btn.setStyleSheet("background-color: rgb(197, 197, 197);\ncolor: rgb(0, 0, 0);")

        self.game.addWidget(self.game_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.game.addItem(self.verticalSpacer_4)

        self.horizontalLayout.addLayout(self.game)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(cultural_down)

        QMetaObject.connectSlotsByName(cultural_down)

    # setupUi

    def retranslateUi(self, cultural_down):
        cultural_down.setWindowTitle(QCoreApplication.translate("cultural_down", "Frame", None))
        self.offline_btn.setText(QCoreApplication.translate("cultural_down", "\u7ebf\u4e0b\u4f53\u9a8c", None))
        self.game_btn.setText(QCoreApplication.translate("cultural_down", "\u5c0f\u6e38\u620f", None))

    # retranslateUi
