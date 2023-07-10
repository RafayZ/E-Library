#Excercise 1.a
print("Excercise 1.A")
print("This excercise appends 12 numbers to 2 empty lists and then concatenates them into a single list, sorting it and printing the output.")
import random

list_1 = []
list_2 = []
list_3 = []

for i in range(12):
    list_1.append(random.randint(0,100))
    list_2.append(random.randint(0,100))

list_1 = sorted(list_1)
list_2 = sorted(list_2)

list_3 = list_1 + list_2
list_3 = sorted(list_3)
print("\n", "List 3 is: ", "\n", list_3)

print("\n")

#Excercise 1.b
print("Excercise 1.B")
print("This excercise takes a input list from the user and rotation factor. It then rotates all elements in that list by that factor.")

import collections
from collections import deque as dq #Importing library to access rotation function

def List_Rotation(inp_list,rotation_factor):
    proc_list = dq(inp_list)
    proc_list.rotate(rotation_factor)
    final_list = list(collections.deque(proc_list))
    f_list = [eval(i) for i in final_list]

    print(f"The List after being rotated with a rotation factor of {rotation_factor} is: ")
    return f_list
    

temp_inp = input("Enter numbers with spaces to add them to the list: ")
temp_inp = temp_inp
inp_list = temp_inp.split()

rotation_factor = int(input(f"Enter a rotation factor which should be less then {len(inp_list)} to rotate the list: "))

if rotation_factor < len(inp_list):
    print(List_Rotation(inp_list,rotation_factor))
elif rotation_factor >= len(inp_list):
    print("Error! your rotation factor is greater than or equal to the length of the input list.")
