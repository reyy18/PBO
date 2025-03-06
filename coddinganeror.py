def calculate_average(numbers):
    try:
        # Memastikan input adalah list
        if not isinstance(numbers, list):
            raise TypeError("Input harus berupa list.")
        
        # Memastikan list tidak kosong
        if len(numbers) == 0:
            raise ValueError("List tidak boleh kosong.")
        
        # Memastikan semua elemen dalam list adalah angka
        for number in numbers:
            if not isinstance(number, (int, float)):
                raise TypeError("Semua elemen dalam list harus berupa angka.")
        
        total = sum(numbers)
        average = total / len(numbers)
        return average

    except (TypeError, ValueError) as e:
        print(f"Peringatan: {e}")
        return None

# Contoh penggunaan
result = calculate_average([5, 5, 7, 8])  # Input yang benar adalah list
print(result)

# Contoh input yang salah
result_invalid = calculate_average("5, 5, 7, 8")  # Input berupa string
print(result_invalid)

result_invalid2 = calculate_average([5, 5, "7", 8])  # Input dengan string dalam list
print(result_invalid2)

result_invalid3 = calculate_average([])  # Input list kosong
print(result_invalid3)
