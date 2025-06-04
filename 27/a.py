def d(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def distance(k1,k2):
    o = 10**10
    for i in range(len(k1)):
        tx,ty = k1[i][0], k2[i][1]
        s = 0
        for j in range(len(k2)):
            cx, cy = k2[j][0], k2[j][1]
            s += d(tx,ty,cx,cy)
            if s < o:
                krx = tx
                kry = ty
                o = s
    return [krx,kry]

print('第一')
s = open('27A_1.txt').readlines()
ak1,ak2 = [],[]
for i in s:
    r = i.split()
    x,y = float(r[0]),float(r[1])
    if y < 4: ak1.append([x,y])
    else: ak2.append([x,y])

x1,y1 = distance(ak1,ak2)
x2,y2 = distance(ak2,ak1)

print( (x1+x2)/2 * 10_000)
print( (y1+y2)/2 * 10_000)


