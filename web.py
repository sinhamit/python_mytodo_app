import streamlit as st
import functions
# To view this Streamlit app on a browser, run it with the following command:
# streamlit run web.py [ARGUMENTS]

todos = functions.get_todos()

def add_todo():
  todo_local = st.session_state["new_todo"] + '\n'
  # print(todo) # would not be printed in same console.
  todos.append(todo_local)
  functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
  checkbox = st.checkbox(todo, key=todo) # dynamic value of keys.
  if checkbox:
    # print(checkbox) # outputs True when checked
    todos.pop(index)
    functions.write_todos(todos)
    del st.session_state[todo]
    st.experimental_rerun() # st.rerun() # rerun() is not function


# st.checkbox("Buy grocery.")
st.text_input(
  label="Enter a todo:", # empty string can also be placed
  placeholder="Add a new todo...",
  on_change = add_todo,
  key='new_todo'
)

# st.session_state # will be displayed on web-browser
