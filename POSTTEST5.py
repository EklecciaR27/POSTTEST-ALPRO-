main_menu = {
    "1. Tequillla" : 40000,
    "2. Berrys" : 35000,
    "3. Peach Mojito" : 30000,
    "4. Fish and Chips" : 50000,
    "5. Sistagor" : 75000
}

# Read Menu
def menu_delmar():
    print(main_menu)

# Crate Menu    
def insert_menu():
    menu_baru = {}
    menu_baru = input("Masukkan nama menu :")
    harga = input("Masukkan Harga Baru : ")
    main_menu[menu_baru] = harga
    print(main_menu)

# Update Menu
def edit_menu():
    print(main_menu)
    pilihan = str(input("Masukkan Menu yang mau diedit :"))
    if pilihan == "1" :
        del main_menu["1. Tequillla"]
    elif pilihan == "2" :
        del main_menu["2. Berrys"]
    elif pilihan == "3" :
        del main_menu["3. Peach Mojito"]
    elif pilihan == "4" :
        del main_menu["4. Fish and Chips"]
    elif pilihan == '5' :
        del main_menu["5. Sistagor"]
    else :
        print("Masukkan menu dengan benar!!")
    menubaru = input("Masukkan Menu Baru :")
    harga = input("Masukkan Harga : ")
    main_menu[menubaru] = harga
    print(main_menu)

#Delete Menu 
def hapus_menu():
    print(main_menu)
    hapus = input("Menu yang dihapus : ")
    del main_menu[hapus] 
    print(main_menu)

def log_out() :
    print("Thank You, Kamsamida")

  
def fungsional_menu():
    print("===== Main Menu =====")
    print("|A| Menu Makanan")
    print("|B| Insert Menu")
    print('|C| Update Menu')
    print('|D| Delete Menu')
    print("|E| Keluar")
    fungsi=input("Pilih salah satu :")
    if fungsi == "A" :
        menu_delmar()
    elif fungsi == "B" :
        insert_menu()
    elif fungsi == "C" :
        edit_menu()
    elif fungsi == "D" :
        hapus_menu()
    elif fungsi == "E" : 
        log_out()

while True :
    fungsional_menu()
    print()


