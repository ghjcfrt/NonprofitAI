#  __Personalized_Recommend__.py
import json
import random
from collections import Counter
from pathlib import Path

# 定义文件路径
project_dict_filename = Path("./NonprofitAI/json/project_dictionary.json")  # 项目字典
click_history_filename = Path("./NonprofitAI/json/click_history.json")  # 点击历史

history_num = 10  # 点击历史记录的数量
commend_num = 4  # 每个类别推荐的数量


class PersonalizedRecommend:
    def __init__(
        self,
        project_dict_filename=project_dict_filename,
        click_history_filename=click_history_filename,
    ):
        self.project_dict_filename = project_dict_filename
        self.click_history_filename = click_history_filename

        # 初始化点击历史和非遗项目字典
        self.click_history = self.load_from_json(self.click_history_filename)
        if not isinstance(self.click_history, list):
            self.click_history = []
            self.save_to_json(self.click_history, self.click_history_filename)

        self.project_dictionary = self.load_from_json(self.project_dict_filename)

    # 保存数据至 JSON 文件
    @staticmethod
    def save_to_json(data, filename):
        try:
            with filename.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"文件操作错误: 无法保存到 {filename}: {e}")
        except TypeError as e:
            print(f"数据序列化错误: 无法保存到 {filename}: {e}")

    # 加载 JSON 文件数据
    @staticmethod
    def load_from_json(filename):
        try:
            if filename.is_file():
                with filename.open(encoding="utf-8") as file:
                    return json.load(file)
        except OSError as e:
            print(f"文件操作错误: 无法加载文件 {filename}: {e}")
        except json.JSONDecodeError as e:
            print(f"JSON 解码错误: 文件 {filename} 格式不正确: {e}")
        return {}

    # 记录点击历史（最多保留10条）
    def record_click(self, item_dict):
        self.click_history.append(item_dict)
        if len(self.click_history) > history_num:
            self.click_history.pop(0)
        self.save_to_json(self.click_history, self.click_history_filename)

    def recommend_based_on_history_or_category(self):
        recommendations_by_category = []
        if not self.click_history:  # 如果历史点击为空，直接进行随机推荐
            recommendations_by_category = random.sample(list(self.project_dictionary.values()), 4)
        else:
            # 获取近十次点击的项目名称
            recent_clicks = self.click_history[-10:]

            # 获取每个项目对应的类别
            categories = []
            for proj_name in recent_clicks:
                for proj in self.project_dictionary.values():
                    if proj["名称"] == proj_name:
                        categories.append(proj["类别"])
                        break

            # 计算类别出现的频率
            category_counts = Counter(categories)

            # 获取类别出现的比例
            total_clicks = len(categories)
            category_weights = {category: count / total_clicks for category, count in category_counts.items()}

            # 根据类别的比例进行推荐
            for category, weight in category_weights.items():
                # 获取该类别下所有的项目
                category_projects = [proj for proj in self.project_dictionary.values() if proj["类别"] == category]

                # 计算推荐数量，按比例推荐
                num_recommendations = max(1, int(weight * 4))  # 至少推荐1个项目
                recommendations_by_category.extend(
                    random.sample(
                        category_projects,
                        min(num_recommendations, len(category_projects)),
                    )
                )

            # 如果推荐项目数少于4，则从其他类别中补充
            if len(recommendations_by_category) < commend_num:
                additional_recommendations = [
                    proj for proj in self.project_dictionary.values() if proj not in recommendations_by_category
                ]
                recommendations_by_category.extend(
                    random.sample(
                        additional_recommendations,
                        min(
                            4 - len(recommendations_by_category),
                            len(additional_recommendations),
                        ),
                    )
                )

        # 返回项目序号和图片路径
        recommendations_with_images = []
        for proj in recommendations_by_category[:4]:  # 确保最多返回4个推荐项目
            proj_name = proj["名称"]

            # 查找对应名称的项目
            project_key = None
            for key, value in self.project_dictionary.items():
                if value["名称"] == proj_name:
                    project_key = key
                    break  # 找到后跳出循环

            project_index = int(project_key.replace("项目", ""))  # 从 key 提取项目编号
            recommendations_with_images.append({"项目序号": f"项目{project_index}", "图片": proj.get("图片", "")})

        return recommendations_with_images
