
def user():
    try:
        print("\nProgram input data mahasiswa")
        print("1. Tambah Data\n2. Tampilkan Data\n3. Update Data\n4. Delete Data\n5. Search Data\n6. Keluar")

        x = int(input("Input pilihan: "))

        if x == 1:
            insert()
        elif x == 2:
            read()
        elif x == 3:
            update()
        elif x == 4:
            delete()
        elif x == 5:
            search()
        else:
            exit()
    except ValueError:
        print("Masukkan angka yang valid!")


def insert():
    with open("mahasiswa.txt", "r") as file:
        lines = file.readlines()

    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    matkul = input("Masukkan Mata Kuliah: ")
    sem = input("Input semester: ")

    for line in lines:
        if nim in line:
            print("NIM sudah ada!\n")
            insert()

        elif len(nim) != 8:
            print("Data NIM tidak sesuai\n")
            insert()

    file = open("mahasiswa.txt", "a")

    file.write(nama+", "+nim+", "+matkul+", "+sem+"\n")
    file.close()
    print('Data berhasil ditambahkan')
    user()


def read():
    file = open("mahasiswa.txt", "r")
    i = 0
    for line in file:
        i += 1

        print("Menampilkan Data ke-", i, ":")
        print("Nama:", line.split(', ')[0])
        print("NIM:", line.split(', ')[1])
        print("Mata Kuliah:", line.split(', ')[2])
        print("Semester:", line.split(', ')[3])
    file.close()
    user()


def update():

    newNim = input("\nMasukkan NIM data yang ingin diupdate: ")
    succes = False
    if len(newNim) == 8:
        with open("mahasiswa.txt", "r+") as file:
            lines = file.readlines()

            for index, line in enumerate(lines):
                if newNim in line:
                    nama = input("Input Nama: ")
                    nim = input("Input NIM: ")
                    if len(nim) != 8:
                        print("Data NIM tidak sesuai\n")
                        update()
                    matkul = input("Masukkan Mata Kuliah: ")
                    sem = input("Input semester: ")

                    updated_line = f"{nama}, {nim}, {matkul}, {sem}\n"
                    lines[index] = updated_line
                    succes = True

            file.seek(0)
            file.truncate()

            file.writelines(lines)
        if succes == True:
            print('Data berhasil di update')
            user()
        else:
            print('Data NIM tidak ada! Cek NIM anda!')
            update()
    else:
        print("Data NIM tidak sesuai")
        update()


def delete():
    file = open("mahasiswa.txt", "r")
    i = 0
    for line in file:
        i += 1
        print("Menampilkan Data ke-", i, ":")
        print("Nama:", line.split(', ')[0])
        print("NIM:", line.split(', ')[1])
        print("Mata Kuliah:", line.split(', ')[2])
        print("Semester:", line.split(', ')[3])
    file.close()

    nim = input("\nMasukkan NIM data yang ingin dihapus: ")
    # succes = False
    if len(nim) == 8:
        with open("mahasiswa.txt", "r") as file:
            lines = file.readlines()
        with open("mahasiswa.txt", "w") as file:

            for line in lines:
                if nim not in line:
                    file.write(line)
                    # succes = True
    else:
        print("Data NIM tidak sesuai")
        delete()

    print('Data berhasil di hapus')
    user()


def search():

    search = input("\nMasukkan NIM data yang ingin dicari: ")
    with open("mahasiswa.txt", "r") as file:

        lines = file.readlines()
        for line in lines:
            if line.find(search) != -1:
                print("Nama: ", line.split(', ')[0])
                print("NIM: ", line.split(', ')[1])
                print("Mata Kuliah: ", line.split(', ')[2])
                print("Semester: ", line.split(', ')[3])

    user()


user()
