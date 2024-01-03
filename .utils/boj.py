import re


p = re.compile("BOJ(\d+)_(가-힣a-zA-Z)_(\d).py")
print(p.findall("BOJ1000_ABC하이하이_1.py"))