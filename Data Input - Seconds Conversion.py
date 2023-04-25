("Algorithm for converting seconds");   
seconds = input("Please, tell me how many seconds you want to convert? ")

days = int(seconds) // 86400
secRestant = int(seconds) % 86400
hours = secRestant // 3600
secRestant = int(seconds) % 3600
minutes = secRestant // 60
secRestant = int(seconds) % 60
seconds_end_result = int(seconds) % 60
print(int(seconds), "seconds, is:", days, "days,", hours, "hours,", minutes, "minutes,", seconds_end_result, "seconds.")
