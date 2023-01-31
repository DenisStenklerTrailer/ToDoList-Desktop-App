import functions
import PySimpleGUI as sg

title = sg.Text('To-Do App')
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[title], [input_box, add_button]], element_justification="center") # Layout mora bit list
window.read() #Displays the window actually on the screen
window.close()




