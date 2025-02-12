time = int(input("Time: "))

if time > 12:
    print("AM")
elif time < 12:
    print("PM")
else:
    print("Noon")
