# meminta input dari pengguna
persen_risk = float(input("Masukkan persentase risiko (dalam desimal): "))
stop_loss = float(input("Masukkan nilai stop loss: "))
entry = float(input("Masukkan nilai entry: "))
modal = float(input("Masukkan modal (dalam juta rupiah): "))

# menghitung jumlah lot
jumlah_lot = persen_risk / (1 - stop_loss / entry) * (modal * 1000000) / entry / 100

# menampilkan hasil perhitungan
print("Jumlah lot yang harus digunakan adalah:", jumlah_lot)
