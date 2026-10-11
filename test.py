sentence = "the quick brown fox jumps over the lazy dog the end"

words = sentence.split()          # 第 1 步：切
counts = {}                       # 第 2 步：备

for w in words:                   # 第 3 步：数
    counts[w] = counts.get(w, 0) + 1

print(counts)                     # 第 4 步：打