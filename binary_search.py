# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/5/16 22:18
File : binary_search.py
二分查找算法

==============================================================================
"""

import traceback


class BinarySearch():

    @staticmethod
    def binary_search(list, item):
        """
        非递归二分查找
        :param list:
        :param item:
        :return:
        """
        pass
        low = 0
        high = len(list)-1

        while low <= high:
            mid = (low+high) // 2  # 注意中间值的选取
            guess = list[mid]
            if guess == item:
                return mid
            elif guess > item:
                high = mid -1
            else:
                low = mid +1
        return None

    # 递归版本
    @classmethod
    def b_search_recursion(cls, li, l, h, tar):
        if l>h: return None
        mid = (h+l)//2
        pivot = li[mid]
        if pivot==tar: return mid
        elif tar<pivot: return cls.b_search_recursion(li,l,mid-1,tar)
        else: return cls.b_search_recursion(li,mid+1,h,tar)

    @staticmethod
    def transform_b_search1(li, tar):
        """
        二分查找变体，查找第一个值等于给定值的元素
        :param li:
        :param tar:
        :return:
        """
        l = 0
        h = len(li) - 1
        while l <= h:
            mid = (h + l) // 2
            pivot = li[mid]
            if tar == pivot:
                if li[mid - 1] != tar or mid == 0:
                    return mid
                else:
                    h = mid - 1
            elif tar < pivot:  # 缩小h
                h = mid - 1
            else:
                l = mid + 1
        return None

    @staticmethod
    def transform_b_search2(li, tar):
        """
        二分查找变体，查找最后一个值等于给定值的元素
        :param li:
        :param tar:
        :return:
        """
        l = 0
        h = len(li) - 1
        while l <= h:
            mid = (h + l) // 2
            pivot = li[mid]
            if tar == pivot:
                if mid == len(li) - 1 or li[mid + 1] != tar:
                    return mid
                else:
                    l = mid + 1
            elif tar < pivot:  # 缩小h
                h = mid - 1
            else:
                l = mid + 1
        return None

    @staticmethod
    def transform_b_search3(li, tar):
        """
        二分查找变体，查找第一个大于等于给定值的元素
        :param li:
        :param tar:
        :return:
        """
        l = 0
        h = len(li) - 1
        while l <= h:
            mid = (h + l) // 2
            pivot = li[mid]
            if pivot >= tar:
                if mid == 0 or li[mid - 1] < tar:
                    return mid
                else:
                    h = mid - 1
            else:
                l = mid + 1
        return None


    @staticmethod
    def transform_b_search4(li, tar):
        """
        二分查找变体，查找最后一个小于等于给定值的元素
        :param li:
        :param tar:
        :return:
        """
        l = 0
        h = len(li) - 1
        while l <= h:
            mid = (h + l) // 2
            pivot = li[mid]
            if pivot <= tar:
                if mid == len(li) - 1 or li[mid + 1] > tar:
                    return mid
                else:
                    l = mid + 1
            else:
                h = mid - 1
        return None

if __name__ == "__main__":
    test_list = [1,3,5,7,9]
    print(f'测试非递归二分查找：')
    print(BinarySearch.binary_search(test_list, 3))
    print(BinarySearch.binary_search(test_list, 7))
    print(BinarySearch.binary_search(test_list, -2))

    print(f'测试递归二分查找：')
    li = [1, 3, 3, 3, 5, 6, 7, 7]
    tar = 7
    print(BinarySearch.b_search_recursion(li, 0, len(li) - 1, tar))

    print(f'测试二分查找变体：')
    li = [1, 3, 3, 3, 5, 6, 7, 7]
    print('位置对应关系：', {str(i): v for i, v in enumerate(li)})
    print(BinarySearch.transform_b_search1(li, 7))  # 查找第一个值等于给定值的元素
    print(BinarySearch.transform_b_search2(li, 7))  # 查找最后一个值等于给定值的元素

    print(BinarySearch.transform_b_search3(li, 3))  #查找第一个大于等于给定值的元素
    print(BinarySearch.transform_b_search4(li, 3))  #查找最后一个小于等于给定值的元素
    print(BinarySearch.transform_b_search4(li, -20))  #查找最后一个小于等于给定值的元素