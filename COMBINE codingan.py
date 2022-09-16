#menu login admin
account_admin_user = ['nama']
account_admin_passw = ['saya']
while True:
        print('====== Selamat datang di menu login. ======')
        print("""
        [1] Login admin user
        [2] Buat akun admin
        [3] Keluar menu login admin
        """)
        opsi_menu = input('Pilih angka (1/2/3) : ')
        opsi_menu = int(opsi_menu)
        if opsi_menu == 2:
            print('Buat akun')
            user = input('Masukkan username baru : ')
            password = input('Masukkan password baru : ')
            account_admin_user.append(user)
            account_admin_passw.append(password)
            print('Akun admin telah dibuat')
            print('Silahkan login.')
        elif opsi_menu == 3:
            print('Terimakasih.')
        elif opsi_menu == 1:
            print('Silahkan login ')
            print("-------------------")
            user = input('User : ')
            password = input('Password : ')
            pesan = False
            for i in range(0,len(account_admin_user)):

                if password == account_admin_passw[i] and user == account_admin_user[i]:
                    pesan = True
            if pesan == True: 
                print("-------------------")
                print('Anda berhasil login')
                break
            else:
                print('Gagal login ')


data = {
        "Aqua 500 ml" : 107,
        "Aqua 250 ml" : 70,
        "Royko Ayam 150 gr" : 20,
        "Royko Sapi 150 gr" : 43,
        "Garam Jempol 200 gr" : 34,
        "Kuaci Rebo Greentea 150 gr" : 22,
        "Kuaci Rebo Milk" : 67, 
        "Indomie Kari Ayam" : 234,
        "Indomie Goreng" : 45,
        "Lemonilo Goreng" : 13,
        "Ultramilk 200 ml" : 73

}


#A
def input_stock() :
    print("""
    ======================================
                INPUT BARANG
    ======================================
    """)
    name = input("Masukkan Nama Barang : ")
    stok = input("Masukkan Jumlah Stock : ")
    data[name]=stok
    for key,val in data.items():
        print(key,":",val)
    looping()

#B
def cek_stock():
    print("""
    ======================================
             STOCK BARANG TERBARU
    ======================================
    """)
    for key,val in data.items():
        print("%s : %d" % (key,val))
    looping()

#C
def update(): 
    for key,val in data.items():
        print("%s : %d" % (key,val))
    print("Data Yang Ingin Diupdate")
    update = input("Masukkan Nama Stock yang ingin diupdate : ")
    stok_up = int(input("Masukkan banyak barang yang masuk : "))
    a = data.get(update)
    total_stok = a+stok_up
    data[update]=total_stok
    print("""
    ======================================
             STOCK BARANG TERUPDATE
    ======================================
    """)
    for key,val in data.items():
        print("%s : %d" % (key,val))
    looping()

#D
def delete():
    for key,val in data.items():
        print("%s : %d" % (key,val))
    print("-----------------------------")
    hapus = input("Masukkan Nama Data yang ingin dihapus : ")
    del data[hapus] 
    print("""
    ======================================
             STOCK TERBARU
    ======================================
    """)
    for key,val in data.items():
        print("%s : %d" % (key,val))
    looping()

#E
def exit() :
    print("="*50)
    print("Sesi Berakhir")
    print("="*50)

#Looping Main MENU 
def looping():
    print()
    loop = input("Back To Main Menu? [Y\T] : ")
    if loop == "Y" or "y" :
        main_menu()
    if loop == "T" or "t" :
        exit()

#MAIN MENU
def main_menu(): 
    print(""" 
    >>>>>>>>>>>>>>>>>>>>>>>>>>>
            MAIN MENU
    <<<<<<<<<<<<<<<<<<<<<<<<<<<
    |A| Input Stok 
    |B| Cek Stok
    |C| Update Stok
    |D| Delete Stok
    |E| EXIT
    """)
    pilihan = input("Pilih menu : ")
    if pilihan == 'A' :
        input_stock()
    elif pilihan == 'B' :
        cek_stock()
    elif pilihan == "C" :
        update()
    elif pilihan == "D" :
        delete()
    elif pilihan == "E" :
        exit()
    else :
        print("Masukkan Variable dengan benar")

main_menu()
