from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout


class Ui_recommend_down:
    def setupUi(self, recommend_down):
        if not recommend_down.objectName():
            recommend_down.setObjectName("recommend_down")
        recommend_down.resize(568, 570)
        recommend_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(recommend_down)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self._1 = QHBoxLayout()
        self._1.setObjectName("_1")
        self._1_1 = QPushButton(recommend_down)
        self._1_1.setObjectName("_1_1")
        self._1_1.setMinimumSize(QSize(270, 270))
        self._1_1.setMaximumSize(QSize(270, 270))
        self._1_1.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-image: url(:/demo.png);")

        self._1.addWidget(self._1_1)

        self._1_2 = QPushButton(recommend_down)
        self._1_2.setObjectName("_1_2")
        self._1_2.setMinimumSize(QSize(270, 270))
        self._1_2.setMaximumSize(QSize(270, 270))
        self._1_2.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-image: url(:/demo.png);")

        self._1.addWidget(self._1_2)

        self.verticalLayout.addLayout(self._1)

        self._2 = QHBoxLayout()
        self._2.setObjectName("_2")
        self._2_1 = QPushButton(recommend_down)
        self._2_1.setObjectName("_2_1")
        self._2_1.setMinimumSize(QSize(270, 270))
        self._2_1.setMaximumSize(QSize(270, 270))
        self._2_1.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-image: url(:/demo.png);")

        self._2.addWidget(self._2_1)

        self._2_2 = QPushButton(recommend_down)
        self._2_2.setObjectName("_2_2")
        self._2_2.setMinimumSize(QSize(270, 270))
        self._2_2.setMaximumSize(QSize(270, 270))
        self._2_2.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-image: url(:/demo.png);")

        self._2.addWidget(self._2_2)

        self.verticalLayout.addLayout(self._2)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(recommend_down)

        QMetaObject.connectSlotsByName(recommend_down)

    # setupUi

    def retranslateUi(self, recommend_down):
        recommend_down.setWindowTitle(QCoreApplication.translate("recommend_down", "Frame", None))
        self._1_1.setText("")
        self._1_2.setText("")
        self._2_1.setText("")
        self._2_2.setText("")

    # retranslateUi
