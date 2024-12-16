# game_down.py
from PySide6.QtCore import QCoreApplication, QLocale, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout


class Ui_game_down:
    def setupUi(self, game_down):  # noqa: PLR0915
        if not game_down.objectName():
            game_down.setObjectName("game_down")
        game_down.resize(798, 522)
        game_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(game_down)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.word_all = QHBoxLayout()
        self.word_all.setObjectName("word_all")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.word_all.addItem(self.horizontalSpacer_3)

        self.word = QLabel(game_down)
        self.word.setObjectName("word")
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(40)
        font.setBold(True)
        self.word.setFont(font)
        self.word.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.word.setStyleSheet("color: rgb(0, 0, 0);")
        self.word.setLocale(QLocale(QLocale.Church, QLocale.Russia))
        self.word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.word_all.addWidget(self.word)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.word_all.addItem(self.horizontalSpacer_4)

        self.verticalLayout.addLayout(self.word_all)

        self.image_all = QHBoxLayout()
        self.image_all.setObjectName("image_all")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.image_all.addItem(self.horizontalSpacer)

        self.image = QPushButton(game_down)
        self.image.setObjectName("image")
        self.image.setMinimumSize(QSize(200, 200))
        self.image.setMaximumSize(QSize(200, 200))
        self.image.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.image.setStyleSheet("border-image: url(:/demo.png);\nbackground-color: rgba(255, 255, 255, 0);")
        self.image.setEnabled(True)

        self.image_all.addWidget(self.image)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.image_all.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.image_all)

        self.lineEdit = QLineEdit(game_down)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamilies(["\u5b8b\u4f53"])
        font1.setPointSize(33)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(168, 168, 168);")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.check_btn = QPushButton(game_down)
        self.check_btn.setObjectName("check_btn")
        font2 = QFont()
        font2.setFamilies(["\u5b8b\u4f53"])
        font2.setPointSize(25)
        font2.setBold(True)
        self.check_btn.setFont(font2)
        self.check_btn.setStyleSheet("color: rgb(0, 0, 0);\nbackground-color: rgb(177, 177, 177);")

        self.horizontalLayout_2.addWidget(self.check_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(game_down)

        QMetaObject.connectSlotsByName(game_down)

    # setupUi

    def retranslateUi(self, game_down):
        game_down.setWindowTitle(QCoreApplication.translate("game_down", "Frame", None))
        self.word.setText(QCoreApplication.translate("game_down", "\u770b\u56fe\u77e5\u975e\u9057", None))
        self.image.setText("")
        self.lineEdit.setText("")
        self.check_btn.setText(QCoreApplication.translate("game_down", "\u786e\u8ba4", None))

    # retranslateUi
