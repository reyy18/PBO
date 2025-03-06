class Mahasiswa:
    def __init__(self, nama, nim, prodi, angkatan):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.angkatan = angkatan

    def praktikum(self):
        return f"{self.nama} sedang mengikuti praktikum."

    def berorganisasi(self):
        return f"{self.nama} aktif dalam kegiatan organisasi."

    def mengerjakan_tugas(self):
        return f"{self.nama} sedang mengerjakan tugas."

mahasiswa1 = Mahasiswa("Andi", "12345678", "Informatika", 2022)

print(mahasiswa1.praktikum())
print(mahasiswa1.berorganisasi())
print(mahasiswa1.mengerjakan_tugas())