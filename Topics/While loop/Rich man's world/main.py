deposit = int(input())
limit = 700000
years = 0
while deposit < limit:
    deposit *= 1.071
    years +=1
print(years)