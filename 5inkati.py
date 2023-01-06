Kat5 = []

print("Merhabalar, 5in katlarını bulan programa hoşgeldiniz :)")


while True:
    sayi = int(input("Lütfen sayı giriniz: "))
    try:
        if sayi % 5 == 0:
            Kat5.append(sayi)
        else: 
            break
    except Exception as ex:
        print(ex)
    finally:
        print("5'in katları yazıldı.")

print(Kat5)

