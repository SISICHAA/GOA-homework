from turtle import *



#we want to paint house

#step 1: draw a square
speed(130)


width(7)
color("purple")



forward(200)
left(90)
  

forward(200)







left(90)

forward(200)
left(90)



forward(200)
left(90)


#end of square
 

#drawing a door

forward(70)
begin_fill()
color("yellow")


left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("purple")


left(30)
forward(30)
begin_fill()

color("gray")
right(270)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()


penup()
goto(200,200)
pendown()
color("purple")

left(90)
forward(30)
begin_fill()
color("gray")
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()


color("purple")

penup()
goto(0,0)
pendown()

forward(70)
left(90)







exitonclick()
