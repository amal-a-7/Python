class Time:
    def __init__(self):
        self.__h=int(input("Enter the time in hour: "))
        self.__m=int(input("Enter the time in minutes:"))
        self.__s=int(input("Enter the time in seconds:"))
    def __add__(tob1,tob2):
        hours=tob1.__h+tob2.__h
        print("sum of hours:",hours)
        minutes=tob1.__m+tob2.__m
        print("sum of minutes:",minutes)
        seconds=tob1.__s+tob2.__s
        if hours>=24:
            hours=hours%24
        if minutes>=60:
            hours=hours+minutes//60
            minutes=minutes%60
        if seconds>=60:
            minutes=minutes+seconds//60
            seconds=seconds%60
        return hours,minutes,seconds
print("Enter the time of first object")
tob1=Time()
print("Enter the time of second object")
tob2=Time()
print("Sum of two Time is: (Hour,Minutes,Seconds)",tob1+tob2)