#!/usr/bin/env python3

import toml, datetime

current_date = datetime.date.today()
current_month = current_date.month

today = current_date
day = today.day
 
day_str = f"{day:02}"

real_day = int(day_str)
 
month_str = f"{current_month:02}"

with open("/home/cie/.config/santosschedule.toml", "r") as f:
    data = toml.load(f)

for section_name in data:
    hour = data[section_name]["hour"]
    day = int(data[section_name]["day"])
    month = data[section_name]["month"]
    match = data[section_name]["match"]
    if month_str == month and day >= real_day:
        if day == real_day:
            matchday = {
                "hour": f"{hour}",
                "match": f"{match}"
            }
            file_name = "/home/cie/.config/santos_matchday.toml"
            with open(file_name, "w") as toml_file:
                toml.dump(matchday, toml_file)

# Print the values (you can format this as needed)
#print(f"{hour}, {day}, {type(month)}, {match}")
#print(current_month)
