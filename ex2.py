#Exercise 2.A
print("Exercise 2.A")
print("This program takes an input of a string and adds a * at the beginning and end, ends a *- in between.")

e_o_f = "End of Program"
def pattern_reverse(inp_stat):
    temp_list = inp_stat.split()
    temp_list.reverse()
    for word in temp_list:
        temp_string = word[::-1]
        temp_stringg = "*-".join(temp_string)
        final_string = "*" + temp_stringg + "*"
        print(final_string,end="  ")
    print("\n")
    return e_o_f

inp_stat = input("Enter a string for the program: ")
print("The final output is: \n")
print(pattern_reverse(inp_stat))

#Exercise 2.B
print("Exercise 2.B")
print("This program takes an input string and returns true only if it is a palindrome.")

def Palindrome(inp_string):
    inp_string = inp_string.replace(" ", "")
    inp_string = inp_string.lower()
    if inp_string == inp_string[::-1]:
        return True
    else:
        return False

inp_string = input("Enter a string to check if it is a palindrome or not: ")
print(Palindrome(inp_string))