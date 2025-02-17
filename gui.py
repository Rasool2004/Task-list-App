import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-do ")
input_text = sg.InputText(tooltip="Enter todo", key='new_todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='edit_todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My Task-list App",
                   layout=[[label], [input_text, add_button],
                           [list_box, edit_button], [complete_button, exit_button]],
                   font=("Helvetica", 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['new_todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['edit_todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['edit_todos'][0]
            new_todo = values['new_todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['edit_todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values["edit_todos"][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_complete)
            todos.pop(index)
            functions.write_todos(todos)
            window['edit_todos'].update(values=todos)
            window['new_todo'].update(value='')
        case "Exit":
            break
        case "edit_todos":
            window["new_todo"].update(value=values['edit_todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()



