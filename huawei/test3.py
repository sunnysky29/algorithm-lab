"""
题目链接
【华为OD机考 统一考试机试C卷】最长合法表达式（C++ Java Python javaScript）
https://blog.csdn.net/banxia_frontend/article/details/134472024

题目描述：最长合法表达式（本题分值200）
提取字符串中的最长合法简单数学表达式字符串长度最长的，
并计算表达式的值。如果没有返回 0
简单数学表达式只能包含以下内容
0-9 数字，符号+-*
说明:
1.所有数字，计算结果都不超过 long

2.如果有多个长度一样的，请返回第一个表达式的结果

3.数学表达式，必须是最长的，合法的
4.操作符不能连续出现，如 +--+1 是不合法的

输入描述 字符串
输出描述 表达式值 
示例一 
输入
1-2abcd
输出
-1

@@@@@@@@@@@@@@@
解题思路:
1, 替换非法字符为 #  精华所在!!!
2， split, # 
del----: 3,字符合法判断（不需要了）---
4， eval 计算


"""

from auto_test import run_test_cases
from collections import deque

legal_sets = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*'}
digit_sets = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',}



def main():
    s = input().strip()
    print(f's: {s}')
    # 步骤1：替换【所有】非法字符为 '#'
    cleaned = ''
    for ind,ch in enumerate(s):
        if ch in legal_sets:
            if ch in {'+','-','*'}:
                # ch为末尾 or 右边不为数字，也要替换:
                if ind==len(s)-1 or s[ind+1] not in digit_sets: 
                    cleaned += '#'
                else:
                    cleaned += ch
            else: # 数字
                cleaned += ch
        else:
            cleaned += '#'
    print(f'cleaned: {cleaned} !!!')
    if not cleaned:
        print('@'+'0'+'@')
        return

    # 步骤2：用 '#' 分割出所有候选表达式
    candidates = cleaned.split('#')
    print(f'candidates: {candidates}')

    # # 步骤3：过滤出合法表达式
    # valid_exprs = [expr for expr in candidates if expr and is_valid(expr)]
    # print(f'valid_exprs: {valid_exprs} ???')
    valid_exprs = candidates

    # 步骤4：找出最长表达式（若有多个相同长度，保留第一个）
    max_len = max(len(expr) for expr in valid_exprs)
    longest_exprs = [expr for expr in valid_exprs if len(expr) == max_len]
    print(f'longest_exprs: {longest_exprs}')

    if longest_exprs[0]:
        print('@'+str(eval(longest_exprs[0]))+'@')
    else:  # 为 ''
        print('@'+'0'+'@')
        



if __name__ == "__main__":
    TEST_CASES = [
        {
            "input": "1-2abcd",
            "expected_output": "@-1@"
        },
           {
            "input": "a1+21b3*4c",
            "expected_output": "@22@"
        },       
           {
            "input": "a+-1+21b3*4c",
            "expected_output": "@20@"
        },         
           {
            "input": "+--+1",
            "expected_output": "@1@"
        },      
           {
            "input": "ab1--+2cd0+5",
            "expected_output": "@5@"
        },
            {
            "input": "-2",
            "expected_output": "@-2@"
        },
        {
            "input": "=2",
            "expected_output": "@2@"
        },
        {
            "input": "+2",
            "expected_output": "@2@"
        },
        {
            "input": "2+",
            "expected_output": "@2@"
        },
        {
            "input": "1+2*33+44+55+abc",
            "expected_output": "@166@"
        },
        {
            "input": "+abc",
            "expected_output": "@0@"
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

