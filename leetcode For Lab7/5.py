from numpy import kaiser


s = input()

x = ""
i = 1
j = len(s)-2

for k in range(i,j+1):
    x+=s[k]

print(x)