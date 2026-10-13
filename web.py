import streamlit as st
import functions

todos = functions.get_todo()

def add_todo():
    new_todo = st.session_state["add_new_todo"]
    todos.append(new_todo+"\n")
    functions.write_todo(todos)


st.title("My Todo App")
st.subheader("This is the Sub header")
st.write("This is to improve the productivity")

for index, item in enumerate(todos):
    checked = st.checkbox(item, key=item)
    if checked:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[item]
        st.rerun()


st.text_input(label="Enter the Todo:", placeholder="Add todo here ....", on_change=add_todo, key="add_new_todo")


