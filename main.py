# U.S. States Game
import turtle
import pandas as pd

BG_IMAGE = r"us-states-game\blank_states_img.gif"
INPUT_CSV_FILE = r"us-states-game\\50_states.csv"
OUTPUT_CSV_FILE = r"us-states-game\\states_to_learn.csv"
FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")


screen.addshape(BG_IMAGE)
turtle.shape(BG_IMAGE)

data = pd.read_csv(INPUT_CSV_FILE)
all_states = data.state.to_list()


game_is_on = True
ans=0
while game_is_on:
    answer_state = screen.textinput(title="Guess the State or enter", prompt="Enter a state name or enter 'exit' to quit:").title()
    if answer_state == "Exit":
        game_is_on = False
        if len(all_states) > 0:
            new_data = pd.DataFrame(all_states)
            new_data.to_csv(OUTPUT_CSV_FILE)
        
        break
    elif answer_state in all_states:
        ans += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        t.write(answer_state, align="center", font=FONT)
        all_states.remove(answer_state)
        if ans == 50:
            game_is_on = False
            t.goto(0, 0)
            t.write("You have guessed all the states!", align="center", font=FONT)
            
            