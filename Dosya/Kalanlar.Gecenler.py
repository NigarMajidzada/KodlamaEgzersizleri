def kalanlar_gecenler(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if son_not >= 50:
        return isim + "----------------------> Başarılı\n"
    else:
        return isim + "----------------------> Kaldı\n"

with open("Dosya", "r", encoding="utf-8") as file:
    gecenler = []
    kalanlar = []
    for satir in file:
        if kalanlar_gecenler(satir).endswith("Başarılı\n"):
            gecenler.append(kalanlar_gecenler(satir))
        else:
            kalanlar.append(kalanlar_gecenler(satir))

with open("gecenler.txt", "w", encoding="utf-8") as gecenler_file:
    for ogrenci in gecenler:
        gecenler_file.write(ogrenci)

with open("kalanlar.txt", "w", encoding="utf-8") as kalanlar_file:
    for ogrenci in kalanlar:
        kalanlar_file.write(ogrenci)
