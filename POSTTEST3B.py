print('''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                WELCOME TO CLOUD X 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Opsi :
1. Sign In
2. Sign Up
''')

data_username = "eklecciarey"
data_password = "satudua"

option = int(input("Sign In atau Sign Up? :"))
a=3

while a>=1:
    if option == 1 :
        print(">>Sign In<<")
        username =str(input("Masukkan Username anda :"))
        password =str(input("Masukkan Password anda :"))
        if username==data_username and password==data_password :
            print("Selamat, Anda berhasil login")
            break
        else :
            a-=1
            if a==0:
                print("Gagal Login, Silakan coba lagi nanti")
            print("Cek Kembali Username dan Password anda!")
            
    else :
        print(">>Sign Up<<")
        new_user = str(input("Masukkan Username yang anda inginkan :"))
        new_pass = str(input("Masukkan Password yang anda inginkan :"))
        print("Selamat akun anda", new_user, "Berhasil dibuat")
        break
