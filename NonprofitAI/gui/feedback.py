# feedback.py
import json
from pathlib import Path

from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import QFrame, QMainWindow, QMessageBox, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import Ui_feedback_down, Ui_feedback_up


class FeedbackPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置布局
        self.layout = QVBoxLayout(self)

        # 上半部分
        self.feedback_up_ui = Ui_feedback_up()
        self.feedback_up_widget = QMainWindow()
        self.feedback_up_ui.setupUi(self.feedback_up_widget)
        self.layout.addWidget(self.feedback_up_widget)
        self.feedback_up_widget.setFixedHeight(70)

        # 下半部分
        self.feedback_down_ui = Ui_feedback_down()
        self.feedback_down_widget = QFrame()
        self.feedback_down_ui.setupUi(self.feedback_down_widget)
        self.layout.addWidget(self.feedback_down_widget)

        # 初始化功能
        self.initialize()

    def initialize(self):
        # 自动换行设置
        self.feedback_down_ui.feedback_input.setWordWrapMode(QTextOption.WrapMode.WordWrap)

        # 确认按钮连接
        self.feedback_down_ui.verify_btn.clicked.connect(self.verify_and_save)

    def verify_and_save(self):
        # 获取用户输入
        feedback = self.feedback_down_ui.feedback_input.toPlainText().strip()
        contact = self.feedback_down_ui.contact_input.text().strip()
        name = self.feedback_down_ui.name_input.text().strip()

        # 检查输入
        if not all([feedback, contact, name]):
            QMessageBox.warning(self, "警告", "所有字段均为必填项！")
            return

        # JSON 文件路径
        json_path = Path("./NonprofitAI/pending/feedback/feedback_data.json")

        # 如果文件不存在，创建一个新的 JSON 文件
        if not json_path.is_file():
            json_data = {}
        else:
            try:
                with json_path.open("r", encoding="utf-8") as f:
                    json_data = json.load(f)
            except json.JSONDecodeError:
                QMessageBox.critical(self, "错误", "JSON 文件格式错误，无法读取！")
                return
            except PermissionError:
                QMessageBox.critical(self, "错误", "没有权限读取 JSON 文件！")
                return
            except FileNotFoundError:
                QMessageBox.critical(self, "错误", "JSON 文件未找到！")
                return
            except OSError as e:
                QMessageBox.critical(self, "错误", f"文件操作失败: {e}")
                return

        # 确定新反馈编号
        feedback_key = f"反馈{len(json_data) + 1}"

        # 准备新反馈数据
        new_feedback = {"反馈": feedback, "联系信息": contact, "名称": name}

        # 添加新反馈到 JSON 数据
        json_data[feedback_key] = new_feedback

        # 保存更新后的 JSON 数据
        try:
            with json_path.open("w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)

            QMessageBox.information(self, "成功", "反馈已提交！")

            # 清空所有输入框
            self.feedback_down_ui.feedback_input.clear()
            self.feedback_down_ui.contact_input.clear()
            self.feedback_down_ui.name_input.clear()

        except PermissionError:
            QMessageBox.critical(self, "错误", "没有权限写入 JSON 文件！")
        except OSError as e:
            QMessageBox.critical(self, "错误", f"文件操作失败: {e}")
        except Exception as e:  # noqa: BLE001
            QMessageBox.critical(self, "错误", f"发生未知错误: {e}")
