class Mahasiswa:
    def __init__(self, nama, nim, prodi, angkatan):
        self.__nama = nama   # Private attribute
        self.__nim = nim     # Private attribute
        self.prodi = prodi
        self.angkatan = angkatan

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    # Getter untuk NIM
    def get_nim(self):
        return self.__nim

    # Setter untuk NIM
    def set_nim(self, nim_baru):
        self.__nim = nim_baru

    def praktikum(self):
        return f"{self.__nama} sedang mengikuti praktikum."

    def berorganisasi(self):
        return f"{self.__nama} aktif dalam kegiatan organisasi."

    def mengerjakan_tugas(self):
        return f"{self.__nama} sedang mengerjakan tugas."


# Membuat objek baru
mahasiswa2 = Mahasiswa("Budi", "87654321", "Teknik Elektro", 2021)

# Mengakses private attribute menggunakan getter
print("Nama:", mahasiswa2.get_nama())
print("NIM:", mahasiswa2.get_nim())

# Mengubah private attribute menggunakan setter
mahasiswa2.set_nama("Joko")
mahasiswa2.set_nim("11223344")

# Mengecek perubahan yang telah dilakukan
print("Nama setelah diubah:", mahasiswa2.get_nama())
print("NIM setelah diubah:", mahasiswa2.get_nim())

# Memanggil metode lain
print(mahasiswa2.praktikum())
print(mahasiswa2.berorganisasi())
print(mahasiswa2.mengerjakan_tugas())
