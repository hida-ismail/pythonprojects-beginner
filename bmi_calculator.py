weight = float(input("ENTER YOUR WEIGHT IN POUNDS: "))
height = float(input("ENTER YOUR HEIGHT IN INCHES: "))

if weight > 0 and height > 0:  # Ensure valid input
    BMI = (weight * 703) / (height * height)
    print("YOUR BMI IS ", BMI)
    
    if BMI < 18.5:
        print("YOU ARE UNDERWEIGHT.")
    elif 18.5 <= BMI <= 24.9:
        print("YOU ARE NORMAL WEIGHT.")
    elif 25 <= BMI <= 29.9:
        print("YOU ARE OVERWEIGHT.")
    elif 30 <= BMI <= 34.9:
        print("YOU ARE OBESE.")
    elif 35 <= BMI <= 39.9:
        print("YOU ARE SEVERELY OBESE.")
    elif BMI >= 40:
        print("YOU ARE MORBIDLY OBESE.")
    else:
        print("Enter Valid Inputs!!")
else:
    print("Please enter valid positive values for both weight and height.")
