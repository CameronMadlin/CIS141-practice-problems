#3. Create a list of strings. Write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
str_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
three_list = []

for lgth in range(len(str_list)):
    if len(str_list[lgth]) == 3:
        continue
    else:
        three_list.append(str_list[lgth])

print(three_list)
