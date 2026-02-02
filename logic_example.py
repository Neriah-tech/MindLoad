study_hours = 4
task_switching = "High"
task_clarity = 2
mental_fatigue = 4

if task_switching == "High" and task_clarity <= 2:
    load_status = "High Cognitive Load"
elif mental_fatigue >= 4:
    load_status = "Moderate Cognitive Load"
else:
    load_status = "Balanced Load"

print(load_status)
