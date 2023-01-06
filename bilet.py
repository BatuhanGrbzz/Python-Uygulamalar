

kisiSayisi = int(input("Kaç kişi için bilet almak istiyorsunuz?: "))

secim = input("Sinema için 1 tiyatro için 2'yi tuşlayınız.")


ogrenci = input("Öğrenci misiniz?(E/H): ")

ucret = 0

# Kişi sayısı ve sinema-tiyatro seçiminden istenilen bilete göre ücret çıkartması
if secim == "1":
    ucret = (15 * kisiSayisi)
elif secim == "2":
    ucret = (10 * kisiSayisi)

# Kişinin öğrenci olup olmamasına göre indirimli ücret uygulanır. (Yarısı alınmıştır.)
if ogrenci == "E" or ogrenci == "e":
    ucret = ucret / 2

print(f"Ödemeniz gereken ücret: {ucret}")