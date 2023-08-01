iomport calendar
#print (calendar.TextCalendar(firstweekday=6).formatyear(2015))
datestr=input()
month=int(datestr.split()[0])
day=int(datestr.split()[1])
year=int(datestr.split()[2])
days = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY",
}
#print (days[calendar.weekday(2015, 12, 25)])
print (days[calendar.weekday(year, month, day)])