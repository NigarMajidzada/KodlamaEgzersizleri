class Kumanda():

    def __init__(self,kanal_listesi):
        self.kanal_listesi=kanal_listesi
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index<len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration


kumanda1=Kumanda(["ATV","BTV","CTV","DTV","ETV"])

# iter(kumanda1)
# print(next(kumanda1))

for i in kumanda1:
    print(i)
