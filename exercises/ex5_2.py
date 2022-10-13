print()
name = input("What's your name?: ")
age = int(input("How old are you (years)?: "))
height = int(input("How tall are you (inches)?: "))
height_in_cms = height * 2.54
weight = int(input("How heavy are you (lbs/pounds)?: "))
weight_in_kgs = weight * 0.453592
eyes = input("What's the color of your eyes?: ")
teeth = input("What's the color of your teeth?: ")
hair = input("What's the color of your hair?: ")

print()

print(f"Let's talk about {name.title()}.")
print(f"He's {height} inches ({round(height_in_cms)} cms) tall.")
print(f"He's {weight} pounds ({round(weight_in_kgs)} kgs) heavy.")
print(f"He's got {eyes.lower()} eyes and {hair.lower()} hair.")
print(f"His teeth are usually {teeth.lower()} depending on coffee.")

# this line is tricky, try to get it exactly right

print()
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
