s = input()

vowel = ['a','e','i','o','u']
string = []
res = []
for i in s:
    string.append(i)
for i in range(len(s)-1,-1,-1):
    if s[i] in vowel:
        res.append(s[i])

for i in range(len(s)):
    if string[i] in vowel:
        string[i] = res[i]

print(string)