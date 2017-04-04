#!/usr/bin/python

import sys, datetime

args = sys.argv[1:] # drops the inital invocation argument

if "-T" in args:
    date_or_time = "Time"
else:
    date_or_time = "Date"

if "-f" in args:
    with open(args[-1], "r") as o:
        val = o.readline()
else:
    val = args[-1]

def hex_to_time(hex_string):
    int_val = int(hex_string[2:], 16)
    bin_val = bin(int_val)[2:]
    bin_val = "0"*(16-len(bin_val)) + bin_val
    hour = int(bin_val[:5], 2)
    minute = int(bin_val[5:11], 2)
    second = int(bin_val[11:], 2)
    dt = datetime.datetime(1900, 1, 1, hour=hour, minute=minute, second=second*2) #Datetime module requires a year/month/day, throwaway values
    return dt.strftime("Time: %I:%M:%S %p") #taking advantage of the formatting module only.
    

def hex_to_date(hex_string):
    int_val = int(hex_string[2:], 16) # [2:] drops the 0x
    bin_val = bin(int_val)[2:] # [2:] drops the 0b
  
    bin_val = "0"*(16-len(bin_val)) + bin_val #0 pads the number to 16 bits

    year = int(bin_val[:7], 2)
    month = int(bin_val[7:11], 2)
    day = int(bin_val[11:], 2)
    dt = datetime.datetime(year + 1980, month, day)
    return (dt.strftime("Date: %B %d, %Y")) #taking advantage of the formatting module only.

switch = {
    "Time": hex_to_time,
    "Date": hex_to_date,
    }


if __name__ == '__main__':
    converted = switch[date_or_time](val)
    print(converted)