from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turn off automatic screen updates
screen.tracer(0)

# Initialize classes
snake = Snake()
food = Food()
score = ScoreBoard()

# Start waiting for keystrokes and act accordingly
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    # Update every 0.1 seconds to give experience of real time update
    screen.update()
    time.sleep(0.1)
    # Move snake towards the directions it is currently facing
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        score.score_point()
        snake.extend()
        food.refresh()

    # Detect collision with wall, and then reset snake and score
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        snake.restart()
        score.restart()
        # game_is_on = False
        # score.game_over()

    # Detect collision with tail, and then reset snake and score
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.restart()
            score.restart()
            # game_is_on = False
            # score.game_over()

screen.exitonclick()
