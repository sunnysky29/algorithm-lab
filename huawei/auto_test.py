



# auto_test.py

from colorama import Fore, Style
from io import StringIO
import sys
from colorama import init

init()  # 初始化 colorama（Windows 必须初始化）


def run_with_input(main_function, test_input: str) -> str:
    """
    模拟输入并捕获输出，用于测试任意 main 函数的行为
    
    参数：
        main_function: 要测试的主函数（如 main_my 或 main_ai）
        test_input: 模拟的标准输入内容（字符串格式）

    返回：
        str: 主函数的输出结果（标准输出）
    """
    stdin_backup = sys.stdin
    stdout_backup = sys.stdout

    sys.stdin = StringIO(test_input)
    sys.stdout = StringIO()

    try:
        main_function()
    except Exception as e:
        output = sys.stdout.getvalue().strip() + f"\n[ERROR: {e}]"
    else:
        output = sys.stdout.getvalue().strip()

    sys.stdin = stdin_backup
    sys.stdout = stdout_backup

    return output


def run_test_cases(main_function, test_cases):
    """
    运行测试用例集合，并输出结果统计

    参数：
        main_function: 被测试的主函数（如 main_my）
        test_cases: 测试用例列表
    """
    passed_count = 0
    for idx, case in enumerate(test_cases):
        print(f"\n🧪 Test Case {idx + 1}")
        print("Input:")
        print(case["input"])
        print("\nExpected Output:")
        print(case["expected_output"])

        actual_output = run_with_input(main_function, case["input"])
        print("\nActual Output:")
        print(actual_output)

        if case["expected_output"].strip() in actual_output.strip():
            print(Fore.GREEN + "✅ Test Passed" + Style.RESET_ALL)
            passed_count += 1
        else:
            print(Fore.RED + "❌ Test Failed" + Style.RESET_ALL)
        print('-' * 20)

    print(f"\n✅ Summary: {passed_count} / {len(test_cases)} tests passed.")
    
    
    
