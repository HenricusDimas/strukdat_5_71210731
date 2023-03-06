class Karyawan: 
    def __init__(self,nama=None,umur=None,jenisKelamin=None,upahPerHari=None):
        self.nama = nama
        self.umur = umur
        self.jenisKelamin = jenisKelamin
        self.upahPerHari = upahPerHari
    def printInfo(self):
        print('============ INFO ============')
        print("Nama             : ",self.nama)
        print("Umur             : ",self.umur)
        print("Jenis Kelamain   : ",self.jenisKelamin)
        print("Upah Per Hari    : ",self.upahPerHari)

    def hitungGajiBulanan(self):
        try:
            gaji = self.upahPerHari * 30
            print("Gaji Bulanan Adalah : ",gaji)
        except:
            print("Belum menginputkan Upah Per Hari !!!")

orang1 = Karyawan("Haniif", 90)

orang1.printInfo()

orang2 = Karyawan("Sindu", 190)

orang2.printInfo()

