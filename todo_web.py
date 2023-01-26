import streamlit as st
import function_todo as fun

todos = fun.get_todos()


def add_todos():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")  # Added New value to list
    fun.write_todos(todos)  # updating list in file


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")  # For Normal Text

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fun.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todos ....", on_change=add_todos, key='new_todo')
