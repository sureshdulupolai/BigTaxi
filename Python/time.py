# power shell
from datetime import datetime, timedelta

def add_minutes(hour, minute, add_min):
    time_obj = datetime.strptime(f"{hour}:{minute}", "%H:%M")
    new_time = time_obj + timedelta(minutes=add_min)
    return new_time.strftime("%I:%M %p")

now = datetime.now()

currentHour = now.hour
currentMinute = now.minute

userInput = int(input('Enter extra minutes: '))

result = add_minutes(currentHour, currentMinute, userInput)
print("New time:", result)

aTuple = ("orange")
print(type(aTuple))