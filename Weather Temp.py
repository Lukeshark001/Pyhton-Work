print("Welcome to the weather Temperature Checker")

temp_list = []

try:
    for counter in range(6):
        temp = input("Please enter temperature " + str(counter + 1) + ': ')
        if temp [-1].lower() in ("c","f"):
            temp_cleaned = int(temp[:-1])

            if temp[- 1].lower() == "f":
                temp_list.append((temp_cleaned - 32) / 1.8)
            else:
                temp_list.append(temp_cleaned)
        else:
            print("Please enter c or f only")

    print("Max Value is c" + str((max(temp_list))) + "f is" + str((max(temp_list) + 32) * 1.8))
    print("Min Value is c" + str((min(temp_list))) + "f is" + str((min(temp_list) + 32) * 1.8))

    Avg = sum(temp_list) / len(temp_list)
    rounded = round(Avg, 2)
    print("Avg is" + str(rounded) + "f is" + str((rounded + 32) * 1.8))

except ValueError:
        print("please enter numbers only")





