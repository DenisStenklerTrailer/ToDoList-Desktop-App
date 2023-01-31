import functions
import PySimpleGUI as sg

title = sg.Text('To-Do App')
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
# showing the todos
list_box = sg.Listbox(values=functions.ReadingTodos(), key="todos", enable_events=True, size=[45,10])

edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[title], [input_box, add_button],[list_box, edit_button]],
                   element_justification="center", font=('Helvetica', 15)) # Layout mora bit list

while True:
    event, values = window.read() #Displays the window actually on the screen
    # print(event)
    # print(values)
    #print(values['todos'][0])
    if event == "Add":
        todos = functions.ReadingTodos()
        new_todo = values["todo"] + "\n" #če ne veš kaj vrne values in event odkomentiraj printe
        todos.append(new_todo)
        functions.WritingTodos(todos)
    elif event == "Edit":
        todo_selected = values["todos"][0]
        new_todo = values["todo"]

        todos = functions.ReadingTodos()

        index = todos.index(new_todo)

        todos[index] = new_todo

        functions.WritingTodos(todos)
    elif sg.WIN_CLOSED == event:
        #print(event)
        break

window.close()






