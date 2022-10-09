number = int(input("Please insert your number : "))
print(list(range(number, 0, -1)))

for x in range(number, 0, -1):
    print((x * ' ' + (number - x) * '*') + '*' + ((number - x) * '*') + (x * ' '))
