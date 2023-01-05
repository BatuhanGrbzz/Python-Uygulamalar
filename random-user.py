print("Oluşturmak istediğiniz yılı ve kaçıncı ay olduğunu giriniz: ")
yil = int(input("Seneyi giriniz: "))
ay = int(input("Ayı giriniz: "))

import calendar

print(calendar.month(yil, ay))