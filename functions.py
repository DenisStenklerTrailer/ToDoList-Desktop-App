FILEPATH = "todos.txt"

def ReadingTodos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file:  # branje iz txt datoteke
        todos_local = file.readlines()  # readlines vrne list, medtem ko če bi dal file.read() dobimo samo v stringu.
    return todos_local

def WritingTodos(todos_local, filepath=FILEPATH):
    """Write a to-do items list in to the text file"""
    with open(filepath, "w") as file:  # pisanje v txt datoteko
        file.writelines(todos_local)

    #funkcijo kličemo tako: WritingTodos(todos)
    # Tuki je fora da že tuki nastavimo filepathu default parameter.
    #Če hočemo še vedno lahko filepathu nastavimo karkol druzga npr. WritingTodos(todos, filepath="neki.txt").

    # print(help(ReadingTodos)) -> To nam vrne kar je napisano v """"""

if __name__ == "__main__": # izpisovanje samo če direkt zaženemo functions.py, če zaženemo main.py se ne zažene
    print("Hello")
    print(ReadingTodos())