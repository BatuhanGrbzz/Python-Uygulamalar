print("-" * 30)
print("1- Celciustan fahrenheite çevirme")
print("2- Fahrenheittan celciusa çevirme")
print("-" * 30)

choice = input("1 veya 2 numara arasından seçim yapınız: ")

if choice == "1":
    print("\n Celciustan fahrenheite")
    celcius = float(input("Dönüştürmek istediğiniz derece: "))

    fahrenheit = (celcius * 1.8) + 32
    print(f"{celcius} santigrat derece = {fahrenheit} derecedir.")
elif choice == "2":
    print("\n Celciustan fahrenheite")
    fahrenheit = float(input("Dönüştürmek istediğiniz derece: "))

    celcius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} santigrat derece = {celcius} derecedir.")
else: 
    print("Lütfen bir seçim yapınız.")
    