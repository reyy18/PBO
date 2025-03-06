def convert_to_int(string):
    try:
        result = int(string)
        return result
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

umur = input('Masukkan umur kamu: ')  # Inputan yang benar adalah angka
umur_int = convert_to_int(umur)

if umur_int is not None:  # Check if conversion was successful
    umur5tahunlagi = umur_int + 5
    print(f"Umur kamu 5 tahun lagi adalah {umur5tahunlagi}")