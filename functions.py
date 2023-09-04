FILEPATH = "todos.txt" # variable and constants are written at the top

# Custom Functions are always created on top of the file
def get_todos(file_path=FILEPATH):
    '''
    Read a text file and Return the list data-type
    of todos items.
    '''
    with open(file_path, 'r') as file_read:
        todos_local = file_read.readlines() # local scope
    return todos_local

# non-default parameters must be before all default parameters
def write_todos(todos_arg, file_path=FILEPATH):
    '''
    Write the todos items of list data-type, in a text file.
    '''
    with open(file_path, 'w') as file_write:
        file_write.writelines(todos_arg)
    # doesn't return anything, only executes the above code

if __name__ == "__main__":
    print( get_todos() ) # will not be executed when called from main.py
print( "Hello from functions" ) # will automatically run, when imported in another file
print( __name__ ) # outputs __main__ (this file)