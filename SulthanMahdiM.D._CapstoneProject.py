import tabulate
global cart

listFilm = [
    {"id": "F01", "judul": "The Shawshank Redemption", "tahun": 1994, "genre": ["Drama"], "rating": 9.3, "stok": 5},
    {"id": "F02", "judul": "The Godfather", "tahun": 1972, "genre": ["Crime", "Drama"], "rating": 9.2, "stok": 3},
    {"id": "F03", "judul": "The Dark Knight", "tahun": 2008, "genre": ["Action", "Crime", "Drama", "Thriller"], "rating": 9.0, "stok": 7},
    {"id": "F04", "judul": "The Lord of the Rings: The Two Towers", "tahun": 2002, "genre": ["Action", "Adventure", "Drama", "Fantasy"], "rating": 8.8, "stok": 8},
    {"id": "F05", "judul": "Inception", "tahun": 2010, "genre": ["Action", "Adventure", "Sci-Fi", "Thriller"], "rating": 8.8, "stok": 4},
    {"id": "F06", "judul": "Gladiator", "tahun": 2000, "genre": ["Action", "Adventure", "Drama"], "rating": 8.5, "stok": 10},
    {"id": "F07", "judul": "Avengers: Infinity War", "tahun": 2018, "genre": ["Action", "Adventure", "Sci-Fi"], "rating": 8.4, "stok": 12},
    {"id": "F08", "judul": "The Dark Knight Rises", "tahun": 2012, "genre": ["Action", "Drama", "Thriller"], "rating": 8.4, "stok": 7},
    {"id": "F09", "judul": "Avengers: Endgame", "tahun": 2019, "genre": ["Action", "Adventure", "Drama", "Sci-Fi"], "rating": 8.4, "stok": 8},
    {"id": "F10", "judul": "Up", "tahun": 2009, "genre": ["Animation", "Adventure", "Comedy", "Drama", "Family"], "rating": 8.3, "stok": 0}]

listPelanggan = [
    {"nama": "Sulthan Mahdi", "no_telp": '082331517992', "member": True, "password": "password"},
    {"nama": "Fadhel Budiman", "no_telp": '081111111111', "member": True, "password": "111111"},
    {"nama": "Sarah Astrid", "no_telp": '082222222222', "member": False, "password": "222222"},
    {"nama": "Kevin Ilham", "no_telp": '083333333333', "member": False, "password": "333333"},
    {"nama": "Aca Suryo", "no_telp": '084444444444', "member": True, "password": "444444"}]

listHistory = [
    {"nama": "Sulthan Mahdi", "no_telp": '082331517992', "judul": ["Inception", "Up", "Avengers: Endgame", "Gladiator"], "nominal": 60000},
    {"nama": "Sarah Astrid", "no_telp": '082222222222', "judul": ["The Godfather", "The Dark Knight", "The Dark Knight Rises", "Up"], "nominal": 80000},
    {"nama": "Sulthan Mahdi", "no_telp": '082331517992', "judul": ["The Shawshank Redemption", "The Lord of the Rings: The Two Towers"], "nominal": 30000}]

# ======================================================
#CREATE
def buatFilm():
    daftarFilm()
    print('''\n    
    1. Tambahkan film
    2. Kembali ke menu sebelumnya
    3. Kembali ke menu utama''')
    inputMenu()
    if pilih == "1":
        id = str(input("\nMasukkan id film: "))
        for film in listFilm:
            if id == film["id"]:
                print("Maaf data sudah tersedia")
                menuAdmin()
        judul = str(input("Masukkan judul film: ")).title()
        tahun = int(input("Masukkan tahun film: "))
        genre = []
        listGenre(genre)
        rating = float(input("Masukkan rating film: "))
        stok = int(input("Masukkan stok film: "))
        listFilm.append({
                "id": id,
                "judul": judul,
                "tahun": tahun,
                "genre": genre,
                "rating": rating,
                "stok": stok})
        cariIdFilm(id)
        simpan = input("Apakah Anda ingin menyimpan data berikut? (Ya/Tidak): ")
        if simpan.title() == "Ya":
            daftarFilm()
            print("Film berhasil ditambahkan")
            menuAdmin()
        elif simpan.title() == "Tidak":
            listFilm.pop()
            print("Data tidak berhasil disimpan")
            menuAdmin()
    elif pilih == "2":
        menuAdmin()
    elif pilih == "3":
        mainMenu()
    else:
        print("Input tidak valid")
        buatFilm()
  
