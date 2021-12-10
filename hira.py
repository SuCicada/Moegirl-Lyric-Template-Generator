#!/bin/env python
import pykakasi
import sys

kakasi = pykakasi.kakasi()

def kanji2moe(kanji_text: list|str):
    """ """
    if type(kanji_text) == "str":
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
                hira_line += "{{PT|%s|%s}}" % (orig, hira)
        hira_text.append(hira_line)
    return hira_text
