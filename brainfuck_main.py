#####################################################
#   MADE BY WAARMY/FARCEUR11
#   Brainf*ck compiler in python
#   Pretty unoptimized but it run so it's ok
#
#   Have fun :)
#####################################################

####################
#   TO-DO
####################

#   Add infinite cells (expends) ✓
#   Optimize

####################
#   Imports
####################

from os import system

####################
#   Errors
####################

class Errors:
    def __init__(self, error, command) -> None:
        self.error = error
        self.command = command

    def SyntaxError(self):
        if self.error == '1':
            print("Brainf*ck > ERROR 001 at line ", "1", " : expected 1 character in ", self.command, " , but got 2 or more.")
        if self.error == '2':
            print("Brainf*ck > ERROR 002 at line ", "1", " : a loop must start (using the '[' character).")

        quit()

####################
#   Interpreter
####################

def interpreter(text):

    #   Variables/Const
    char_i = 0  #   The character we are at 
    output = ""
    cell = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   #   10 cell (infinit)
    pointer = 0
    key_pressed = None
    loop_start = None
    pointer_last = 0
    loop_cell_temp = None
    loop_end = None

    #   Main
    while char_i < len(text):
        match text[char_i]:
            case ">":
                pointer = pointer + 1
                if pointer >= len(cell): cell.append(0)
            case "<":
                pointer -= 1
                if pointer < 0:
                    print("Brainf*ck > WARNING : you can't go bellow 0 with the pointer")
                    pointer = 0
            case "+":
                cell[pointer] += 1
            case "-":
                cell[pointer] -= 1
                if cell[pointer] < 0:
                    cell[pointer] = 255
            case ".":
                output = output + chr(cell[pointer])
            case ",":
                key_pressed = input("brainf*ck > INPUT 1 CHARACTER :\n")
                if len(key_pressed) > 1 or len(key_pressed) == 0:
                    Errors(2, "','")
                cell[pointer] = ord(key_pressed)
            case "[":
                loop_start = char_i
                loop_cell_temp = cell[pointer]
                pointer_last = pointer
            case "]":
                if not loop_start == None:
                    loop_cell_temp = cell[pointer_last]
                    if not loop_cell_temp == 0:
                        loop_end = pointer
                        char_i = loop_start
                else:
                    Errors(1, ']')
            case "!":
                print("Cell : ", cell)
                print("Pointer : ", pointer)
                
        char_i += 1

    if not output == "":
        print(output)

####################
#   Commands
####################

def commands():
    match text_input:
        case "help":
            help_thingy()
        case "cls":
            system('clear')
        case "exit":
            if input("Brainf*ck > Are you sure you want to quit ? (y/n) : ") in "y" + "yes":
                quit()
            

def help_thingy():
    print("\nHELP:\n")
    print("'>' : change the pointer by 1.")
    print("'<' : change the pointer by -1.")
    print("'+' : add 1 to the cell pointed by the pointer.")
    print("'-' : sub 1 to the cell pointed by the pointer.")
    print("'.' : output the ASCII character of the cell pointed by the pointer.")
    print("',' : take a letter and write the ASCII value to the cell pointed by the pointer.")
    print("'[]' : create a loop (the loop finish when the first cell hit zero).")
    print("'!' : output the state of the cells and the value of the pointer (NOT AN ORIGINAL COMMAND).")
    print("'open' : open a file (provided by a path).")
    print("'cls' : clear the console.")
    print("'exit' : exit the program.\n\n")

####################
#   Run
####################

while True:
    text_input = input("Brainf*ck > ")
    commands()
    if text_input == "open":
        file_path = input("Brainf*ck > PLEASE GIVE FILE PATH : \n")
        file_input = open(file_path, 'r')
        interpreter(file_input.read())

    else: interpreter(text_input)
