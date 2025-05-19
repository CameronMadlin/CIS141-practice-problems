#1. Create a list of integers (you get to pick!). Write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
nums = [1, 2, 4, 5, 6, 8, 9, 10]
evens = 0
for num in nums:
    if num % 2 == 0:
        evens += num

print(f"The sum of all even numbers in the list is {evens}")
