class PersegiPanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l
    
    def keliling (self):
        return "Kelilingnya adalah = " +  str(2*self.p + 2*self.l) + "cm"
    def luas (self):
        return "Luasnya adalah = " + str(self.p * self.l) + "CM"
    def __str__(self):
        return "persegi panjang" + ", panjang " + str(self.p) + " Cm" + ", Lebar " + str(self.l) + " Cm"


def main():
    try:
        panjang = float(input("Masukkan Panjang = "))
        lebar = float(input("Masukkan Lebar = "))
        if panjang <= 0 or lebar <= 0:
            print ("Harus Positif")
            return
        pp = PersegiPanjang(panjang, lebar)
        print ( pp.keliling())
        print ( pp.luas())
    except ValueError:
        print("Nilai harus sesuai")

main()