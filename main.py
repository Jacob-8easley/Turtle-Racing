from turtle import Turtle , Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_cash = 500
def game():
    global user_cash
    user_color = screen.textinput(title="Make your bet",prompt="Which colour turtle will win the race? Enter a colour:")
    user_bet = screen.numinput(title="Turtle Races",prompt="How much do you gamble?",default=0,minval=0,maxval=user_cash)

    is_race_on = False

    colors = ["red","orange","yellow","green","blue","purple"]
    all_turtles = []
    first_position = 75
    for racer in range(0,6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[racer])
        new_turtle.goto(x=-230,y=first_position)
        first_position -= 30
        all_turtles.append(new_turtle)

        

    if user_bet and user_color:
        is_race_on =True

    while is_race_on:
        for turtle in all_turtles:
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance)

            if turtle.xcor() >= 230:
                is_race_on = False
                winning_colour = turtle.pencolor()
                if winning_colour == user_color:
                    print(f"Well done you won! The {winning_colour} was victorious!!")
                    print(f"You earned {user_bet}")
                    user_cash += user_bet
                    play_again = screen.textinput(title="Replay",prompt="Yes or No")
                    if play_again == "yes":
                        screen.clearscreen()
                        game()
                    else:
                        screen.bye()


                else:
                    print(f"Your turtle did not win! The winning turtle was {winning_colour}")
                    user_cash -= user_bet
                    play_again = screen.textinput(title="Replay",prompt="Yes or No")
                    if play_again == "yes":
                        screen.clearscreen()
                        game()
                    else:
                        screen.bye()
                        
game()
        



screen.exitonclick()