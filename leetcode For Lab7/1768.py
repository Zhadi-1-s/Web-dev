word1 = input()
word2 = input()

n = max(len(word1),len(word2))
x = min(len(word1),len(word2))
s = ""

i = 0

while i < n:
    if len(s)%2 == 0 and i < x:
        s+=word1[i]
        s+=word2[i]
        i+=1
    elif len(s)%2 == 1 and i < x:
        s+=word2[i]
        s+=word1[i]
        i+=1
    if len(word1) > len(word2) and i >=len(word2):
        s+=word1[i]
        i+=1
    elif len(word2) > len(word1) and i >= len(word1):
        s+=word2[i]
        i+=1
print(s)