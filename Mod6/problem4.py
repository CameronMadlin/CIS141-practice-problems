#4.  Create a list of integers. Write code that counts how many numbers are positive and how many are negative, then print both counts.
nums = [-34, -4, 7, -23, 4, 534, 63, -43, 4, -5, -4, -7]
pos = 0
neg = 0
for num in nums:
    if num >= 0:
        pos += 1
    else:
        neg += 1


print(f"Total positive numbers is {pos}, while negative is {neg}")
