# Taha Bisgin 2018
# BMI Calculator

#Dont know if I can do this but lets give it a try
name = input("your name? ")
height_m = float(input("height? "))
weight_kg = float(input("weight? "))

def bmi(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("Bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " not overweight"
    else:
        return name + " overweight"


result0 = bmi(name, height_m, weight_kg)

print(result0)
