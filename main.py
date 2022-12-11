import os, time

def clear():
    os.system('cls' or 'clear')


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def isi_list(self):
        count = 1
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
                print(f"| {count}. {n.data:<26} |")           
                n = n.ref
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
        if self.start_node is None:
            print("   ===>> Jumlah Barang <<===")
            print("-"*31)
            print (f"| {'Jumlah Barang --->> 0':<27} |")
            print("-"*31)
            return
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return print(f"Jumlah Barang --->> {count}")


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):
        self.stack.insert(data)

    def pop(self):
        removed = self.stack.delete()
        return removed
    
    def peek(self):
        if self.stack.start_node is None:
            print("Stack has no element")
            return
        else:
            n = self.stack.start_node
            print("data teratas adalah :", n.data )

    def peek_all(self):
        return self.stack.isi_list()

    def count(self):
        return self.stack.count()


# Menginisialisasikan class Stack dalam variabel "stack"
stack = Stack()

def lihat_barang():
    stack.peek_all()
    input("Tekan Enter...")
    menu()

def insert_barang():
    barang = input("\nImportkan Barang --->> ")
    stack.push(barang)
    print(f"[{barang}] Berhasil Ditambahkan...")
    tanya = input("Apakah ingin menambahkan barang lagi (y/n)? ")
    if tanya == "y":
        insert_barang()
    elif tanya == "n":
        menu()

def hapus_barang():
    stack.pop()
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


menu()