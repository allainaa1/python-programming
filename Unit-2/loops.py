name_first = "Allaina"

'''for count in range(0, 10):
    if count % 2 != 0:
        print(count)
    else:
        print(count, "even")'''

total_num =  0

for count in range(1, 11):
    if count % 2 == 0:
        total_num += count
print(total_num)


full_name ="Allaina Abraham"
for count in full_name:
    if count == "a" or count == "e" or count == "i" or count == "o" or count == "u":
        print(count)
