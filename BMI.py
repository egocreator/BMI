from decimal import Decimal

print('Please write your data to know your body mass index (BMI)')

Weight = float(input('Enter your weight:'))

Height = float(input('Enter your height:'))


if Height > 3 :

        print('please be consistent with the numbers')

if Weight > 180:

        print('please be consistent with the numbers')

elif Height >1.00 and Weight > 10:


    Result = Weight/Height **2



    print(f'your (BMI) is {Result:0.2f} ')  
    
    print('Is your BMI is --- > Below 18.5 [Underweight]')   
    print('Is your BMI is --- > 18.5 and 24.9[Normal]')
    print('Is your BMI is --- > 25.0 and 29.9 [Overweight]')
    print('Is your BMI is --- > 30.0 or more [Obesity]')
else :

    print('Error')


