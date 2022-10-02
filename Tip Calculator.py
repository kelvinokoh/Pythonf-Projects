#name = 'okoh kelvin'
#age = '22'
#print(name,age)
#width, height = 400,500
#print(width)
#print(height)
#print(width,height)

#num1 = input('enter a number: ')
#num2 = input('enter a number: ')
#print(num1)
#print(num2)
#print('your total is: '+ str(int(num1) + int(num2)))

# Tip Calculator
# math operators:( +, -, /, *, ** )

# Food_amount = float(input('Enter food amount $: '))
# Tip_percent = float(input('Enter tip percentage %: ')) / 100
# Tip_amount = Food_amount * Tip_percent
# Total_paid = Tip_amount + Food_amount
# print('----------------------------')
# print(f'Food Amount:${Food_amount}')
# print(f'Tip Amount:${Tip_amount}')
# print('\n')
# print(f'Total Amoutn:${Total_paid}')
# print('----------------------------')

def calculatefoodtotal(food, tip_percent):
    tip = food * (tip_percent / 100)
    total = tip + food
    print('----------------------------')
    print(f'Food Amount:${food}')
    print(f'Tip Amount:${tip}')
    print('\n')
    print(f'Total Amoutn:${total}')
    print('----------------------------')
    return total


# print(calculatefoodtotal(100, 10))
calculatefoodtotal(food=100, tip_percent=10)


