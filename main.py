import os, time

def clear():
    os.system('cls' or 'clear')


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Stack:
    def __init__(self):
        self.start_node = None

    def isi_list(self):
        count = 1
        barang = []
        if self.start_node is None:
            print("    ===>> Isi Gudang <<===")
            print("-"*30)
            print(f"| {'Isi Gudang Kosong...':<26} |") 
            print("-"*30)
            return
        else:
            n = self.start_node
            print("      ===>> Isi Gudang <<===")   
            print("-"*33)
            while n is not None:
                barang.append(n.data)         
                n = n.ref
            for i in barang[::-1]:
                print(f"| {count}. {i:<26} |")
                count += 1
            print("-"*33)

    def insert(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
    
    def delete(self):
        if self.start_node is None:
            print("    ===>> Isi Gudang <<===")
            print("-"*30)
            print(f"| {'Isi Gudang Kosong...':<26} |") 
            print("-"*30)
            return
        data = self.start_node.data
        self.start_node = self.start_node.ref
        print("         ===>> Isi Gudang <<===")
        print("-"*40)
        print(f"| [{data}] {'Berhasil dihapus...':<26} |")
        print("-"*40)
        return data
    
    def count(self):
        barang = []
        if self.start_node is None:
            print("   ===>> Jumlah Barang <<===")
            print("-"*31)
            print (f"| {'Jumlah Barang --->> 0':<27} |")
            print("-"*31)
            return
        else:
            count = 0
            n = self.start_node
            while n is not None:
                count += 1
                barang.append(n.data)
                n = n.ref
            print("   ===>> Jumlah Barang <<===")
            print("-"*31)
            print(f"| {'Jumlah Barang -->>'} {count:<8} |")
            print("-"*31)
            set_barang = set(barang)
            for i in set_barang:
                jum = 0
                for u in barang:
                    if i == u:
                        jum += 1
                print(f"| {jum} {i:<25} |")
            print("-"*31)

# ====================================================================================================================================

# Menginisialisasikan class Stack dalam variabel "stack"
stack = Stack()

def lihat_barang():
    stack.isi_list()
    input("Tekan Enter...")
    menu()

def insert_barang():
    clear()
    barang = input("\nImportkan Barang --->> ")
    stack.insert(barang)
    print(f"[{barang}] Berhasil Ditambahkan...")
    tanya = input("Apakah ingin menambahkan barang lagi (y/n)? ")
    if tanya == "y":
        insert_barang()
    elif tanya == "n":
        menu()
    else:
        print("\nMaaf, inputan anda salah..!")
        time.sleep(1)
        insert_barang()

def hapus_barang():
    stack.delete()
    time.sleep(1)
    menu()

def jumlah_barang():
    stack.count()
    input("Tekan Enter...")
    menu()

def menu():
    clear()
    print("     ===>> Stock.co <<===")
    print("-"*30)
    print(f"| {'[1] Lihat Barang' :<26} |")
    print(f"| {'[2] Tambahkan Barang' :<26} |")
    print(f"| {'[3] Hapus Barang' :<26} |")
    print(f"| {'[4] Jumlah Barang' :<26} |")
    print(f"| {'[5] Exit' :<26} |")
    print("-"*30)
    pilihan = input("\nPilih Menu --->> ")
    if pilihan == "1":
        clear()
        lihat_barang()
    elif pilihan == "2":
        clear()
        insert_barang()
    elif pilihan == "3":
        clear()
        hapus_barang()
    elif pilihan == "4":
        clear()
        jumlah_barang()
    elif pilihan == "5":
        clear()
        exit()
    else:
        clear()
        print("Maaf, inputan anda salah..!")
        time.sleep(1)
        menu()


if __name__ == "__main__":
    while True:
        menu()