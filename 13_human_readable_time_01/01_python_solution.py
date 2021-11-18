import time
def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    minutes = seconds //  60 % 60
    seconds %= 60
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

print(format_seconds_to_hhmmss(7500))

# from time module
print(time.strftime('%H:%M:%S', time.gmtime(7500)))





