number = int(input())
total = 0
count = 0
while number != 55:
    total = total + number
    count += 1
    number = int(input())
print(count)
print(total)
print(round(total / count))
