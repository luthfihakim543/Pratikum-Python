# halo.py - program Python pertama
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}! Selamat datang di praktikum Python.")
print("Semoga sukses!")
tahun_lahir = input("Masukkan tahun lahir: ")

try:
    tahun_lahir = int(tahun_lahir)
    usia = 2026 - tahun_lahir

    print("Perkiraan usia:", usia, "tahun")

except ValueError:
    print("Input harus berupa angka!")