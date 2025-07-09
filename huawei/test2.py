"""
华为od机试 字符串变换最小字符串


给定一个字符串 s，最多只能进行一次变换，
返回变换后能得到的最小字符串(按照字典 序进行比较)
变换规则: 交换字符串中任意两个不同位置的字符

输入描述

一串小写字母组成的字符串 s

输出描述

按照要求进行变换得到的最小字符串。

用例1

输入
abcdef
输出
abcdef
说明
abcdef已经是最小字符串，不需要交换。


解题思路
如果字符串已经是字典序最小的（即非递减排序的），
则直接返回原字符串。
否则，我们寻找可以通过一次交换得到的最小字符串：
遍历字符串，寻找第一个可以替换的位置 i
对于位置 i，找后面最小的字符 c
在更后面的字符中寻找比 c 小的最小字符，以获得最小结果
找到合适的一对字符进行交换，得到最小字符串


字典序（Lexicographical Order）
字典序是字符串比较的基础，类似于字典中单词的排列顺序

比较规则：从左到右逐个字符比较ASCII码值，第一个不同字符决定整体顺序

例如："apple" < "apricot"（因为'l' < 'r'）

2. 贪心算法（Greedy Algorithm）
本题采用贪心策略：在第一个能使字符串变小的位置进行最优交换

贪心选择性质：每次选择当前看起来最优的交换（最左边的可交换位置+最右边的最小值）

最优子结构：局部最优交换能保证全局最优结果


main()：O(n²)
main_other()：O(n log n)

"""

from auto_test import run_test_cases
from collections import deque

def main():
    s = input().strip()

    # 如果字符串已经是字典序最小的，直接返回
    if ''.join(sorted(s)) == s:
        print(s)
        return
    
    s_li = list(s)
    n = len(s_li)
    
    for i in range(n-1):
        # 找到当前字符后面最小的字符
        min_char = min(s_li[i+1:])  #  ord() 比较
        
        # 如果找到更小的字符，可以进行交换
        if min_char < s_li[i]:
            # 找到最小字符的最右位置（保证交换后整体最小）
            for j in range(n-1, i, -1): #  注意这里是倒着找
                if s_li[j] == min_char:
                    s_li[i], s_li[j] = s_li[j], s_li[i]
                break
            break  #  两个 break 终止两个for
                    
    print(''.join(s_li))



def main_other():
    s = input().strip()
    minArr = list(s)

    minArr.sort() # 先排序一把
    # 边界判断
    if s == "".join(minArr):# 这里因为minArr已经是list了。
        return s
    sArr = list(s) # 把s搞成list
    # 然后一个个来对比。
    for i in range(len(s)):
        # 因为已经拍好序了，所以第一个出现不同的就要把他揪出来。
        if sArr[i] != minArr[i]:
            # 把sArr[i] 存好，
            tmp = sArr[i]
            # 把sArr[i]替换成minArr[i]
            sArr[i] = minArr[i]
            # 接下来就要找tmp 在sArr的位置了。从右边开始找。
            swapIdx = s.rindex(minArr[i])
            sArr[swapIdx] = tmp
            # 找到了就break结束循环
            break
    print(''.join(sArr))



if __name__ == "__main__":
    TEST_CASES = [
        {
            "input": "bcdefa",
            "expected_output": "acdefb"
        },
        {
            "input": "badea",
            "expected_output": "aadeb"
        },   
        {
            "input": "baafaaaa",
            "expected_output": "aaafaaab"
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

