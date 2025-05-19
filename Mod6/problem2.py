#2. Create a list of strings. Write code that counts how many times the word "Olympic" appears in the list, and then print the count.
str_list = ["Olympic", "Wow", "Example", "Olympic", "Olympic", "Test", "Olympic"]

counter = 0

for num in range(len(str_list)):
    if str_list[num] == "Olympic":
        counter += 1

print(counter)
