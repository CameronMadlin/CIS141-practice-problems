#5. Create a list of integers. Use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_nums = []

for num in nums:
    new_nums.append(num**2)
    
print(new_nums)
