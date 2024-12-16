from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout


class Ui_fund_down:
    def setupUi(self, fund_down):  # noqa: PLR0915
        if not fund_down.objectName():
            fund_down.setObjectName("fund_down")
        fund_down.resize(729, 540)
        fund_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(fund_down)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(160, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text = QLabel(fund_down)
        self.text.setObjectName("text")
        self.text.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(25)
        font.setBold(True)
        self.text.setFont(font)
        self.text.setStyleSheet("color: rgb(0, 0, 0);")
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.text)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.name = QLabel(fund_down)
        self.name.setObjectName("name")
        self.name.setMinimumSize(QSize(70, 35))
        self.name.setMaximumSize(QSize(70, 35))
        font1 = QFont()
        font1.setFamilies(["\u5b8b\u4f53"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.name.setFont(font1)
        self.name.setStyleSheet("color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.name)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.name_display = QLabel(fund_down)
        self.name_display.setObjectName("name_display")
        self.name_display.setMinimumSize(QSize(150, 40))
        self.name_display.setMaximumSize(QSize(200, 50))
        self.name_display.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')
        self.name_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.name_display)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.phone = QLabel(fund_down)
        self.phone.setObjectName("phone")
        self.phone.setMinimumSize(QSize(70, 35))
        self.phone.setMaximumSize(QSize(70, 35))
        self.phone.setFont(font1)
        self.phone.setStyleSheet("color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.phone)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.phone_display = QLabel(fund_down)
        self.phone_display.setObjectName("phone_display")
        self.phone_display.setMinimumSize(QSize(150, 40))
        self.phone_display.setMaximumSize(QSize(200, 50))
        self.phone_display.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')
        self.phone_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.phone_display)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.wechat = QLabel(fund_down)
        self.wechat.setObjectName("wechat")
        self.wechat.setMinimumSize(QSize(70, 35))
        self.wechat.setMaximumSize(QSize(70, 35))
        self.wechat.setFont(font1)
        self.wechat.setStyleSheet("color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.wechat)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.wechat_display = QLabel(fund_down)
        self.wechat_display.setObjectName("wechat_display")
        self.wechat_display.setMinimumSize(QSize(150, 40))
        self.wechat_display.setMaximumSize(QSize(200, 50))
        self.wechat_display.setSizeIncrement(QSize(0, 0))
        self.wechat_display.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')
        self.wechat_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.wechat_display)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.adress = QLabel(fund_down)
        self.adress.setObjectName("adress")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adress.sizePolicy().hasHeightForWidth())
        self.adress.setSizePolicy(sizePolicy)
        self.adress.setMinimumSize(QSize(70, 35))
        self.adress.setMaximumSize(QSize(70, 35))
        self.adress.setFont(font1)
        self.adress.setStyleSheet("color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.adress)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.adress_display = QLabel(fund_down)
        self.adress_display.setObjectName("adress_display")
        self.adress_display.setMinimumSize(QSize(300, 100))
        self.adress_display.setMaximumSize(QSize(700, 16777215))
        self.adress_display.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";')
        self.adress_display.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )

        self.horizontalLayout.addWidget(self.adress_display)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(160, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.retranslateUi(fund_down)

        QMetaObject.connectSlotsByName(fund_down)

    # setupUi

    def retranslateUi(self, fund_down):
        fund_down.setWindowTitle(QCoreApplication.translate("fund_down", "Frame", None))
        self.text.setText(
            QCoreApplication.translate(
                "fund_down", "\u5982\u9700\u8d44\u91d1\u6216\u6350\u6b3e\n\u8bf7\u8054\u7cfb", None
            )
        )
        self.name.setText(QCoreApplication.translate("fund_down", "\u59d3\u540d\uff1a", None))
        self.name_display.setText("")
        self.phone.setText(QCoreApplication.translate("fund_down", "\u7535\u8bdd\uff1a", None))
        self.phone_display.setText("")
        self.wechat.setText(QCoreApplication.translate("fund_down", "\u5fae\u4fe1\uff1a", None))
        self.wechat_display.setText("")
        self.adress.setText(QCoreApplication.translate("fund_down", "\u5730\u5740\uff1a", None))
        self.adress_display.setText("")

    # retranslateUi
