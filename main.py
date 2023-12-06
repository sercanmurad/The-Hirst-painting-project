###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import turtle as turtle_module

turtle_module.colormode(255)#rgb mode open
tim=turtle_module.Turtle()#Create tim turtle
tim.speed("fastest")#Change tim speed
tim.penup()#To look more good we use penup function
tim.hideturtle()#Hide tim because it look more good
color_list=[(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots=100

for dots_count in range(1, number_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dots_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen=turtle_module.Screen()#it is important this function help us to exit screen after we click
screen.exitonclick()