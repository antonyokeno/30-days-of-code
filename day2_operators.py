def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    tip = (meal_cost / 100) * tip_percent
    tax = (tax_percent / 100) * meal_cost
    total_cost = float(meal_cost + tip + tax)
    rounded_number = round(total_cost)
    print(rounded_number)


solve(12,20,8)
