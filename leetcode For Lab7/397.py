hash = {1:0}

def rec(n):
        if n in hash:
            return hash[n]
        if n%2:
            hash[n] = 1 + min(rec(n+1),rec(n-1))
        else:
            hash[n] = 1 + rec(n/2)
            return hash[n]
        return rec(n)

print(rec(8))