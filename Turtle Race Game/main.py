import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLOURS = ["red", "blue", "black", "yellow", "orange", "green", "brown", "cyan", "pink", "purple"]

def number_of_racers():
    racers = 0
    while True:
        try:
            racers = int(input("Enter the number of racers (2-10): "))
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number not in range 2 - 10. Try again!")
        except ValueError:
            print("Input is not numeric....Try again!")
            continue

def racing_turtle(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def turtle_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


racers = number_of_racers()
turtle_screen()

random.shuffle(COLOURS)
colors = COLOURS[:racers]

winner = racing_turtle(colors)
print(f"The winner is: {winner.capitalize()}")
time.sleep(3)