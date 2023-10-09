class Persegi():
    def __init__(self,sisi):
        self.sisi = sisi
        
    def luas(self):
        luas = self.sisi * self.sisi
        return f"Persegi : {luas}"
    
    def keliling(self):
        keliling = 4*self.sisi
        return f"Persegi : {keliling}"
        
class Segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def luas(self):
        luas = self.alas * self.tinggi / 2
        return f"Segitiga : {luas}"
    
    def keliling(self):
        sisi = (self.alas*self.alas + self.tinggi*self.tinggi)** 0.5
        keliling = self.alas + self.tinggi + sisi
        return f"Segitiga : {keliling}"

class Persegipanjang():
    def __init__(self, panjang, tinggi):
        self.panjang = panjang
        self.tinggi = tinggi
        
    def luas(self):
        luas = self.panjang * self.tinggi
        return f"Persegi Panjang : {luas}"
    
    def keliling(self):
        keliling = 2*self.panjang + 2*self.tinggi
        return f"Persegi Panjang : {keliling}"

param_persegi = Persegi(4)
param_segitiga = Segitiga(3,4)
param_persegipanjang = Persegipanjang(7,8)

print(f"Luas \n{param_persegi.luas()}\n{param_segitiga.luas()}\n{param_persegipanjang.luas()}")
print(f"Keliling \n{param_persegi.keliling()}\n{param_segitiga.keliling()}\n{param_persegipanjang.keliling()}")
