from turtle import * #tartle-იდან პროექტის დაწყება

speed(300) #სისწრაფის დაყენება

#ხაზის დიზაინი
width(7)
color("black")

#საწყის წერტილზე გადატანა
penup()
goto(-50, -100)
pendown()

#მოძრაობის დაწყება
forward (450)
left(90)

forward(400)
right(90)

forward (30)
right(90)

forward(400)
right(90)

forward(30)


penup()
right(90)
forward(400)
pendown()

color("red")
begin_fill()
right(45)
forward(22.5)
right(90)
forward(22.5)
end_fill()

color("black")
right(135)
forward(480)

left(90)
forward(400)

right(90)
forward(30)

right(90)
forward(400)

color("red")

begin_fill() #გაფერადების დაწყება
right(45)
forward(22.5)
right(90)
forward(22.5)
end_fill() #გაფერადების დასრულება

penup()
goto(115, 0)
pendown()

right(45)

color("brown")

begin_fill()
forward(100)
left(90)
forward(150)
left(90)
forward(225)
left(90)
forward(150)
left(90)
forward(125)
end_fill()

color("red")
penup()
goto(400, 300)
pendown()

begin_fill()
right(115)
forward(245)
left(50)
forward(245)
end_fill()


exitonclick() #კლიკზე გასვლა