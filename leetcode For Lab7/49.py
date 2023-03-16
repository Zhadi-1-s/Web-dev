from collections import Counter, defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

dic = defaultdict(list)

for i in strs:
    dic[frozenset(Counter(i).items())].append(i)

print(dic)