def listGenre(genre):
    kondisi = True
    while kondisi == True:
        tempGenre = str(input(f"Masukkan katagori genre: ")).title()
        genre.append(tempGenre)
        lanjut = input(f"Apakah Anda ingin memasukkan genre lain (Ya/Tidak): ").title()
        while lanjut.title() != "Ya":
            if lanjut.title() != "Tidak":
                print("Input Anda tidak valid")
                lanjut = input(f"Apakah Anda ingin memasukkan genre lain (Ya/Tidak): ").title()
            elif lanjut.title() == "Tidak":
                kondisi = False
                break
        if  lanjut.title() == "Ya":
            kondisi = True

# ---------------------------------                
#READ
def daftarFilm():
    if len(listFilm) == 0:
        print("Film tidak tersedia")
        menu1()
    header = listFilm[0].keys()
    rows = []
    for film in listFilm:
        temp = [film["id"], film["judul"], film["tahun"], ", ".join(film["genre"]), film["rating"], film["stok"]]
        rows.append(temp)
    print("\n")
    print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))

def cariJudulFilm():
    if len(listFilm) == 0:
        print("Film tidak tersedia")
        menu1()
    judul = str(input("Masukkan judul film: "))
    header = listFilm[0].keys()
    rows = []
    for film in listFilm:
        if judul.title() in film["judul"]:
            temp = [film["id"], film["judul"], film["tahun"], ", ".join(film["genre"]), film["rating"], film["stok"]]
            rows.append(temp)
    if rows:
        print("\n")
        print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))
    else:
        print(f"\nFilm dengan judul '{judul.title()}' tidak ditemukan")
        menu1()

def cariGenreFilm():
    if len(listFilm) == 0:
        print("Film tidak tersedia")
        menu1()
    genre = str(input("\nMasukkan genre film: "))
    header = listFilm[0].keys()
    rows = []
    for film in listFilm:
        if genre.title() in ", ".join(film["genre"]):
            temp = [film["id"], film["judul"], film["tahun"], ", ".join(film["genre"]), film["rating"], film["stok"]]
            rows.append(temp)
    if rows:
        print("\n")
        print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))
    else:
        print(f"\nFilm dengan genre '{genre.title()}' tidak ditemukan")
        menu1()

def cariIdFilm(id):
    if len(listFilm) == 0:
        print("Film tidak tersedia")
        menu1()
    header = listFilm[0].keys()
    rows = []
    for film in listFilm:
        if film["id"] == id:
            temp = [film["id"], film["judul"], film["tahun"], ", ".join(film["genre"]), film["rating"], film["stok"]]
            rows.append(temp)
    if rows:
        print("\n")
        print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))
    else:
        print(f"\nFilm dengan id '{id}' tidak ditemukan")

def tampilkanFilm(dataTypeList):
    header = dataTypeList[0].keys()
    rows = []
    for film in dataTypeList:
        temp = [film["id"], film["judul"], film["tahun"], ", ".join(film["genre"]), film["rating"], film["stok"]]
        rows.append(temp)
    print("\n")
    print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))

def daftarPelanggan():
    if len(listPelanggan) == 0:
        print("Pelanggan tidak tersedia")
        menuAdmin()
    header = listPelanggan[0].keys()
    rows = []
    for pelanggan in listPelanggan:
        temp = [pelanggan["nama"], pelanggan["no_telp"], pelanggan["member"]]
        rows.append(temp)
    print("\n")
    print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))

def daftarPenjualan():
    if len(listHistory) == 0:
        print("Belum ada film yang terjual")
        menuAdmin()
    header = listHistory[0].keys()
    rows = []
    for penjualan in listHistory:
        temp = [penjualan["nama"], penjualan["no_telp"], ",\n".join(penjualan["judul"]), penjualan["nominal"]]
        rows.append(temp)
    print("\n")
    print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))

def riwayatPeminjaman(hp):
    if len(listHistory) == 0:
        print("Film tidak tersedia")
        menu1()
    header = listHistory[0].keys()
    rows = []
    for pelanggan in listHistory:
        if hp in pelanggan["no_telp"]:
            temp = [pelanggan["nama"], pelanggan["no_telp"], ", ".join(pelanggan["judul"]), pelanggan["nominal"]]
            rows.append(temp)
    if rows:
        print("\n")
        print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))
        menu2()

