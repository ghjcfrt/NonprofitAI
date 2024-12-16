# submit.py
import json
import shutil
from pathlib import Path

from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import QFileDialog, QFrame, QMainWindow, QMessageBox, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import Ui_submit_down, Ui_submit_up


class SubmitPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置布局
        self.layout = QVBoxLayout(self)

        # 上半部分
        self.submit_up_ui = Ui_submit_up()
        self.submit_up_widget = QMainWindow()
        self.submit_up_ui.setupUi(self.submit_up_widget)
        self.layout.addWidget(self.submit_up_widget)
        self.submit_up_widget.setFixedHeight(70)

        # 下半部分
        self.submit_down_ui = Ui_submit_down()
        self.submit_down_widget = QFrame()
        self.submit_down_ui.setupUi(self.submit_down_widget)
        self.layout.addWidget(self.submit_down_widget)

        # 初始化功能
        self.initialize()

    def initialize(self):
        # 自动换行设置
        self.submit_down_ui.name_input.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.submit_down_ui.category_input.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.submit_down_ui.area_input.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.submit_down_ui.introduction_input.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.submit_down_ui.history_input.setWordWrapMode(QTextOption.WrapMode.WordWrap)

        # 上传按钮连接
        self.submit_down_ui.pushButton_2.clicked.connect(self.upload_image)

        # 确认按钮连接
        self.submit_down_ui.verify.clicked.connect(self.verify_and_save)

    def upload_image(self):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.submit_down_ui.image_input.setText(file_path)

    def verify_and_save(self):
        # 获取用户输入
        name = self.submit_down_ui.name_input.toPlainText().strip()
        category = self.submit_down_ui.category_input.toPlainText().strip()
        area = self.submit_down_ui.area_input.toPlainText().strip()
        introduction = self.submit_down_ui.introduction_input.toPlainText().strip()
        history = self.submit_down_ui.history_input.toPlainText().strip()
        # 获取 QLabel 的文本内容并转换为 Path 对象
        image_path = Path(self.submit_down_ui.image_input.text().strip())

        # 检查输入
        if not all([name, category, area, introduction, history, image_path]):
            QMessageBox.warning(self, "警告", "所有字段均为必填项！")
            return

        # 检查图片路径有效性
        if not image_path.is_file():
            QMessageBox.warning(self, "警告", "请选择有效的图片文件！")
            return

        # 目标文件夹和文件路径
        img_dir = Path("./NonprofitAI/pending/img")
        img_dir.mkdir(parents=True, exist_ok=True)

        new_image_name = f"{name}{image_path.suffix}"  # 使用用户输入的名称和原文件扩展名
        new_image_path = img_dir / new_image_name

        # 转换为相对路径，当前目录为起点
        relative_image_path = new_image_path.relative_to(Path.cwd())

        try:
            # 复制图片而不是移动
            shutil.copy(str(image_path), new_image_path)  # 复制文件

            # JSON 文件路径
            json_path = Path("./NonprofitAI/pending/awaiting_review.json")
            json_path.parent.mkdir(parents=True, exist_ok=True)

            # 读取或创建 JSON 数据
            if json_path.is_file():
                with json_path.open("r", encoding="utf-8") as f:
                    json_data = json.load(f)
            else:
                json_data = {}

            # 确定新项目编号
            project_key = f"项目{len(json_data) + 1}"

            # 准备新项目数据
            new_project = {
                "名称": name,
                "类别": category,
                "地区": area,
                "简介": introduction,
                "历史": history,
                "图片": str(relative_image_path).replace("/", "\\"),  # 转换为 Windows 样式路径
            }

            # 添加新项目到 JSON 数据
            json_data[project_key] = new_project

            # 保存更新后的 JSON 数据
            with json_path.open("w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)

            QMessageBox.critical(self, "成功", f"提交成功！数据已保存到 {json_path}")

            # 清空所有输入框
            self.submit_down_ui.name_input.clear()
            self.submit_down_ui.category_input.clear()
            self.submit_down_ui.area_input.clear()
            self.submit_down_ui.introduction_input.clear()
            self.submit_down_ui.history_input.clear()
            self.submit_down_ui.image_input.clear()

        except FileNotFoundError:
            QMessageBox.critical(self, "错误", "图片文件未找到，无法复制！")
        except PermissionError:
            QMessageBox.critical(self, "错误", "文件操作权限不足！")
        except OSError as e:
            QMessageBox.critical(self, "错误", f"文件操作失败：{e}")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "错误", "保存 JSON 数据时发生错误！")
        except Exception as e:  # noqa: BLE001
            QMessageBox.critical(self, "错误", f"发生未知错误：{e}")
