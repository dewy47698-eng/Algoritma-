from time import sleep
from colorama import Fore, Style

class Player:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

    def tampil(self):
        print(Fore.CYAN + f"🔥 Player: {self.nama} | HP: {self.hp}" + Style.RESET_ALL)

    def serang(self, damage):
        self.hp -= damage
        print(Fore.YELLOW + f"⚔ {self.nama} terkena serangan {damage} damage!" + Style.RESET_ALL)
        print(Fore.RED + f"❤️ HP tersisa: {self.hp}\n" + Style.RESET_ALL)
        sleep(0.5)


# Membuat objek pemain
p1 = Player("Ana", 100)
p2 = Player("Laila", 120)

print("\n===== STATUS PEMAIN AWAL =====")
p1.tampil()
p2.tampil()

print("\n===== PERTARUNGAN DIMULAI =====\n")

p1.serang(10)
p2.serang(25)
p1.serang(40)

print("===== PERTARUNGAN SELESAI =====")
p1.tampil()
p2.tampil()
