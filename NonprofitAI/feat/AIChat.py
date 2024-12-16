# AIChat.py
import json

import requests

from config import CHAT_API_KEY, CHAT_SECRET_KEY, CHAT_URL, URL


class AIChat:
    def __init__(self, system_memory_id="非遗技艺"):
        self.messages = []  # 用于存储对话历史
        self.system_memory_id = system_memory_id
        self.access_token = self._get_access_token()

    @staticmethod  # 静态方法
    def _get_access_token():
        """
        使用 API_KEY 和 SECRET_KEY 生成 Access Token
        """
        url = URL
        params = {
            "grant_type": "client_credentials",
            "client_id": CHAT_API_KEY,
            "client_secret": CHAT_SECRET_KEY,
        }
        try:
            response = requests.post(url, params=params, timeout=100)
            response.raise_for_status()  # 如果请求失败，抛出异常
            return response.json().get("access_token")
        except requests.exceptions.RequestException as e:
            print(f"获取访问令牌时出错： {e}")
            return None

    def generate_response(self, user_input):
        """
        使用用户输入生成AI的回复，并更新对话历史。
        """
        # 更新对话历史
        self.messages.append({"role": "user", "content": user_input})

        # AI接口调用
        url = CHAT_URL + self.access_token
        payload = json.dumps({
            "messages": self.messages,
            "temperature": 0.95,
            "top_p": 0.8,
            "penalty_score": 1,
            "enable_system_memory": True,
            "system_memory_id": self.system_memory_id,
            "system": "你是一个非遗技艺专业领域的专家，非常擅长讲解非遗技艺方面",
            "disable_search": False,
            "enable_citation": False,
        })
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=100)
            response.raise_for_status()
            result = response.json().get("result", "")
        except requests.exceptions.RequestException as e:  # 如果请求失败，抛出异常
            print(f"生成响应时出错： {e}")
            result = "抱歉，AI无法回应您的请求。请稍后再试。"

        # 保存 AI 回复到对话历史
        self.messages.append({"role": "assistant", "content": result})
        return result
