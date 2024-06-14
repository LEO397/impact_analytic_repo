num_of_combinations = 0
last_day_miss = 0


def attendance_prob(missing_attendance, prev_attendance, curr_attendance, num_of_days, attendance, miss_flag):
    global num_of_combinations
    global last_day_miss

    if missing_attendance >= 4:
        miss_flag = True
        return

    if num_of_days == attendance:
        if miss_flag:
            return
        if curr_attendance == 'A':
            last_day_miss += 1
        num_of_combinations += 1
        return

    attendance_prob(missing_attendance=0, prev_attendance=prev_attendance+curr_attendance, curr_attendance="P",
                    num_of_days=num_of_days+1, attendance=attendance, miss_flag=miss_flag)
    attendance_prob(missing_attendance=missing_attendance+1, prev_attendance=prev_attendance+curr_attendance, curr_attendance="A",
                    num_of_days=num_of_days+1, attendance=attendance, miss_flag=miss_flag)
    return


value_of_n = int(input("Please enter the value of N: "))
attendance_prob(0, "", "", 0,  value_of_n, False)

print(str(last_day_miss)+'/'+str(num_of_combinations))
