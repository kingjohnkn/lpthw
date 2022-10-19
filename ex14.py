from sys import argv

script, first_name, second_name = argv
prompt = '> '
first_name = first_name.title()
second_name = second_name.title()

print(f"Hi {first_name} {second_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print("Do you like me?")
likes = input(prompt)

print(f"Where do you live {first_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives.title()}. Not sure where that is.
And you have a(n) {computer.upper()} computer. Nice.
""")
