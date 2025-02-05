# from functions import get_todos, write_todos
import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()          # It will read all the tasks and stores in todos

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos,1):
            item = item.strip("\n")
            print(f"{index} - {item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your Command is not Valid.")
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            print(f"You successfully removed {todo_to_remove} from list")

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")
print("Bye!")

