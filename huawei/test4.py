"""
题目描述
一个有N个选手参加比赛，选手编号为1~N（3<=N<=100），有M（3<=M<=10）个评委对选手进行打分。

打分规则为每个评委对选手打分，最高分10分，最低分1分。

请计算得分最多的3位选手的编号。

如果得分相同，则得分高分值最多的选手排名靠前

(10分数量相同，则比较9分的数量，以此类推，用例中不会出现多个选手得分完全相同的情况)。

​

输入描述
第一行为半角逗号分割的两个正整数，第一个数字表示M（3<=M<=10）个评委，第二个数字表示N（3<=N<=100）个选手。

第2到M+1行是半角逗号分割的整数序列，表示评委为每个选手的打分，0号下标数字表示1号选手分数，1号下标数字表示2号选手分数，依次类推。

输出描述
选手前3名的编号。

**注：**若输入为异常，输出-1，如M、N、打分不在范围内。

"""


from auto_test import run_test_cases


def main_my():

    # 输入处理
    m_str, n_str = input("输入:M个评委/3<=M<=10 N选手/3<=N<=100\n").strip().split(",")
    m, n = int(m_str), int(n_str)


    if not (3 <= m <= 10 and 3 <= n <= 100):
        print(-1)
        return

    scores = []  # 存储每个评委对所有选手的打分
    valid_score_range = set(range(1, 11))  # 合法分数范围：1~10
    print(f'valid_score_range :{valid_score_range} ?? ')
    
    for i in range(m):
        line = input(f"请输入第{i + 1}个评委的{n}个打分，用逗号分隔:\n")
        score_list = list(map(int, line.strip().split(',')))

        # 检查是否数量正确以及每项是否在合法范围内, all() 函数接收一个可迭代对象（如生成器、列表等），
        # 如果其中 所有元素都为 True ，则返回 True；只要有一个为 False，就立即返回 False。
        if len(score_list) != n or not all(s in valid_score_range for s in score_list):
            print(-1)
            return

        scores.append(score_list)
    print('scores:  \n', scores, '????') #  [[10, 6, 9, 7, 6], [9, 10, 6, 7, 5], [8, 10, 6, 5, 10], [9, 10, 8, 4, 9]] ????
    
    # 统计每位选手的总分和各分数出现次数
    player_stats = []  #  使用字典保存选手信息

    for player_idx in range(n):
        total_score = 0
        freq = [0] * 11  # freq[10] 表示10分的次数，freq[9]表示9分的次数...

        for round_score in scores:
            score = round_score[player_idx]
            total_score += score
            freq[score] += 1

        # 将选手信息记录下来：包括总分和分数分布（用于后续排序）
        player_stats.append({
            'id': player_idx + 1,  # 选手编号从1开始
            'total': total_score,
            'freq': freq  # 从索引1到10分别代表1~10分的数量
        })
    print(f'player_stats: {player_stats}  ???') # player_stats: [{'id': 1, 'total': 36, 'freq': [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1]}, {'id': 2, 'total': 36, 'freq': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3]}, {'id': 3, 'total': 29, 'freq': [0, 0, 0, 0, 0, 0, 
    
 # 自定义排序函数：先按总分降序，再按各分数数量依次降序
    def sort_key(x):
        # 返回一个元组，Python会自动按元组顺序做多级排序
        # 总分取负实现降序，后面分数分布从10到1依次降序
        return (-x['total'], [-x['freq'][i] for i in range(10, 0, -1)])

    # 排序并取前三名
    player_stats.sort(key=sort_key)
    print(f'排序后的：{player_stats}')
    top3 = [str(p['id']) for p in player_stats[:3]]

    # 输出结果
    print(",".join(top3))


if __name__ == "__main__":
    TEST_CASES = [
        {
            "input": "4,5\n10,6,9,7,6\n9,10,6,7,5\n8,10,6,5,10\n9,10,8,4,9",
            "expected_output": "2,1,5"
        },
        {
            "input": "2,5\n7,3,5,4,2\n8,5,4,4,3",
            "expected_output": "-1"
        },

    ]

    # === 自动测试部分 ===
    print("🔍 正在运行预定义测试用例...")
    run_test_cases(main_my, TEST_CASES)

    # === 手动交互模式 ===
    print("\n🔄 自动测试已完成。")
    print("🎮 现在进入交互模式，请手动输入数据运行程序（输入 Ctrl+C 可随时退出）。\n")

    while True:
        try:
            main_my()
            print('=' * 20)
        except Exception as e:
            print(f'Error: {e}')
            print('=' * 20)