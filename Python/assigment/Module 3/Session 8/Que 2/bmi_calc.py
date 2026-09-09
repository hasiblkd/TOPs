import math

weight=float(input("Enter a Weight:-"))
height=float(input("Enter a Height:-"))

height_squre=math.pow(height,2)

bmi=weight/height_squre

print("BMI:-",round(bmi,2))