# --------------------------------------------
#UPDATE
def updateFilm():
    daftarFilm()
    print('''\n    
    1. Update film
    2. Kembali ke menu sebelumnya
    3. Kembali ke menu utama''')
    inputMenu()
    if pilih == "1":
        temp = []
        id = str(input("Masukkan id film yang ingin diubah: "))
        for film in listFilm:
            if film["id"] == id:
                cariIdFilm(id)
                temp.append(film)
                kolom = str(input("Masukkan kolom yang ingin diubah: ")).lower()
                if kolom in film:
                    if kolom == "stok":
                        dataBaru = int(input(f"Masukkan data baru untuk kolom {kolom}: "))
                        temp[0][kolom] = dataBaru
                        tampilkanFilm(temp)
                        print('''\n   
    1. Apakah Anda yakin untuk melakukan update
    2. Batalkan''')
                        inputMenu()
                        if pilih == "1":
                            film[kolom] = dataBaru
                            daftarFilm()
                            print("Data berhasil diubah")
                            menuAdmin()
                        elif pilih == "2":
                            updateFilm()
                        else:
                            print("Input tidak valid")
                            updateFilm()
                    elif kolom == "genre":
                        genre = []
                        listGenre(genre)
                        temp[0][kolom] = genre
                        tampilkanFilm(temp)
                        print('''\n
    1. Apakah Anda yakin untuk melakukan update
    2. Batalkan''')
                        inputMenu()
                        if pilih == "1":
                            film[kolom] = genre
                            daftarFilm()
                            print("Data berhasil diubah")
                            menuAdmin()
                        elif pilih == "2":
                            updateFilm()
                        else:
                            print("Input tidak valid")
                            updateFilm()
                    else:
                        dataBaru = input(f"Masukkan data baru untuk kolom {kolom}: ")
                        temp[0][kolom] = dataBaru
                        tampilkanFilm(temp)
                        print('''\n   
    1. Apakah Anda yakin untuk melakukan update
    2. Batalkan''')
                        inputMenu()
                        if pilih == "1":
                            film[kolom] = dataBaru
                            daftarFilm()
                            print("Data berhasil diubah")
                            menuAdmin()
                        elif pilih == "2":
                            updateFilm()
                        else:
                            print("Input tidak valid")
                            updateFilm()
                else:
                    print(f"Data {kolom} tidak tersedia dalam list film")
                    menuAdmin()
        print(f"Film dengan id {id} tidak ditemukan dalam list film")
        menuAdmin()
    elif pilih == "2":
        menuAdmin()
    elif pilih == "3":
        mainMenu()
    else:
        print("Input tidak valid")
        updateFilm()

# ----------------------------------------
#DELETE
def deleteFilm():
    daftarFilm()
    print('''\n
    1. Delete film
    2. Kembali ke menu sebelumnya
    3. Kembali ke menu utama''')
    inputMenu()
    if pilih == "1":
        id = str(input("Masukkan id yang ingin Anda hapus: "))
        for film in listFilm:
            if film["id"] == id:
                cariIdFilm(id)
                print(f'''\n
    1. Apakah Anda yakin untuk menghapus film {id}
    2. Batalkan''')
                inputMenu()
                if pilih == "1":
                    listFilm.remove(film)
                    daftarFilm()
                    print("Film berhasil dihapus")
                    menuAdmin()
                elif pilih == "2":
                    print("Penghapusan dibatalkan")
                    menuAdmin()
                else:
                    print("Input error, silakan ulangi lagi")
                    menuAdmin()
        print(f"Film dengan id {id} tidak ditemukan")
        menuAdmin()
    elif pilih == "2":
        menuAdmin()
    elif pilih == "3":
        mainMenu()
    else:
        print("Input tidak valid")
        deleteFilm()

# =========================================================
# MENU PEMINJAMAN
cart = []
def pinjamFilm():
    global cart
    kondisi = True
    pinjam = str(input("Masukkan id film yang ingin dipinjam: "))
    while kondisi == True:
        for film in listFilm:
            if film["id"] == pinjam:
                if film["stok"] >= 1:
                    film["stok"] -= 1
                    cart.append(film)
                    showCart()
                    menuCart()
                else:
                    print(f"Mohon maaf film {film["judul"]} sedang habis")
                    daftarFilm()
                    pinjamFilm()
        print("Input tidak valid")
        daftarFilm()
        pinjamFilm()

def showCart():
    global cart
    header = ["id", "judul"]
    rows = []
    for cartFilm in cart:
        temp = [cartFilm["id"],cartFilm["judul"]]
        rows.append(temp)
    print("\n")
    print("Daftar film yang berada di cart saat ini adalah: ")
    print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))

