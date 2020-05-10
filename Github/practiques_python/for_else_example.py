names = ["John", "Mary"]
for name in names:
    if name.startswith("x"):
        print("Found")
        break
else:
    print("Not found")
