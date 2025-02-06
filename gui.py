import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-do")
input_text = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My Task-list App", layout=[[label], [input_text, add_button]])
window.read()
window.close()




