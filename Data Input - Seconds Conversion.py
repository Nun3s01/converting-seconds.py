#   Algorithm for converting seconds
seconds = int(input("Please, tell me how many seconds you want to convert? "))

years = (seconds) // 31104000
secRestant = (seconds) % 31104000
months = secRestant // 2592000
secRestant = (seconds) % 2592000
days = secRestant // 86400
secRestant = (seconds) % 86400
hours = secRestant // 3600
secRestant = (seconds) % 3600
minutes = secRestant // 60
secRestant = (seconds) % 60
seconds_end_result = secRestant % 60
print(f"{seconds} seconds, is: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds_end_result} seconds.")
