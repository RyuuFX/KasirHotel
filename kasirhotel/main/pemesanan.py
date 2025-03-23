import time
from data import data_pemesanan

HARGA_KAMAR = {
    "Standar": 500000,
    "Deluxe": 750000,
    "Suite": 1000000
}

def pesan():
    while True:
        print("\n=== PEMESANAN HOTEL ===")
        nama = input("Masukkan Nama Anda: ")
        print("Tipe Kamar:")
        print("1. Standar - Rp 500.000/malam")
        print("2. Deluxe  - Rp 750.000/malam")
        print("3. Suite   - Rp 1.000.000/malam")

        try:
            pilihan_kamar = int(input("Pilih Tipe Kamar (1/2/3): "))
            if pilihan_kamar not in [1, 2, 3]:
                print("Pilihan tidak valid!")
                continue
            malam = int(input("Berapa malam menginap? "))
            if malam <= 0:
                print("Jumlah malam harus lebih dari 0!")
                continue
        except ValueError:
            print("Input tidak valid!")
            continue

        # Tentukan tipe kamar
        kamar = list(HARGA_KAMAR.keys())[pilihan_kamar - 1]
        total_harga = HARGA_KAMAR[kamar] * malam

        print("\n=== Detail Pemesanan ===")
        print(f"Nama        : {nama}")
        print(f"Tipe Kamar  : {kamar}")
        print(f"Lama Menginap : {malam} malam")
        print(f"Total Harga : Rp {total_harga:,}")
        print("Terima kasih telah memesan di Hotelku!")

        data_pemesanan.append({"nama": nama, "kamar": kamar, "malam": malam, "total": total_harga})

        time.sleep(2)
        break 

if __name__ == "__main__":
    pesan()
