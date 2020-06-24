from tkinter import *
from time import sleep


root = Tk()
root.title("Tic Tac Toe")
root.geometry("270x275")
root.config(bg="white")


canvas = Canvas(root, height=150, width=150, bg="black", highlightthickness=0)
canvas.place(x=60, y=90)

frames = [[]]
buttons = [[]]

turning = "O"

plays = 0

scoreX = 0
scoreO = 0

counterX = Label(root, text="X = " + str(scoreX), font="Consolas 20 bold")
counterX.place(x=25, y=25)

counterO = Label(root, text="O = " + str(scoreO), font="Consolas 20 bold")
counterO.place(x=160, y=25)


def generategame():

    for m in range(3):

        frames.append([])
        buttons.append([])

        for n in range(3):

            frames[m].append(Frame(canvas, width=48, height=48))
            frames[m][n].propagate(0)
            frames[m][n].place(x=(n*51), y=(m*51))

            buttons[m].append(Button(frames[m][n], text="", command=lambda i=m, j=n: turn(i, j)))
            buttons[m][n].config(bg="white", activebackground="white", disabledforeground="black", bd=0)
            buttons[m][n].pack(fill=BOTH, expand=1)


def turn(m, n):

    global plays
    global buttons
    global turning

    if turning == "X":
        turning = "O"

    else:
        turning = "X"

    buttons[m][n].config(font="Franklin 20 bold", text=turning)
    buttons[m][n].config(state=DISABLED)

    plays += 1

    checkwin(turning)


def checkwin(winner):

    if buttons[0][0]["text"] == buttons[0][1]["text"] == buttons[0][2]["text"] != "":
        print(winner + " WINS")

    elif buttons[1][0]["text"] == buttons[1][1]["text"] == buttons[1][2]["text"] != "":
        print(winner + " WINS")

    elif buttons[2][0]["text"] == buttons[2][1]["text"] == buttons[2][2]["text"] != "":
        print(winner + " WINS")

    elif buttons[0][0]["text"] == buttons[1][0]["text"] == buttons[2][0]["text"] != "":
        print(winner + " WINS")

    elif buttons[0][1]["text"] == buttons[1][1]["text"] == buttons[2][1]["text"] != "":
        print(winner + " WINS")

    elif buttons[0][2]["text"] == buttons[1][2]["text"] == buttons[2][2]["text"] != "":
        print(winner + " WINS")

    elif buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        print(winner + " WINS")

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        print(winner + " WINS")

    elif plays == 9:
        restartgame()
        return

    else:
        return

    updatecounter(winner)
    restartgame()


def updatecounter(winner):

    global scoreX
    global scoreO

    if winner == "X":
        scoreX += 1
        counterX.config(text="X = " + str(scoreX))

    if winner == "O":
        scoreO += 1
        counterO.config(text="O = " + str(scoreO))


def restartgame():

    global plays

    root.update()
    sleep(0.1)

    flash = Frame(root, width=150, height=150, bg="white")
    flash.place(x=60, y=90)

    root.update()
    sleep(0.1)

    flash.place(x=400, y=400)

    root.update()
    sleep(1)
    flash.place(x=60, y=90)

    root.update()
    sleep(0.1)

    plays = 0

    buttons.clear()
    frames.clear()
    generategame()

    root.update()
    flash.destroy()


generategame()
root.mainloop()
