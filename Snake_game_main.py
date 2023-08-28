from turtle import Screen
from Snake_class import Snake
from snake_food import Food
from my_score import Scoreboard
import winsound
import pygame
import time

pygame.init()
pygame.mixer.init() #Initalize pygame mixer for the background music

my_screen = Screen()
my_screen.setup(width=700, height=700)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

#Background music using pygame
pygame.mixer.music.load("C:\\Users\\Hero\\Desktop\\Mini-projects\\Snake game\\Background_music.wav")
pygame.mixer.music.play(-1)  

game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.moving()
    
    #Detecting food collision
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        scoreboard.increase_score()
        winsound.PlaySound("C:\\Users\\Hero\\Desktop\\Mini-projects\\Snake game\\Yummy.wav", winsound.SND_ASYNC)

    #Detecing wall collision
    if my_snake.head.xcor() > 345 or my_snake.head.xcor() < -345 or my_snake.head.ycor() > 345 or my_snake.head.ycor() < -345:
        game_on = False
        scoreboard.game_over()
        winsound.PlaySound("C:\\Users\\Hero\\Desktop\\Mini-projects\\Snake game\\Game_over_sound.wav", winsound.SND_ASYNC)

    #Detecting tail collision
    for segment in my_snake.new_bits:
        if segment == my_snake.head:
            pass
        elif my_snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
            winsound.PlaySound("C:\\Users\\Hero\\Desktop\\Mini-projects\\Snake game\\Game_over_sound.wav", winsound.SND_ASYNC)
            
pygame.mixer.music.stop()
my_screen.exitonclick()