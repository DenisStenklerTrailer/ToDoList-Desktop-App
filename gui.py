import functions
import PySimpleGUI as sg
import time

sg.theme("DarkTeal1")

clock = sg.Text("",key="clock")
title = sg.Text('To-Do App')
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button(size=3, image_source="add.png", tooltip="Add to-do", key="Add")
# showing the todos
list_box = sg.Listbox(values=functions.ReadingTodos(), key="todos", enable_events=True, size=[45,10])


edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],[title], [input_box, add_button],[list_box, edit_button, complete_button], [exit_button]],
                   font=('Helvetica', 15)) # Layout mora bit list

while True:
    event, values = window.read(timeout=10) #Displays the window actually on the screen, Izvaja se na vsake 10ms.

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    if event == "Add":
        todos = functions.ReadingTodos()
        new_todo = values["todo"] + "\n" #če ne veš kaj vrne values in event odkomentiraj printe
        todos.append(new_todo)
        functions.WritingTodos(todos)
        window["todos"].update(values=todos)  #todos je tukaj key ki ga definiramo zgoraj ko kreiramo objekt
    elif event == "Edit":
        try:
            todo_to_edit = values["todos"][0]

            new_todo = values["todo"] + "\n"

            todos = functions.ReadingTodos()

            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.WritingTodos(todos)
            window["todos"].update(values=todos) #updejtanje seznama ko kliknemo edit
        except IndexError:
            sg.popup("Please select an item first!", font=("Helvetica", 16))
    elif event == "Complete":
        try:
            todo_to_complete = values["todos"][0]
            todos = functions.ReadingTodos()
            todos.remove(todo_to_complete)

            functions.WritingTodos(todos)
            window["todos"].update(values=todos)
            window["todo"].update("")
        except IndexError:
            sg.popup("Please select an item first!", font=("Helvetica", 16))
    elif event == "Exit":
        break
    elif event == "todos": #ta event je na todos ko kliknemo na enega izmed to do-jev v seznamu
        data = values['todos'][0].strip() # znebimo se \n na koncu
        window["todo"].update(value=data)
    elif sg.WIN_CLOSED == event:
        #print(event)
        break

window.close()






