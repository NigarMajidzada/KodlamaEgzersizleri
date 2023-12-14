from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")
#https://docs.python.org/2/library/time.html
#Datetime

print(datetime.now())
su_an=datetime.now()
print(su_an.year)
print(su_an.month)
print(su_an.day)
print(su_an.microsecond)
print(su_an.hour)

print(datetime.ctime(su_an))


#Strftime

print(datetime.strftime(su_an,"%Y"))
print(datetime.strftime(su_an,"%B"))
print(datetime.strftime(su_an,"%D"))
print(datetime.strftime(su_an,"%A"))


#Timestamp an fromtimestamp

su_an=datetime.now()

saniye=datetime.timestamp(su_an)
print(saniye)

su_an2=datetime.fromtimestamp(saniye)
print(su_an2)
x=datetime.fromtimestamp(0)# epoktime
print(x)

tarih=datetime (2005,6,11)
su_an=datetime.now()
yas=(su_an-tarih)
yas=yas.days//365
print("Yas: ",yas)
