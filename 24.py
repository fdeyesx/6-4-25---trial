s = open('24 (1).txt').readline()
mxp = ''
p = ''
for i in s:
    p += i
    if p[0] not in '18':
        p = ''
    if len(p) > 2:
        if p[-1] in '18':
            if p[0] != p[-1]:
                if p.count('B') == p.count('C'):
                    if len(p) > len(mxp):
                        mxp = p
                        p = p[-1]
print(len(mxp))
