class Kubus():
    def __init__(self,sisi):
        self.sisi = sisi
        
    def volume(self):
        volume = self.sisi **3
        return f"Kubus : {volume}"
    

class Balok():
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        
    def volume(self):
        volume = self.panjang * self.lebar * self.tinggi
        return  f"Balok : {volume}"
        


class Tabung():
    def __init__(self, jarijari, tinggi):
        self.jarijari = jarijari
        self.tinggi = tinggi
        
    def volume(self):
        alas = (22/7) * self.jarijari**2
        volume = alas * self.tinggi
        return f"Tabung : {volume}"

param_kubus = Kubus(10)
param_balok = Balok(3,6,10)
param_tabung = Tabung(7,10)

print(f"Volume \n {param_kubus.volume()}\n {param_balok.volume()}\n {param_tabung.volume()}")
