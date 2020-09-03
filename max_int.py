"""
all_numbers = []
while True:
    num = int(input("Input a number:"))
    if num < 0:
        break
    else:
        all_numbers.append(num)


max_int = max(all_numbers)
print("The maximum is", max_int)
"""

all_numbers = [1, 2, 3]

n = int(input("Enter the length of the sequence: "))
if n >3:
    for i in range(n-3):
        the_sum = 0
        for i in range(3):
            the_sum += all_numbers[-(i+1)]

        all_numbers.append(the_sum)

if n == 1:
    print(all_numbers[0])
elif n == 2:
    print(all_numbers[0])
    print(all_numbers[1])
elif n == 3:
    print(all_numbers[0])
    print(all_numbers[1])
    print(all_numbers[2])
else:
    for i in range(len(all_numbers)):
        print(all_numbers[i])
