import moehira
import sys
inn = sys.argv[1]
out = sys.argv[2]

with open(inn, "r", encoding='UTF-8') as file:
    
    txt = file.readlines()
    res = moehira.kanji2moe(txt)
    print(res)
    
    with open(out, "w", encoding='UTF-8') as file:
        file.write("\n".join(res))
