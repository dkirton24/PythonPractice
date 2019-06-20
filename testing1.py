flag = True

ages = [22,54,16,46,61,23,42,12,13,71,24]

for age in ages:
    if age <= 21:
        flag = False



if flag == False:
    print("There are underage people going!")
