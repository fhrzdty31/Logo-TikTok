from turtle import *

width(20)
bgcolor('#ffffff')
warna= ['#ff0050', '#00f2ea', '#010101']
posisi= [(4,0), (-4,14), (0,7)]

for (x,y),col in zip(posisi,warna):
    up()
    goto(x,y)
    down()
    color(col)
    left(180)
    circle(50, 270)
    forward(120)
    left(180)
    circle(50, 90)

input("")