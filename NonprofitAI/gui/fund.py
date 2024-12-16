# fund.py
import json
from pathlib import Path

from PySide6.QtWidgets import QFrame, QMainWindow, QMessageBox, QVBoxLayout, QWidget

from NonprofitAI.gui.up_and_down import Ui_fund_down, Ui_fund_up

# JSON 文件路径
FUND_PATH = "./NonprofitAI/json/fund.json"


class FundPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置布局
        self.layout = QVBoxLayout(self)

        # 上半部分
        self.fund_up_ui = Ui_fund_up()
        self.fund_up_widget = QMainWindow()
        self.fund_up_ui.setupUi(self.fund_up_widget)
        self.layout.addWidget(self.fund_up_widget)
        self.fund_up_widget.setFixedHeight(70)

        # 下半部分
        self.fund_down_ui = Ui_fund_down()
        self.fund_down_widget = QFrame()
        self.fund_down_ui.setupUi(self.fund_down_widget)
        self.layout.addWidget(self.fund_down_widget)

        # 设置文本换行
        self._set_word_wrap()

        # 加载并展示 JSON 数据
        self.load_json_data()

    def _set_word_wrap(self):
        """配置文本框的换行属性"""
        self.fund_down_ui.adress_display.setWordWrap(True)

    def load_json_data(self):
        """加载 JSON 数据并显示在界面上"""
        json_path = Path(FUND_PATH)
        data = self._read_json_file(json_path)
        self._validate_json_fields(data)
        self._update_display(data)

    def _read_json_file(self, path):
        """读取 JSON 文件内容"""
        if not path.exists():
            error_message = f"文件未找到：{FUND_PATH}"
            self._raise_exception(FileNotFoundError, error_message)

        try:
            with path.open(encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as err:
            error_message = "JSON 格式错误"
            self._raise_exception(ValueError, error_message, err)

    def _validate_json_fields(self, data):
        """验证 JSON 数据中是否包含必需字段"""
        required_fields = ["姓名", "电话", "微信", "地址"]
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            error_message = f"缺少必需字段：{', '.join(missing_fields)}"
            self._raise_exception(KeyError, error_message)

    def _update_display(self, data):
        """将 JSON 数据更新到界面"""
        self.fund_down_ui.name_display.setText(data["姓名"])
        self.fund_down_ui.phone_display.setText(data["电话"])
        self.fund_down_ui.wechat_display.setText(data["微信"])
        self.fund_down_ui.adress_display.setText(data["地址"])

    @staticmethod
    def _raise_exception(error_type, message, original_error=None):
        """抽象 raise 逻辑"""
        if original_error:
            raise error_type(message) from original_error
        raise error_type(message)

    def show_error_message(self, message):
        """显示错误提示框"""
        QMessageBox.critical(self, "错误", message)
