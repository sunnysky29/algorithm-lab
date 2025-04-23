"""
关于一些常用的辅助函数
"""

import os
import time

module_path = os.path.dirname(__file__)  # needed because sample data files are located in the same folder


def remove_nan_string(li):
    """移去列表中的 ''

    :param li:
    :return:

    Examples
    --------
    demo = ['元器件', '', '', '电感', 'l4', '', '4*4mm']
    print(remove_nan_string(demo))
    >>>  ['元器件', '电感', 'l4', '4*4mm']
    """
    return [x for x in li if x!='']


def datapath(fname):
    """
    方便加载路径
    :param fname:
    :return:
    """
    return os.path.join(module_path, fname)


def cal_time(func):
    """
    计时装饰器

    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'{func.__name__} running time：{t2 - t1}secs')
        return result
    return wrapper



