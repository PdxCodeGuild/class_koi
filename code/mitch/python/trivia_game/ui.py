from appJar import gui

def press(rb):
    print(app.getRadioButton("selection"))

###################THIS needs work...
def set_buttons():
    app.setRadioButton("selection", "1AA", callFunction=False)
    app.setRadioButton("selection", "2SS", callFunction=False)
    app.setRadioButton("selection", "3GG", callFunction=False)
    app.setRadioButton("selection", "4TT", callFunction=False)

app = gui()
app.addRadioButton("selection", "11")
app.addRadioButton("selection", "22")
app.addRadioButton("selection", "33")
app.addRadioButton("selection", "44")


app.addButton("SUBMIT", press)
app.addButton("SET BUTTONS", set_buttons)

app.go()

















