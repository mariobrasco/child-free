id_nav = 0
jumlah_nav = 0

#Menu Navigasi
def nav_belum_login():
    global jumlah_nav
    global id_nav
    id_nav = 0
    jumlah_nav = 2
    print("============== MENU NAVIGASI ===============")
    print("1. Login") 
    print("2. Registrasi")
    print("0. Keluar")
    print("============================================")

def nav_sudah_login():
    global jumlah_nav
    global id_nav
    id_nav = 1
    jumlah_nav = 3
    print("============== MENU NAVIGASI ===============")
    print("1. Profil Saya") 
    print("2. For You Page")
    print("3. Kembali ke Menu Sebelumnya")
    print("0. Keluar")
    print("============================================")
#Menu Navigasi--

def nav_hub():
    global input_navigasi
    
    if (id_nav == 0):
        nav_belum_login()
        input_navigasi = int(input(f"Masukkan angka untuk navigasi (1-{jumlah_nav}) atau 0 untuk keluar: "))
    elif (id_nav == 1):
        nav_sudah_login()
        input_navigasi = int(input(f"Masukkan angka untuk navigasi (1-{jumlah_nav}) atau 0 untuk keluar: "))


while True:
    
    nav_hub()

    #Login
    if (id_nav == 0 and input_navigasi == 1):
        print("============================ MENU LOGIN =================================")
        print("Jika Ingin membatalkan login, ketik 'batal' pada username atau password")
        
        input_username = input("Masukkan username: ")
        if (input_username == "batal"):
            print("Login dibatalkan, kembali ke menu navigasi.")
        elif (input_username != "batal"):
            input_password = input("Masukkan password: ")
            if (input_password == "batal"):
                print("Login dibatalkan, kembali ke menu navigasi.")
                
        print("=========================================================================")
        if (input_username == "batal" or input_password == "batal"):
            print("Login dibatalkan, kembali ke menu navigasi.")
        elif (input_username == "admin" or input_password == "admin123"):
            print(f"Berhasil login sebagai {input_username}.")
            id_nav = 1 
        else:
            print("Gagal login, username atau password salah.")
    #Login--
    
    if (input_navigasi == 0):
        print("Keluar dari program, Terimakasih Telah menggunakan program ini  .")
        break