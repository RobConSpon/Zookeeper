days = int(input())
food_per_day = int(input())
flight_cost = int(input())
night_cost = int(input())
total_cost = (days * food_per_day) + (2 * flight_cost) +((days - 1) * night_cost)
print(total_cost)