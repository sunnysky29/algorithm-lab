# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/5/1 14:28
File : fmm_word_seg.py

正向最大匹配分词，从前往后扫描句子中的字符串，尽量找到词典中较长的单词作为分词结果
缺点：
    研究生命---> 研究生 命
==============================================================================
"""
from utils import datapath


def load_dict():
    f = open(datapath("data/lexicon.txt"))
    lexicon = set()
    max_len = 0
    for line in f:
        word = line.strip()
        lexicon.add(word)
        if len(word) > max_len:
            max_len = len(word)
    f.close()

    return lexicon, max_len

def fmm_word_seg(sentence, lexicon, max_len):
    begin = 0
    end = min(begin + max_len, len(sentence))
    words = []
    while begin < end:
        word = sentence[begin:end]
        if word in lexicon or end - begin == 1:
            words.append(word)
            begin = end
            end = min(begin + max_len, len(sentence))
        else:
            end -= 1
    return words

lexicon, max_len = load_dict()
words = fmm_word_seg(input("请输入句子："), lexicon, max_len)

for word in words:
    print(word,)