arg1 = int(input())
entry_status = {}
for i in range(0, arg1):
    line = str(input())
    action, person  = line.split(" ")
    if person not in entry_status:
        entry_status[person] = ""
    # If person is entering
    if "entry" in line:
        if entry_status[person] == "entered":
            print(person + " entered (ANOMALY)")
        else:
            print(person + " entered")
            entry_status[person] = "entered"
    else:
        if entry_status[person] == "exited" or entry_status[person] == "":
            print(person + " exited (ANOMALY)")
        else:
            print(person + " exited")
            entry_status[person] = "exited"
