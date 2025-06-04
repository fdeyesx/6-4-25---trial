def f(n):
    s = ''
    while n!=0:
        s = str(n%3) + s
        n //= 3
    return s

def main(n):
    s = f(n)
    if n%3 == 0:
        s = s + s[-2:]
    else: s = s + f((n%3)*5)
    return int(s,3)

a = []
for n in range(1,1000):
    r = main(n)
    if r > 133:
        a.append(r)

print(min(a))
