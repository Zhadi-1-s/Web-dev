dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
subtract = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
s = input()

sum = 0

for i in s:
    sum+=dict[i]

