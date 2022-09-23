import os

for each in os.listdir():
    if '.html' not in each: continue
    with open(each , 'r', encoding='utf-8') as f:
        sss = f.read()
    sss = sss.replace('/caricaturesource/OPM/', 'caricaturesource/OPM/')
    with open(each , 'w', encoding='utf-8') as f:
        f.write(sss)