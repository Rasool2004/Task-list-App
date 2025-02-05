FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath,'r') as file_local:        # It will store them in a list called todos = ["Shower", "Eat"]
        todos_local = file_local.readlines()                 # New task entered in todo is appended to todos
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items list in a text file  [ updates tasks or to-do items] """
    with open(filepath,'w') as file:                 # Clears all the existing data
        file.writelines(todos_arg)                     # shows all the tasks in todos list


if __name__ == "__main__":
    print("hello")
    print(get_todos())