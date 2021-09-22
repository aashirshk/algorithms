def timeConversion(time):

    if time[:2] == "12" and time[-2:].upper() == "AM":
        # return f"00{time}"
        return f'00{time[2:-2]}'
    elif time[-2:].upper() == "AM":
        return time[:-2]
    elif time[:2] == "12" and time[-2:].upper() == "PM":
        return time[:-2]
    else:
        if time[2] != ":":
            time = f'0{time}'
        
        return f'{str(int(time[:2])+12)}{time[2:-2]}'

if __name__ == "__main__":
    time = "7:05:45PM"
    result = timeConversion(time)

    print(result)
