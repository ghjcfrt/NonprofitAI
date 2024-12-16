import csv
import random
import os

csv_filename = "click.csv"
click_history = []


# 记录点击历史
def record_in_history(item_dict):
    click_history.append(item_dict)
    if len(click_history) > 20:
        click_history.pop(0)


# 写入csv文件
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


# 从csv文件中读取数据
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


# 判断项目是否相似
def is_similar(project1, project2):
    big_classify_similarity = (
        project1["big-classify"].lower() == project2["big-classify"].lower()
    )
    return big_classify_similarity


# 推荐相似项目
def recommend_similar(project):
    all_projects = load_data()
    similar_projects = [p for p in all_projects if is_similar(p, project)]
    if not similar_projects:
        return None
    total_weight = sum(int(p.get("weight", 1)) for p in similar_projects)
    random_number = random.randint(1, total_weight)
    running_sum = 0
    for p in similar_projects:
        running_sum += int(p.get("weight", 1))
        if running_sum >= random_number:
            return p
    return None


# 测试主函数
def main():
    # 定义一些测试项目
    project1 = {"id": "1", "name": "项目A", "big-classify": "文化", "weight": "5"}
    project2 = {"id": "2", "name": "项目B", "big-classify": "文化", "weight": "3"}
    project3 = {"id": "3", "name": "项目C", "big-classify": "非文化", "weight": "2"}

    # 模拟点击记录
    record_in_history(project1)
    record_in_history(project2)
    record_in_history(project3)

    # 将点击记录写入文件
    record_click()
    print("点击记录已写入文件。")

    # 从文件中加载数据
    all_data = load_data()
    print("从文件中加载的数据：")
    for item in all_data:
        print(item)

    # 测试推荐功能
    test_project = {"id": "4", "name": "测试项目", "big-classify": "文化"}
    recommendation = recommend_similar(test_project)
    if recommendation:
        print("推荐的相似项目：", recommendation)
    else:
        print("没有找到相似的项目。")


if __name__ == "__main__":
    main()
