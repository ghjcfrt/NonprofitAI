# personalized_recommend.py
import json
import random
import os

# 定义文件路径
project_dict_filename = "./1/project_dictionary.json"
click_history_filename = "./1/click_history.json"


# 保存数据至 JSON 文件
def save_to_json(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"将数据保存到 {filename}: {e} 时出错")


# 加载 JSON 文件数据
def load_from_json(filename):
    try:
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
    except Exception as e:
        print(f"加载数据 {filename}: {e} 时出错")
    return {}


# 初始化点击历史和非遗项目字典
click_history = load_from_json(click_history_filename)
if not isinstance(click_history, list):
    click_history = []
    save_to_json(click_history, click_history_filename)

project_dictionary = load_from_json(project_dict_filename)


# 记录点击历史（最多保留10条）
def record_click(item_dict):
    click_history.append(item_dict)
    if len(click_history) > 10:
        click_history.pop(0)
    save_to_json(click_history, click_history_filename)


# 推荐算法：推荐4个项目，如果没有点击历史则推荐前四个
def recommend_based_on_history_or_category():
    if click_history:
        current_item = click_history[-1]
        current_category = current_item["类别"]

        recommendations = [
            proj
            for proj in project_dictionary.values()
            if proj["类别"] == current_category and proj["名称"] != current_item["名称"]
        ]

        if len(recommendations) < 4:
            additional_recommendations = [
                proj
                for proj in project_dictionary.values()
                if proj not in recommendations and proj["名称"] != current_item["名称"]
            ]
            recommendations.extend(
                random.sample(
                    additional_recommendations,
                    min(4 - len(recommendations), len(additional_recommendations)),
                )
            )

    else:
        recommendations = list(project_dictionary.values())[:4]

    return [proj["名称"] for proj in recommendations]


# 主程序
def main():
    sample_click = {"名称": "京剧", "类别": "传统戏剧", "地区": "北京"}
    record_click(sample_click)
    print("推荐项目：", recommend_based_on_history_or_category())


# 数据初始化并保存到 JSON
if not os.path.isfile(project_dict_filename):
    save_to_json({}, project_dict_filename)

if __name__ == "__main__":
    main()
