#import time

# Warna teks
class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    END = "\033[0m"

print(Color.HEADER + "========== PROGRAM STACK (LIFO) ==========" + Color.END)

# ----------------------------------------------------------
#                       CLASS STACK
# ----------------------------------------------------------
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        print(Color.GREEN + f"[ PUSH ] → {item} ditambahkan ke stack" + Color.END)
        self.visual()

    def pop(self):
        if self.is_empty():
            print(Color.RED + "[ POP ] Stack kosong! Tidak dapat menghapus." + Color.END)
            return None
        removed = self.items.pop()
        print(Color.YELLOW + f"[ POP ] → {removed} dihapus dari stack" + Color.END)
        self.visual()
        return removed

    def peek(self):
        if self.is_empty():
            print(Color.RED + "[ PEEK ] Stack kosong!" + Color.END)
            return None
        print(Color.CYAN + f"[ PEEK ] Data teratas: {self.items[-1]}" + Color.END)
        return self.items[-1]

    def visual(self):
        print(Color.BLUE + "\n--- Tampilan Stack (atas ↓) ---" + Color.END)
        if self.is_empty():
            print(Color.RED + "[ KOSONG ]" + Color.END)
        else:
            for item in reversed(self.items):
                print(Color.GREEN + f"|  {item}  |" + Color.END)
                print(Color.BLUE + "------" + Color.END)
        print()
        time.sleep(0.5)

# ----------------------------------------------------------
#                PROGRAM INTERAKTIF STACK
# ----------------------------------------------------------
stack = Stack()

while True:
    print(Color.HEADER + "\nPilih Operasi Stack:" + Color.END)
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Keluar")

    choice = input(Color.YELLOW + "Masukkan pilihan (1-4): " + Color.END)

    if choice == '1':
        value = input("Masukkan nilai untuk push: ")
        stack.push(value)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.peek()
    elif choice == '4':
        print(Color.HEADER + "\n========== PROGRAM SELESAI ==========" + Color.END)
        break
    else:
        print(Color.RED + "Pilihan tidak valid! Silakan pilih 1-4." + Color.END)
