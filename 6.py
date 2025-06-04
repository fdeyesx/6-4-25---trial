from turtle import *
k = 20
tracer(0)
screensize(5000,5000)
left(90)

for i in range(8):
    forward(10*k)
    right(50)

up()
for x in range(0,100):
    for y in range(0,100):
        goto(x*k,y*k)
        dot(3)
goto(0,0)
dot(5,'red')
done()
