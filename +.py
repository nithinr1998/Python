class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        return 'time is: ' + str(self.__hour + other.__hour) + ':' + str(self.__minute + other.__minute) + ':' + str(
            self.__second + other.__second)


h = int(input("Enter the hour: "))
m = int(input("Enter the minute: "))
s = int(input("Enter the second: "))
h1 = int(input("Enter the hour: "))
m1 = int(input("Enter the minute: "))
s1 = int(input("Enter the second: "))
t1 = Time(h, m, s)
t2 = Time(h1, m1, s1)
print(t1 + t2)
