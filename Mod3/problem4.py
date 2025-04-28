#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word = input("What word do you want to use? ")
index1 = int(input("What is the start of the index? "))
index2 = int(input("What is the end of the index? "))
#plus 1 so that index2 doesn't cut the last letter off
print(word[index1:index2+1])
