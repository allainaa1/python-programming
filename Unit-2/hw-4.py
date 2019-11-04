test_string = "Python Programming at General Assembly is Awesome!!"
new_string = ""
for char in test_string:
    if char != "m" and char != " " and char != "e":
        new_string = char + new_string
print(new_string)


