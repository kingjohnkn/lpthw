f = open("demofile.txt", "r")
f.seek(0, 1)
print(f.read())