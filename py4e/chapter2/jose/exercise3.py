from datetime import datetime
date_time = datetime.now()
print(date_time)

customizeYear = 2023
customizeMonth = 8

if  customizeYear < date_time.year:
    print('year expired')
elif customizeYear >= date_time.year:
    print('year on date')
    if customizeMonth < date_time.month:
        print('month expired')
    elif customizeMonth >= date_time.month:
        print('month on date')
    else:
        print('never print')
else:
    print('never print')