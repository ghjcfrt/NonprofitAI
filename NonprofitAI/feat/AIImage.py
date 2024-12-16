# AIImage.py

import base64
import json
import time
import urllib

import requests

from config import IMAGE_API_KEY, IMAGE_GET_RESULT_URL, IMAGE_REQUEST_URL, IMAGE_SECRET_KEY, URL


class AIImage:
    def __init__(self):
        self.access_token = self._get_access_token()

    @staticmethod  # 静态方法
    def _get_access_token():
        """
        使用 API_KEY 和 SECRET_KEY 生成 Access Token
        """
        url = URL
        params = {
            "grant_type": "client_credentials",
            "client_id": IMAGE_API_KEY,
            "client_secret": IMAGE_SECRET_KEY,
        }
        try:
            response = requests.post(url, params=params, timeout=20)
            response.raise_for_status()
            token_data = response.json()
            if "access_token" in token_data:
                return token_data["access_token"]
            print("获取 access_token 失败:", token_data.get("error_description", "未知错误"))
        except requests.exceptions.Timeout:
            print("请求超时，请检查网络连接。")
        except requests.exceptions.ConnectionError:
            print("无法连接到服务器，请检查网络连接。")
        except requests.exceptions.RequestException as e:
            print(f"获取 access_token 出错: {e}")
        return None

    @staticmethod
    def get_file_content_as_base64(path, *, urlencoded=False):
        """
        获取文件base64编码
        :param path: 文件路径
        :param urlencoded: 是否对结果进行urlencoded
        :return: base64编码信息
        """
        with path.open("rb") as f:
            content = base64.b64encode(f.read()).decode("utf8")
            if urlencoded:
                content = urllib.parse.quote_plus(content)
        return content

    def get_task_id(self, image_path):
        """
        上传图像并获取任务 ID
        """
        url = f"{IMAGE_REQUEST_URL}{self.access_token}"

        # 获取图像的 base64 编码
        get_image = self.get_file_content_as_base64(image_path)

        payload = json.dumps({"image": get_image, "question": "识别图片中非遗技艺并介绍一下"})
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, headers=headers, data=payload, timeout=100)
            response.raise_for_status()
            response_data = response.json()

            if "result" in response_data:
                return response_data["result"]["task_id"]
            print("获取任务 ID 失败:", response_data.get("error_msg", "未知错误"))
        except requests.exceptions.RequestException as e:
            print(f"获取任务 ID 出错: {e}")
        return None

    def get_task_result(self, task_id, image_path):
        """
        根据任务 ID 获取识别结果
        """
        get_image = self.get_file_content_as_base64(image_path)
        url = f"{IMAGE_GET_RESULT_URL}{self.access_token}"
        payload = json.dumps({"task_id": task_id, "question": "识别图片中非遗技艺并介绍一下", "image": get_image})
        headers = {"Content-Type": "application/json"}

        max_retries = 5  # 最大重试次数
        retry_interval = 10  # 重试间隔时间（秒）

        for retry in range(max_retries):
            try:
                response = requests.post(url, headers=headers, data=payload, timeout=100)
                response.raise_for_status()
                response_data = response.json()

                if "result" in response_data and "description" in response_data["result"]:
                    return response_data["result"]["description"]

                if "result" in response_data and response_data["result"].get("ret_msg") == "processing":
                    print(f"正在重试第 {retry + 1} 次...")
                    time.sleep(retry_interval)
                else:
                    print("获取任务结果失败:", response_data.get("error_msg", "未知错误"))
                    return None
            except requests.exceptions.RequestException as e:
                print(f"获取任务结果出错: {e}")
                if retry < max_retries - 1:
                    time.sleep(retry_interval)
        return None
