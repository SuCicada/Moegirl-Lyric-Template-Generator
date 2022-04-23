#!/bin/env python
import pykakasi
import sys

kakasi = pykakasi.kakasi()


def kanji2moe(kanji_text: list):
    """ """
    # print(type(kanji_text))
    if type(kanji_text) is str:
        kanji_text = [kanji_text]

    hira_text = []
    for line in kanji_text:
        text = line.strip()
        result = kakasi.convert(text)
        hira_line = ""
        for item in result:
            orig = item['orig']
            hira = item['hira']

            if orig == hira:
                hira_line += orig
            else:
                res_kanji, res_hira, common_hira = tidyHira(orig, hira)
                hira_line += "{{PT|%s|%s}}%s" % (
                    res_kanji, res_hira, common_hira)
        hira_text.append(hira_line)
    return hira_text


def tidyHira(kanji, hira):
    """ 去掉包含在汉字末尾中的平假名 """
    res_kanji = kanji
    res_hira = hira
    common_hira = ""
    # print(kanji+" "+hira)
    kanji_len = len(kanji)
    hira_len = len(hira)
    for i in range(1, kanji_len+1):
        # print(i)
        if kanji[kanji_len-i] != hira[hira_len-i]:
            res_kanji = kanji[:kanji_len-i+1]
            res_hira = hira[:hira_len-i+1]
            common_hira = hira[hira_len-i+1:]
            # print(kanji, hira)
            # print(res_kanji, res_hira, common_hira)
            break
    return res_kanji, res_hira, common_hira
