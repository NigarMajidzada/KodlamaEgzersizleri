class Bilgisayar:
    def __init__(self,marka="Lenova",model="Thinkpad",ram_gb=8,depolama_gb=238,acik_mi=False):
        self.marka=marka
        self.model=model
        self.ram_gb=ram_gb
        self.depolama_gb=depolama_gb
        self.acik_mi=acik_mi

    def bilgisayari_ac(self):
        if self.acik_mi ==True:
            print(f"{self.marka} {self.model} bilgisayar acik")
        else:
            self.acik_mi=True
            print(f"{self.marka} {self.model} bilgisayar aciliyor")


    def pc_info(self):
        print("Marka: {}\nModel: {}\nRam: {} GB\nDepo: {} GB\n".format(self.marka,self.model,self.ram_gb,self.depolama_gb))


bilgisayar1=Bilgisayar()
print("Islem secin:\n "
      "1. Power Tusu\n"
      "2. PC info ")
islem=input("Islem secin: ")
if islem=="1":
    bilgisayar1.bilgisayari_ac()
if islem=="2":
    bilgisayar1.pc_info()
