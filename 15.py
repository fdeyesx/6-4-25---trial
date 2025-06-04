def f(x1,m):
    if x1 in m: return True
    return False

b = [i for i in range(54,120+1)]
c = [i for i in range(78,151+1)]

for r in range(0,1000):
    a = [i for i in range(0-r,r+1)]
    d = set()
    for x in range(-2000,2000):
        l = f(x,c) => ((f(x,b) or not(f(x,a))) => not(f(x,c)))
        d.add(f)
    if False not in d:
        print(len(a))
        break

