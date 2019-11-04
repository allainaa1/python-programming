worker_type = "part_time"
hours_worked = 25

if worker_type == "full_time" and hours_worked > 40:
    regular_hours = 40 * 50
    overtime = (hours_worked - 40) * 60
    print(overtime + regular_hours)
elif worker_type == "full_time":
    print(hours_worked * 50)
elif worker_type == "part_time" and hours_worked > 20:
    regular_hours = 20 * 65
    overtime = (hours_worked - 20) * 70
    print(overtime + regular_hours)
elif worker_type == "part_time":
    print(hours_worked * 65)
elif worker_type == "contract":
    regular_hours = hours_worked * 120
    tax_pay = regular_hours - (regular_hours * 0.25)
    print(tax_pay)
else:
    print("You aren't getting paid")


