import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()

screen.onkey(player.move, 'Up')

reps = 0
game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    if reps % 6 == 0:
        car_manager.create_car()
    reps += 1
    car_manager.move_cars()
    if car_manager.is_collision(player):
        game_over = True
    if player.at_finish_line():
        player.set_player()
        scoreboard.level_up()
        car_manager.level_up()

player.game_over()
car_manager.game_over()
scoreboard.game_over()

screen.exitonclick()
