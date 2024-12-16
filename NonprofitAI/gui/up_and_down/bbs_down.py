from PySide6.QtCore import QEvent, QMimeData, Qt, QTimer, QUrl
from PySide6.QtGui import QClipboard
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QToolTip,
    QVBoxLayout,
    QWidget,
)

from config import BBS_URL


class CustomWebEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)  # 确保关闭时释放资源

    def createWindow(self, _type):
        """处理新窗口请求"""
        return self


class CustomWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, _type, is_main_frame):
        """处理导航请求，确保在当前窗口中打开链接"""
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            # 使用 self.parent() 获取到 CustomWebEngineView，然后设置 URL
            self.parent().setUrl(url)  # 在当前视图中加载链接
            return False  # 阻止新窗口的创建
        return super().acceptNavigationRequest(url, _type, is_main_frame)


class BBSDOWN:
    def setupUi(self, bbs_down):
        # 设置主布局
        self.main_layout = QVBoxLayout(bbs_down)
        self.main_layout.setContentsMargins(5, 5, 5, 5)

        # 创建顶部导航栏
        self.nav_bar = QHBoxLayout()
        self.back_btn = QPushButton("后退")
        self.forward_btn = QPushButton("前进")
        self.refresh_btn = QPushButton("刷新")
        self.back_btn.setMinimumSize(75, 31)
        self.forward_btn.setMinimumSize(75, 31)
        self.refresh_btn.setMinimumSize(75, 31)
        self.back_btn.setStyleSheet("color:rgb(255, 255, 255);\nbackground-color:rgb(0, 119, 0);\n")
        self.forward_btn.setStyleSheet("color:rgb(255, 255, 255);\nbackground-color:rgb(0, 119, 0);\n")
        self.refresh_btn.setStyleSheet("color:rgb(255, 255, 255);\nbackground-color:rgb(0, 119, 0);\n")
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText(BBS_URL)
        self.url_bar.setEnabled(False)  # 禁用用户输入
        self.url_bar.setStyleSheet("color:rgb(0, 0, 0);\n")
        self.nav_bar.addWidget(self.back_btn)
        self.nav_bar.addWidget(self.forward_btn)
        self.nav_bar.addWidget(self.refresh_btn)
        self.nav_bar.addWidget(self.url_bar)

        # 创建浏览器视图
        self.web_view = CustomWebEngineView()
        self.web_view.setPage(CustomWebEnginePage(self.web_view))
        self.web_view.setUrl(QUrl(BBS_URL))
        self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 将导航栏和浏览器添加到主布局
        self.main_layout.addLayout(self.nav_bar)
        self.main_layout.addWidget(self.web_view)

    def set_device_viewport_size(self, width, height):
        """注入 JavaScript 来设置网页的视口大小"""
        script = f"""
        var viewport = document.querySelector('meta[name="viewport"]');
        if (viewport) {{
            viewport.parentNode.removeChild(viewport);
        }}
        var newViewport = document.createElement('meta');
        newViewport.name = 'viewport';
        newViewport.content = 'width={width}, height={height}, initial-scale=1.0';
        document.getElementsByTagName('head')[0].appendChild(newViewport);
        """
        self.web_view.page().runJavaScript(script)


class Ui_bbs_down(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置 UI
        self.ui = BBSDOWN()
        self.ui.setupUi(self)

        # 设置用户代理（User-Agent）
        profile = self.ui.web_view.page().profile()  # 获取 QWebEngineProfile
        profile.setHttpUserAgent(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        )

        web_view_settings = self.ui.web_view.settings()
        web_view_settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)  # noqa: FBT003
        web_view_settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)  # noqa: FBT003
        # 设置不阻止混合内容加载
        web_view_settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)  # noqa: FBT003
        web_view_settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)  # noqa: FBT003
        web_view_settings.setAttribute(QWebEngineSettings.AutoLoadImages, True)  # noqa: FBT003
        web_view_settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)  # noqa: FBT003
        web_view_settings.setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)  # noqa: FBT003
        web_view_settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)  # noqa: FBT003
        web_view_settings.setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)  # noqa: FBT003

        # 启用事件过滤器来处理点击事件
        self.ui.url_bar.installEventFilter(self)

        # 信号连接
        self.ui.back_btn.clicked.connect(self.navigate_back)
        self.ui.forward_btn.clicked.connect(self.navigate_forward)
        self.ui.refresh_btn.clicked.connect(self.refresh_page)
        self.ui.url_bar.mousePressEvent = self.copy_url_to_clipboard

        # 更新地址栏
        self.ui.web_view.urlChanged.connect(self.update_url_bar)

        # 设置网页视口大小
        self.ui.set_device_viewport_size(750, 550)

    def navigate_back(self):
        """后退"""
        self.ui.web_view.back()

    def navigate_forward(self):
        """前进"""
        self.ui.web_view.forward()

    def refresh_page(self):
        """刷新"""
        self.ui.web_view.reload()

    def update_url_bar(self, url):
        """更新地址栏"""
        self.ui.url_bar.setText(url.toString())

    def eventFilter(self, obj, event):
        """事件过滤器处理点击事件"""
        if obj == self.ui.url_bar and event.type() == QEvent.MouseButtonPress:
            # 如果是点击事件，执行复制操作
            self.copy_url_to_clipboard(event)
            return True  # 阻止事件传播
        return super().eventFilter(obj, event)

    def copy_url_to_clipboard(self, event):
        """复制当前网址到剪贴板"""
        clipboard = QApplication.clipboard()
        mime_data = QMimeData()
        mime_data.setText(self.ui.url_bar.text())
        clipboard.setMimeData(mime_data, QClipboard.Mode.Clipboard)

        # 提示已复制
        QToolTip.showText(self.ui.url_bar.mapToGlobal(event.pos()), "已复制到剪贴板")
        QTimer.singleShot(1000, QToolTip.hideText)
