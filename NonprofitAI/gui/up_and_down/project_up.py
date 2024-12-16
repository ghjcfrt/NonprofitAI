from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget


class Ui_MainWindow:
    def setupUi(self, MainWindow):  # noqa: PLR0915
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 500)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QHBoxLayout()
        self.top.setObjectName("top")
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName("back")
        self.back.setEnabled(False)
        self.back.setMinimumSize(QSize(75, 31))
        self.back.setMaximumSize(QSize(75, 31))
        font1 = QFont()
        font1.setFamilies(["\u5b8b\u4f53"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.back.setFont(font1)
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
        font2 = QFont()
        font2.setFamilies(["\u5b8b\u4f53"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.page_name.setFont(font2)
        self.page_name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page_name.setStyleSheet(
            'color:rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";\nbackground-color: rgb(168,218,181);\n'
        )
        self.page_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.top.addWidget(self.page_name, 0, Qt.AlignmentFlag.AlignTop)

        self.home_page = QPushButton(self.centralwidget)
        self.home_page.setObjectName("home_page")
        self.home_page.setEnabled(False)
        self.home_page.setMinimumSize(QSize(75, 31))
        self.home_page.setMaximumSize(QSize(75, 31))
        self.home_page.setFont(font1)
        self.home_page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.home_page.setStyleSheet(
            "color:rgb(0, 0, 0);\n"
            'font: 15pt "\u5b8b\u4f53";\n'
            "background-color: rgb(168,218,181);\n"
            "border-color: rgb(168,218,181);\n"
            "border-radius: 0px;"
        )
        self.home_page.setAutoRepeatInterval(100)

        self.top.addWidget(self.home_page, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addLayout(self.top)

        self.verticalSpacer = QSpacerItem(17, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.back.setText(QCoreApplication.translate("MainWindow", "<\u8fd4\u56de", None))
        self.page_name.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u9879\u76ee</p></body></html>",
                None,
            )
        )
        self.home_page.setText(QCoreApplication.translate("MainWindow", "\u9996\u9875", None))

    # retranslateUi
