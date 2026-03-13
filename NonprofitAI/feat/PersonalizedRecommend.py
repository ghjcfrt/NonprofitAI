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
        loaded_history = self.load_from_json(self.click_history_filename)
        if isinstance(loaded_history, list):
            self.click_history = loaded_history
        else:
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

    def _sample_random_projects(self, limit):
        projects = list(self.project_dictionary.values())
        return random.sample(projects, min(limit, len(projects)))

    def _collect_categories_from_recent_clicks(self):
        recent_clicks = self.click_history[-history_num:]
        categories = []
        for proj_name in recent_clicks:
            for proj in self.project_dictionary.values():
                if proj["名称"] == proj_name:
                    categories.append(proj["类别"])
                    break
        return categories

    def _build_weighted_recommendations(self, category_weights):
        recommendations = []
        for category, weight in category_weights.items():
            category_projects = [proj for proj in self.project_dictionary.values() if proj["类别"] == category]
            num_recommendations = max(1, int(weight * commend_num))
            recommendations.extend(
                random.sample(
                    category_projects,
                    min(num_recommendations, len(category_projects)),
                )
            )
        return recommendations

    def _fill_recommendations(self, recommendations):
        if len(recommendations) >= commend_num:
            return recommendations

        additional_recommendations = [
            proj for proj in self.project_dictionary.values() if proj not in recommendations
        ]
        recommendations.extend(
            random.sample(
                additional_recommendations,
                min(commend_num - len(recommendations), len(additional_recommendations)),
            )
        )
        return recommendations

    def _attach_project_index_and_image(self, recommendations):
        recommendations_with_images = []
        for proj in recommendations[:commend_num]:
            proj_name = proj["名称"]

            project_key = None
            for key, value in self.project_dictionary.items():
                if value["名称"] == proj_name:
                    project_key = key
                    break

            if project_key is None:
                continue

            project_index = int(project_key.replace("项目", ""))
            recommendations_with_images.append({"项目序号": f"项目{project_index}", "图片": proj.get("图片", "")})

        return recommendations_with_images

    def recommend_based_on_history_or_category(self):
        if not self.click_history:
            recommendations = self._sample_random_projects(commend_num)
            return self._attach_project_index_and_image(recommendations)

        categories = self._collect_categories_from_recent_clicks()
        if not categories:
            recommendations = self._sample_random_projects(commend_num)
            return self._attach_project_index_and_image(recommendations)

        category_counts = Counter(categories)
        total_clicks = len(categories)
        category_weights = {category: count / total_clicks for category, count in category_counts.items()}

        recommendations = self._build_weighted_recommendations(category_weights)
        recommendations = self._fill_recommendations(recommendations)
        return self._attach_project_index_and_image(recommendations)
