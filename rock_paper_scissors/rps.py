import turtle
import time
from random import choice

#create a screen
screen = turtle.Screen()

# add shapes into turtle
turtle.register_shape('win.gif')
turtle.register_shape('lose.gif')
turtle.register_shape('draw.gif')
turtle.register_shape('paper.gif')
turtle.register_shape('rock.gif')
turtle.register_shape('scissor.gif')

#crete turtle
robot = turtle.Turtle(shape='turtle')
rock = turtle.Turtle(shape='rock.gif')
paper = turtle.Turtle(shape='paper.gif')
scissor = turtle.Turtle(shape='scissor.gif')

# move turtle to new pos
robot.sety(200)
rock.goto(-200, -200)
paper.sety(-200)
scissor.goto(200, -200)

# click func
def choose_shape(x, y):
    player_choice = None
    robot_choice = None
    choices = ['rock', 'paper', 'scissor']

    # check user click 
    if rock.distance((x,y)) < paper.distance((x,y)) and rock.distance((x,y)) < scissor.distance((x,y)):
        player_choice = 'rock'
    if paper.distance((x,y)) < rock.distance((x,y)) and paper.distance((x,y)) < scissor.distance((x,y)):
        player_choice = 'paper'
    if scissor.distance((x,y)) < paper.distance((x,y)) and scissor.distance((x,y)) < rock.distance((x,y)):
        player_choice = 'scissor'

    # robot random choices
    for _ in range(20):
        robot_choice = choice(choices)
        robot.shape(robot_choice + '.gif')
        time.sleep(0.1)

    # show result
    if player_choice == 'rock' and robot_choice == 'rock':
        turtle.Turtle(shape='draw.gif')
    if player_choice == 'rock' and robot_choice == 'paper':
        turtle.Turtle(shape='lose.gif')
    if player_choice == 'rock' and robot_choice == 'scissor':
        turtle.Turtle(shape='win.gif')

    if player_choice == 'paper' and robot_choice == 'paper':
        turtle.Turtle(shape='draw.gif')
    if player_choice == 'paper' and robot_choice == 'scissor':
        turtle.Turtle(shape='lose.gif')
    if player_choice == 'paper' and robot_choice == 'rock':
        turtle.Turtle(shape='win.gif')

    if player_choice == 'scissor' and robot_choice == 'scissor':
        turtle.Turtle(shape='draw.gif')
    if player_choice == 'scissor' and robot_choice == 'rock':
        turtle.Turtle(shape='lose.gif')
    if player_choice == 'scissor' and robot_choice == 'paper':
        turtle.Turtle(shape='win.gif')    


# listen for mouse click
screen.onclick(choose_shape)

turtle.done()