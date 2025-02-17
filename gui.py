import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text(key='clock')
label = sg.Text("Type in a To-do ")
input_text = sg.InputText(tooltip="Enter todo", key='new_todo')
add_button = sg.Button("Add", size=8)

list_box = sg.Listbox(values=functions.get_todos(), key='edit_todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete", size=8)
exit_button = sg.Button("Exit")

window = sg.Window("My Task-list App",
                   layout=[[clock], [label],
                           [input_text, add_button],
                           [list_box, edit_button], [complete_button, exit_button]],
                   font=("Helvetica", 15))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['new_todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['edit_todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['edit_todos'][0]
                new_todo = values['new_todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['edit_todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select the task first.", font=("Helvetica", 15))
        case "Complete":
            try:
                todo_to_complete = values["edit_todos"][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window['edit_todos'].update(values=todos)
                window['new_todo'].update(value='')
            except IndexError:
                sg.popup("Please select the task first.", font=("Helvetica", 20))
        case "Exit":
            break
        case "edit_todos":
            window["new_todo"].update(value=values['edit_todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()



