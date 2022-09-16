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
jawab = "Ya"
while (True):
    keranjang = input("Masukkan Pesanan Anda (Sesuai dengan menu):") #Input A-E
    if keranjang == "A" :
        print("Menu : Tequilla")
        harga = 45000
        banyaknya = int(input("Banyak Pesanan :"))
        t = (banyaknya*harga)
        if banyaknya >= 3:
            diskon= int(t*0.1)
            total = t-diskon
            print("Total harga Tequilla :", total)
        else : 
            print("Total harga Tequilla :",total)
    elif keranjang == 'B' :
        print("Menu Berrys")
        harga = 35000
        banyaknya = int(input("Banyak Pesanan :"))
        t = (banyaknya*harga)
        if banyaknya >= 3:
            diskon= int(t*0.1)
            total = t-diskon
            print("Total harga Berrys :", total)
        else : 
            print("Total harga Berrys :",total)
    elif keranjang == 'C' :
        print("Menu Peach Mojito")
        harga = 40000
        banyaknya = int(input("Banyak Pesanan :"))
        t = (banyaknya*harga)
        if banyaknya >= 3:
            diskon= int(t*0.1)
            total = t-diskon
            print("Total harga Peach Mojito :", total)
        else : 
            print("Total harga Peach Mojito :",total)
    elif keranjang == 'D' :
        print("Menu Fish and Chips")
        harga = 70000
        banyaknya = int(input("Banyak Pesanan :"))
        t = (banyaknya*harga)
        if banyaknya >= 2:
            diskon= int(t*0.05)
            total = t-diskon
            print("Total harga Fish and Chips :", total)
        else : 
            print("Total harga Fish and chips :",total)
    elif keranjang == 'E' :
        print("Menu Sistagor")
        harga = 50000
        banyaknya = int(input("Banyak Pesanan :"))
        t = (banyaknya*harga)
        if banyaknya >= 2:
            diskon= int(t*0.05)
            total = t-diskon
            print("Total harga Sistagor :", total)
        else : 
            print("Total harga Sistagor :",total)

    bayar = input("Apakah anda membayar dengan emoney (Y/T) :")
    if bayar == "Y" :
        diskon = int(total*0.05)
        total = int(diskon)
        print  ("Karena anda membayar dengan emoney anda dapat diskon 5% : ", total)
    if bayar == "T" :
        print  ("Karena anda tidak mebayar dengan emoney anda tidak mendapat diskon :", total)
    
    Hari = input("Weekend? (Y/T) :")
    if Hari == "Y" :
        diskon = int(total*0.05)
        total = int(diskon)
        print  ("Karena anda makan saat weekend, maka mendapatkan diskon lagi 5% :", total)
    if Hari == "T" :
        diskon = int(total*0.1)
        total = int(diskon)
        print  ("Karena anda makan saat hari kerja, maka mendapatkan diskon lagi 10%:", total)
