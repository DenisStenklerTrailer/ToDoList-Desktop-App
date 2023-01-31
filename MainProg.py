# from Functions import ReadingTodos,WritingTodos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_input = input("Select 'Add', 'Show', 'Edit', 'Complete' or 'Exit': ")
    user_input = user_input.lower()

    if user_input.startswith("add"):
        to_do = user_input[4:] # shranimo vse kar se nahaja za add

        if to_do != "":
            print(to_do)

            todos = functions.ReadingTodos()

            todos.append(to_do + "\n")  # dodajanje elementa v list

            functions.WritingTodos(todos)

    elif user_input.startswith("show"):

        todos = functions.ReadingTodos()

        # Odstranjevanje \n za vsakim objektov v listu
        # Odstranjevanje \n za vsakim objektov v listu
        # Odstranjevanje \n za vsakim objektov v listu

        """
        new_todos = [item.strip('\n') for item in todos] # List comprehension. Na začetku je kaj hočemo nardit in sledi navadn for loop čez listo
        """

        """
        for item in todos: #Odstranjevanje \n za vsakim objektov v listu 
            new_item = item.stip('\n')
            new_todos = new_todos.append(new_item)
        """

        for index, item in enumerate(todos):
            item = item.strip("\n")  # enumerate nam oštevilči objekte po katerih gre foor loop čez. Enumarate nam ubistvu zgenerira tuple torej: [(1, prva),(2,druga),...]
            print(f"{index + 1}. {item}")  # f" se uporablja da ni treba pisat recimo "ena" + "dva". v {} damo variable ostalo pišemo normalo

    elif user_input.startswith("edit"):
        try: # Če vpišemo vse ok in ne dobimo errorja nam gre v try:
            number = user_input[5:]
            number = int(number) - 1

            new_to_do = input("Insert new to do: ")

            todos = functions.ReadingTodos()

            todos[number] = new_to_do + "\n"

            functions.WritingTodos(todos)

        except ValueError: # Če imamo error gremo v expect
            print("There in no 'to do' with that number! ")
            continue #Continue nam izvede to da gremo še enkrat od začetka v while loop

    elif user_input.startswith("complete"):
        try:
            complete = int(user_input[9:])

            todos = functions.ReadingTodos()

            todo_to_remove = todos[complete - 1].strip('\n') #strip() pobriše vse \n in pa tudi presledke. V našem primeru samo \n.
            todos.pop(complete - 1)  # pop izbriše index (complete), ki mu ga določimo

            functions.WritingTodos(todos)

            message = f"To do '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("There in no 'to do' with that number! ")
            continue
    elif user_input.startswith("exit"):
        break
    else:
        print("Command is not valid!")

print("That's it!")