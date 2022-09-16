print('''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    DELMAR CAFE
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
MENU DEL MAR :
    A. Tequilla = Rp. 45.000
    B. Berrys = Rp. 35.000
    C. Peach Mojito = Rp. 40.000
    D. Fish and Chips = Rp. 70.000
    E. Sistagor = Rp. 50.000
''')

main_menu = [
    ["Teqilla", "Berrys", "Peach Mojito"],
    ["Fish and Chips", "Sistagor"]
]

#ListMultidimensi 
print("1.", main_menu[0][0])
print("2.", main_menu[0][1])
print("3.", main_menu[0][2])
print("4.", main_menu[1][0])
print("5.", main_menu[1][1])

#Mengedit Nama Menu
main_menu = [
    ["Teqilla", "Berrys", "Peach Mojito"],
    ["Fish and Chips", "Sistagor"]
]
main_menu[0][1] = "Kopi Susu"
print(main_menu)

#Menambah Nilai List 
sub_menu = []

#Dibelakang 
menambah = input("Menambah list dibelakang\ditengah (B Belakang, T tengah) :")
if menambah == "B" :
    print("Menambah Nilai List Belakang")
    sub_menu.append("Nasi Goreng Kambeng")
    main_menu.append(sub_menu)
    print(main_menu)
    print()

#Di tengah 
elif menambah == "T" :
    print("Menambah List di tengah")
    sub_menu.append('Nasi Ayam Bakar')
    main_menu.insert(1, sub_menu)
    print(main_menu)
    print()

#Menghapus Menu 
#1
print("Menghapus Menu 1")
del main_menu[0][1]
print(main_menu)
print()

print('Menghapus Menu 2')
sub_menu.remove('Nasi Ayam Bakar' or 'Nasi Goreng Kambeng')
print(main_menu)

