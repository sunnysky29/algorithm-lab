
# 流浪地球

"""

题目描述
流浪地球计划在赤道上均匀部署了N个转向发动机，按位置顺序编号为0~N-1。发动机的启动方式分为“手动启动”和“关联启动”两种方式。

如果一个发动机被手动启动，下一个时刻与之相邻的两个发动机会被“关联启动”。

如果准备启动某个发动机时，它已经被启动了，则什么都不用做。

发动机0与发动机N-1是相邻。地球联合政府准备挑选某些发动机在某些时刻进行“手动启动”，最终所有的发动机都会被启动。需要找出哪些发动机最晚被启动。

输入描述
第一行两个数字N和E，中间有空格。

N代表部署发动机的总个数，E代表计划手动启动的发动机总个数。

1<N<=1000，1<=E<=1000,E<=N。

接下来共E行，每行都是两个数字T和P，中间有空格。

T代表发动机的手动启动时刻，P代表此发动机的位置编号。0<=T<=N,0<=P<=N。

输出描述
第一行一个数字N，以回车结束。

N代表最后被启动的发动机个数。

第二行N个数字，中间有空格，以回车结束。每个数字代表发动机的位置编号，从小到大排序。


原文链接：https://blog.csdn.net/tu123456s/article/details/147547713


测试用例1：
    3 1  #  发动机数，手动启动事件数
    0 0  #  手动启动事件，时间0，位置0
    ------- 
    2    # 最后被启动的发动机个数
    1 2  # 最后被启动的发动机位置编号，从小到大排序

"""
from auto_test import run_test_cases
from collections import deque

def main_my():
    # 输入处理
    n, e = map(int, input("输入:发动机数量 手动启动数\n").strip().split() )
    manual_events = {} # 读取发动机总数 N 和手动启动事件数 E
    if n <= 1:
        print("Invalid input: N must be greater than 1.")
        return
    if e <= 0:
        print("Warning: No manual activation events (E <= 0). All engines remain inactive.")
        return
    
     # 循环读取每一个手动启动事件（T, P）, (时间，位置)
    for _ in range(e):
        t, p = map(int, input('输入：t p \n').strip().split())
        # manual_events[t].append(p)
        manual_events.setdefault(t, []).append(p)      
    print(f'manual_events : {manual_events}') # {1: [6], 0: [0, 3]}
    
    # 初始化一个数组 on_time，
    # 记录每个发动机被激活的时间  ！！
    # 初始值为 -1 表示尚未激活
    on_time = [-1] * n
    
    # 构建多源队列：将手动启动的发动机加入队列，并记录其启动时间
    q = deque()
    for t, p in manual_events.items():
        if len(p)>1:  #  处理列表
            for p_i in p:
                on_time[p_i] = t
                q.append((p_i, t))
        else:
            on_time[p[0]] = t
            q.append((p[0], t))
    print(f'初始q: {q} ???') #  deque([(6, 1), (0, 0), (3, 0)]) ???
    print(f'初始on_time: {on_time} ???')
    
    time = 0 # 记录当前时间
    
    # BFS 层序遍历，模拟发动机扩散过程
    while q:
        level_size = len(q)
        for _ in range(level_size):
            pos, t = q.popleft()
            if t==time:
                # 向左右两个方向传播
                for dx in (-1, 1):
                    next_pos = (pos + dx) % n  # 环形结构
                    next_time = t + 1
                    if on_time[next_pos] == -1:
                        on_time[next_pos] = next_time
                        q.append((next_pos, next_time))
            else: #  需要延迟启动（因为手动启动时候，时间不固定）
                q.append((pos, t))
        time += 1

    print(f'最终 on_time: {on_time} ???')
    # 找出最晚被启动的发动机时间 & 发动机编号
    latest_time = max(on_time)
    result = [i for i, t in enumerate(on_time) if t == latest_time]
    result.sort()

    print(len(result))
    print(" ".join(map(str, result)))
    
    
def main_AI():
    '''
    AI 代码
    '''
    # 输入处理
    n, e = map(int, input().strip().split() )
    manual_events = {} # 读取发动机总数 N 和手动启动事件数 E
    if n <= 1:
        print("Invalid input: N must be greater than 1.")
        return
    if e <= 0:
        print("Warning: No manual activation events (E <= 0). All engines remain inactive.")
        return
    
     # 循环读取每一个手动启动事件（T, P）, (时间，位置)
    for _ in range(e):
        t, p = map(int, input().strip().split())
        # manual_events[t].append(p)
        manual_events.setdefault(t, []).append(p)      
    print(f'manual_events : {manual_events}')
    
    # 初始化一个数组 on_time，
    # 记录每个发动机被激活的时间  ！！
    # 初始值为 -1 表示尚未激活
    on_time = [-1] * n

    q = deque() # BFS 队列
    
    # 初始化手动启动事件到队列中， {1: [6], 0: [0, 3]}
    for t in sorted(manual_events.keys()): #  按照时间排序
        for pos in manual_events[t]:
            if on_time[pos] == -1:
                on_time[pos] = t
                q.append((pos, t))  # 注意，（位置，t）
    print(f'on_time: {on_time}') #  [0, -1, -1, 0, -1, -1, 1, -1]
    print(f'q: {q}') #  q: deque([(0, 0), (3, 0), (6, 1)])

    # 进行 BFS 扩散
    while q:
        pos, time = q.popleft()
        for dx in (-1, 1):
            next_pos = (pos + dx + n) % n  # 环形结构
            next_time = time + 1
            if on_time[next_pos] == -1:
                on_time[next_pos] = next_time
                q.append((next_pos, next_time))

    # 找出最晚被激活的发动机
    latest_time = max(on_time)
    result = [i for i, t in enumerate(on_time) if t == latest_time]

    # 输出结果
    print(len(result))
    print(' '.join(map(str, sorted(result))))



if __name__ == "__main__":
    TEST_CASES = [
        {
            "input": "3 1\n0 0",
            "expected_output": "2\n1 2"
        },
        {
            "input": "8 2\n0 0\n1 7",
            "expected_output": "1\n4"
        },
        {
            "input": "4 2\n0 0\n0 2",
            "expected_output": "2\n1 3"
        },
        {
            "input": "8 3\n1 6\n0 0\n0 3",
            "expected_output": "1\n5"
        },
        {
            "input": "16 3\n0 2\n0 6\n2 10",
            "expected_output": "1\n13"
        }
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