# project.py
from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame, QMainWindow, QScrollArea, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import ProjectUpUI, Ui_project_down


class ProjectPage(QWidget):
    project_selected = Signal(str)  # 定义信号，用于传递被点击项目的键

    def __init__(self, project_data, parent=None):
        super().__init__(parent)
        self.project_data = project_data

        # 设置布局
        self.layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: white;")

        # 上半部分
        self.project_up_ui = ProjectUpUI()
        self.project_up_widget = QMainWindow()
        self.project_up_ui.setupUi(self.project_up_widget)
        self.layout.addWidget(self.project_up_widget)
        self.project_up_widget.setFixedHeight(70)

        # 下半部分 (project_down)  # noqa: ERA001
        self.project_down_ui = Ui_project_down()
        self.project_down_widget = QFrame()
        self.project_down_ui.setupUi(self.project_down_widget)
        self.setup_project_down_buttons()

        # 将下半部分放入滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.project_down_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: #f1f1f1;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #888;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #555;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        self.layout.addWidget(scroll_area)

    def setup_project_down_buttons(self):
        """配置 project_down 界面的按钮图标和文本"""
        # 定义行列的范围
        rows = 6
        cols = 5

        # 遍历行列来设置按钮和标签
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                button = getattr(self.project_down_ui, f"btn_{row}_{col}")
                label = getattr(self.project_down_ui, f"name_{row}_{col}")
                project_key = f"项目{(row - 1) * 5 + col}"

                if project_key in self.project_data:
                    project_info = self.project_data[project_key]
                    # 设置按钮图标
                    icon_path = project_info["图片"]
                    button.setIcon(QIcon(icon_path))
                    button.setIconSize(QSize(60, 60))

                    # 设置标签文本和自动换行
                    label.setText(project_info["名称"])
                    label.setWordWrap(True)
                    label.setFixedHeight(40)
                    label.adjustSize()

                    # 绑定点击事件
                    button.clicked.connect(lambda _, pk=project_key: self.project_selected.emit(pk))
                else:
                    button.hide()
                    label.hide()
