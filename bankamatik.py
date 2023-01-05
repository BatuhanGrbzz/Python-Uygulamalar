


BatuHesap = {
    'ad' : 'Batuhan Gürbüz',
    'hesapNo': '12345639',
    'bakiye': 3000,
    'ekHesap': 2000
}

BusraHesap = {
    'ad' : 'Büşra Gürbüz',
    'hesapNo': '1579874',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    print(type(hesap['bakiye']))

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input("ek hesap kullanmak istiyor musunuz? (E/H)")
            if ekHesapKullanimi == "E":
                ekhesapKullanılacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanılacakMiktar

                print("Paranızı alabilirsiniz.")
            else:
                ParaYatir = input("Hesabınızda yeterli bakiye yoktur. Para yüklemek ister misiniz? (E/H)")
                if ParaYatir == "E":
                    paraYukle = int(input("Ne kadar para yüklemek istersiniz? "))
                    bakiye = hesap['bakiye']
                    bakiye += int(paraYukle)
                    hesap['bakiye'] = bakiye
                    if bakiye >= miktar:
                        print("Para çekme işlemi yapabilirsiniz.")

                else:
                    print("İşleminiz sonlandırılmıştır.")
        else:
            print("Bakiye yüklemeden para çekemezsiniz.")
            
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL Bulunmaktadır.")


paraCek(BatuHesap, 5000)