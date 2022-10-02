#BABY WEATHER APP
# if its raining grab umbrella Otherwisw grab sunglasses
#Boolean( True or False)
#comparison operators( ==, <, >, <=, >=)

# weather = input('How is the weather today? ')
# if weather == 'rain':
#     print('Grab Umbrella')
#     print('Make sure to keep dry')
# elif weather == 'cloudy':
#     print('Jacket')
#     print('Might be a cool day')
# elif weather == 'windy':
#     print('Windbreaker')
#     print('Do not get blown away')
# elif weather == "thunderstorm":
#     print('Take cover')
#     print('Lightning incoming')
# else:
#     print('Sunglasses')
#     print('Might be a good day for a swim')
   
# Using Defining Functions

def weathertowarning(weather):
    if weather == 'rain':
        print('Grab Umbrella')
        print('Make sure to keep dry')
    elif weather == 'cloudy':
        print('Jacket')
        print('Might be a cool day')
    elif weather == 'windy':
        print('Windbreaker')
        print('Do not get blown away')
    elif weather == "thunderstorm":
        print('Take cover')
        print('Lightning incoming')
    else:
        print('Sunglasses')
        print('Might be a good day for a swim')


weathertowarning('cloudy')


