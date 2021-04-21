"""
User Interface script
Mainly, it has 2 functions
->gets input from user [eg a comment]
->passes the input to the Bayes Classifier and "returns" the label to the user
"""
#TODO redo this as a website
import PySimpleGUI as gui

def start_interface():
    gui.theme('DarkAmber')
    layout = [[gui.Text("Please enter a comment and let us label it for you")],
              [gui.Text("!!! it should not be bigger than 250 characters !!!")],
              [gui.Text('Insert comment here \n', size=(15, 1)), gui.InputText()],
              [gui.Button("Label the comment"), gui.Button("Close")]]

    # Create the window
    window = gui.Window("Offensive Language Detection", layout, size=(650, 300))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == gui.WIN_CLOSED:
            break
        if event == "Submit":
            break
    layout.clear()
    window.close()
    return str(values[0])


if __name__ == '__main__':
    start_interface()

