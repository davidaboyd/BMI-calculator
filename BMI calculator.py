#Below code is a Body Mass Index Calculator
#Coded by David Boyd

try:
    h=float(input("Please enter your height in feet: "))
except:
    print("Please enter a number")
    
    
try:
    height=float(input("Please enter inches now: "))
except:
    print("Please enter a number")
    
try:
    weight=float(input("Please enter your weight in pounds: "))
except:
    print("Please enter a number")

kilograms=weight/2.2046
m=height+(h*12)
meters=m*0.0254
meters2=meters **2
BMI=kilograms/meters2
if BMI <= 18.5:
   print("Your BMI is " , BMI , ", you are underweight")
elif BMI <=18.6 or BMI <= 24.9:
     print("Your BMI is ", BMI , ",you are in the normal range")
elif BMI <= 25 or BMI <= 29.9:
     print("Your BMI is " , BMI , ", you are in the over weight range")
else:
     print("Your BMI is ", BMI , ", you are in the obese category")

