number = int(input())
if 1 <= number <= 100:
    output = 1
    fact = 1
    while fact < number:
        output = output * (fact + 1)
        fact += 1
     #   print(output, fact)
    print(output)

