import random

def generateName():
    firstNames = ["Batuhan","Büşra","Yusuf Can", "Süleyman", "Ümmügülsüm", "Durmuş"]
    lastNames = ["Gürbüz", "Keçi", "Saygı", "Koca", "Duran"]

    return "{} {}".format(random.choice(firstNames), random.choice(lastNames))

for i in range(5):
        print(generateName())
