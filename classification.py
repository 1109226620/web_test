# -*- coding:utf-8 -*-
__author__ = "songyibin"
__time__ = "2019/4/2"

import fasttext as ft
import jieba
# from venv.scripts import jieba
# from base64 import jieba


def classifi(lst):
    classifier = ft.load_model('static/data/news_fasttext_n.model.bin')
    test = []
    stopwords = {}.fromkeys([line.rstrip() for line in open('static/data/stopwdlst.txt', encoding='gbk')])
    for j in range(0, len(lst)):
        segs = jieba.lcut(lst[j], cut_all=False)
        segs = filter(lambda x: x not in stopwords, segs)
        segs = " ".join(segs)
        test.append(segs)
    pre_lst = classifier.predict(test)
    res = []
    for i in range(0,len(pre_lst)):
        item = pre_lst[i]
        name = lst[i]
        all = name + "--->" + item
        res.append(all)
    return res