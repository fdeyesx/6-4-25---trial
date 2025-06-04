def f(s,e):
    if s < e or s == 32: return 0 
    if s == e: return 1
    return f(s-2,e)+f(s-5,e)+f(s//3,e)

print(f(46,19)*f(19,7))
