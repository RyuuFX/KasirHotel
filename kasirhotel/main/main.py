while True :
    print("<====================================>")
    print("|            Hotelku.Apps            |")
    print("<====================================>")
    print("1.Admin")
    print("2.User")
    login = int(input("Login Sebagai : "))
    
    if login == 1:
        from admin import mimin
        mimin()
    elif login == 2:
        from pemesanan import pesan
        pesan()
    else :
        print("pilihan tidak tersedia,mohon memilih ulang")
