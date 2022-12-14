def body_mass_index():
    height=float(input("enter the height"))
    weight=float(input("enter the  weight"))
    bmi=weight/height**2
    if bmi<=18.5:
        print("you are underweight")
    elif bmi<=24.9:
        print("normal")
    elif bmi<30.0:
        print("overweight")
    else:
        print("obese")
body_mass_index()