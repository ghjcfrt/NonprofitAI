# feedback_down.py
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextEdit,
    QVBoxLayout,
)


class Ui_feedback_down:
    def setupUi(self, feedback_down):  # noqa: PLR0915
        if not feedback_down.objectName():
            feedback_down.setObjectName("feedback_down")
        feedback_down.resize(670, 465)
        feedback_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(feedback_down)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.feedback_word = QLabel(feedback_down)
        self.feedback_word.setObjectName("feedback_word")
        self.feedback_word.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.feedback_word.setFont(font)
        self.feedback_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";\nfont-weight: bold;')

        self.horizontalLayout.addWidget(self.feedback_word)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.feedback_input = QTextEdit(feedback_down)
        self.feedback_input.setObjectName("feedback_input")
        self.feedback_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 15pt "\u5b8b\u4f53";')

        self.verticalLayout.addWidget(self.feedback_input)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.contact_word = QLabel(feedback_down)
        self.contact_word.setObjectName("contact_word")
        self.contact_word.setMinimumSize(QSize(0, 30))
        self.contact_word.setFont(font)
        self.contact_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";\nfont-weight: bold;')

        self.horizontalLayout_2.addWidget(self.contact_word)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.contact_input = QLineEdit(feedback_down)
        self.contact_input.setObjectName("contact_input")
        self.contact_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 15pt "\u5b8b\u4f53";')
        self.contact_input.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )

        self.verticalLayout.addWidget(self.contact_input)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.name_word = QLabel(feedback_down)
        self.name_word.setObjectName("name_word")
        self.name_word.setMinimumSize(QSize(0, 30))
        self.name_word.setFont(font)
        self.name_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 20pt "\u5b8b\u4f53";\nfont-weight: bold;')

        self.horizontalLayout_3.addWidget(self.name_word)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.name_input = QLineEdit(feedback_down)
        self.name_input.setObjectName("name_input")
        self.name_input.setStyleSheet('color: rgb(0, 0, 0);\nfont: 15pt "\u5b8b\u4f53";')
        self.name_input.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )

        self.verticalLayout.addWidget(self.name_input)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.verify_btn = QPushButton(feedback_down)
        self.verify_btn.setObjectName("verify_btn")
        self.verify_btn.setMaximumSize(QSize(75, 35))
        self.verify_btn.setStyleSheet('color: rgb(0, 0, 0);\nfont-weight: bold;\nfont: 20pt "\u5b8b\u4f53";')

        self.horizontalLayout_4.addWidget(self.verify_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(feedback_down)

        QMetaObject.connectSlotsByName(feedback_down)

    # setupUi

    def retranslateUi(self, feedback_down):
        feedback_down.setWindowTitle(QCoreApplication.translate("feedback_down", "Frame", None))
        self.feedback_word.setText(QCoreApplication.translate("feedback_down", "\u610f\u89c1\u53cd\u9988\uff1a", None))
        self.contact_word.setText(QCoreApplication.translate("feedback_down", "\u8054\u7cfb\u65b9\u5f0f\uff1a", None))
        self.contact_input.setText("")
        self.name_word.setText(QCoreApplication.translate("feedback_down", "\u6635\u79f0\uff1a", None))
        self.verify_btn.setText(QCoreApplication.translate("feedback_down", "\u786e\u8ba4", None))

    # retranslateUi
