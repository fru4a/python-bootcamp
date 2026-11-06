weight = float(input ("donner moi x "))
height = float(input("donner moi y"))
BMI = weight / height ** 2
if BMI < 18.5 :
    print (f"la valeur de BMI est :{BMI:.1f} , Underweight" ) 
elif BMI > 18.5 and BMI < 24.9:
    print (f"la valeur de BMI est :{BMI:.1f} , Normal" ) 
elif BMI > 25 and BMI < 29.9:
    print (f"la valeur de BMI est :{BMI:.1f} , Overweight" ) 
else:
    print (f"la valeur de BMI est :{BMI:.1f} , obese" ) 



   
