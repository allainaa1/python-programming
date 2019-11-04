temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]
sum_pos = 0
sum_neg = 0
for temp in temperature_readings:
    if temp > 0:
        sum_pos += temp
    elif temp < 0:
        sum_neg += temp

average_pos  = sum_pos / len(temperature_readings)
average_neg  = sum_neg / len(temperature_readings)
print ("Average of positive readings:", average_pos)
print ("Average of negative readings:", average_neg)