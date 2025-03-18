from datetime import datetime

date1_str = "2024-01-01 12:00:00"
date2_str = "2024-01-03 12:00:01"

# Convert string dates to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

# Calculate time difference in seconds
time_difference = (date2 - date1).total_seconds()
print(time_difference)

if time_difference > 2 * 24 * 60 * 60:  # 2 days in seconds
    print("The time difference is greater than 2 days.")
else:
    print("The time difference is less than or equal to 2 days.")
