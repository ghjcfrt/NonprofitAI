from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout


class Ui_more_down:
    def setupUi(self, more_down):
        if not more_down.objectName():
            more_down.setObjectName("more_down")
        more_down.resize(572, 490)
        more_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(more_down)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.first = QPushButton(more_down)
        self.first.setObjectName("first")
        self.first.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(20)
        font.setBold(True)
        self.first.setFont(font)
        self.first.setStyleSheet("background-color: rgb(181, 181, 181);\ncolor: rgb(0, 0, 0);")
        self.first.setCheckable(False)
        self.first.setAutoRepeat(False)
        self.first.setAutoDefault(False)
        self.first.setFlat(False)

        self.verticalLayout.addWidget(self.first)

        self.second = QPushButton(more_down)
        self.second.setObjectName("second")
        self.second.setMinimumSize(QSize(0, 45))
        self.second.setFont(font)
        self.second.setStyleSheet("background-color: rgb(181, 181, 181);\ncolor: rgb(0, 0, 0);")
        self.second.setCheckable(False)
        self.second.setAutoRepeat(False)
        self.second.setAutoDefault(False)
        self.second.setFlat(False)

        self.verticalLayout.addWidget(self.second)

        self.third = QPushButton(more_down)
        self.third.setObjectName("third")
        self.third.setMinimumSize(QSize(0, 45))
        self.third.setFont(font)
        self.third.setStyleSheet("background-color: rgb(181, 181, 181);\ncolor: rgb(0, 0, 0);")
        self.third.setCheckable(False)
        self.third.setAutoRepeat(False)
        self.third.setAutoDefault(False)
        self.third.setFlat(False)

        self.verticalLayout.addWidget(self.third)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(more_down)

        self.first.setDefault(True)
        self.second.setDefault(True)
        self.third.setDefault(True)

        QMetaObject.connectSlotsByName(more_down)

    # setupUi

    def retranslateUi(self, more_down):
        more_down.setWindowTitle(QCoreApplication.translate("more_down", "Frame", None))
        self.first.setText(
            QCoreApplication.translate("more_down", "\u5c0f\u4f17\u975e\u9057\u9879\u76ee\u7533\u8bf7", None)
        )
        self.second.setText(QCoreApplication.translate("more_down", "\u7528\u6237\u53cd\u9988\u7cfb\u7edf", None))
        self.third.setText(
            QCoreApplication.translate("more_down", "\u975e\u9057\u6587\u5316\u4fdd\u62a4\u57fa\u91d1", None)
        )

    # retranslateUi
