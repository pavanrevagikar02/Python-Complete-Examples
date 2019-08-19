# In python, all the functions are called by reference,
# i.e., all the changes made to the reference inside the function revert back to the original value referred by the reference.
#
# However, there is an exception in the case of mutable objects since the changes made to the mutable objects like string do not revert to the original string rather, a new string object is made, and therefore the two different objects are printed.
#
# Example 1 Passing Immutable Object (List)


# defining the function
def change_list(list1):
    list1.append(20);
    list1.append(30);
    print("list inside function = ", list1)


# defining the list
list1 = [10, 30, 40, 50]

# calling the function
change_list(list1);
print("list outside function = ", list1)

# Example 2 Passing mutable Object (String)
def change_string(str):
    str = str + " Hows you";
    print("printing the string inside function :", str);


string1 = "Hi I am there"

# calling the function
change_string(string1)

print("printing the string outside function :", string1)