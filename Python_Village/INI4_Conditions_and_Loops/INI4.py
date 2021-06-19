a = 4379
b = 9203

sum = 0

# a is even number
if a % 2 == 0:
    for i in range(a+1, b+1, 2):
        sum += i
        print(i)
# a is odd number
else:
    for i in range(a, b+1, 2):
        sum += i
        print(i)

print(sum)
