number = int(input())
hundreds_digit = number // 100
tens_digit = number % 100 // 10
ones_digit = number % 10
sum = hundreds_digit + tens_digit + ones_digit
print(sum)