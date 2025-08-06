from decimal import Decimal,getcontext
getcontext().prec = 4

mass = Decimal(input("Enter your weight in Kilogram[kg] :"))
height = Decimal(input("Enter your height in Metres[m] :"))

print(" BMI(Body mass index = Weight(in kg)) ")
print("                       -------------" )
print(f"                     (Height(in m))^2")

BMI = mass / (height * height)
BMI = BMI.quantize(Decimal('0.01'))

print(f"Your BMI is : {BMI}.")

if BMI < 18.5:
    print("As per your BMI , you are classified as Underweight.")
elif 18.5 <= BMI <= 24.9:
    print("As per your BMI , you are classified as Normal weight.")
elif 25.0 <= BMI <= 29.9:
    print("As per your BMI , you are classified as Overweight.")
elif 30.0 <= BMI <= 34.9:
    print("As per your BMI , you are classified as Obese (Class I).")
elif 35.0 <= BMI <= 39.9:
    print("As per your BMI , you are classified as Obese (Class II).")
else:
    print("As per your BMI , you are classified as Obese (Class III).")
