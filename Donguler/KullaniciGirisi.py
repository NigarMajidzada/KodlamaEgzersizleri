print('''
**********************
Kullanici Girisi Programi
***********************''')

sys_kullanici_adi="Nigar"
sys_kullanici_parolu="12345"
deneme_sayisi=3
while True:
    kullanici_adi=input("Kullanici adinizi giriniz: ")
    parol=input("Parol: ")
    if(kullanici_adi !=sys_kullanici_adi and parol==sys_kullanici_parolu):
        print("Kullanici adi hatali....")
        deneme_sayisi-=1

    elif    (kullanici_adi ==sys_kullanici_adi and parol!=sys_kullanici_parolu):
        print("Kullanic parolasi hatali....")
        deneme_sayisi-=1
    elif   (kullanici_adi !=sys_kullanici_adi and parol !=sys_kullanici_parolu):
        print("Kullanici adi ve parolasi hatali...")
        deneme_sayisi-=1
    else:
        print("Sisteme basariyla giris yapildi...")
        break
    if(deneme_sayisi==0):
        print("Deneme hakkiniz bitmisdir...")
        break