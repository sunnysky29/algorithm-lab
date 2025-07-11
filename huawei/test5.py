"""
最新华为OD机试
真题目录：点击查看目录 华为OD面试真题精选：点击立即查看

题目描述
某个打印机根据打印队列执行打印任务。打印任务分为九个优先级，分别用数字1-9表示，数字越大优先级越高。打印机每次从队列头部取出第一个任务A，

然后检查队列余下任务中有没有比A优先级更高的任务，如果有比A优先级高的任务，则将任务A放到队列尾部，否则就执行任务A的打印。

请编写一个程序，根据输入的打印队列，输出实际的打印顺序。

输入描述
输入一行，为每个任务的优先级，优先级之间用逗号隔开，优先级取值范围是1~9。

输出描述
输出一行，为每个任务的打印顺序，打印顺序从0开始，用逗号隔开

示例1
输入

9,3,5
输出

0,2,1
说明

队列头部任务的优先级为9，最先打印，故序号为0； 接着队列头部任务优先级为3，队列中还有优先级为5的任务，优先级3任务被移到队列尾部； 接着打印优先级为5的任务，故其序号为1； 最后优先级为3的任务的序号为2。

"""

from auto_test import run_test_cases
from collections import deque

def main():
    priorities = input().strip().split(',') # [1,2,2]
    
    queue = deque()
    for idx, priority in enumerate(priorities):
        queue.append((priority, idx))
    
    order = [0] * len(priorities)
    cur_order = 0
    
    while queue:
        cur = queue.popleft()
        # 检查队列中是否有比当前更高优先级的任务
        has_higher = any(item[0] > cur[0] for item in queue)
        if has_higher:
            queue.append(cur)
        else:
            order[cur[1]] = cur_order
            cur_order += 1
    print(order, '>??')
    print(','.join(map(str,order)))






if __name__ == "__main__":
    TEST_CASES = [
        {
            "input": "9,3,5",
            "expected_output": "0,2,1"
        },
        {
            "input": "1,2,2",
            "expected_output": "2,0,1"
        },


        
    ]

    # === 自动测试部分 ===
    print("🔍 正在运行预定义测试用例...")
    run_test_cases(main, TEST_CASES)

    # === 手动交互模式 ===
    print("\n🔄 自动测试已完成。")
    print("🎮 现在进入交互模式，请手动输入数据运行程序（输入 Ctrl+C 可随时退出）。\n")

    while True:
        try:
            main()
            print('=' * 20)
        except Exception as e:
            print(f'Error: {e}')
            print('=' * 20)

