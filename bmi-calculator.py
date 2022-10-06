#bmi calculator
height= float(input('Please input your height in meters: '))
weight=float(input('Please input your weight in kg: '))
bmi = weight/(height*height)

if bmi<18.5:
    print('Your BMI is',bmi,' which is Underweight')

elif(bmi>=18.5 and bmi<=24.9):
    print('Your BMI is',bmi,'which is healthy')

elif(bmi>24.9 and bmi<=29.9):
    print('Your BMI is',bmi,'which is Overweight')

elif(bmi>30):
    print('Your BMI is',bmi,'which is Obese')
