import time
from data import data_pemesanan
def mimin():
    while True:
        print("\n=== PANEL ADMIN ===")
        print("1. Lihat Data Pemesanan")
        print("2. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Masukkan angka yang benar!")
            continue

        if pilihan == 1:
            print("\n=== Daftar Pemesanan ===")
            if data_pemesanan:
                for i, pesanan in enumerate(data_pemesanan, 1):
                    print(f"{i}. Nama: {pesanan['nama']}, Kamar: {pesanan['kamar']}, Malam: {pesanan['malam']}, Total: Rp {pesanan['total']:,}")
            else:
                print("Belum ada pemesanan.")
            time.sleep(2)

        elif pilihan == 2:
            print("Keluar dari mode Admin.")
            break

        else:
            print("Pilihan tidak tersedia!")

if __name__ == "__main__":
    mimin()
