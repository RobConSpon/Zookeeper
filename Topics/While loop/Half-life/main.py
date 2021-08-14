atoms = int(input())
end_atoms = int(input())
periods = 0
while atoms >= end_atoms:
    atoms /=2
    periods +=1
print(periods * 12)