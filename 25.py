def pr(n):
    d = set()
    for k in range(1,int(n**0.5)+1):
        if n%k == 0:
            if k != 1 and k!=n:
                return False
            d.add(k)
            d.add(n%k)
    return True

k = 0
for x in range(23_600_000,10**10):
    d = set()
    for i in range(2,int(x**0.5)):
        if x%i == 0:
            d.add(i)
            d.add(x%i)
    d = sorted(list(d))
    if len(d) > 2:
        r = []
        for j in d:
            if pr(j) == True:
                r.append(j)
        if len(r) > 2:
            M = min(r) + max(r)
            if M%213 == 171:
                k+=1
                print(x,M)
                if k == 6: break
