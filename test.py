#!/bin/env python
import pykakasi
import sys
inn = sys.argv[1]
out = sys.argv[2]
kakasi = pykakasi.kakasi()
hira_text = []
with open(inn, "r", encoding='UTF-8') as file:
    for line in file.readlines():
        text = line.strip()
        result = kakasi.convert(text)
        print(text)
        hira_line=""
        for item in result:
            orig = item['orig']
            hira = item['hira']
            if orig == hira:
                hira_line += orig
            else:
                hira_line += "{{PT|{}|{}}}".format(orig, hira)
        print(hira_line)
        hira_text.append(hira_line)
print(hira_text)

with open(out, "w", encoding='UTF-8') as file:
    file.write("\n".join(hira_text))
