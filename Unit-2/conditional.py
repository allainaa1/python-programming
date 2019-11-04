''' total = 2

if total % 2 == 0:
    print('even')
else:
    print('odd')

first_name = 'Allaina'
if len(first_name) > 7:
    print('Good')
else:
    print('less than')


score = 2

if score >= 80:
    print('A')
elif score >= 60 <= 79:
    print('B')
elif score >= 50 <= 59:
    print('C')
else:
    print('F')


for num in range (1, 51):
    if num % 15 == 0:
        print('fizzbuzz')
    elif num % 5 == 0:
        print ('buzz')
    elif num % 3 == 0:
        print ('fizz')
    else:
        print(num)'''

if "hello world":
    print("Yes it's true")

if "":
    print("it's true")
else:
    print("it's false")

a = -10
b = -11

if a > 0 or b < 0:
    print("Good!")

if a > 0 and b < 0:
    print("Excellent!")