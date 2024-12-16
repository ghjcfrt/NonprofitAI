
import csv
import random
import os
from collections import defaultdict

csv_filename = "click.csv"

culture_data = {
    "传统美术": {
        "中国篆刻": {"item": ["西泠印社金石篆刻", "津派传统篆刻"]},
        "中国剪纸": {"item": ["蔚县剪纸", "佛山剪纸"]},
        "热贡艺术": {"item": ["徽州三雕", "莆田木雕", "青田石雕"]},
        "传统绘画": {"item": ["杨柳青木版年画", "桃花坞木版年画", "内画"]}
    },
    "传统舞蹈": {"item": ["中国朝鲜族农乐舞", "蒙古族呼麦歌唱艺术", "侗族大歌", "锅庄舞", "热巴舞", "芦笙舞", "孔雀舞", "安塞腰鼓"]},
    "传统音乐": {"item": ["新疆维吾尔木卡姆艺术", "蒙古族长调民歌", "南音", "西安鼓乐", "花儿", "纳西古乐", "潮州音乐", "蒙古族马头琴音乐", "哈萨克族冬不拉艺术"]},
    "传统技艺": {
        "中国雕版印刷技艺": {"item": []},
        "中国传统木结构建筑营造技艺": {"item": ["应县木塔"]},
        "中国织造": {"item": ["南京云锦织造技艺", "中国蚕桑丝织技艺", "花丝镶嵌制作技艺", "苏州缂丝织造技艺", "蜀绣", "苏绣", "湘绣"]},
        "瓷器技艺": {"item": ["龙泉青瓷传统烧制技艺", "宣纸传统制作技艺", "醴陵釉下五彩瓷烧制技艺", "德化瓷烧制技艺", "景德镇手工制瓷技艺"]}
    },
    "传统戏剧": {"item": ["昆曲", "粤剧", "藏戏", "京剧", "越剧", "黄梅戏", "评剧", "豫剧", "秦腔", "晋剧"]},
    "传统体育": {"item": ["太极拳", "少林功夫", "武当武术", "五禽戏", "八段锦"]},
    "传统医药": {"item": ["针灸", "藏医药（浴法等）", "蒙医药", "苗医药"]},
    "民俗": {"item": ["端午节", "妈祖信俗", "春节", "中秋节", "重阳节", "清明节", "七夕节", "火把节", "泼水节"]},
    "曲艺": {"item": []}
}

def fix_culture_data():
    fixed_data = {}
    for big_category, content in culture_data.items():
        if isinstance(content, dict) and "small_category" in content:
            fixed_small_categories = {}
            for small_category, items_dict in content["small_category"].items():
                if "item" in items_dict and isinstance(items_dict["item"], list):
                    fixed_small_categories[small_category] = items_dict
                else:
                    fixed_small_categories[small_category] = {"item": []}
            fixed_data[big_category] = {"small_category": fixed_small_categories}
        else:
            if "item" in content and isinstance(content["item"], list):
                fixed_data[big_category] = content
            else:
                fixed_data[big_category] = {"item": []}
    return fixed_data

culture_data = fix_culture_data()

# 将字典数据写入 CSV 文件
def write_culture_data_to_csv():
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        for big_category, small_categories in culture_data.items():
            for small_category, items in small_categories.items():
                if isinstance(items, dict):
                    for item in items["item"]:
                        writer.writerow([big_category, small_category, item])
                else:
                    for item in items:
                        writer.writerow([big_category, small_category, item])

# 记录点击历史
click_history = []

def record_in_history(item_dict):
    click_history.append(item_dict)
    if len(click_history) > 20:
        click_history.pop(0)

# 写入 csv 文件
def record_click():
    file_exists = os.path.isfile(csv_filename)

    with open(csv_filename, "a", newline="") as file:
        if click_history:
            fieldnames = click_history[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:  # 文件不存在则写入表头
                writer.writeheader()
            for click_item in click_history:
                writer.writerow(click_item)

# 从 csv 文件中读取数据
def load_data():
    data = []
    try:
        with open(csv_filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def recommend_item():
    # 同一小分类下不同具体项目推荐（60%概率）
    subcategories = [subcat for category in culture_data.values() for subcat in category.values()]
    selected_subcategory = random.choice(subcategories)
    if isinstance(selected_subcategory, dict) and "item" in selected_subcategory and selected_subcategory["item"]:
        item = random.choice(selected_subcategory["item"])
        return f"推荐同一小分类下的项目：{item}"

    # 同一大项目下不同小分类不同项目推荐（20%概率）
    categories = list(culture_data.keys())
    selected_category = random.choice(categories)
    subcategories_in_category = list(culture_data[selected_category].values())
    selected_subcategory = random.choice(subcategories_in_category)
    if isinstance(selected_subcategory, dict) and "item" in selected_subcategory and selected_subcategory["item"]:
        item = random.choice(selected_subcategory["item"])
        return f"推荐同一大项目下不同小分类的项目：{item}"

    # 不同大项目下的具体项目推荐（20%概率）
    all_items = [item for category in culture_data.values() for subcat in category.values() for item in subcat["item"]]
    if all_items:
        item = random.choice(all_items)
        return f"推荐不同大项目下的项目：{item}"

    return "无法推荐项目"

def calculate_similarity(item1, item2):
    # 简单的相似度计算，可以根据实际情况进行更复杂的计算
    if item1["big_category"] == item2["big_category"]:
        return 0.5
    elif item1["small_category"] == item2["small_category"]:
        return 0.3
    else:
        return 0.1

def recommend_item():
    # 同一小分类下不同具体项目推荐（60%概率）
    subcategories = [subcat for category in culture_data.values() for subcat in category.values()]
    selected_subcategory = random.choice(subcategories)
    if isinstance(selected_subcategory, dict) and "item" in selected_subcategory and selected_subcategory["item"]:
        item = random.choice(selected_subcategory["item"])
        return f"推荐同一小分类下的项目：{item}"

    # 同一大项目下不同小分类不同项目推荐（20%概率）
    categories = list(culture_data.keys())
    selected_category = random.choice(categories)
    subcategories_in_category = list(culture_data[selected_category].values())
    selected_subcategory = random.choice(subcategories_in_category)
    if isinstance(selected_subcategory, dict) and "item" in selected_subcategory and selected_subcategory["item"]:
        item = random.choice(selected_subcategory["item"])
        return f"推荐同一大项目下不同小分类的项目：{item}"

    # 不同大项目下的具体项目推荐（20%概率）
    all_items = [item for category in culture_data.values() for subcat_dict in category.values() if isinstance(subcat_dict, dict) for item in subcat_dict.get("item", [])]
    if all_items:
        item = random.choice(all_items)
        return f"推荐不同大项目下的项目：{item}"

def main():
    # 模拟点击记录
    for _ in range(10):
        item = random.choice(list(culture_data.values()))
        small_category = random.choice(list(item.values()))
        if isinstance(small_category, dict) and small_category["item"]:
            clicked_item = random.choice(small_category["item"])
            item_dict = {
                "big_category": list(item.keys())[0],
                "small_category": list(small_category.keys())[0],
                "item": clicked_item
            }
            record_in_history(item_dict)
            record_click()

    # 推荐相似项目
    print(recommend_item())

if __name__ == "__main__":
    main()