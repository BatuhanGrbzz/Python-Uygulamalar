meyve = input("Hangi meyveyi istiyorsunuz: ")

if(meyve == "Muz"):
    kilo = int(input("Kaç kilo muz istiyorsunuz? "))
    print(kilo * 5, "Tl ücret ödeyeceksiniz.")
elif(meyve == "Elma"):
    renk = input("Hangi renk elma istiyorsunuz?")
    if(renk == "Kırmızı"):
        kilo = kilo = int(input("Kaç kilo kirmizi elma istiyorsunuz? "))
    elif(renk == "Sarı"):
        kilo = kilo = int(input("Kaç kilo sari elma istiyorsunuz? "))
    elif(renk == "Yeşil"):
        kilo = kilo = int(input("Kaç kilo yesil elma istiyorsunuz? "))
    else:
        print("Sadece Kirmizi, sari ve yeşil elmalarimiz mevcuttur.")
    print(kilo * 10, "TL ücret ödeyeceksiniz.")
elif(meyve == "Üzüm"): 
    renk = input("Hangi renk üzüm istiyorsunuz?")
    if(renk == "Mor"):
        kilo = kilo = int(input("Kaç kilo mor üzüm istiyorsunuz? "))
    elif(renk == "Yeşil"):
        kilo = kilo = int(input("Kaç kilo yeşil üzüm istiyorsunuz? "))
    print(kilo * 15, "TL ücret ödeyeceksiniz.")

elif(meyve == "Hıyar"):
    if(meyve == "Salatalık"):
        print("Salatalık değil hıyar diceksin.")
    else:
        kilo = kilo = int(input("Kaç kilo yeşil üzüm istiyorsunuz? "))
        print(kilo * 8, "Tl ücret ödeyeceksiniz.")
    

        
    
