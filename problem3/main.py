class Kalkulator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def Penjumlahan(self):
        penjumlahan = self.a + self.b
        return f"Penjumlahan : {penjumlahan}"
    def Pengurangan(self):
        pengurangan = self.a - self.b
        return f"Pengurangan : {pengurangan}"
    def Perkalian(self):
        perkalian = self.a * self.b
        return f"Perkalian : {perkalian}"
    def Pembagian(self):
        pembagian = self.a / self.b
        return f"Pembagian : {pembagian}"
    
h_penjumlahan = Kalkulator(3,4)
h_pengurangan = Kalkulator(15,4)
h_perkalian = Kalkulator(10,10)
h_pembagian = Kalkulator(12,3)

print(f"Kalkulator \n {h_penjumlahan.Penjumlahan()}\n {h_pengurangan.Pengurangan()}\n {h_perkalian.Perkalian()}\n {h_pembagian.Pembagian()}")