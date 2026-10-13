FILEPATH = "Todo.txt"

def get_todo(filepath=FILEPATH):
    with open(filepath, "r") as f:
        todo_values = f.readlines()
    return todo_values

def write_todo(todo_data , filepath=FILEPATH):
    with open(filepath, "w") as f:
        f.writelines(todo_data)


if __name__ == "__main__":
    todo_value = get_todo()
    print(todo_value)
    test_data = "Test2" + "\n"
    todo_value.append(test_data)
    print(todo_value)
    write_todo(todo_value)
    print(get_todo())