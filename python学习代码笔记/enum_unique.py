from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
from enum import unique
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sta=6
day1=Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(2))
for name,member in Weekday.__members__.items():
    print(name,member)