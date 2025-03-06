class Cashier:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices

    def calculate_total(self, selected_items):
        total = 0
        unavailable_items = []  # Daftar untuk menyimpan barang yang tidak tersedia

        for item in selected_items:
            if item in self.items:
                index = self.items.index(item)
                price = self.prices[index]
                total += price
            else:
                unavailable_items.append(item)  # Tambahkan item yang tidak tersedia ke daftar

        # Jika ada barang yang tidak tersedia, tampilkan pesan peringatan
        if unavailable_items:
            print("Peringatan: Barang berikut tidak tersedia:", ", ".join(unavailable_items))

        return total

# Daftar barang dan harga
items = ["apel", "pisang", "jeruk"]
prices = [2500, 1500, 3000]

# Membuat objek kasir
cashier = Cashier(items, prices)

# Meminta input dari pengguna
selected_items = input("Masukkan item yang dibeli (pisahkan dengan koma): ").lower().split(",")

# Menghapus spasi dari setiap item
selected_items = [item.strip() for item in selected_items]

# Menghitung total belanja
total_price = cashier.calculate_total(selected_items)
print("Total belanja:", total_price)