class Ongkir():
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat   
        
    def ongkoskirim(self):
        dimensi = self.panjang * self.lebar * self.tinggi
        h_1kg = 50000
        if dimensi <= 50:
            t_ongkir = self.berat * h_1kg
        return f"Harga : {t_ongkir}"
   
h_ongkir = Ongkir(5,2,4,1)
print(f"Ongkos Kirim \n{h_ongkir.ongkoskirim()}")