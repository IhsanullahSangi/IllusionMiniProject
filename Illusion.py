import turtle
import random


line_in_turtle = turtle.Turtle()
line_in_turtle_colors = ["#8E44AD","#00FFFF","#FF7F50","#40E0D0","#FF69B4","#708090","#F4A460","#0000FF","#DDA0DD",
                         "#87ceeb","#708090","#4169E1","#FFD700","#000080","#800080","#20B2AA","#ADD8E6","#F08080",
                         "#5f9ea0","#483D8B","#6b8e23", "#00ff7f", "#6495ED", "#ff77ff", "#cd853f", "#48D1CC",
                         "#DC143C", "#4682B4","#c3b091","#7fffd4","#dfff00", "#008B8B", "#FF0000", "#e9967a",
                         "#00FFFF", "#cd5c5c", "#B22222", "#c71585","#00bfff", "#BA55D3","#ff6347", "#b8860b",
                         "#87cefa", "#9370DB", "#2F4F4F", "#ff8c69", "#b0c4de", "#00CED1","#556B2F", "#FF1493",
                         "#1E90FF", "#66CDAA", "#9932CC", "#db7093", "#98FB98", "#D2691E", "#008080", "#FF8C00",
                         "#006400", "#DAA520",]

line_in_turtle.speed(0)
line_in_turtle.width(6)

for s in range(360):
    color = random.choice(line_in_turtle_colors)
    line_in_turtle.color(color)
    line_in_turtle.forward(200)
    line_in_turtle.right(40)
    line_in_turtle.forward(50)  # main
    line_in_turtle.left(60)
    line_in_turtle.forward(90)  # main
    line_in_turtle.right(30)  # main

    line_in_turtle.up()
    line_in_turtle.setposition(0,0)
    line_in_turtle.pendown()

    line_in_turtle.right(1)

turtle_inside_illusion = turtle.Turtle()

r = 1

for i in range(185):
    turtle_inside_illusion.circle(r + i, 45)
    turtle_inside_illusion.hideturtle()

turtle.done()
