import time

#time.time()
print(f"The current time in second since the Unix epoch (jan 1, 1970) : {time.time()}")
print()

#time.time_ns()
print(f"The current time in nanosecond since the Unix epoch (jan 1, 1970) : {time.time_ns()}")
print()

#time.localtime([sec])
print(f"The local time in seconds is: {time.localtime()}")
print(f"It can convert a time in seconds since the epoch to a local time tuple: {time.localtime(170000000)}")
print()

#time.ctime([sec])
print(f"The current c time is: {time.ctime()}")
print(f"It can convert a time in seconds since the epoch to a readable string : {time.ctime(170000000)}")
print()

#time.gmtime([sec])
print(f"The UTC time in seconds is: {time.localtime()}")
print(f"It can convert a time in seconds since the epoch to a UTC time tuple: {time.gmtime(170000000)}")
