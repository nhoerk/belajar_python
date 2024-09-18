import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001,1,1)

        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a,birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA
                    
print("""Paradoks ulang tahun menunjukkan bahwa dalam sebuah kelompok yang terdiri dari N orang, kemungkinan bahwa dua dari mereka memiliki tanggal ulang tahun yang sama ternyata sangat besar. Program ini melakukan simulasi Monte Carlo (yaitu, simulasi acak berulang) untuk mengeksplorasi konsep ini.

(Sebenarnya ini bukan paradoks, melainkan hanya hasil yang mengejutkan.)""")

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("Berapa banyak tanggal lahir yang akan di generate? (max 100)")
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
    print()
    
print("Disini ada ",numBDays, " birthdays:" )
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')

print()
print()

match = getMatch(birthdays)

print("Pada simulasi ini, ",end="")
if match != None:
    monthName == MONTHS[match.month -1]
    dateText = '{}{}'.format(monthName, match.day)
    print("Banyaknya orang yang berulang tahun, ", dateText)
else:
    print("tidak ada ulang tahun nya sama.")
print()

print()