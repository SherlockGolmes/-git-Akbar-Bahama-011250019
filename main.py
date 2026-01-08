# -*- coding: utf-8 -*-
# Project Sherlock Golmes Misteri Tongkat Terbang
# Nama    : Muhammad Akbar Bahama
# NIM     : 011250019

import sys

# Data karakter
player_name = "Sherlock Golmes"
suspects = ["Profesor A", "Lady B", "Inspektur C"]
clues_found = []

# Fungsi untuk menampilkan narasi
def narrate(text):
    print("\n" + text)

# Fungsi interaksi
def choose_action():
    print("\nApa yang ingin kamu lakukan?")
    print("1. Periksa lokasi")
    print("2. Tanyakan saksi")
    print("3. Periksa bukti")
    print("4. Akhiri permainan")
    
    choice = input("Masukkan pilihan (1-4): ")
    return choice

# Fungsi untuk menentukan ending
def ending():
    if "jejak kaki" in clues_found and "tongkat patah" in clues_found:
        narrate("Setelah menyatukan semua bukti, kamu berhasil menemukan pelaku!")
        narrate("Ternyata Lady B yang mencuri tongkat terbang untuk eksperimen rahasia.")
        narrate("Selamat, Detektif Sherlock Golmes! Misteri terselesaikan.")
    elif "jejak kaki" in clues_found:
        narrate("Kamu menemukan beberapa petunjuk, tapi belum cukup untuk menangkap pelaku.")
        narrate("Misteri masih belum terpecahkan. Cobalah lagi untuk mencari lebih banyak bukti.")
    else:
        narrate("Kamu gagal menemukan bukti yang cukup.")
        narrate("Misteri tongkat terbang tetap menjadi rahasia. Permainan berakhir.")

# Fungsi utama game
def main_game():
    narrate(f"Selamat datang, Detektif {player_name}!")
    narrate("Kamu ditugaskan untuk memecahkan misteri tongkat terbang yang hilang.")
    
    while True:
        choice = choose_action()
        
        if choice == "1":
            narrate("Kamu memeriksa lokasi dan menemukan sebuah jejak kaki aneh.")
            clues_found.append("jejak kaki")
            narrate("Selain itu, kamu melihat sesuatu yang berserakan... ternyata tongkat patah!")
            clues_found.append("tongkat patah")
        elif choice == "2":
            narrate(f"Kamu menanyai saksi: {suspects[0]}. Dia mengatakan dia melihat seseorang mencurigakan.")
        elif choice == "3":
            if clues_found:
                narrate(f"Kamu memeriksa bukti: {', '.join(clues_found)}")
            else:
                narrate("Belum ada bukti yang ditemukan.")
        elif choice == "4":
            narrate("Permainan berakhir.")
            ending()
            sys.exit()
        else:
            narrate("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan game
if __name__ == "__main__":
    main_game()
