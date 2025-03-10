import turtle
import pandas,csv

IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.setup(width=725,height= 491)
screen.title("U.S. States Game")

screen.addshape(IMAGE)          #turtle only work with gif, and addshape method will add this method to the shapes in turtle

# # now i can use the image
turtle.shape(IMAGE)

# #now i need to get the coordinates of each state in the map
# def get_mouse_click_coor(x,y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)              # this method will print the coordinates of each click on the screen
# turtle.mainloop()                                       # this is similar to "turtle.exitonclick()" but the difference is that it keep the screen on



#this part of code is commented because it has been done and saved to "50_states.csv"
data = pandas.read_csv("50_states.csv")      # I did read the csv file here
all_states = data.state.to_list()            # I created a list to deal with it
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States is correct ", prompt="what's another state name: ").title()

    if answer_state == "Exit":       #exit case 
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.Series(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]       # this will give me the row in the pandas هنا ببساطة هيرجع الصف اللي انا محتاجه
        t.goto(state_data.x.item(), state_data.y.item())    # ".item()" is used to retrieve the data in the selected col
        t.write(answer_state)

 