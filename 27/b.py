def d(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def distance(k1,k2,k3):
    o = 10**10
    for i in range(len(k1)):
        tx,ty = k1[i][0], k2[i][1]
        s = 0
        for j in range(len(k2)):
            for l in range(len(k3)):
                cx, cy = k2[j][0], k2[j][1]
                cx2, cy2 = k3[l][0], k3[l][1]
                s += d(tx, ty, cx, cy)
                s += d(tx, ty, cx2, cy2)
                if s < o:
                    krx = tx
                    kry = ty
                    o = s
    return [krx,kry]

print('第一')
s = open('27B_1.txt').readlines()
bk1,bk2,bk3 = [],[],[]
for i in s:
    r = i.split()
    x,y = float(r[0]),float(r[1])
    if y >5 : bk1.append([x,y])
    else:
        if x < 2: bk2.append([x,y])
        else: bk3.append([x,y])

x1,y1 = distance(bk1,bk2,bk3)
x2,y2 = distance(bk2,bk1,bk3)
x3,y3 = distance(bk3,bk1,bk2)

print( (x1+x2+x3)/3 * 10_000)
print( (y1+y2+y3)/3 * 10_000)


