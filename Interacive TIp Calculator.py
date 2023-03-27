food_amount = float(input('Enter your bill amount: $'))
tip_amount = float(input('Enter your tip percentage: $'))
tip_percentage = tip_amount * food_amount

print(f'Tip: ${tip_amount}')
print(f'Food Cost: ${food_amount}')

total = food_amount + tip_percentage
print('Your complete total is: $' + str(total))
