from itertools import product
k=0
for i in product('01234567',repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('6') == 1:
            for j in '1357':
                s = s.replace(j,'-')
            if '-6' not in s and '6-' not in s:
                k+=1
                print(s)
print(k)
