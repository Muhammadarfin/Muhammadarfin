import time
import random
from colorama import Fore, Back, init

# Inisialisasi colorama
init(autoreset=True)

# Definisikan ukuran matriks (baris x kolom)
baris = 37
kolom = 37

# Inisialisasi matriks dengan karakter acak
matrix = [[random.choice(['$', '#', '@', '*', '+', '-']) for _ in range(kolom)] for _ in range(baris)]

# Fungsi untuk mencetak matriks dengan teks berjalan
def print_matrix():
    for i in range(baris):
        for j in range(kolom):
            print(get_colored_char(matrix[i][j]), end=" ")
        print()

# Fungsi untuk mendapatkan karakter berwarna acak
def get_colored_char(char):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    return random.choice(colors) + char + Fore.RESET

# Fungsi untuk mencetak panel RGB
def print_rgb_panel():
    print(f"{Fore.RED}R{Fore.RESET}{Fore.GREEN}G{Fore.RESET}{Fore.BLUE}B{Fore.RESET} Panel")
    print("=" * (kolom * 4))

# Fungsi untuk mencetak panel waktu
def print_time_panel():
    current_time = time.strftime("%H:%M:%S")
    print(f"{Fore.YELLOW}Current Time: {current_time}{Fore.RESET}")
    print("=" * (kolom * 4))

# Fungsi untuk mencetak pesan selamat datang
def print_welcome_message():
    print(f"{Fore.CYAN}Welcome to the Matrix Animation!{Fore.RESET}")
    print("=" * (kolom * 4))

# Mengatur kecepatan pergerakan teks (dalam detik)
kecepatan = 0.2

# Mencetak panel RGB di awal
print_rgb_panel()

# Mencetak panel waktu di awal
print_time_panel()

# Mencetak pesan selamat datang di awal
print_welcome_message()

# Mengulang untuk membuat efek matriks berjalan dari atas ke bawah dengan animasi latar belakang putih
for _ in range(baris + kolom * 2):
    # Ganti warna latar belakang menjadi putih
    print("\033[0;47m")
    print_matrix()
    time.sleep(kecepatan)
    print("\033[H\033[J")  # Membersihkan terminal (Hapus baris ini jika tidak bekerja di Termux)

    # Menggeser matriks ke bawah
    if _ < baris:
        matrix[_] = [random.choice(['$', '#', '@', '*', '+', '-']) for _ in range(kolom)]
    else:
        matrix.insert(0, [random.choice(['$', '#', '@', '*', '+', '-']) for _ in range(kolom)])
        matrix.pop()

# Ganti warna latar belakang kembali ke hitam
print("\033[0;47m")

# Hapus baris ini jika dijalankan di Termux untuk menjaga terminal tetap terbuka setelah selesai
input("Press Enter to exit...")

