citizenship = input ("Enter your citizenship:")
age =int(input("Enter your age"))
east_african_countries = ["Kenyan", "Ugandan", "Tanzanian"]
if citizenship.lower() in east_african_countries and age >=18:
    print("you are eligible to vote,")
else:
    print("you are not eligible to vote,")
    