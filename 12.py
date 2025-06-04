def pr(n):
    d = set()
    for k in range(1,int(n*0.5)+1):
        if n%k == 0:
            if k != 1 and k!=n:
                return False
            d.add(k)
            d.add(n%k)
    return True

for n in range(0,1000):
    s = '>'+ 39*'0' +  n*'1' + 39*'2'
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1','22>',1)
        s = s.replace('>2','2>',1)
        s = s.replace('>0','1>',1)

    s = s.replace('>','0')
    sum1 = 0
    for j in s:
        sum1 += int(j)
    if pr(sum1) == True:
        print(n, sum1)
        break
