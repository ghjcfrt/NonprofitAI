# Game.py
import json
import random
from pathlib import Path

project_dict_filename = Path("./NonprofitAI/json/project_dictionary.json")  # 项目字典


class Game:
    def __init__(self, project_dict_filename=project_dict_filename):
        self.project_dict_filename = project_dict_filename
        self.project_dict = self.load_from_json(self.project_dict_filename)
        self.project_list = list(self.project_dict.keys())  # 项目列表
        self.current_project = None  # 当前随机选中的项目

    # 加载 JSON 文件数据
    @staticmethod
    def load_from_json(filename):
        try:
            if filename.is_file():
                with filename.open(encoding="utf-8") as file:
                    return json.load(file)
            else:
                print(f"错误: 文件 {filename} 不存在。")
        except OSError as e:
            print(f"文件操作错误: 无法加载文件 {filename}: {e}")
        except json.JSONDecodeError as e:
            print(f"JSON 解码错误: 文件 {filename} 格式不正确: {e}")
        return {}

    # 从项目字典中随机获取一个项目的名称和图片地址
    def get_random_project(self):
        self.current_project = random.choice(self.project_list)  # 随机选择 key  # noqa: S311
        project = self.project_dict.get(self.current_project, {})
        image = project.get("图片", "无图片地址")
        return image, self.current_project  # 返回图片路径和项目 key

    # 验证用户输入是否正确
    def verify_answer(self, user_input):
        project = self.project_dict.get(self.current_project, {})
        name = project.get("名称", "未知项目")
        return user_input.strip() == name
