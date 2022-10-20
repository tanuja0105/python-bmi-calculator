#bmi calculator
height= float(input('Please input your height in meters: '))
weight=float(input('Please input your weight in kg: '))
bmi = weight/(height*height)

# Adding an easter-egg like fun exception for a typo (or really the tallest person!)
if height > 2.72:
    print("Congratulations! You beat the world record for the tallest person!")
    print("Carry on and find your BMI")

if bmi<18.5:
    print('Your BMI is',bmi,' which is Underweight')

elif(bmi>=18.5 and bmi<=24.9):
    print('Your BMI is',bmi,'which is healthy')

elif(bmi>24.9 and bmi<=29.9):
    print('Your BMI is',bmi,'which is Overweight')

elif(bmi>30):
    print('Your BMI is',bmi,'which is Obese')