def menuCart():
    global cart
    print('''\n
    1. Pinjam film lainnya
    2. Hapus film
    3. Lakukan pembayaran
    4. Batalkan''')
    inputMenu()
    if pilih == "1":
        daftarFilm()
        pinjamFilm()
    elif pilih == "2":
        delCart()
    elif pilih == "3":
        bayar()
    elif pilih == "4":
        emptyCart()
        menu1()

def bayar():
    global cart
    tempJudul = []
    showCart()
    noHP = str(input("Masukkan no HP Anda untuk membayar: "))
    cariNoHP(noHP)
    if adaHP == True:
        if isMember(noHP):
            total = int(len(cart))*15000
            print(f"Total biaya yang harus anda bayar adalah {total}")
            uang = int(input("Masukkan uang Anda: "))
            if uang < total:
                print(f'''\n  
            Uang Anda kurang sebesar Rp{total-uang}\n  
            1. Lakukan pembayaran ulang
            2. Batalkan pembelian''')
                inputMenu()
                if pilih == 1:
                    bayar()
                elif pilih == 2:
                    emptyCart()
                    menu1()
                else:
                    print("Input tidak valid")
                    bayar()
            else:
                print('''\n
========================================================
|   Terima kasih telah berbelanja di Sulthan Cinema    |
========================================================\n\n''')
                for film in cart:
                    tempJudul.append(film["judul"])
                listHistory.append({
                    "nama": cariNama(noHP),
                    "no_telp": noHP,
                    "judul": tempJudul,
                    "nominal": total})
                emptyCart()
                menu1()
        else:
            total = int(len(cart))*20000
            print(f"Total biaya yang harus anda bayar adalah {total}")
            uang = int(input("Masukkan uang Anda: "))
            if uang < total:
                print(f'''\n  
            Uang Anda kurang sebesar Rp{total-uang}\n  
            1. Lakukan pembayaran ulang
            2. Batalkan pembelian''')
                inputMenu()
                if pilih == 1:
                    bayar()
                elif pilih == 2:
                    emptyCart()
                    menu1()
                else:
                    print("Input tidak valid")
                    bayar()
            else:
                print('''\n
========================================================
|   Terima kasih telah berbelanja di Sulthan Cinema    |
========================================================\n\n''')
                for film in cart:
                    tempJudul.append(film["judul"])
                listHistory.append({
                    "nama": cariNama(noHP),
                    "no_telp": noHP,
                    "judul": tempJudul,
                    "nominal": total})
                emptyCart()
                menu1()
    else:
        namaBaru = input("Masukkan nama Anda: ")
        total = int(len(cart))*25000
        print(f"Total biaya yang harus anda bayar adalah {total}")
        uang = int(input("Masukkan uang Anda: "))
        if uang < total:
            print(f'''\n  
        Uang Anda kurang sebesar Rp{total-uang}\n  
        1. Lakukan pembayaran ulang
        2. Batalkan pembelian''')
            inputMenu()
            if pilih == 1:
                bayar()
            elif pilih == 2:
                emptyCart()
                menu1()
            else:
                print("Input tidak valid")
                bayar()
        else:
            print('''\n
========================================================
|   Terima kasih telah berbelanja di Sulthan Cinema    |
========================================================\n\n''')
            for film in cart:
                tempJudul.append(film["judul"])
            listHistory.append({
                "nama": namaBaru,
                "no_telp": noHP,
                "judul": tempJudul,
                "nominal": total})
            listPelanggan.append({
                "nama": namaBaru,
                "no_telp": noHP,
                "member": False,
                "password": noHP})
            emptyCart()
            menu1()

def cariIdCart(id):
    global cart
    if len(cart) == 0:
        print("Film tidak tersedia")
        menuCart()
    header = cart[0].keys()
    rows = []
    for film in cart:
        if film["id"] == id:
            temp = [film["id"], film["judul"]]
            rows.append(temp)
            break
    if rows:
        print("\n")
        print(tabulate.tabulate(rows, header, tablefmt="fancy_grid"))
    else:
        print(f"\nFilm dengan id '{id}' tidak ditemukan")
        menuCart()

def delCart():
    global cart
    id = str(input("Masukkan id yang ingin Anda hapus: "))
    for film in cart:
        if film["id"] == id:
            cariIdCart(id)
            qtyFilmPlus(id)
            cart.remove(film)
            print("Film berhasil dihapus")
            showCart()
            menuCart()
    print("Input tidak valid/data tidak ditemukan")
    showCart()
    menuCart()  

