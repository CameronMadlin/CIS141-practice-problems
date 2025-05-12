#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Output example:
# 1   2   3   4   5         
# 2   4   6   8   10        
# 3   6   9   12  15        
# 4   8   12  16  20
# 5   10  15  20  25

for i in range(6):
    for j in range(i, i*5, i+1):
        line = print(i, i*2, i*3, i*4, i*5)
        print(line)
        if line == line:
            break
