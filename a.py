


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:  # 处理空数组情况
            return False
        
        rows = len(matrix)     # 获取行数
        cols = len(matrix[0])  # 获取列数
        
        # 从左下角开始查找
        row, col = rows - 1, 0
        
        while row >= 0 and col < cols:
            current = matrix[row][col]
            if current == target:
                print(f'{target} found!!')
                return True
            elif current > target:  # 如果当前值大于目标值，上移一行
                row -= 1
            else:                   # 如果当前值小于目标值，右移一列
                col += 1
                
        return False

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    matrix1 = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target1 = 14
    print(solution.findNumberIn2DArray(matrix1, target1))  # 输出: True
    
    # 测试用例2
    target2 = 20
    print(solution.findNumberIn2DArray(matrix1, target2))  # 输出: False
    
    # 测试空数组
    matrix_empty = []
    print(solution.findNumberIn2DArray(matrix_empty, 1))   # 输出: False
    
    # 测试单元素数组
    matrix_single = [[5]]
    print(solution.findNumberIn2DArray(matrix_single, 5))  # 输出: True
    print(solution.findNumberIn2DArray(matrix_single, 3))  # 输出: False