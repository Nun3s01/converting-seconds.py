("Algorithm for converting seconds");   
seconds = int(input("Please, tell me how many seconds you want to convert? "))

days = (seconds) // 86400
secRestant = (seconds) % 86400
hours = secRestant // 3600
secRestant = (seconds) % 3600
minutes = secRestant // 60
secRestant = (seconds) % 60
seconds_end_result = (seconds) % 60
print(seconds, "seconds, is:", days, "days,", hours, "hours,", minutes, "minutes,", seconds_end_result, "seconds.")
