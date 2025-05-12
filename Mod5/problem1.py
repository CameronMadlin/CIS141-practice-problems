#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("How many numbers do you want to add together? "))
#due to starting at 0, this will make it include the number in the prompt so it's not cut off
n+=1
sum = 0
counter = 1
while counter < n:
    sum+=counter
    print(sum)
    counter+=1
print(f"The sum of all the numbers combined is {sum}")
