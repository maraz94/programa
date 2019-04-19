import datetime
"""
year =int(input("Dime el año: "))
month =int(input("Dime el mes: "))
day =int(input("Dime el día: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_emaining = user_date - datetime.datetime.now()

print("Faltan {} dias y {} horas".format(time_emaining.days, int(time_emaining.seconds / 3600)))
print("Mañana es {}".format(datetime.datetime.now() + datetime.timedelta(days=1)))
"""

manana = datetime.datetime.now() + datetime.timedelta(days=1)
manana_medianoche = datetime.datetime(year=manana.year, month= manana.month, day= manana.day)
hoy = datetime.datetime.now()
faltanta_para_manana = manana_medianoche - hoy

print("Mañana es {}".format(manana.strftime("%d del %m del %Y")))
print("Faltan {} horas para mañana".format(int(faltanta_para_manana.total_seconds() /3600)))