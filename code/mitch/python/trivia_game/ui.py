from appJar import gui

def press(rb):
    print(app.getRadioButton("selection"))


app = gui()
app.addRadioButton("selection", "11")
app.addRadioButton("selection", "22")
app.addRadioButton("selection", "33")
app.addRadioButton("selection", "44")


app.addButton("SUBMIT", press)

app.go()

















