from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget


class Ui_detail_up:
    def setupUi(self, detail_up):  # noqa: PLR0915
        if not detail_up.objectName():
            detail_up.setObjectName("detail_up")
        detail_up.resize(800, 600)
        detail_up.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(detail_up)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QHBoxLayout()
        self.top.setObjectName("top")
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName("back")
        self.back.setEnabled(True)
        self.back.setMinimumSize(QSize(75, 31))
        self.back.setMaximumSize(QSize(75, 31))
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.back.setFont(font)
        self.back.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.back.setStyleSheet(
            "color:rgb(0, 0, 0);\n"
            'font: 15pt "\u5b8b\u4f53";\n'
            "background-color: rgb(168,218,181);\n"
            "border-color: rgb(168,218,181);\n"
            "border-radius: 0px;"
        )
        self.back.setAutoRepeatInterval(100)

        self.top.addWidget(self.back, 0, Qt.AlignmentFlag.AlignTop)

        self.page_name = QLabel(self.centralwidget)
        self.page_name.setObjectName("page_name")
        self.page_name.setMinimumSize(QSize(0, 31))
        self.page_name.setMaximumSize(QSize(16777215, 31))
        font1 = QFont()
        font1.setFamilies(["\u5b8b\u4f53"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.page_name.setFont(font1)
        self.page_name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page_name.setStyleSheet(
            'color:rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";\nbackground-color: rgb(168,218,181);\n'
        )
        self.page_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.top.addWidget(self.page_name)

        self.home_page = QPushButton(self.centralwidget)
        self.home_page.setObjectName("home_page")
        self.home_page.setEnabled(True)
        self.home_page.setMinimumSize(QSize(75, 31))
        self.home_page.setMaximumSize(QSize(75, 31))
        self.home_page.setFont(font)
        self.home_page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.home_page.setStyleSheet(
            "color:rgb(0, 0, 0);\n"
            'font: 15pt "\u5b8b\u4f53";\n'
            "background-color: rgb(168,218,181);\n"
            "border-color: rgb(168,218,181);\n"
            "border-radius: 0px;"
        )
        self.home_page.setAutoRepeatInterval(100)

        self.top.addWidget(self.home_page)

        self.verticalLayout.addLayout(self.top)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        detail_up.setCentralWidget(self.centralwidget)

        self.retranslateUi(detail_up)

        QMetaObject.connectSlotsByName(detail_up)

    # setupUi

    def retranslateUi(self, detail_up):
        detail_up.setWindowTitle(QCoreApplication.translate("detail_up", "MainWindow", None))
        self.back.setText(QCoreApplication.translate("detail_up", "<\u8fd4\u56de", None))
        self.page_name.setText(
            QCoreApplication.translate(
                "detail_up",
                "<html><head/><body><p>\u8be6\u60c5</p></body></html>",
                None,
            )
        )
        self.home_page.setText(QCoreApplication.translate("detail_up", "\u9996\u9875", None))

    # retranslateUi