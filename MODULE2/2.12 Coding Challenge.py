students = ["Joy", "Asha", "Oscar"]
vocal_ranges = ["soprano", "alto", "tenor"]

singers = dict(zip(students, vocal_ranges))
print(singers)

print("\n")

teacher_info = {"Name:": "Rina", "Subject:": "Math"}

for key, value in teacher_info.items():
    print(key)
    print(value)

print("\n")

weather_in_asia = {"Japan": 22, "Malaysia": 25, "Philippines": 48}
weather_in_asia["Singapore"] = 27
print(weather_in_asia)

print("\n")

school_supplies = {"pencils": 2, "pens": 4, "eraser": 1}

print(school_supplies.get("Ballpen"))