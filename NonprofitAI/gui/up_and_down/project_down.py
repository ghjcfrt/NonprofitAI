from PySide6.QtCore import QCoreApplication, QLocale, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Ui_project_down:
    def setupUi(self, project_down):  # noqa: PLR0915
        if not project_down.objectName():
            project_down.setObjectName("project_down")
        project_down.resize(400, 632)
        project_down.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(project_down)
        self.verticalLayout.setObjectName("verticalLayout")
        self.project_down_all = QVBoxLayout()
        self.project_down_all.setObjectName("project_down_all")
        self.top_all = QHBoxLayout()
        self.top_all.setObjectName("top_all")
        self.top_all.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.top_all.setContentsMargins(-1, 0, -1, -1)
        self.categorization = QComboBox(project_down)
        self.categorization.addItem("")
        self.categorization.addItem("")
        self.categorization.addItem("")
        self.categorization.addItem("")
        self.categorization.addItem("")
        self.categorization.addItem("")
        self.categorization.addItem("")
        self.categorization.addItem("")
        self.categorization.addItem("")
        self.categorization.setObjectName("categorization")
        self.categorization.setMinimumSize(QSize(160, 22))
        self.categorization.setMaximumSize(QSize(160, 22))
        font = QFont()
        font.setFamilies(["\u5b8b\u4f53"])
        font.setPointSize(12)
        self.categorization.setFont(font)
        self.categorization.setStyleSheet("color: rgb(0, 0, 0);")

        self.top_all.addWidget(self.categorization)

        self.none = QLabel(project_down)
        self.none.setObjectName("none")
        self.none.setMinimumSize(QSize(0, 22))
        self.none.setMaximumSize(QSize(16777215, 22))
        self.none.setSizeIncrement(QSize(1, 0))

        self.top_all.addWidget(self.none)

        self.project_down_all.addLayout(self.top_all)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.project_down_all.addItem(self.verticalSpacer_7)

        self.first_all = QHBoxLayout()
        self.first_all.setObjectName("first_all")
        self._1_1 = QVBoxLayout()
        self._1_1.setObjectName("_1_1")
        self.btn_1_1 = QPushButton(project_down)
        self.btn_1_1.setObjectName("btn_1_1")
        self.btn_1_1.setMinimumSize(QSize(60, 60))
        self.btn_1_1.setMaximumSize(QSize(60, 60))
        self.btn_1_1.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_1_1.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._1_1.addWidget(self.btn_1_1)

        self.name_1_1 = QLabel(project_down)
        self.name_1_1.setObjectName("name_1_1")
        self.name_1_1.setMinimumSize(QSize(60, 15))
        self.name_1_1.setMaximumSize(QSize(60, 15))
        self.name_1_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._1_1.addWidget(self.name_1_1)

        self.first_all.addLayout(self._1_1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.first_all.addItem(self.horizontalSpacer)

        self._1_2 = QVBoxLayout()
        self._1_2.setObjectName("_1_2")
        self.btn_1_2 = QPushButton(project_down)
        self.btn_1_2.setObjectName("btn_1_2")
        self.btn_1_2.setMinimumSize(QSize(60, 60))
        self.btn_1_2.setMaximumSize(QSize(60, 60))
        self.btn_1_2.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_1_2.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._1_2.addWidget(self.btn_1_2)

        self.name_1_2 = QLabel(project_down)
        self.name_1_2.setObjectName("name_1_2")
        self.name_1_2.setMinimumSize(QSize(60, 15))
        self.name_1_2.setMaximumSize(QSize(60, 15))
        self.name_1_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._1_2.addWidget(self.name_1_2)

        self.first_all.addLayout(self._1_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.first_all.addItem(self.horizontalSpacer_2)

        self._1_3 = QVBoxLayout()
        self._1_3.setObjectName("_1_3")
        self.btn_1_3 = QPushButton(project_down)
        self.btn_1_3.setObjectName("btn_1_3")
        self.btn_1_3.setMinimumSize(QSize(60, 60))
        self.btn_1_3.setMaximumSize(QSize(60, 60))
        self.btn_1_3.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_1_3.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._1_3.addWidget(self.btn_1_3)

        self.name_1_3 = QLabel(project_down)
        self.name_1_3.setObjectName("name_1_3")
        self.name_1_3.setMinimumSize(QSize(60, 15))
        self.name_1_3.setMaximumSize(QSize(60, 15))
        self.name_1_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._1_3.addWidget(self.name_1_3)

        self.first_all.addLayout(self._1_3)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.first_all.addItem(self.horizontalSpacer_9)

        self._1_4 = QVBoxLayout()
        self._1_4.setObjectName("_1_4")
        self.btn_1_4 = QPushButton(project_down)
        self.btn_1_4.setObjectName("btn_1_4")
        self.btn_1_4.setMinimumSize(QSize(60, 60))
        self.btn_1_4.setMaximumSize(QSize(60, 60))
        self.btn_1_4.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_1_4.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._1_4.addWidget(self.btn_1_4)

        self.name_1_4 = QLabel(project_down)
        self.name_1_4.setObjectName("name_1_4")
        self.name_1_4.setMinimumSize(QSize(60, 15))
        self.name_1_4.setMaximumSize(QSize(60, 15))
        self.name_1_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_1_4.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        self._1_4.addWidget(self.name_1_4)

        self.first_all.addLayout(self._1_4)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.first_all.addItem(self.horizontalSpacer_19)

        self._1_5 = QVBoxLayout()
        self._1_5.setObjectName("_1_5")
        self.btn_1_5 = QPushButton(project_down)
        self.btn_1_5.setObjectName("btn_1_5")
        self.btn_1_5.setMinimumSize(QSize(60, 60))
        self.btn_1_5.setMaximumSize(QSize(60, 60))
        self.btn_1_5.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_1_5.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._1_5.addWidget(self.btn_1_5)

        self.name_1_5 = QLabel(project_down)
        self.name_1_5.setObjectName("name_1_5")
        self.name_1_5.setMinimumSize(QSize(60, 15))
        self.name_1_5.setMaximumSize(QSize(60, 15))
        self.name_1_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_1_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._1_5.addWidget(self.name_1_5)

        self.first_all.addLayout(self._1_5)

        self.project_down_all.addLayout(self.first_all)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.project_down_all.addItem(self.verticalSpacer)

        self.second_all = QHBoxLayout()
        self.second_all.setObjectName("second_all")
        self._2_1 = QVBoxLayout()
        self._2_1.setObjectName("_2_1")
        self.btn_2_1 = QPushButton(project_down)
        self.btn_2_1.setObjectName("btn_2_1")
        self.btn_2_1.setMinimumSize(QSize(60, 60))
        self.btn_2_1.setMaximumSize(QSize(60, 60))
        self.btn_2_1.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_2_1.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._2_1.addWidget(self.btn_2_1)

        self.name_2_1 = QLabel(project_down)
        self.name_2_1.setObjectName("name_2_1")
        self.name_2_1.setMinimumSize(QSize(60, 15))
        self.name_2_1.setMaximumSize(QSize(60, 15))
        self.name_2_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_2_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._2_1.addWidget(self.name_2_1)

        self.second_all.addLayout(self._2_1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.second_all.addItem(self.horizontalSpacer_20)

        self._2_2 = QVBoxLayout()
        self._2_2.setObjectName("_2_2")
        self.btn_2_2 = QPushButton(project_down)
        self.btn_2_2.setObjectName("btn_2_2")
        self.btn_2_2.setMinimumSize(QSize(60, 60))
        self.btn_2_2.setMaximumSize(QSize(60, 60))
        self.btn_2_2.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_2_2.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._2_2.addWidget(self.btn_2_2)

        self.name_2_2 = QLabel(project_down)
        self.name_2_2.setObjectName("name_2_2")
        self.name_2_2.setMinimumSize(QSize(60, 15))
        self.name_2_2.setMaximumSize(QSize(60, 15))
        self.name_2_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_2_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._2_2.addWidget(self.name_2_2)

        self.second_all.addLayout(self._2_2)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.second_all.addItem(self.horizontalSpacer_21)

        self._2_3 = QVBoxLayout()
        self._2_3.setObjectName("_2_3")
        self.btn_2_3 = QPushButton(project_down)
        self.btn_2_3.setObjectName("btn_2_3")
        self.btn_2_3.setMinimumSize(QSize(60, 60))
        self.btn_2_3.setMaximumSize(QSize(60, 60))
        self.btn_2_3.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_2_3.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._2_3.addWidget(self.btn_2_3)

        self.name_2_3 = QLabel(project_down)
        self.name_2_3.setObjectName("name_2_3")
        self.name_2_3.setMinimumSize(QSize(60, 15))
        self.name_2_3.setMaximumSize(QSize(60, 15))
        self.name_2_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_2_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._2_3.addWidget(self.name_2_3)

        self.second_all.addLayout(self._2_3)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.second_all.addItem(self.horizontalSpacer_24)

        self._2_4 = QVBoxLayout()
        self._2_4.setObjectName("_2_4")
        self.btn_2_4 = QPushButton(project_down)
        self.btn_2_4.setObjectName("btn_2_4")
        self.btn_2_4.setMinimumSize(QSize(60, 60))
        self.btn_2_4.setMaximumSize(QSize(60, 60))
        self.btn_2_4.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_2_4.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._2_4.addWidget(self.btn_2_4)

        self.name_2_4 = QLabel(project_down)
        self.name_2_4.setObjectName("name_2_4")
        self.name_2_4.setMinimumSize(QSize(60, 15))
        self.name_2_4.setMaximumSize(QSize(60, 15))
        self.name_2_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_2_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._2_4.addWidget(self.name_2_4)

        self.second_all.addLayout(self._2_4)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.second_all.addItem(self.horizontalSpacer_25)

        self._2_5 = QVBoxLayout()
        self._2_5.setObjectName("_2_5")
        self.btn_2_5 = QPushButton(project_down)
        self.btn_2_5.setObjectName("btn_2_5")
        self.btn_2_5.setMinimumSize(QSize(60, 60))
        self.btn_2_5.setMaximumSize(QSize(60, 60))
        self.btn_2_5.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_2_5.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._2_5.addWidget(self.btn_2_5)

        self.name_2_5 = QLabel(project_down)
        self.name_2_5.setObjectName("name_2_5")
        self.name_2_5.setMinimumSize(QSize(60, 15))
        self.name_2_5.setMaximumSize(QSize(60, 15))
        self.name_2_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_2_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._2_5.addWidget(self.name_2_5)

        self.second_all.addLayout(self._2_5)

        self.project_down_all.addLayout(self.second_all)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.project_down_all.addItem(self.verticalSpacer_2)

        self.third_all = QHBoxLayout()
        self.third_all.setObjectName("third_all")
        self._3_1 = QVBoxLayout()
        self._3_1.setObjectName("_3_1")
        self.btn_3_1 = QPushButton(project_down)
        self.btn_3_1.setObjectName("btn_3_1")
        self.btn_3_1.setMinimumSize(QSize(60, 60))
        self.btn_3_1.setMaximumSize(QSize(60, 60))
        self.btn_3_1.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_3_1.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._3_1.addWidget(self.btn_3_1)

        self.name_3_1 = QLabel(project_down)
        self.name_3_1.setObjectName("name_3_1")
        self.name_3_1.setMinimumSize(QSize(60, 15))
        self.name_3_1.setMaximumSize(QSize(60, 15))
        self.name_3_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._3_1.addWidget(self.name_3_1)

        self.third_all.addLayout(self._3_1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.third_all.addItem(self.horizontalSpacer_26)

        self._3_2 = QVBoxLayout()
        self._3_2.setObjectName("_3_2")
        self.btn_3_2 = QPushButton(project_down)
        self.btn_3_2.setObjectName("btn_3_2")
        self.btn_3_2.setMinimumSize(QSize(60, 60))
        self.btn_3_2.setMaximumSize(QSize(60, 60))
        self.btn_3_2.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_3_2.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._3_2.addWidget(self.btn_3_2)

        self.name_3_2 = QLabel(project_down)
        self.name_3_2.setObjectName("name_3_2")
        self.name_3_2.setMinimumSize(QSize(60, 15))
        self.name_3_2.setMaximumSize(QSize(60, 15))
        self.name_3_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._3_2.addWidget(self.name_3_2)

        self.third_all.addLayout(self._3_2)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.third_all.addItem(self.horizontalSpacer_27)

        self._3_3 = QVBoxLayout()
        self._3_3.setObjectName("_3_3")
        self.btn_3_3 = QPushButton(project_down)
        self.btn_3_3.setObjectName("btn_3_3")
        self.btn_3_3.setMinimumSize(QSize(60, 60))
        self.btn_3_3.setMaximumSize(QSize(60, 60))
        self.btn_3_3.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_3_3.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._3_3.addWidget(self.btn_3_3)

        self.name_3_3 = QLabel(project_down)
        self.name_3_3.setObjectName("name_3_3")
        self.name_3_3.setMinimumSize(QSize(60, 15))
        self.name_3_3.setMaximumSize(QSize(60, 15))
        self.name_3_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_3_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._3_3.addWidget(self.name_3_3)

        self.third_all.addLayout(self._3_3)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.third_all.addItem(self.horizontalSpacer_28)

        self._3_4 = QVBoxLayout()
        self._3_4.setObjectName("_3_4")
        self.btn_3_4 = QPushButton(project_down)
        self.btn_3_4.setObjectName("btn_3_4")
        self.btn_3_4.setMinimumSize(QSize(60, 60))
        self.btn_3_4.setMaximumSize(QSize(60, 60))
        self.btn_3_4.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_3_4.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._3_4.addWidget(self.btn_3_4)

        self.name_3_4 = QLabel(project_down)
        self.name_3_4.setObjectName("name_3_4")
        self.name_3_4.setMinimumSize(QSize(60, 15))
        self.name_3_4.setMaximumSize(QSize(60, 15))
        self.name_3_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._3_4.addWidget(self.name_3_4)

        self.third_all.addLayout(self._3_4)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.third_all.addItem(self.horizontalSpacer_29)

        self._3_5 = QVBoxLayout()
        self._3_5.setObjectName("_3_5")
        self.btn_3_5 = QPushButton(project_down)
        self.btn_3_5.setObjectName("btn_3_5")
        self.btn_3_5.setMinimumSize(QSize(60, 60))
        self.btn_3_5.setMaximumSize(QSize(60, 60))
        self.btn_3_5.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_3_5.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._3_5.addWidget(self.btn_3_5)

        self.name_3_5 = QLabel(project_down)
        self.name_3_5.setObjectName("name_3_5")
        self.name_3_5.setMinimumSize(QSize(60, 15))
        self.name_3_5.setMaximumSize(QSize(60, 15))
        self.name_3_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_3_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._3_5.addWidget(self.name_3_5)

        self.third_all.addLayout(self._3_5)

        self.project_down_all.addLayout(self.third_all)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.project_down_all.addItem(self.verticalSpacer_3)

        self.fourth__all = QHBoxLayout()
        self.fourth__all.setObjectName("fourth__all")
        self._4_1 = QVBoxLayout()
        self._4_1.setObjectName("_4_1")
        self.btn_4_1 = QPushButton(project_down)
        self.btn_4_1.setObjectName("btn_4_1")
        self.btn_4_1.setMinimumSize(QSize(60, 60))
        self.btn_4_1.setMaximumSize(QSize(60, 60))
        self.btn_4_1.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_4_1.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._4_1.addWidget(self.btn_4_1)

        self.name_4_1 = QLabel(project_down)
        self.name_4_1.setObjectName("name_4_1")
        self.name_4_1.setMinimumSize(QSize(60, 15))
        self.name_4_1.setMaximumSize(QSize(60, 15))
        self.name_4_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_4_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4_1.addWidget(self.name_4_1)

        self.fourth__all.addLayout(self._4_1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fourth__all.addItem(self.horizontalSpacer_30)

        self._4_2 = QVBoxLayout()
        self._4_2.setObjectName("_4_2")
        self.btn_4_2 = QPushButton(project_down)
        self.btn_4_2.setObjectName("btn_4_2")
        self.btn_4_2.setMinimumSize(QSize(60, 60))
        self.btn_4_2.setMaximumSize(QSize(60, 60))
        self.btn_4_2.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_4_2.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._4_2.addWidget(self.btn_4_2)

        self.name_4_2 = QLabel(project_down)
        self.name_4_2.setObjectName("name_4_2")
        self.name_4_2.setMinimumSize(QSize(60, 15))
        self.name_4_2.setMaximumSize(QSize(60, 15))
        self.name_4_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_4_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4_2.addWidget(self.name_4_2)

        self.fourth__all.addLayout(self._4_2)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fourth__all.addItem(self.horizontalSpacer_31)

        self._4_3 = QVBoxLayout()
        self._4_3.setObjectName("_4_3")
        self.btn_4_3 = QPushButton(project_down)
        self.btn_4_3.setObjectName("btn_4_3")
        self.btn_4_3.setMinimumSize(QSize(60, 60))
        self.btn_4_3.setMaximumSize(QSize(60, 60))
        self.btn_4_3.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_4_3.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._4_3.addWidget(self.btn_4_3)

        self.name_4_3 = QLabel(project_down)
        self.name_4_3.setObjectName("name_4_3")
        self.name_4_3.setMinimumSize(QSize(60, 15))
        self.name_4_3.setMaximumSize(QSize(60, 15))
        self.name_4_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_4_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4_3.addWidget(self.name_4_3)

        self.fourth__all.addLayout(self._4_3)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fourth__all.addItem(self.horizontalSpacer_32)

        self._4_4 = QVBoxLayout()
        self._4_4.setObjectName("_4_4")
        self.btn_4_4 = QPushButton(project_down)
        self.btn_4_4.setObjectName("btn_4_4")
        self.btn_4_4.setMinimumSize(QSize(60, 60))
        self.btn_4_4.setMaximumSize(QSize(60, 60))
        self.btn_4_4.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_4_4.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._4_4.addWidget(self.btn_4_4)

        self.name_4_4 = QLabel(project_down)
        self.name_4_4.setObjectName("name_4_4")
        self.name_4_4.setMinimumSize(QSize(60, 15))
        self.name_4_4.setMaximumSize(QSize(60, 15))
        self.name_4_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_4_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4_4.addWidget(self.name_4_4)

        self.fourth__all.addLayout(self._4_4)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fourth__all.addItem(self.horizontalSpacer_33)

        self._4_5 = QVBoxLayout()
        self._4_5.setObjectName("_4_5")
        self.btn_4_5 = QPushButton(project_down)
        self.btn_4_5.setObjectName("btn_4_5")
        self.btn_4_5.setMinimumSize(QSize(60, 60))
        self.btn_4_5.setMaximumSize(QSize(60, 60))
        self.btn_4_5.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_4_5.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._4_5.addWidget(self.btn_4_5)

        self.name_4_5 = QLabel(project_down)
        self.name_4_5.setObjectName("name_4_5")
        self.name_4_5.setMinimumSize(QSize(60, 15))
        self.name_4_5.setMaximumSize(QSize(60, 15))
        self.name_4_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_4_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._4_5.addWidget(self.name_4_5)

        self.fourth__all.addLayout(self._4_5)

        self.project_down_all.addLayout(self.fourth__all)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.project_down_all.addItem(self.verticalSpacer_4)

        self.fifth_all = QHBoxLayout()
        self.fifth_all.setObjectName("fifth_all")
        self._5_1 = QVBoxLayout()
        self._5_1.setObjectName("_5_1")
        self.btn_5_1 = QPushButton(project_down)
        self.btn_5_1.setObjectName("btn_5_1")
        self.btn_5_1.setMinimumSize(QSize(60, 60))
        self.btn_5_1.setMaximumSize(QSize(60, 60))
        self.btn_5_1.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_5_1.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._5_1.addWidget(self.btn_5_1)

        self.name_5_1 = QLabel(project_down)
        self.name_5_1.setObjectName("name_5_1")
        self.name_5_1.setMinimumSize(QSize(60, 15))
        self.name_5_1.setMaximumSize(QSize(60, 15))
        self.name_5_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_5_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._5_1.addWidget(self.name_5_1)

        self.fifth_all.addLayout(self._5_1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fifth_all.addItem(self.horizontalSpacer_34)

        self._5_2 = QVBoxLayout()
        self._5_2.setObjectName("_5_2")
        self.btn_5_2 = QPushButton(project_down)
        self.btn_5_2.setObjectName("btn_5_2")
        self.btn_5_2.setMinimumSize(QSize(60, 60))
        self.btn_5_2.setMaximumSize(QSize(60, 60))
        self.btn_5_2.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_5_2.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._5_2.addWidget(self.btn_5_2)

        self.name_5_2 = QLabel(project_down)
        self.name_5_2.setObjectName("name_5_2")
        self.name_5_2.setMinimumSize(QSize(60, 15))
        self.name_5_2.setMaximumSize(QSize(60, 15))
        self.name_5_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_5_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._5_2.addWidget(self.name_5_2)

        self.fifth_all.addLayout(self._5_2)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fifth_all.addItem(self.horizontalSpacer_35)

        self._5_3 = QVBoxLayout()
        self._5_3.setObjectName("_5_3")
        self.btn_5_3 = QPushButton(project_down)
        self.btn_5_3.setObjectName("btn_5_3")
        self.btn_5_3.setMinimumSize(QSize(60, 60))
        self.btn_5_3.setMaximumSize(QSize(60, 60))
        self.btn_5_3.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_5_3.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._5_3.addWidget(self.btn_5_3)

        self.name_5_3 = QLabel(project_down)
        self.name_5_3.setObjectName("name_5_3")
        self.name_5_3.setMinimumSize(QSize(60, 15))
        self.name_5_3.setMaximumSize(QSize(60, 15))
        self.name_5_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_5_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._5_3.addWidget(self.name_5_3)

        self.fifth_all.addLayout(self._5_3)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fifth_all.addItem(self.horizontalSpacer_36)

        self._5_4 = QVBoxLayout()
        self._5_4.setObjectName("_5_4")
        self.btn_5_4 = QPushButton(project_down)
        self.btn_5_4.setObjectName("btn_5_4")
        self.btn_5_4.setMinimumSize(QSize(60, 60))
        self.btn_5_4.setMaximumSize(QSize(60, 60))
        self.btn_5_4.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_5_4.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._5_4.addWidget(self.btn_5_4)

        self.name_5_4 = QLabel(project_down)
        self.name_5_4.setObjectName("name_5_4")
        self.name_5_4.setMinimumSize(QSize(60, 15))
        self.name_5_4.setMaximumSize(QSize(60, 15))
        self.name_5_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_5_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._5_4.addWidget(self.name_5_4)

        self.fifth_all.addLayout(self._5_4)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fifth_all.addItem(self.horizontalSpacer_37)

        self._5_5 = QVBoxLayout()
        self._5_5.setObjectName("_5_5")
        self.btn_5_5 = QPushButton(project_down)
        self.btn_5_5.setObjectName("btn_5_5")
        self.btn_5_5.setMinimumSize(QSize(60, 60))
        self.btn_5_5.setMaximumSize(QSize(60, 60))
        self.btn_5_5.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_5_5.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._5_5.addWidget(self.btn_5_5)

        self.name_5_5 = QLabel(project_down)
        self.name_5_5.setObjectName("name_5_5")
        self.name_5_5.setMinimumSize(QSize(60, 15))
        self.name_5_5.setMaximumSize(QSize(60, 15))
        self.name_5_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_5_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._5_5.addWidget(self.name_5_5)

        self.fifth_all.addLayout(self._5_5)

        self.project_down_all.addLayout(self.fifth_all)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.project_down_all.addItem(self.verticalSpacer_5)

        self.sixth_all = QHBoxLayout()
        self.sixth_all.setObjectName("sixth_all")
        self._6_1 = QVBoxLayout()
        self._6_1.setObjectName("_6_1")
        self.btn_6_1 = QPushButton(project_down)
        self.btn_6_1.setObjectName("btn_6_1")
        self.btn_6_1.setMinimumSize(QSize(60, 60))
        self.btn_6_1.setMaximumSize(QSize(60, 60))
        self.btn_6_1.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_6_1.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._6_1.addWidget(self.btn_6_1)

        self.name_6_1 = QLabel(project_down)
        self.name_6_1.setObjectName("name_6_1")
        self.name_6_1.setMinimumSize(QSize(60, 15))
        self.name_6_1.setMaximumSize(QSize(60, 15))
        self.name_6_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_6_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._6_1.addWidget(self.name_6_1)

        self.sixth_all.addLayout(self._6_1)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sixth_all.addItem(self.horizontalSpacer_38)

        self._6_2 = QVBoxLayout()
        self._6_2.setObjectName("_6_2")
        self.btn_6_2 = QPushButton(project_down)
        self.btn_6_2.setObjectName("btn_6_2")
        self.btn_6_2.setMinimumSize(QSize(60, 60))
        self.btn_6_2.setMaximumSize(QSize(60, 60))
        self.btn_6_2.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_6_2.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._6_2.addWidget(self.btn_6_2)

        self.name_6_2 = QLabel(project_down)
        self.name_6_2.setObjectName("name_6_2")
        self.name_6_2.setMinimumSize(QSize(60, 15))
        self.name_6_2.setMaximumSize(QSize(60, 15))
        self.name_6_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_6_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._6_2.addWidget(self.name_6_2)

        self.sixth_all.addLayout(self._6_2)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sixth_all.addItem(self.horizontalSpacer_39)

        self._6_3 = QVBoxLayout()
        self._6_3.setObjectName("_6_3")
        self.btn_6_3 = QPushButton(project_down)
        self.btn_6_3.setObjectName("btn_6_3")
        self.btn_6_3.setMinimumSize(QSize(60, 60))
        self.btn_6_3.setMaximumSize(QSize(60, 60))
        self.btn_6_3.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_6_3.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._6_3.addWidget(self.btn_6_3)

        self.name_6_3 = QLabel(project_down)
        self.name_6_3.setObjectName("name_6_3")
        self.name_6_3.setMinimumSize(QSize(60, 15))
        self.name_6_3.setMaximumSize(QSize(60, 15))
        self.name_6_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_6_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._6_3.addWidget(self.name_6_3)

        self.sixth_all.addLayout(self._6_3)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sixth_all.addItem(self.horizontalSpacer_40)

        self._6_4 = QVBoxLayout()
        self._6_4.setObjectName("_6_4")
        self.btn_6_4 = QPushButton(project_down)
        self.btn_6_4.setObjectName("btn_6_4")
        self.btn_6_4.setMinimumSize(QSize(60, 60))
        self.btn_6_4.setMaximumSize(QSize(60, 60))
        self.btn_6_4.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_6_4.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._6_4.addWidget(self.btn_6_4)

        self.name_6_4 = QLabel(project_down)
        self.name_6_4.setObjectName("name_6_4")
        self.name_6_4.setMinimumSize(QSize(60, 15))
        self.name_6_4.setMaximumSize(QSize(60, 15))
        self.name_6_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_6_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._6_4.addWidget(self.name_6_4)

        self.sixth_all.addLayout(self._6_4)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sixth_all.addItem(self.horizontalSpacer_41)

        self._6_5 = QVBoxLayout()
        self._6_5.setObjectName("_6_5")
        self.btn_6_5 = QPushButton(project_down)
        self.btn_6_5.setObjectName("btn_6_5")
        self.btn_6_5.setMinimumSize(QSize(60, 60))
        self.btn_6_5.setMaximumSize(QSize(60, 60))
        self.btn_6_5.setStyleSheet(
            "border-radius: 30px;\nbackground-color: rgb(0, 0, 0);\nborder-image: url(:/demo.png);"
        )
        self.btn_6_5.setLocale(QLocale(QLocale.Church, QLocale.Russia))

        self._6_5.addWidget(self.btn_6_5)

        self.name_6_5 = QLabel(project_down)
        self.name_6_5.setObjectName("name_6_5")
        self.name_6_5.setMinimumSize(QSize(60, 15))
        self.name_6_5.setMaximumSize(QSize(60, 15))
        self.name_6_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_6_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._6_5.addWidget(self.name_6_5)

        self.sixth_all.addLayout(self._6_5)

        self.project_down_all.addLayout(self.sixth_all)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.project_down_all.addItem(self.verticalSpacer_6)

        self.verticalLayout.addLayout(self.project_down_all)

        self.retranslateUi(project_down)

        QMetaObject.connectSlotsByName(project_down)

    # setupUi

    def retranslateUi(self, project_down):  # noqa: PLR0915
        project_down.setWindowTitle(QCoreApplication.translate("project_down", "Frame", None))
        self.categorization.setItemText(0, QCoreApplication.translate("project_down", "\u5168\u90e8", None))
        self.categorization.setItemText(
            1,
            QCoreApplication.translate("project_down", "\u4f20\u7edf\u620f\u5267", None),
        )
        self.categorization.setItemText(
            2,
            QCoreApplication.translate("project_down", "\u6c11\u95f4\u7f8e\u672f", None),
        )
        self.categorization.setItemText(
            3,
            QCoreApplication.translate("project_down", "\u4f20\u7edf\u533b\u836f", None),
        )
        self.categorization.setItemText(
            4,
            QCoreApplication.translate("project_down", "\u4f20\u7edf\u6280\u827a", None),
        )
        self.categorization.setItemText(
            5,
            QCoreApplication.translate("project_down", "\u4f20\u7edf\u97f3\u4e50", None),
        )
        self.categorization.setItemText(
            6,
            QCoreApplication.translate("project_down", "\u6c11\u95f4\u97f3\u4e50", None),
        )
        self.categorization.setItemText(
            7,
            QCoreApplication.translate("project_down", "\u4f20\u7edf\u8282\u65e5", None),
        )
        self.categorization.setItemText(
            8,
            QCoreApplication.translate("project_down", "\u4f20\u7edf\u4f53\u80b2", None),
        )

        self.none.setText("")
        self.btn_1_1.setText("")
        self.name_1_1.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_1_2.setText("")
        self.name_1_2.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_1_3.setText("")
        self.name_1_3.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_1_4.setText("")
        self.name_1_4.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_1_5.setText("")
        self.name_1_5.setText(QCoreApplication.translate("project_down", "111", None))
        self.btn_2_1.setText("")
        self.name_2_1.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_2_2.setText("")
        self.name_2_2.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_2_3.setText("")
        self.name_2_3.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_2_4.setText("")
        self.name_2_4.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_2_5.setText("")
        self.name_2_5.setText(QCoreApplication.translate("project_down", "111", None))
        self.btn_3_1.setText("")
        self.name_3_1.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_3_2.setText("")
        self.name_3_2.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_3_3.setText("")
        self.name_3_3.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_3_4.setText("")
        self.name_3_4.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_3_5.setText("")
        self.name_3_5.setText(QCoreApplication.translate("project_down", "111", None))
        self.btn_4_1.setText("")
        self.name_4_1.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_4_2.setText("")
        self.name_4_2.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_4_3.setText("")
        self.name_4_3.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_4_4.setText("")
        self.name_4_4.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_4_5.setText("")
        self.name_4_5.setText(QCoreApplication.translate("project_down", "111", None))
        self.btn_5_1.setText("")
        self.name_5_1.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_5_2.setText("")
        self.name_5_2.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_5_3.setText("")
        self.name_5_3.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_5_4.setText("")
        self.name_5_4.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_5_5.setText("")
        self.name_5_5.setText(QCoreApplication.translate("project_down", "111", None))
        self.btn_6_1.setText("")
        self.name_6_1.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_6_2.setText("")
        self.name_6_2.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_6_3.setText("")
        self.name_6_3.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_6_4.setText("")
        self.name_6_4.setText(QCoreApplication.translate("project_down", "TextLabel", None))
        self.btn_6_5.setText("")
        self.name_6_5.setText(QCoreApplication.translate("project_down", "111", None))

    # retranslateUi
