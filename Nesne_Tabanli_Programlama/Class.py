class Animal:
    def speak(self):
        print("Animal speaks")

class Parrot(Animal):
    def speak(self):
        super().speak()  # Üst sınıftaki speak metodunu çağırır
        print("Parrot talks")  # Alt sınıftaki özel işlev

parrot_instance = Parrot()
parrot_instance.speak()