def qtyFilmPlus(id):
    for film in listFilm:
        if film["id"] == id:
            film["stok"] += 1

def emptyCart():
    global cart
    for film in cart:
        qtyFilmPlus(film["id"])
    cart = []

def isMember(noHP):
    global member
    for akun in listPelanggan:
        if akun["no_telp"] == noHP:
            if akun["member"] == True:
                member = True
                break
            else:
                member = False
        member = False
    return member

def cariNama(noHP):
    global namaPelanggan
    for akun in listPelanggan:
        if akun["no_telp"] == noHP:
            namaPelanggan = akun["nama"]
            return namaPelanggan
    return namaPelanggan

def cariNoHP(noHP):
    global adaHP
    for pelanggan in listPelanggan:
        if pelanggan["no_telp"] == noHP:
            adaHP = True
            break
        else:
            adaHP = False
    return adaHP

# =========================================================
# LIST TAMPILAN MENU
def inputMenu():
    global pilih
    pilih = str(input("\nPilih Menu: "))
    return pilih

def mainMenu():
    print(f'''\n
========================================
|   Selamat datang di Sulthan Cinema   |
========================================
    
    Daftar Menu:
    1. Guest
    2. Login akun pembeli
    3. Admin
    4. Keluar''')
    inputMenu()
    if pilih == "1":
        menu1()
    elif pilih == "2":
        menu2Login()
    elif pilih == "3":
        menu3()
    elif pilih == "4":
        print('''\n
========================================================
|   Terima kasih telah berbelanja di Sulthan Cinema    |
========================================================\n\n''')
        exit()
    else:
        print("Input tidak valid")
        mainMenu()
    
def menu1():
    print('''\n    
    1. Tampilkan semua film
    2. Cari judul film
    3. Cari genre film
    4. Kembali ke menu utama''')
    inputMenu()
    if pilih == "1":
        daftarFilm()
        menu1Back()
    elif pilih == "2":
        daftarFilm()
        cariJudulFilm()
        menu1Back()
    elif pilih == "3":
        daftarFilm()
        cariGenreFilm()
        menu1Back()
    elif pilih == "4":
        mainMenu()
    else:
        print("Input tidak valid")
        menu1Back()

def menu1Back():
    print('''\n    
    1. Sewa film
    2. Kembali ke menu sebelumnya
    3. Kembali ke menu utama''')
    inputMenu()
    if pilih == "1":
        pinjamFilm()
    elif pilih == "2":
        menu1()
    elif pilih == "3":
        mainMenu()
    else:
        print("Input tidak valid")
        menu1Back()
    
def menu2Login():
    global hp
    hp = input("Masukkan no HP Anda: ")
    cariNoHP(hp)
    if adaHP == True:
        password = input("Masukkan password Anda: ")
        for pelanggan in listPelanggan:
            if pelanggan["no_telp"] == hp:
                if pelanggan["password"] == password:
                    menu2()
                else:
                    print("Password salah, silakan login kembali")
                    menu2Login()
    else:
        print("No.HP tidak ditemukan, silakan masuk menggunakan akun Guest")
        mainMenu()    

def menu2():
    global hp
    x = cariNama(hp)
    print(f'''\n 
    Selamat datang, {x}

    1. Lihat daftar film yang pernah dipinjam
    2. Kembali ke menu utama''')
    inputMenu()
    if pilih == "1":
        riwayatPeminjaman(hp)
    elif pilih == "2":
        mainMenu()
    else:
        print("Input tidak valid")
        menu2()

def menu3():
    password = input("\nMasukkan password: ")
    while password != "admin123":
        print("Password salah")
        print('''\n 
    1. Coba lagi
    2. Kembali ke menu sebelumnya''')
        inputMenu()
        if pilih == "1":
            menu3()
        elif pilih == "2":
            mainMenu()
    menuAdmin()

def menuAdmin():
    print('''\n    
    1. Menambahkan film baru
    2. Mengedit data film
    3. Menghapus film
    4. Tampilkan data pelanggan
    5. Tampilkan riwayat penjualan
    6. Kembali ke menu utama''')
    inputMenu()
    if pilih == "1":
        buatFilm()
    elif pilih == "2":
        updateFilm()
    elif pilih == "3":
        deleteFilm()
    elif pilih == "4":
        daftarPelanggan()
        menuAdmin()
    elif pilih == "5":
        daftarPenjualan()
        menuAdmin()
    elif pilih == "6":
        mainMenu()
    else:
        print("Input tidak valid")
        menuAdmin()

# =====================================
mainMenu()

                


